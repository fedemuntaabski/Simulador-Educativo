"""
Página de simulación del Modelo Epidemiológico SIR.
Versión refactorizada usando clase base.
"""

from pages.base_simulator import BaseSimulatorPage
from utils.styles import GRAPH_STYLE
from utils.simulator import SIRSimulator


class SIRPage(BaseSimulatorPage):
    """
    Página para simular el modelo epidemiológico SIR.
    S: Susceptibles, I: Infectados, R: Recuperados
    """
    
    TITLE = "Modelo Epidemiológico SIR"
    ICON = "🦠"
    
    def _init_parameters(self):
        """Define los parámetros específicos del modelo SIR."""
        self.parameters = [
            ('S0', 'Susceptibles Iniciales S(0)', 0, 1000, 10, 990.0, 0),
            ('I0', 'Infectados Iniciales I(0)', 0, 100, 1, 10.0, 0),
            ('R0', 'Recuperados Iniciales R(0)', 0, 100, 1, 0.0, 0),
            ('beta', 'Tasa de Contacto β', 0.1, 1.0, 0.05, 0.3, 2),
            ('gamma', 'Tasa de Recuperación γ', 0.01, 0.5, 0.01, 0.1, 2),
            ('t_max', 'Tiempo Máximo (días)', 50, 300, 10, 160.0, 0),
        ]
    
    def _get_equations_info(self):
        """Información de las ecuaciones SIR."""
        return {
            'title': 'Ecuaciones SIR',
            'equations': [
                'dS/dt = -βSI/N',
                'dI/dt = βSI/N - γI',
                'dR/dt = γI'
            ],
            'note': 'R₀ = β/γ'
        }
    
    def _setup_initial_graph(self):
        """Configuración inicial del gráfico."""
        self.graph.set_labels(
            xlabel='Tiempo (días)',
            ylabel='Población',
            title='Modelo Epidemiológico SIR'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del modelo SIR."""
        S0 = self.get_param('S0')
        I0 = self.get_param('I0')
        R0 = self.get_param('R0')
        beta = self.get_param('beta')
        gamma = self.get_param('gamma')
        t_max = self.get_param('t_max')
        
        # Simular
        t, S, I, R = SIRSimulator.simulate(S0, I0, R0, beta, gamma, t_max)
        
        # Calcular R₀
        R0_basic = beta / gamma
        
        # Graficar
        self.graph.clear()
        self.graph.plot(t, S, color=GRAPH_STYLE['colors']['primary'], label='Susceptibles (S)')
        self.graph.plot(t, I, color=GRAPH_STYLE['colors']['secondary'], label='Infectados (I)')
        self.graph.plot(t, R, color=GRAPH_STYLE['colors']['tertiary'], label='Recuperados (R)')
        
        self.graph.set_labels(
            xlabel='Tiempo (días)',
            ylabel='Población',
            title=f'Modelo SIR (R₀ = {R0_basic:.2f}, β = {beta:.2f}, γ = {gamma:.2f})'
        )
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
