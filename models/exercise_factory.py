"""
Fábrica y validador para creación de ejercicios educativos.
"""

from typing import List, Dict, Optional, Tuple
from .exercise import (
    Exercise, 
    Parameter, 
    ExerciseMetadata,
    ParameterType,
    ActivityType,
    DifficultyLevel
)


class ExerciseValidator:
    """Validador de ejercicios educativos."""
    
    @staticmethod
    def validate_exercise(exercise: Exercise) -> Tuple[bool, List[str]]:
        """
        Valida que un ejercicio esté completo y bien formado.
        
        Args:
            exercise: Ejercicio a validar
            
        Returns:
            Tupla (es_valido, lista_de_errores)
        """
        errors = []
        
        # Validar campos básicos requeridos
        if not exercise.id or not exercise.id.strip():
            errors.append("El campo 'id' es requerido y no puede estar vacío")
        
        if not exercise.name or not exercise.name.strip():
            errors.append("El campo 'name' es requerido y no puede estar vacío")
        
        if not exercise.main_topic or not exercise.main_topic.strip():
            errors.append("El campo 'main_topic' es requerido y no puede estar vacío")
        
        if not exercise.educational_objective or not exercise.educational_objective.strip():
            errors.append("El campo 'educational_objective' es requerido y no puede estar vacío")
        
        if not exercise.description or not exercise.description.strip():
            errors.append("El campo 'description' es requerido y no puede estar vacío")
        
        if not exercise.activity_description or not exercise.activity_description.strip():
            errors.append("El campo 'activity_description' es requerido y no puede estar vacío")
        
        if not exercise.expected_observation or not exercise.expected_observation.strip():
            errors.append("El campo 'expected_observation' es requerido y no puede estar vacío")
        
        # Validar parámetros
        if not exercise.parameters:
            errors.append("El ejercicio debe tener al menos un parámetro modificable")
        else:
            for i, param in enumerate(exercise.parameters):
                param_errors = ExerciseValidator._validate_parameter(param, i)
                errors.extend(param_errors)
        
        # Validar preguntas de análisis
        if not exercise.analysis_questions:
            errors.append("El ejercicio debe tener al menos una pregunta de análisis")
        elif len(exercise.analysis_questions) < 3:
            errors.append(f"Se recomiendan al menos 3 preguntas de análisis (encontradas: {len(exercise.analysis_questions)})")
        
        for i, question in enumerate(exercise.analysis_questions):
            if not question or not question.strip():
                errors.append(f"La pregunta de análisis #{i+1} está vacía")
        
        # Validar longitudes razonables
        if len(exercise.description) < 50:
            errors.append("La descripción debería tener al menos 50 caracteres para ser significativa")
        
        if len(exercise.expected_observation) < 50:
            errors.append("La observación esperada debería tener al menos 50 caracteres")
        
        return (len(errors) == 0, errors)
    
    @staticmethod
    def _validate_parameter(param: Parameter, index: int) -> List[str]:
        """Valida un parámetro individual."""
        errors = []
        
        if not param.name or not param.name.strip():
            errors.append(f"Parámetro #{index+1}: el nombre es requerido")
        
        if not param.display_name or not param.display_name.strip():
            errors.append(f"Parámetro '{param.name}': display_name es requerido")
        
        if not param.description or not param.description.strip():
            errors.append(f"Parámetro '{param.name}': descripción es requerida")
        
        # Validación específica por tipo
        if param.param_type in [ParameterType.FLOAT, ParameterType.INTEGER]:
            if param.min_value is None:
                errors.append(f"Parámetro '{param.name}': min_value es requerido para tipo numérico")
            if param.max_value is None:
                errors.append(f"Parámetro '{param.name}': max_value es requerido para tipo numérico")
            
            if param.min_value is not None and param.max_value is not None:
                if param.min_value >= param.max_value:
                    errors.append(f"Parámetro '{param.name}': min_value debe ser menor que max_value")
                
                # Validar que default_value esté en rango
                if not (param.min_value <= param.default_value <= param.max_value):
                    errors.append(f"Parámetro '{param.name}': default_value debe estar entre min_value y max_value")
        
        if param.param_type == ParameterType.SELECTION:
            if not param.options:
                errors.append(f"Parámetro '{param.name}': tipo SELECTION requiere lista de opciones")
            elif param.default_value not in param.options:
                errors.append(f"Parámetro '{param.name}': default_value debe estar en la lista de opciones")
        
        return errors


