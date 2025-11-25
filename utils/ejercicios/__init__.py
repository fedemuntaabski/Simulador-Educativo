"""
Paquete de generación de ejercicios educativos.
Modularizado siguiendo principios DRY y KISS.
"""

from .base import EjercicioBase
from .generator import EjercicioGenerator
from .preguntas import PreguntasPool

__all__ = ['EjercicioGenerator', 'EjercicioBase', 'PreguntasPool']
