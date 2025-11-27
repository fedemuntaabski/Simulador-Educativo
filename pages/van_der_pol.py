"""
Página de simulación del Oscilador de Van der Pol.
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS, GRAPH_STYLE
from utils.graph_helper import GraphCanvas
from utils.simulator import VanDerPolSimulator


class VanDerPolPage(tk.Frame):
    """
    Página para simular el oscilador de Van der Pol.
    Sistema: dx/dt = y, dy/dt = μ(1-x²)y - x
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        # Variables de parámetros
        self.x0_var = tk.DoubleVar(value=1.0)
        self.v0_var = tk.DoubleVar(value=0.0)
        self.mu_var = tk.DoubleVar(value=1.0)
        self.t_max_var = tk.DoubleVar(value=50.0)
        
        # Variables para mostrar valores formateados
        self.display_vars = {}
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la página."""
        main_container = tk.Frame(self, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        self.create_control_panel(main_container)
        self.create_graph_panel(main_container)
    
    def create_control_panel(self, parent):
        """Crea el panel de controles."""
        control_frame = tk.Frame(parent, bg=COLORS['header'], relief=tk.RAISED, borderwidth=2)
        control_frame.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        
        title = tk.Label(
            control_frame,
            text="⚙️ Parámetros",
            font=FONTS['section_title'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        title.pack(pady=(15, 20), padx=20)
        
        # Posición inicial
        self.create_parameter_control(
            control_frame,
            "Posición Inicial x(0)",
            self.x0_var,
            -3, 3, 0.1,
            'x0'
        )
        
        # Velocidad inicial
        self.create_parameter_control(
            control_frame,
            "Velocidad Inicial dx/dt(0)",
            self.v0_var,
            -3, 3, 0.1,
            'v0'
        )
        
        # Parámetro μ
        self.create_parameter_control(
            control_frame,
            "Parámetro μ (no linealidad)",
            self.mu_var,
            0.1, 10.0, 0.1,
            'mu'
        )
        
        # Tiempo máximo
        self.create_parameter_control(
            control_frame,
            "Tiempo Máximo",
            self.t_max_var,
            10, 100, 5,
            't_max'
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
            text="📋 Ecuaciones",
            font=FONTS['label'],
            bg='white',
            fg=COLORS['text_dark']
        )
        info_title.pack(pady=(10, 5))
        
        eq1 = tk.Label(
            info_frame,
            text="dx/dt = y",
            font=('Courier New', 10, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq1.pack()
        
        eq2 = tk.Label(
            info_frame,
            text="dy/dt = μ(1-x²)y - x",
            font=('Courier New', 10, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq2.pack(pady=(0, 10))
    
    def create_parameter_control(self, parent, label_text, variable, min_val, max_val, resolution, param_id):
        """Crea un control de parámetro con slider y valor formateado a 2 decimales."""
        container = tk.Frame(parent, bg=COLORS['header'])
        container.pack(pady=10, padx=20, fill=tk.X)
        
        label = tk.Label(
            container,
            text=label_text,
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        label.pack(anchor='w')
        
        slider_frame = tk.Frame(container, bg=COLORS['header'])
        slider_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Variable para mostrar valor formateado
        display_var = tk.StringVar(value=f"{variable.get():.2f}")
        self.display_vars[param_id] = display_var
        
        slider = ttk.Scale(
            slider_frame,
            from_=min_val,
            to=max_val,
            variable=variable,
            orient=tk.HORIZONTAL,
            length=DIMENSIONS['slider_length'],
            command=lambda v, dv=display_var: dv.set(f"{float(v):.2f}")
        )
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        value_label = tk.Label(
            slider_frame,
            textvariable=display_var,
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
        
        self.graph.set_labels(
            xlabel='x (Posición)',
            ylabel='dx/dt (Velocidad)',
            title='Diagrama de Fase - Oscilador de Van der Pol'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del oscilador de Van der Pol."""
        # Obtener parámetros
        x0 = self.x0_var.get()
        v0 = self.v0_var.get()
        mu = self.mu_var.get()
        t_max = self.t_max_var.get()
        
        # Simular
        t, x, v = VanDerPolSimulator.simulate(x0, v0, mu, t_max)
        
        # Graficar retrato de fase con estilo mejorado
        self.graph.clear()
        self.graph.plot(x, v, color=GRAPH_STYLE['colors']['primary'], label=f'μ = {mu:.2f}')
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
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
        self.graph.set_labels(
            xlabel='x (Posición)',
            ylabel='dx/dt (Velocidad)',
            title='Diagrama de Fase - Oscilador de Van der Pol'
        )
        self.graph.grid(True)