class ExerciseFactory:
    """Fábrica para crear ejercicios con configuraciones predefinidas."""
    
    def __init__(self):
        self.exercises: Dict[str, Exercise] = {}
    
    def create_exercise(
        self,
        exercise_id: str,
        name: str,
        main_topic: str,
        educational_objective: str,
        description: str,
        parameters: List[Parameter],
        activity_type: ActivityType,
        activity_description: str,
        analysis_questions: List[str],
        expected_observation: str,
        metadata: Optional[ExerciseMetadata] = None,
        validate: bool = True
    ) -> Exercise:
        """
        Crea un nuevo ejercicio con validación opcional.
        
        Args:
            exercise_id: ID único del ejercicio
            name: Nombre del ejercicio
            main_topic: Tema principal
            educational_objective: Objetivo educativo
            description: Descripción conceptual
            parameters: Lista de parámetros modificables
            activity_type: Tipo de actividad
            activity_description: Descripción de la actividad
            analysis_questions: Preguntas de análisis
            expected_observation: Observación esperada
            metadata: Metadatos opcionales
            validate: Si True, valida el ejercicio antes de crearlo
            
        Returns:
            Exercise creado
            
        Raises:
            ValueError: Si la validación falla
        """
        if metadata is None:
            metadata = ExerciseMetadata()
        
        exercise = Exercise(
            id=exercise_id,
            name=name,
            main_topic=main_topic,
            educational_objective=educational_objective,
            description=description,
            parameters=parameters,
            activity_type=activity_type,
            activity_description=activity_description,
            analysis_questions=analysis_questions,
            expected_observation=expected_observation,
            metadata=metadata
        )
        
        if validate:
            is_valid, errors = ExerciseValidator.validate_exercise(exercise)
            if not is_valid:
                error_msg = "El ejercicio no es válido:\n" + "\n".join(f"  - {err}" for err in errors)
                raise ValueError(error_msg)
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def get_exercise(self, exercise_id: str) -> Optional[Exercise]:
        """Obtiene un ejercicio por su ID."""
        return self.exercises.get(exercise_id)
    
    def get_all_exercises(self) -> List[Exercise]:
        """Retorna todos los ejercicios creados."""
        return list(self.exercises.values())
    
    def get_exercises_by_topic(self, topic: str) -> List[Exercise]:
        """Retorna ejercicios filtrados por tema principal."""
        return [ex for ex in self.exercises.values() if ex.main_topic.lower() == topic.lower()]
    
    def get_exercises_by_difficulty(self, difficulty: DifficultyLevel) -> List[Exercise]:
        """Retorna ejercicios filtrados por nivel de dificultad."""
        return [
            ex for ex in self.exercises.values() 
            if ex.metadata.difficulty == difficulty
        ]
    
    def get_exercises_by_tag(self, tag: str) -> List[Exercise]:
        """Retorna ejercicios que contienen un tag específico."""
        return [
            ex for ex in self.exercises.values() 
            if tag.lower() in [t.lower() for t in ex.metadata.tags]
        ]
    
    def clear(self):
        """Elimina todos los ejercicios del contenedor."""
        self.exercises.clear()
    
    def remove_exercise(self, exercise_id: str) -> bool:
        """
        Elimina un ejercicio por su ID.
        
        Returns:
            True si se eliminó, False si no existía
        """
        if exercise_id in self.exercises:
            del self.exercises[exercise_id]
            return True
        return False
