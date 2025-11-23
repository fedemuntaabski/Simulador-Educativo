import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

USER_DATA_FILE = "user_data.json"

class UserMetrics:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserMetrics, cls).__new__(cls)
            cls._instance._load_data()
        return cls._instance

    def _load_data(self):
        if os.path.exists(USER_DATA_FILE):
            try:
                with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except Exception:
                self._init_default_data()
        else:
            self._init_default_data()

    def _init_default_data(self):
        self.data = {
            "user_id": "default_user",
            "level": 1,
            "xp": 0,
            "exercises_completed": 0,
            "total_time_minutes": 0.0,
            "skills": {},  # topic -> level (0-100)
            "history": []
        }
        self._save_data()

    def _save_data(self):
        try:
            with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"Error saving user data: {e}")

    def record_exercise_completion(self, exercise_id: str, topic: str, score: float, time_taken_seconds: float):
        """
        Registra la finalización de un ejercicio y actualiza métricas.
        """
        # Update basic stats
        self.data["exercises_completed"] += 1
        self.data["total_time_minutes"] += time_taken_seconds / 60.0

        # Calculate XP based on score and difficulty (simplified)
        xp_gained = int(score * 1.5)  # Base XP
        self.data["xp"] += xp_gained

        # Update Level
        # Simple formula: Level = 1 + sqrt(XP / 100)
        self.data["level"] = int(1 + (self.data["xp"] / 500) ** 0.5)

        # Update Skills
        current_skill = self.data["skills"].get(topic, 0)
        # Skill increases more if score is high, but harder to increase as it gets higher
        skill_increase = (score / 100.0) * (100 - current_skill) * 0.1
        self.data["skills"][topic] = min(100, current_skill + skill_increase)

        # Add to history
        entry = {
            "exercise_id": exercise_id,
            "topic": topic,
            "score": score,
            "time_taken": time_taken_seconds,
            "date": datetime.now().isoformat(),
            "xp_gained": xp_gained
        }
        self.data["history"].append(entry)
        
        self._save_data()
        
        return {
            "xp_gained": xp_gained,
            "new_level": self.data["level"],
            "skill_progress": skill_increase
        }

    def get_dashboard_stats(self) -> Dict[str, Any]:
        """
        Retorna estadísticas para el dashboard.
        """
        history = self.data["history"]
        if not history:
            avg_score = 0
            improvement_rate = 0
        else:
            scores = [h["score"] for h in history]
            avg_score = sum(scores) / len(scores)
            
            # Simple improvement rate: compare last 5 vs first 5
            if len(scores) > 5:
                recent_avg = sum(scores[-5:]) / 5
                old_avg = sum(scores[:5]) / 5
                improvement_rate = recent_avg - old_avg
            else:
                improvement_rate = 0

        return {
            "level": self.data["level"],
            "xp": self.data["xp"],
            "exercises_completed": self.data["exercises_completed"],
            "avg_score": avg_score,
            "total_time_minutes": self.data["total_time_minutes"],
            "improvement_rate": improvement_rate,
            "skills": self.data["skills"]
        }

    def get_level_progress(self) -> float:
        """
        Retorna el progreso hacia el siguiente nivel (0.0 a 1.0).
        """
        current_level = self.data["level"]
        # XP needed for current level
        xp_current = 500 * ((current_level - 1) ** 2)
        # XP needed for next level
        xp_next = 500 * (current_level ** 2)
        
        if xp_next == xp_current: return 1.0
        
        return (self.data["xp"] - xp_current) / (xp_next - xp_current)
