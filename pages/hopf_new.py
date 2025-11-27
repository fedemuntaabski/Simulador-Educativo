"""
Página de simulación de la Bifurcación de Hopf.
Versión refactorizada usando clase base.
"""

from pages.base_simulator import BaseSimulatorPage
from utils.styles import GRAPH_STYLE
from utils.simulator import HopfSimulator


class HopfPage(BaseSimulatorPage):
    """
    Página para simular la bifurcación de Hopf.
    """
    
    TITLE = "Bifurcación de Hopf"
    ICON = "🔄"
    
    def _init_parameters(self):
        """Define los parámetros específicos de la bifurcación de Hopf."""
        self.parameters = [
            ('x0', 'x₀', -2, 2, 0.1, 0.1, 2),
            ('y0', 'y₀', -2, 2, 0.1, 0.1, 2),
            ('mu', 'μ (bifurcación)', -2, 3, 0.1, 0.5, 2),
            ('omega', 'ω (frecuencia)', 0.1, 3, 0.1, 1.0, 2),
            ('t_max', 'Tiempo Máximo', 10, 100, 5, 50.0, 0),
        ]
    
    def _get_equations_info(self):
        """Información de las ecuaciones de Hopf."""
        return {
            'title': 'Ecuaciones',
            'equations': [
                'dx/dt = μx - ωy - x(x²+y²)',
                'dy/dt = ωx + μy - y(x²+y²)'
            ],
            'note': 'μ < 0: Punto fijo estable\nμ > 0: Ciclo límite'
        }
    
    def _setup_initial_graph(self):
        """Configuración inicial del gráfico de fase."""
        self.graph.set_labels(
            xlabel='x',
            ylabel='y',
            title='Bifurcación de Hopf - Diagrama de Fase'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación de Hopf."""
        x0 = self.get_param('x0')
        y0 = self.get_param('y0')
        mu = self.get_param('mu')
        omega = self.get_param('omega')
        t_max = self.get_param('t_max')
        
        t, x, y = HopfSimulator.simulate(x0, y0, mu, omega, t_max)
        
        self.graph.clear()
        self.graph.plot(x, y, color=GRAPH_STYLE['colors']['primary'], 
                       linewidth=GRAPH_STYLE['linewidth'], label=f'μ={mu:.2f}')
        self.graph.scatter([x[0]], [y[0]], color=GRAPH_STYLE['colors']['success'], 
                          s=GRAPH_STYLE['marker_size'], marker='o', label='Inicio', zorder=5)
        self.graph.scatter([x[-1]], [y[-1]], color=GRAPH_STYLE['colors']['danger'], 
                          s=GRAPH_STYLE['marker_size'], marker='s', label='Final', zorder=5)
        
        title = f'Bifurcación de Hopf (μ={mu:.2f}) - '
        title += 'Punto Fijo Estable' if mu < 0 else 'Ciclo Límite'
        
        self.graph.set_labels(xlabel='x', ylabel='y', title=title)
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
