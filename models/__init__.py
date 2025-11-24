"""
Modelos de datos para ejercicios educativos del laboratorio de sistemas dinámicos.
Incluye estructuras completas, factory pattern y ejemplos predefinidos.
"""

from .exercise import (
    Exercise, 
    Parameter, 
    ExerciseMetadata,
    ParameterType,
    ActivityType,
    DifficultyLevel
)
from .exercise_factory import ExerciseFactory, ExerciseValidator
from .example_exercises import (
    create_pendulum_exercise,
    create_lorenz_exercise,
    create_sir_exercise,
    load_example_exercises
)

__all__ = [
    # Clases principales
    'Exercise',
    'Parameter',
    'ExerciseMetadata',
    'ParameterType',
    'ActivityType',
    'DifficultyLevel',
    'ExerciseFactory',
    'ExerciseValidator',
    
    # Funciones de creación
    'create_pendulum_exercise',
    'create_lorenz_exercise',
    'create_sir_exercise',
    'load_example_exercises'
]

__version__ = '1.0.0'
