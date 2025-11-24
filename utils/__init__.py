"""
Paquete de utilidades para la aplicación de simulación.
Incluye estilos, gráficos, simuladores y generadores de ejercicios.
"""

from .styles import COLORS, FONTS, DIMENSIONS
from .graph_helper import GraphCanvas, Graph3DCanvas

# Simuladores
from .simulator import (
    NewtonCoolingSimulator,
    VanDerPolSimulator,
    SIRSimulator,
    RLCSimulator,
    LorenzSimulator
)

# Generadores de ejercicios
from .ejercicio_generator import EjercicioGenerator
from .exercise_generator import generate_exercise

# Sistema de evaluación
from .evaluador import Evaluador
from .ejercicio_state import EjercicioState

__all__ = [
    # Estilos y UI
    'COLORS',
    'FONTS',
    'DIMENSIONS',
    'GraphCanvas',
    'Graph3DCanvas',
    
    # Simuladores
    'NewtonCoolingSimulator',
    'VanDerPolSimulator',
    'SIRSimulator',
    'RLCSimulator',
    'LorenzSimulator',
    
    # Generadores de ejercicios
    'EjercicioGenerator',
    'generate_exercise',
    
    # Evaluación
    'Evaluador',
    'EjercicioState'
]
