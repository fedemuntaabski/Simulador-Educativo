"""
Generador automático de ejercicios educacionales para sistemas dinámicos.

Este archivo actúa como wrapper de compatibilidad.
La implementación modularizada está en utils/ejercicios/

Principios de diseño:
- DRY: Métodos helper para evitar repetición
- KISS: Lógica simple y clara
- Separación: Datos de preguntas separados de lógica
"""

# Re-exportar desde el módulo modularizado
from .ejercicios import EjercicioGenerator, EjercicioBase, PreguntasPool

__all__ = ['EjercicioGenerator', 'EjercicioBase', 'PreguntasPool']
