"""
Página de simulación del Modelo Epidemiológico SIR.
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS
from utils.graph_helper import GraphCanvas
from utils.simulator import SIRSimulator


class SIRPage(tk.Frame):
    """
    Página para simular el modelo epidemiológico SIR.
    S: Susceptibles, I: Infectados, R: Recuperados
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        # Variables de parámetros
        self.S0_var = tk.DoubleVar(value=990.0)
        self.I0_var = tk.DoubleVar(value=10.0)
        self.R0_var = tk.DoubleVar(value=0.0)
        self.beta_var = tk.DoubleVar(value=0.3)
        self.gamma_var = tk.DoubleVar(value=0.1)
        self.t_max_var = tk.DoubleVar(value=160.0)
        
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
        
        # Población susceptible inicial
        self.create_parameter_control(
            control_frame,
            "Susceptibles Iniciales S(0)",
            self.S0_var,
            0, 1000, 10
        )
        
        # Población infectada inicial
        self.create_parameter_control(
            control_frame,
            "Infectados Iniciales I(0)",
            self.I0_var,
            0, 100, 1
        )
        
        # Población recuperada inicial
        self.create_parameter_control(
            control_frame,
            "Recuperados Iniciales R(0)",
            self.R0_var,
            0, 100, 1
        )
        
        # Tasa de contacto β
        self.create_parameter_control(
            control_frame,
            "Tasa de Contacto β",
            self.beta_var,
            0.1, 1.0, 0.05
        )
        
        # Tasa de recuperación γ
        self.create_parameter_control(
            control_frame,
            "Tasa de Recuperación γ",
            self.gamma_var,
            0.01, 0.5, 0.01
        )
        
        # Tiempo máximo
        self.create_parameter_control(
            control_frame,
            "Tiempo Máximo (días)",
            self.t_max_var,
            50, 300, 10
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
            text="📋 Ecuaciones SIR",
            font=FONTS['label'],
            bg='white',
            fg=COLORS['text_dark']
        )
        info_title.pack(pady=(10, 5))
        
        eq1 = tk.Label(
            info_frame,
            text="dS/dt = -βSI/N",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq1.pack()
        
        eq2 = tk.Label(
            info_frame,
            text="dI/dt = βSI/N - γI",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq2.pack()
        
        eq3 = tk.Label(
            info_frame,
            text="dR/dt = γI",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq3.pack(pady=(0, 10))
        
        # R₀ básico
        r0_label = tk.Label(
            info_frame,
            text="R₀ = β/γ",
            font=('Courier New', 9, 'italic'),
            bg='white',
            fg=COLORS['text_muted']
        )
        r0_label.pack(pady=(0, 10))
    
    def create_parameter_control(self, parent, label_text, variable, min_val, max_val, resolution):
        """Crea un control de parámetro con slider."""
        container = tk.Frame(parent, bg=COLORS['header'])
        container.pack(pady=8, padx=20, fill=tk.X)
        
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
        
        slider = ttk.Scale(
            slider_frame,
            from_=min_val,
            to=max_val,
            variable=variable,
            orient=tk.HORIZONTAL,
            length=DIMENSIONS['slider_length']
        )
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
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
        
        self.graph.set_labels(
            xlabel='Tiempo (días)',
            ylabel='Población',
            title='Modelo Epidemiológico SIR'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del modelo SIR."""
        # Obtener parámetros
        S0 = self.S0_var.get()
        I0 = self.I0_var.get()
        R0 = self.R0_var.get()
        beta = self.beta_var.get()
        gamma = self.gamma_var.get()
        t_max = self.t_max_var.get()
        
        # Simular
        t, S, I, R = SIRSimulator.simulate(S0, I0, R0, beta, gamma, t_max)
        
        # Calcular R₀
        R0_basic = beta / gamma
        
        # Graficar
        self.graph.clear()
        self.graph.plot(t, S, 'b-', linewidth=2, label='Susceptibles (S)')
        self.graph.plot(t, I, 'r-', linewidth=2, label='Infectados (I)')
        self.graph.plot(t, R, 'g-', linewidth=2, label='Recuperados (R)')
        
        title_text = f'Modelo Epidemiológico SIR (R₀ = {R0_basic:.2f})'
        self.graph.set_labels(
            xlabel='Tiempo (días)',
            ylabel='Población',
            title=title_text
        )
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
        self.graph.set_labels(
            xlabel='Tiempo (días)',
            ylabel='Población',
            title='Modelo Epidemiológico SIR'
        )
        self.graph.grid(True)
