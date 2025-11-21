"""
Página de simulación de la Bifurcación de Hopf.
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS
from utils.graph_helper import GraphCanvas
from utils.simulator import HopfSimulator


class HopfPage(tk.Frame):
    """
    Página para simular la bifurcación de Hopf.
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        # Variables de parámetros
        self.x0_var = tk.DoubleVar(value=0.1)
        self.y0_var = tk.DoubleVar(value=0.1)
        self.mu_var = tk.DoubleVar(value=0.5)
        self.omega_var = tk.DoubleVar(value=1.0)
        self.t_max_var = tk.DoubleVar(value=50.0)
        
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
        
        # Condiciones iniciales
        self.create_parameter_control(control_frame, "x₀", self.x0_var, -2, 2, 0.1)
        self.create_parameter_control(control_frame, "y₀", self.y0_var, -2, 2, 0.1)
        
        # Parámetro de bifurcación
        self.create_parameter_control(control_frame, "μ (bifurcación)", self.mu_var, -2, 3, 0.1)
        self.create_parameter_control(control_frame, "ω (frecuencia)", self.omega_var, 0.1, 3, 0.1)
        self.create_parameter_control(control_frame, "Tiempo Máximo", self.t_max_var, 10, 100, 5)
        
        # Botones
        button_frame = tk.Frame(control_frame, bg=COLORS['header'])
        button_frame.pack(pady=30, padx=20, fill=tk.X)
        
        tk.Button(
            button_frame, text="▶ Ejecutar Simulación", font=FONTS['button'],
            bg=COLORS['success'], fg='white', cursor="hand2",
            command=self.run_simulation, pady=10
        ).pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(
            button_frame, text="🗑️ Limpiar Gráfico", font=FONTS['button'],
            bg=COLORS['danger'], fg='white', cursor="hand2",
            command=self.clear_graph, pady=10
        ).pack(fill=tk.X)
        
        # Información
        info_frame = tk.Frame(control_frame, bg='white', relief=tk.SUNKEN, borderwidth=1)
        info_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        tk.Label(info_frame, text="📋 Ecuaciones", font=FONTS['label'],
                bg='white', fg=COLORS['text_dark']).pack(pady=(10, 5))
        
        tk.Label(info_frame, text="dx/dt = μx - ωy - x(x²+y²)",
                font=('Courier New', 9, 'bold'), bg='white', fg=COLORS['accent']).pack()
        tk.Label(info_frame, text="dy/dt = ωx + μy - y(x²+y²)",
                font=('Courier New', 9, 'bold'), bg='white', fg=COLORS['accent']).pack(pady=(0, 10))
        
        # Nota sobre bifurcación
        tk.Label(info_frame, text="μ < 0: Punto fijo estable\nμ > 0: Ciclo límite",
                font=FONTS['small'], bg='white', fg=COLORS['text_muted'],
                justify=tk.CENTER).pack(pady=(5, 10))
    
    def create_parameter_control(self, parent, label_text, variable, min_val, max_val, resolution):
        """Crea un control de parámetro con slider."""
        container = tk.Frame(parent, bg=COLORS['header'])
        container.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(container, text=label_text, font=FONTS['label'],
                bg=COLORS['header'], fg=COLORS['text_dark']).pack(anchor='w')
        
        slider_frame = tk.Frame(container, bg=COLORS['header'])
        slider_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Scale(slider_frame, from_=min_val, to=max_val, variable=variable,
                 orient=tk.HORIZONTAL, length=DIMENSIONS['slider_length']).pack(
                 side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(slider_frame, textvariable=variable, font=FONTS['value'],
                bg=COLORS['header'], fg=COLORS['accent'], width=8).pack(
                side=tk.LEFT, padx=(10, 0))
    
    def create_graph_panel(self, parent):
        """Crea el panel del gráfico."""
        graph_frame = tk.Frame(parent, bg='white', relief=tk.SUNKEN, borderwidth=2)
        graph_frame.grid(row=0, column=1, sticky="nsew")
        
        self.graph = GraphCanvas(graph_frame, figsize=(9, 6))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.graph.set_labels(xlabel='x', ylabel='y', title='Bifurcación de Hopf - Diagrama de Fase')
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación de Hopf."""
        x0 = self.x0_var.get()
        y0 = self.y0_var.get()
        mu = self.mu_var.get()
        omega = self.omega_var.get()
        t_max = self.t_max_var.get()
        
        t, x, y = HopfSimulator.simulate(x0, y0, mu, omega, t_max)
        
        self.graph.clear()
        self.graph.plot(x, y, 'b-', linewidth=1.5, label=f'μ={mu}')
        self.graph.scatter([x[0]], [y[0]], color='green', s=100, marker='o', label='Inicio', zorder=5)
        self.graph.scatter([x[-1]], [y[-1]], color='red', s=100, marker='s', label='Final', zorder=5)
        
        title = f'Bifurcación de Hopf (μ={mu}) - '
        title += 'Punto Fijo Estable' if mu < 0 else 'Ciclo Límite'
        
        self.graph.set_labels(xlabel='x', ylabel='y', title=title)
        self.graph.grid(True)
        self.graph.legend()
        self.graph.tight_layout()
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
        self.graph.set_labels(xlabel='x', ylabel='y', title='Bifurcación de Hopf - Diagrama de Fase')
        self.graph.grid(True)
