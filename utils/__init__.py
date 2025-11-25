"""
Paquete de utilidades para la aplicación de simulación.
Incluye estilos, gráficos, simuladores y generadores de ejercicios.
"""

from .styles import COLORS, FONTS, DIMENSIONS, ICONS
from .graph_helper import GraphCanvas, Graph3DCanvas

# Simuladores
from .simulator import (
    NewtonCoolingSimulator,
    VanDerPolSimulator,
    SIRSimulator,
    RLCSimulator,
    LorenzSimulator,
    HopfSimulator,
    LogisticSimulator,
    VerhulstSimulator,
    OrbitalSimulator,
    DamperSimulator,
    ButterflySimulator
)

# Generadores de ejercicios
from .ejercicio_generator import EjercicioGenerator

# Sistema de evaluación
from .evaluador import Evaluador
from .ejercicio_state import EjercicioState

__all__ = [
    # Estilos y UI
    'COLORS',
    'FONTS',
    'DIMENSIONS',
    'ICONS',
    'GraphCanvas',
    'Graph3DCanvas',
    
    # Simuladores
    'NewtonCoolingSimulator',
    'VanDerPolSimulator',
    'SIRSimulator',
    'RLCSimulator',
    'LorenzSimulator',
    'HopfSimulator',
    'LogisticSimulator',
    'VerhulstSimulator',
    'OrbitalSimulator',
    'DamperSimulator',
    'ButterflySimulator',
    
    # Generadores de ejercicios
    'EjercicioGenerator',
    
    # Evaluación
    'Evaluador',
    'EjercicioState'
]
