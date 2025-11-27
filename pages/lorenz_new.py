"""
Página de simulación del Sistema de Lorenz (Atractor Caótico).
Versión refactorizada usando clase base.
"""

import tkinter as tk
from tkinter import ttk
from pages.base_simulator import BaseSimulatorPage
from utils.styles import COLORS, FONTS, DIMENSIONS, GRAPH_STYLE
from utils.graph_helper import Graph3DCanvas
from utils.simulator import LorenzSimulator


class LorenzPage(BaseSimulatorPage):
    """
    Página para simular el sistema de Lorenz (atractor caótico 3D).
    """
    
    TITLE = "Sistema de Lorenz"
    ICON = "🌀"
    
    def _init_parameters(self):
        """Define los parámetros específicos del sistema de Lorenz."""
        self.parameters = [
            ('x0', 'x₀', -10, 10, 0.5, 1.0, 2),
            ('y0', 'y₀', -10, 10, 0.5, 1.0, 2),
            ('z0', 'z₀', -10, 10, 0.5, 1.0, 2),
            ('sigma', 'σ (sigma)', 1, 20, 0.5, 10.0, 2),
            ('rho', 'ρ (rho)', 1, 50, 1, 28.0, 2),
            ('beta', 'β (beta)', 0.5, 5.0, 0.1, 2.667, 3),
            ('t_max', 'Tiempo Máximo', 10, 100, 5, 40.0, 0),
        ]
    
    def _get_equations_info(self):
        """Información de las ecuaciones de Lorenz."""
        return {
            'title': 'Ecuaciones de Lorenz',
            'equations': [
                'dx/dt = σ(y - x)',
                'dy/dt = x(ρ - z) - y',
                'dz/dt = xy - βz'
            ]
        }
    
    def _create_control_panel(self, parent):
        """Crea el panel de controles con secciones para condiciones iniciales y parámetros."""
        control_frame = tk.Frame(parent, bg=COLORS['header'], relief=tk.RAISED, borderwidth=2)
        control_frame.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        
        tk.Label(
            control_frame,
            text="⚙️ Parámetros",
            font=FONTS['section_title'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        ).pack(pady=(15, 20), padx=20)
        
        # Sección: Condiciones Iniciales
        tk.Label(
            control_frame,
            text="Condiciones Iniciales:",
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        ).pack(pady=(5, 10), padx=20, anchor='w')
        
        # Crear controles de condiciones iniciales
        for param_config in self.parameters[:3]:  # x0, y0, z0
            self._create_parameter_control(control_frame, *param_config)
        
        # Sección: Parámetros del Sistema
        tk.Label(
            control_frame,
            text="Parámetros del Sistema:",
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        ).pack(pady=(15, 10), padx=20, anchor='w')
        
        # Crear controles de parámetros del sistema
        for param_config in self.parameters[3:]:  # sigma, rho, beta, t_max
            self._create_parameter_control(control_frame, *param_config)
        
        self._create_action_buttons(control_frame)
        self._create_info_panel(control_frame)
    
    def _create_graph_panel(self, parent):
        """Crea el panel del gráfico 3D."""
        graph_frame = tk.Frame(parent, bg='white', relief=tk.SUNKEN, borderwidth=2)
        graph_frame.grid(row=0, column=1, sticky="nsew")
        
        self.graph = Graph3DCanvas(graph_frame, figsize=(9, 6))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self._setup_initial_graph()
    
    def _setup_initial_graph(self):
        """Configuración inicial del gráfico 3D."""
        self.graph.set_labels(
            xlabel='X',
            ylabel='Y',
            zlabel='Z',
            title='Atractor de Lorenz'
        )
    
    def run_simulation(self):
        """Ejecuta la simulación del sistema de Lorenz."""
        x0 = self.get_param('x0')
        y0 = self.get_param('y0')
        z0 = self.get_param('z0')
        sigma = self.get_param('sigma')
        rho = self.get_param('rho')
        beta = self.get_param('beta')
        t_max = self.get_param('t_max')
        
        # Simular
        t, x, y, z = LorenzSimulator.simulate(x0, y0, z0, sigma, rho, beta, t_max)
        
        # Graficar en 3D
        self.graph.clear()
        
        # Gradiente de color basado en el tiempo
        colors = t
        
        self.graph.ax.plot(x, y, z, linewidth=0.8, alpha=0.8, 
                          color=GRAPH_STYLE['colors']['primary'])
        self.graph.ax.scatter(x, y, z, c=colors, cmap='viridis', s=1, alpha=0.6)
        
        # Marcar inicio y fin
        self.graph.ax.scatter([x[0]], [y[0]], [z[0]], 
                             color=GRAPH_STYLE['colors']['success'], 
                             s=GRAPH_STYLE['marker_size'], marker='o', label='Inicio')
        self.graph.ax.scatter([x[-1]], [y[-1]], [z[-1]], 
                             color=GRAPH_STYLE['colors']['danger'], 
                             s=GRAPH_STYLE['marker_size'], marker='s', label='Final')
        
        self.graph.set_labels(
            xlabel='X',
            ylabel='Y',
            zlabel='Z',
            title=f'Atractor de Lorenz (σ={sigma:.2f}, ρ={rho:.2f}, β={beta:.2f})'
        )
        
        self.graph.legend()
        self.graph.tight_layout()
    
    def clear_graph(self):
        """Limpia el gráfico 3D."""
        self.graph.clear()
        self._setup_initial_graph()
