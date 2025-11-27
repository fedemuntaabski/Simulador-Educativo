"""
Página de simulación del Oscilador de Van der Pol.
Versión refactorizada usando clase base.
"""

from pages.base_simulator import BaseSimulatorPage
from utils.styles import GRAPH_STYLE
from utils.simulator import VanDerPolSimulator


class VanDerPolPage(BaseSimulatorPage):
    """
    Página para simular el oscilador de Van der Pol.
    Sistema: dx/dt = y, dy/dt = μ(1-x²)y - x
    """
    
    TITLE = "Oscilador de Van der Pol"
    ICON = "📈"
    
    def _init_parameters(self):
        """Define los parámetros específicos de Van der Pol."""
        # (param_id, label, min_val, max_val, resolution, default, decimals)
        self.parameters = [
            ('x0', 'Posición Inicial x(0)', -3, 3, 0.1, 1.0, 2),
            ('v0', 'Velocidad Inicial dx/dt(0)', -3, 3, 0.1, 0.0, 2),
            ('mu', 'Parámetro μ (no linealidad)', 0.1, 10.0, 0.1, 1.0, 2),
            ('t_max', 'Tiempo Máximo', 10, 100, 5, 50.0, 0),
        ]
    
    def _get_equations_info(self):
        """Información de las ecuaciones de Van der Pol."""
        return {
            'title': 'Ecuaciones',
            'equations': [
                'dx/dt = y',
                'dy/dt = μ(1-x²)y - x'
            ]
        }
    
    def _setup_initial_graph(self):
        """Configuración inicial del gráfico de fase."""
        self.graph.set_labels(
            xlabel='x (Posición)',
            ylabel='dx/dt (Velocidad)',
            title='Diagrama de Fase - Oscilador de Van der Pol'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del oscilador de Van der Pol."""
        x0 = self.get_param('x0')
        v0 = self.get_param('v0')
        mu = self.get_param('mu')
        t_max = self.get_param('t_max')
        
        # Simular
        t, x, v = VanDerPolSimulator.simulate(x0, v0, mu, t_max)
        
        # Graficar retrato de fase
        self.graph.clear()
        self.graph.plot(x, v, color=GRAPH_STYLE['colors']['primary'], 
                       label=f'μ = {mu:.2f}')
        self.graph.scatter([x[0]], [v[0]], color=GRAPH_STYLE['colors']['start_marker'], 
                          s=100, marker='o', label='Inicio', zorder=5)
        self.graph.scatter([x[-1]], [v[-1]], color=GRAPH_STYLE['colors']['end_marker'], 
                          s=100, marker='s', label='Final', zorder=5)
        self.graph.set_labels(
            xlabel='x (Posición)',
            ylabel='dx/dt (Velocidad)',
            title=f'Diagrama de Fase - Van der Pol (μ = {mu:.2f})'
        )
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
