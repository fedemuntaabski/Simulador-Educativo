"""
Página de simulación de la Ley de Enfriamiento de Newton.
Versión refactorizada usando clase base, con soporte para modo laboratorio.
"""

import tkinter as tk
import numpy as np
from pages.base_simulator import BaseSimulatorPage
from utils.styles import COLORS, FONTS, GRAPH_STYLE
from utils.graph_helper import GraphCanvas
from utils.simulator import NewtonCoolingSimulator
from utils.ejercicio_state import EjercicioState


class NewtonPage(BaseSimulatorPage):
    """
    Página para simular la Ley de Enfriamiento de Newton.
    Integrada con el sistema de ejercicios del laboratorio.
    """
    
    TITLE = "Ley de Enfriamiento de Newton"
    ICON = "🌡️"
    
    def __init__(self, parent):
        # Verificar ejercicio activo antes de inicializar
        self.tiene_ejercicio = False
        self.parametros_ejercicio = None
        if EjercicioState.tiene_ejercicio() and EjercicioState.get_sistema_ejercicio() == 'newton':
            self.tiene_ejercicio = True
            self.parametros_ejercicio = EjercicioState.get_parametros_ejercicio()
        
        super().__init__(parent)
    
    def _init_parameters(self):
        """Define los parámetros específicos de enfriamiento de Newton."""
        self.parameters = [
            ('T0', 'Temperatura Inicial (°C)', 0, 200, 1, 100.0, 2),
            ('T_env', 'Temperatura Ambiente (°C)', -20, 50, 0.5, 25.0, 2),
            ('k', 'Constante k (min⁻¹)', 0.01, 1.0, 0.01, 0.1, 2),
            ('t_max', 'Tiempo de Simulación (min)', 10, 200, 5, 50.0, 0),
        ]
    
    def _get_equations_info(self):
        """Información de las ecuaciones de Newton."""
        return {
            'title': 'Información del Modelo',
            'equations': [
                'dT/dt = -k(T - T_amb)',
                'T(t) = T_amb + (T₀ - T_amb)e^(-kt)'
            ],
            'note': 'τ = 1/k (constante de tiempo)'
        }
    
    def _create_widgets(self):
        """Sobrescribe para agregar elementos específicos de Newton."""
        # Header con título
        header_frame = tk.Frame(self, bg=COLORS['accent'], height=70)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text=f"{self.ICON} {self.TITLE}",
            font=('Segoe UI', 18, 'bold'),
            bg=COLORS['accent'],
            fg='white'
        ).pack(expand=True)
        
        # Banner de ejercicio activo
        if self.tiene_ejercicio:
            self._create_ejercicio_banner()
        
        # Información teórica compacta
        info_frame = tk.LabelFrame(
            self,
            text="📚 Información del Modelo",
            font=FONTS['section_title'],
            bg='white',
            fg=COLORS['text_dark']
        )
        info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            info_frame,
            text=(
                "Ecuación: dT/dt = -k(T - T_amb)  |  "
                "Solución: T(t) = T_amb + (T₀ - T_amb)e^(-kt)  |  "
                "τ = 1/k (constante de tiempo)"
            ),
            font=('Segoe UI', 9),
            bg='white',
            fg=COLORS['text_muted']
        ).pack(padx=15, pady=10)
        
        # Controles
        controls_frame = tk.LabelFrame(
            self,
            text="⚙️ Parámetros",
            font=FONTS['section_title'],
            bg='white'
        )
        controls_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self._create_newton_controls(controls_frame)
        
        # Gráfico
        graph_frame = tk.LabelFrame(
            self,
            text="📊 Simulación",
            font=FONTS['section_title'],
            bg='white'
        )
        graph_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.graph = GraphCanvas(graph_frame, figsize=(10, 5))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def _create_ejercicio_banner(self):
        """Crea banner de ejercicio activo."""
        banner = tk.Frame(self, bg='#4CAF50')
        banner.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            banner,
            text=f"📋 Ejercicio Activo: {EjercicioState.get_info_ejercicio()}",
            font=('Segoe UI', 10, 'bold'),
            bg='#4CAF50',
            fg='white'
        ).pack(side=tk.LEFT, padx=15, pady=8)
        
        tk.Button(
            banner,
            text="⚙ Cargar Parámetros",
            font=('Segoe UI', 9),
            bg='white',
            fg='#4CAF50',
            command=self._cargar_parametros_ejercicio,
            padx=10,
            pady=5
        ).pack(side=tk.RIGHT, padx=15, pady=5)
    
    def _create_newton_controls(self, parent):
        """Crea controles específicos para Newton."""
        inner = tk.Frame(parent, bg='white')
        inner.pack(fill=tk.X, padx=15, pady=10)
        
        for param_config in self.parameters:
            self._create_newton_slider(inner, *param_config)
        
        # Botón simular
        tk.Button(
            inner,
            text="▶ Ejecutar Simulación",
            font=('Segoe UI', 12, 'bold'),
            bg=COLORS['success'],
            fg='white',
            command=self.run_simulation,
            pady=10,
            padx=30
        ).pack(pady=15)
    
    def _create_newton_slider(self, parent, param_id, label, min_val, max_val, res, default, decimals):
        """Crea un slider específico para Newton con estilo diferente."""
        frame = tk.Frame(parent, bg='white')
        frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            frame,
            text=label,
            font=('Segoe UI', 10),
            bg='white',
            width=30,
            anchor='w'
        ).pack(side=tk.LEFT)
        
        var = tk.DoubleVar(value=default)
        display_var = tk.StringVar(value=f"{default:.{decimals}f}")
        
        self.param_vars[param_id] = var
        self.display_vars[param_id] = display_var
        
        slider = tk.Scale(
            frame,
            from_=min_val,
            to=max_val,
            resolution=res,
            orient=tk.HORIZONTAL,
            variable=var,
            bg='white',
            length=300,
            showvalue=False,
            command=lambda v, dv=display_var, d=decimals: dv.set(f"{float(v):.{d}f}")
        )
        slider.pack(side=tk.LEFT, padx=10)
        
        tk.Label(
            frame,
            textvariable=display_var,
            font=('Segoe UI', 10, 'bold'),
            bg='white',
            fg=COLORS['accent'],
            width=8
        ).pack(side=tk.LEFT)
    
    def _cargar_parametros_ejercicio(self):
        """Carga parámetros del ejercicio en los sliders."""
        if self.parametros_ejercicio:
            for param, valor in self.parametros_ejercicio.items():
                if param in self.param_vars:
                    self.param_vars[param].set(valor)
                    if param in self.display_vars:
                        decimals = 2
                        for p in self.parameters:
                            if p[0] == param:
                                decimals = p[6]
                                break
                        self.display_vars[param].set(f"{valor:.{decimals}f}")
    
    def _setup_initial_graph(self):
        """Configuración inicial del gráfico."""
        pass  # Newton no usa esta configuración inicial
    
    def run_simulation(self):
        """Ejecuta la simulación con gráficos mejorados."""
        T0 = self.get_param('T0')
        T_env = self.get_param('T_env')
        k = self.get_param('k')
        t_max = self.get_param('t_max')
        
        # Simular
        t, T = NewtonCoolingSimulator.simulate(T0, T_env, k, t_max)
        
        # Graficar
        self.graph.clear()
        
        # Color según enfriamiento o calentamiento
        color = GRAPH_STYLE['colors']['primary'] if T0 > T_env else GRAPH_STYLE['colors']['secondary']
        self.graph.plot(t, T, color=color, label='T(t)')
        
        # Línea de temperatura ambiente
        self.graph.ax.axhline(y=T_env, color=GRAPH_STYLE['colors']['tertiary'], 
                             linestyle='--', linewidth=2, alpha=0.7, 
                             label=f'T_amb = {T_env:.2f}°C')
        
        # Marcar constante de tiempo
        tau = 1/k
        if tau < t_max:
            T_tau = T_env + (T0 - T_env) * np.exp(-1)
            self.graph.scatter([tau], [T_tau], color=GRAPH_STYLE['colors']['secondary'], 
                              s=100, marker='o', zorder=5, label=f'τ = {tau:.2f} min')
        
        self.graph.set_labels(
            'Tiempo (min)',
            'Temperatura (°C)',
            f'Enfriamiento de Newton (k = {k:.2f})'
        )
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
