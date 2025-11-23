"""
Definición de estructuras de datos para ejercicios educativos.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Union, Tuple
from datetime import datetime
from enum import Enum


class ParameterType(Enum):
    """Tipos de parámetros que puede modificar el estudiante."""
    FLOAT = "float"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    SELECTION = "selection"  # Para opciones discretas


class DifficultyLevel(Enum):
    """Niveles de dificultad de los ejercicios."""
    BASICO = "básico"
    INTERMEDIO = "intermedio"
    AVANZADO = "avanzado"


class ActivityType(Enum):
    """Tipos de actividades que puede realizar el estudiante."""
    SIMULACION = "simulación"
    GRAFICACION = "graficación"
    INTERPRETACION = "interpretación"
    COMPARACION = "comparación"
    ANALISIS_FASE = "análisis de fase"
    CLASIFICACION = "clasificación"


@dataclass
class Parameter:
    """
    Representa un parámetro modificable del ejercicio.
    
    Attributes:
        name: Nombre del parámetro (ej: "mu", "tasa_transmision")
        display_name: Nombre para mostrar al usuario (ej: "μ (mu)", "Tasa de transmisión β")
        description: Descripción breve del parámetro
        param_type: Tipo de dato del parámetro
        min_value: Valor mínimo permitido (para numéricos)
        max_value: Valor máximo permitido (para numéricos)
        default_value: Valor inicial sugerido
        unit: Unidad de medida (opcional, ej: "kg", "°C", "rad/s")
        step: Paso de incremento para sliders (opcional)
        options: Lista de opciones válidas (para tipo SELECTION)
    """
    name: str
    display_name: str
    description: str
    param_type: ParameterType
    default_value: Union[float, int, bool, str]
    min_value: Optional[Union[float, int]] = None
    max_value: Optional[Union[float, int]] = None
    unit: Optional[str] = None
    step: Optional[float] = None
    options: Optional[List[str]] = None
    
    def __post_init__(self):
        """Validación básica de coherencia."""
        if self.param_type == ParameterType.SELECTION and not self.options:
            raise ValueError(f"Parameter '{self.name}' de tipo SELECTION requiere opciones")
        
        if self.param_type in [ParameterType.FLOAT, ParameterType.INTEGER]:
            if self.min_value is None or self.max_value is None:
                raise ValueError(f"Parameter '{self.name}' numérico requiere min_value y max_value")
            if self.min_value > self.max_value:
                raise ValueError(f"Parameter '{self.name}': min_value debe ser <= max_value")


@dataclass
class ExerciseMetadata:
    """
    Metadatos opcionales del ejercicio.
    
    Attributes:
        difficulty: Nivel de dificultad
        category: Categoría temática amplia (ej: "Mecánica", "Eléctrica", "Biología")
        tags: Etiquetas para búsqueda y clasificación
        estimated_time: Tiempo estimado en minutos
        creation_date: Fecha de creación del ejercicio
        author: Autor o fuente del ejercicio
        version: Versión del ejercicio
    """
    difficulty: Optional[DifficultyLevel] = None
    category: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    estimated_time: Optional[int] = None  # en minutos
    creation_date: datetime = field(default_factory=datetime.now)
    author: Optional[str] = None
    version: str = "1.0"


@dataclass
class Exercise:
    """
    Representa un ejercicio educativo completo del laboratorio.
    
    Attributes:
        id: Identificador único del ejercicio
        name: Nombre del ejercicio
        main_topic: Tema principal (ej: "Atractor de Lorenz", "Modelo SIR")
        educational_objective: Objetivo pedagógico del ejercicio
        description: Descripción conceptual del fenómeno o sistema
        parameters: Lista de parámetros que el estudiante puede modificar
        activity_type: Tipo de actividad principal
        activity_description: Descripción detallada de la actividad a realizar
        analysis_questions: Lista de preguntas de análisis para el estudiante
        expected_observation: Qué debería observar si el ejercicio se realiza correctamente
        metadata: Información adicional sobre el ejercicio
    """
    id: str
    name: str
    main_topic: str
    educational_objective: str
    description: str
    parameters: List[Parameter]
    activity_type: ActivityType
    activity_description: str
    analysis_questions: List[str]
    expected_observation: str
    metadata: ExerciseMetadata = field(default_factory=ExerciseMetadata)
    
    def __post_init__(self):
        """Validación básica de campos requeridos."""
        if not self.id or not self.id.strip():
            raise ValueError("El ejercicio requiere un ID válido")
        if not self.name or not self.name.strip():
            raise ValueError("El ejercicio requiere un nombre")
        if not self.parameters:
            raise ValueError("El ejercicio debe tener al menos un parámetro modificable")
        if not self.analysis_questions:
            raise ValueError("El ejercicio debe tener al menos una pregunta de análisis")
        if len(self.analysis_questions) < 3:
            raise ValueError("Se recomiendan al menos 3 preguntas de análisis")
    
    def get_parameter(self, name: str) -> Optional[Parameter]:
        """Obtiene un parámetro por su nombre."""
        for param in self.parameters:
            if param.name == name:
                return param
        return None
    
    def get_parameter_names(self) -> List[str]:
        """Retorna lista con los nombres de todos los parámetros."""
        return [p.name for p in self.parameters]
    
    def to_dict(self) -> dict:
        """Convierte el ejercicio a diccionario para serialización."""
        return {
            'id': self.id,
            'name': self.name,
            'main_topic': self.main_topic,
            'educational_objective': self.educational_objective,
            'description': self.description,
            'parameters': [
                {
                    'name': p.name,
                    'display_name': p.display_name,
                    'description': p.description,
                    'type': p.param_type.value,
                    'default_value': p.default_value,
                    'min_value': p.min_value,
                    'max_value': p.max_value,
                    'unit': p.unit,
                    'step': p.step,
                    'options': p.options
                }
                for p in self.parameters
            ],
            'activity_type': self.activity_type.value,
            'activity_description': self.activity_description,
            'analysis_questions': self.analysis_questions,
            'expected_observation': self.expected_observation,
            'metadata': {
                'difficulty': self.metadata.difficulty.value if self.metadata.difficulty else None,
                'category': self.metadata.category,
                'tags': self.metadata.tags,
                'estimated_time': self.metadata.estimated_time,
                'creation_date': self.metadata.creation_date.isoformat(),
                'author': self.metadata.author,
                'version': self.metadata.version
            }
        }
