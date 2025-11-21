"""
Paquete de páginas de la aplicación.
"""

from .inicio import InicioPage
from .newton import NewtonPage
from .van_der_pol import VanDerPolPage
from .sir import SIRPage
from .rlc import RLCPage
from .lorenz import LorenzPage

__all__ = [
    'InicioPage',
    'NewtonPage',
    'VanDerPolPage',
    'SIRPage',
    'RLCPage',
    'LorenzPage'
]
