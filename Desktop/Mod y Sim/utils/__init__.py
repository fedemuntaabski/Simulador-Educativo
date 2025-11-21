"""
Paquete de utilidades para la aplicación de simulación.
"""

from .styles import COLORS, FONTS, DIMENSIONS
from .graph_helper import GraphCanvas, Graph3DCanvas
from .simulator import (
    NewtonCoolingSimulator,
    VanDerPolSimulator,
    SIRSimulator,
    RLCSimulator,
    LorenzSimulator
)

__all__ = [
    'COLORS',
    'FONTS',
    'DIMENSIONS',
    'GraphCanvas',
    'Graph3DCanvas',
    'NewtonCoolingSimulator',
    'VanDerPolSimulator',
    'SIRSimulator',
    'RLCSimulator',
    'LorenzSimulator'
]
