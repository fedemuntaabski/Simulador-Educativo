"""
Página de simulación del Circuito RLC.
Versión refactorizada usando clase base.
"""

import tkinter as tk
from pages.base_simulator import BaseSimulatorPage
from utils.styles import GRAPH_STYLE
from utils.simulator import RLCSimulator


class RLCPage(BaseSimulatorPage):
    """
    Página para simular un circuito RLC serie.
    """
    
    TITLE = "Circuito RLC Serie"
    ICON = "⚡"
    
    def _init_parameters(self):
        """Define los parámetros específicos del circuito RLC."""
        self.parameters = [
            ('R', 'Resistencia R (Ω)', 1, 100, 1, 10.0, 2),
            ('L', 'Inductancia L (H)', 0.01, 1.0, 0.01, 0.1, 2),
            ('C', 'Capacitancia C (F)', 0.0001, 0.01, 0.0001, 0.001, 4),
            ('V0', 'Voltaje V₀ (V)', 0, 50, 1, 10.0, 2),
            ('I0', 'Corriente Inicial I₀ (A)', 0, 5, 0.1, 0.0, 2),
            ('Q0', 'Carga Inicial Q₀ (C)', 0, 0.1, 0.001, 0.0, 3),
            ('t_max', 'Tiempo Máximo (s)', 0.1, 2.0, 0.1, 0.5, 2),
        ]
    
    def _get_equations_info(self):
        """Información de las ecuaciones del circuito RLC."""
        return {
            'title': 'Ecuaciones',
            'equations': [
                'L(dI/dt) + RI + Q/C = V₀',
                'dQ/dt = I'
            ]
        }
    
    def _setup_initial_graph(self):
        """Configuración inicial del gráfico."""
        self.graph.set_labels(
            xlabel='Tiempo (s)',
            ylabel='Corriente (A)',
            title='Circuito RLC Serie'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del circuito RLC con dos ejes Y."""
        R = self.get_param('R')
        L = self.get_param('L')
        C = self.get_param('C')
        V0 = self.get_param('V0')
        I0 = self.get_param('I0')
        Q0 = self.get_param('Q0')
        t_max = self.get_param('t_max')
        
        # Simular
        t, I, Q, V = RLCSimulator.simulate(I0, Q0, R, L, C, V0, t_max)
        
        # Graficar corriente y voltaje con dos ejes Y
        self.graph.clear()
        
        ax1 = self.graph.ax
        ax2 = ax1.twinx()
        
        # Estilo de ejes
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_color(GRAPH_STYLE['colors']['primary'])
        ax1.spines['bottom'].set_color('#bdc3c7')
        
        # Corriente en eje izquierdo
        line1 = ax1.plot(t, I, color=GRAPH_STYLE['colors']['primary'], 
                        linewidth=GRAPH_STYLE['linewidth'], label='Corriente I(t)')
        ax1.set_xlabel('Tiempo (s)', fontsize=GRAPH_STYLE['label_fontsize'], 
                      color='#2c3e50', fontweight='medium')
        ax1.set_ylabel('Corriente (A)', color=GRAPH_STYLE['colors']['primary'],
                      fontsize=GRAPH_STYLE['label_fontsize'], fontweight='medium')
        ax1.tick_params(axis='y', labelcolor=GRAPH_STYLE['colors']['primary'])
        
        # Voltaje en eje derecho
        line2 = ax2.plot(t, V, color=GRAPH_STYLE['colors']['secondary'], 
                        linewidth=GRAPH_STYLE['linewidth'], label='Voltaje V_C(t)')
        ax2.set_ylabel('Voltaje (V)', color=GRAPH_STYLE['colors']['secondary'],
                      fontsize=GRAPH_STYLE['label_fontsize'], fontweight='medium')
        ax2.tick_params(axis='y', labelcolor=GRAPH_STYLE['colors']['secondary'])
        ax2.spines['right'].set_color(GRAPH_STYLE['colors']['secondary'])
        ax2.spines['top'].set_visible(False)
        
        # Leyenda combinada
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='upper right', fontsize=GRAPH_STYLE['legend_fontsize'],
                  framealpha=0.9, edgecolor='#bdc3c7')
        
        ax1.set_title(f'Circuito RLC (R = {R:.2f}Ω, L = {L:.2f}H, C = {C:.4f}F)', 
                     fontsize=GRAPH_STYLE['title_fontsize'], color='#2c3e50', fontweight='bold')
        ax1.grid(True, alpha=GRAPH_STYLE['grid_alpha'], linestyle='--', color='#bdc3c7')
        
        self.graph.tight_layout()
        self.graph.canvas.draw()
