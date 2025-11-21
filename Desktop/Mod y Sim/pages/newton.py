"""
Página de simulación de la Ley de Enfriamiento de Newton.
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS
from utils.graph_helper import GraphCanvas
from utils.simulator import NewtonCoolingSimulator


class NewtonPage(tk.Frame):
    """
    Página para simular la Ley de Enfriamiento de Newton.
    Ecuación: dT/dt = -k(T - T_ambiente)
    """
    
    def __init__(self, parent):
        """
        Inicializa la página de enfriamiento de Newton.
        
        Args:
            parent: Widget padre
        """
        super().__init__(parent, bg=COLORS['content_bg'])
        
        # Variables de parámetros
        self.T0_var = tk.DoubleVar(value=100.0)
        self.T_env_var = tk.DoubleVar(value=25.0)
        self.k_var = tk.DoubleVar(value=0.1)
        self.t_max_var = tk.DoubleVar(value=50.0)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la página."""
        # Contenedor principal
        main_container = tk.Frame(self, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Configurar grid
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        # Panel de controles (izquierda)
        self.create_control_panel(main_container)
        
        # Panel de gráfico (derecha)
        self.create_graph_panel(main_container)
    
    def create_control_panel(self, parent):
        """Crea el panel de controles."""
        control_frame = tk.Frame(parent, bg=COLORS['header'], relief=tk.RAISED, borderwidth=2)
        control_frame.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        
        # Título del panel
        title = tk.Label(
            control_frame,
            text="⚙️ Parámetros",
            font=FONTS['section_title'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        title.pack(pady=(15, 20), padx=20)
        
        # Temperatura inicial
        self.create_parameter_control(
            control_frame,
            "Temperatura Inicial (°C)",
            self.T0_var,
            0, 200, 1
        )
        
        # Temperatura ambiente
        self.create_parameter_control(
            control_frame,
            "Temperatura Ambiente (°C)",
            self.T_env_var,
            0, 50, 0.5
        )
        
        # Constante k
        self.create_parameter_control(
            control_frame,
            "Constante k (enfriamiento)",
            self.k_var,
            0.01, 1.0, 0.01
        )
        
        # Tiempo máximo
        self.create_parameter_control(
            control_frame,
            "Tiempo Máximo (min)",
            self.t_max_var,
            10, 200, 5
        )
        
        # Botones
        button_frame = tk.Frame(control_frame, bg=COLORS['header'])
        button_frame.pack(pady=30, padx=20, fill=tk.X)
        
        simulate_btn = tk.Button(
            button_frame,
            text="▶ Ejecutar Simulación",
            font=FONTS['button'],
            bg=COLORS['success'],
            fg='white',
            cursor="hand2",
            command=self.run_simulation,
            pady=10
        )
        simulate_btn.pack(fill=tk.X, pady=(0, 10))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Limpiar Gráfico",
            font=FONTS['button'],
            bg=COLORS['danger'],
            fg='white',
            cursor="hand2",
            command=self.clear_graph,
            pady=10
        )
        clear_btn.pack(fill=tk.X)
        
        # Información del modelo
        info_frame = tk.Frame(control_frame, bg='white', relief=tk.SUNKEN, borderwidth=1)
        info_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        info_title = tk.Label(
            info_frame,
            text="📋 Ecuación",
            font=FONTS['label'],
            bg='white',
            fg=COLORS['text_dark']
        )
        info_title.pack(pady=(10, 5))
        
        equation = tk.Label(
            info_frame,
            text="dT/dt = -k(T - T_amb)",
            font=('Courier New', 11, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        equation.pack(pady=(0, 10))
    
    def create_parameter_control(self, parent, label_text, variable, min_val, max_val, resolution):
        """
        Crea un control de parámetro con slider y valor.
        
        Args:
            parent: Widget padre
            label_text: Texto de la etiqueta
            variable: Variable de Tkinter asociada
            min_val: Valor mínimo del slider
            max_val: Valor máximo del slider
            resolution: Resolución del slider
        """
        container = tk.Frame(parent, bg=COLORS['header'])
        container.pack(pady=10, padx=20, fill=tk.X)
        
        # Etiqueta
        label = tk.Label(
            container,
            text=label_text,
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        label.pack(anchor='w')
        
        # Frame para slider y valor
        slider_frame = tk.Frame(container, bg=COLORS['header'])
        slider_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Slider
        slider = ttk.Scale(
            slider_frame,
            from_=min_val,
            to=max_val,
            variable=variable,
            orient=tk.HORIZONTAL,
            length=DIMENSIONS['slider_length']
        )
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Valor actual
        value_label = tk.Label(
            slider_frame,
            textvariable=variable,
            font=FONTS['value'],
            bg=COLORS['header'],
            fg=COLORS['accent'],
            width=8
        )
        value_label.pack(side=tk.LEFT, padx=(10, 0))
    
    def create_graph_panel(self, parent):
        """Crea el panel del gráfico."""
        graph_frame = tk.Frame(parent, bg='white', relief=tk.SUNKEN, borderwidth=2)
        graph_frame.grid(row=0, column=1, sticky="nsew")
        
        # Canvas de Matplotlib
        self.graph = GraphCanvas(graph_frame, figsize=(9, 6))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configuración inicial del gráfico
        self.graph.set_labels(
            xlabel='Tiempo (minutos)',
            ylabel='Temperatura (°C)',
            title='Ley de Enfriamiento de Newton'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del enfriamiento de Newton."""
        # Obtener parámetros
        T0 = self.T0_var.get()
        T_env = self.T_env_var.get()
        k = self.k_var.get()
        t_max = self.t_max_var.get()
        
        # Simular
        t, T = NewtonCoolingSimulator.simulate(T0, T_env, k, t_max)
        
        # Graficar
        self.graph.clear()
        self.graph.plot(t, T, 'b-', linewidth=2, label=f'T₀={T0}°C, k={k}')
        self.graph.ax.axhline(y=T_env, color='r', linestyle='--', linewidth=1.5, 
                              label=f'T_ambiente={T_env}°C')
        self.graph.set_labels(
            xlabel='Tiempo (minutos)',
            ylabel='Temperatura (°C)',
            title='Ley de Enfriamiento de Newton'
        )
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
        self.graph.set_labels(
            xlabel='Tiempo (minutos)',
            ylabel='Temperatura (°C)',
            title='Ley de Enfriamiento de Newton'
        )
        self.graph.grid(True)
