"""
Página de simulación de la Ley de Enfriamiento de Newton.
Simplificada e integrada con el modo laboratorio.
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from utils.simulator import NewtonCoolingSimulator
from utils.graph_helper import GraphCanvas
from utils.ejercicio_state import EjercicioState
from utils.styles import COLORS, FONTS


class NewtonPage(tk.Frame):
    """
    Página para simular la Ley de Enfriamiento de Newton.
    Integrada con el sistema de ejercicios del laboratorio.
    """
    
    def __init__(self, parent):
        """Inicializa la página de enfriamiento de Newton."""
        super().__init__(parent, bg=COLORS['content_bg'])
        
        self.parametros = {
            'T0': 100.0,
            'T_env': 25.0,
            'k': 0.1,
            't_max': 50.0
        }
        
        # Verificar ejercicio activo
        self.tiene_ejercicio = False
        self.parametros_ejercicio = None
        if EjercicioState.tiene_ejercicio() and EjercicioState.get_sistema_ejercicio() == 'newton':
            self.tiene_ejercicio = True
            self.parametros_ejercicio = EjercicioState.get_parametros_ejercicio()
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la interfaz."""
        # Título
        header_frame = tk.Frame(self, bg=COLORS['accent'], height=70)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="🌡️ Ley de Enfriamiento de Newton",
            font=('Segoe UI', 18, 'bold'),
            bg=COLORS['accent'],
            fg='white'
        ).pack(expand=True)
        
        # Banner de ejercicio activo
        if self.tiene_ejercicio:
            self.create_ejercicio_banner()
        
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
        
        self.create_controls(controls_frame)
        
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
    
    def create_ejercicio_banner(self):
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
            command=self.cargar_parametros_ejercicio,
            padx=10,
            pady=5
        ).pack(side=tk.RIGHT, padx=15, pady=5)
    
    def create_controls(self, parent):
        """Crea los controles de parámetros."""
        inner = tk.Frame(parent, bg='white')
        inner.pack(fill=tk.X, padx=15, pady=10)
        
        # Definir parámetros
        params = [
            ('T0', 'Temperatura Inicial (°C)', 0, 200, 1),
            ('T_env', 'Temperatura Ambiente (°C)', -20, 50, 0.5),
            ('k', 'Constante k (min⁻¹)', 0.01, 1.0, 0.01),
            ('t_max', 'Tiempo de Simulación (min)', 10, 200, 5)
        ]
        
        self.sliders = {}
        
        for param_id, label, min_val, max_val, res in params:
            frame = tk.Frame(inner, bg='white')
            frame.pack(fill=tk.X, pady=5)
            
            tk.Label(
                frame,
                text=label,
                font=('Segoe UI', 10),
                bg='white',
                width=30,
                anchor='w'
            ).pack(side=tk.LEFT)
            
            var = tk.DoubleVar(value=self.parametros[param_id])
            
            slider = tk.Scale(
                frame,
                from_=min_val,
                to=max_val,
                resolution=res,
                orient=tk.HORIZONTAL,
                variable=var,
                bg='white',
                length=300,
                command=lambda v, p=param_id: self.update_param(p, v)
            )
            slider.pack(side=tk.LEFT, padx=10)
            
            tk.Label(
                frame,
                textvariable=var,
                font=('Segoe UI', 10),
                bg='white',
                width=8
            ).pack(side=tk.LEFT)
            
            self.sliders[param_id] = var
        
        # Botón simular
        tk.Button(
            inner,
            text="▶ Ejecutar Simulación",
            font=('Segoe UI', 12, 'bold'),
            bg=COLORS['success'],
            fg='white',
            command=self.ejecutar_simulacion,
            pady=10,
            padx=30
        ).pack(pady=15)
    
    def update_param(self, param_id, value):
        """Actualiza un parámetro."""
        self.parametros[param_id] = float(value)
    
    def cargar_parametros_ejercicio(self):
        """Carga parámetros del ejercicio en los sliders."""
        if self.parametros_ejercicio:
            for param, valor in self.parametros_ejercicio.items():
                if param in self.sliders:
                    self.sliders[param].set(valor)
                    self.parametros[param] = valor
    
    def ejecutar_simulacion(self):
        """Ejecuta la simulación."""
        T0 = self.parametros['T0']
        T_env = self.parametros['T_env']
        k = self.parametros['k']
        t_max = self.parametros['t_max']
        
        # Simular
        t, T = NewtonCoolingSimulator.simulate(T0, T_env, k, t_max)
        
        # Graficar
        self.graph.clear()
        
        color = 'b' if T0 > T_env else 'r'
        self.graph.plot(t, T, color=color, linewidth=2.5, label='T(t)')
        
        self.graph.ax.axhline(y=T_env, color='green', linestyle='--', 
                             linewidth=2, alpha=0.7, label=f'T_amb = {T_env}°C')
        
        # Marcar constante de tiempo
        tau = 1/k
        if tau < t_max:
            T_tau = T_env + (T0 - T_env) * np.exp(-1)
            self.graph.ax.plot(tau, T_tau, 'ro', markersize=8, 
                              label=f'τ = {tau:.1f} min')
        
        self.graph.set_labels(
            'Tiempo (min)',
            'Temperatura (°C)',
            f'Enfriamiento de Newton (k={k})'
        )
        self.graph.grid(True, alpha=0.3)
        self.graph.legend()
        self.graph.tight_layout()
