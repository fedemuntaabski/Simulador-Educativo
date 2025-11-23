"""
Página de simulación del Sistema de Lorenz (Atractor Caótico).
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS
from utils.graph_helper import Graph3DCanvas
from utils.simulator import LorenzSimulator


class LorenzPage(tk.Frame):
    """
    Página para simular el sistema de Lorenz (atractor caótico 3D).
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        # Variables de parámetros
        self.x0_var = tk.DoubleVar(value=1.0)
        self.y0_var = tk.DoubleVar(value=1.0)
        self.z0_var = tk.DoubleVar(value=1.0)
        self.sigma_var = tk.DoubleVar(value=10.0)
        self.rho_var = tk.DoubleVar(value=28.0)
        self.beta_var = tk.DoubleVar(value=2.667)
        self.t_max_var = tk.DoubleVar(value=40.0)
        
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
        init_label = tk.Label(
            control_frame,
            text="Condiciones Iniciales:",
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        init_label.pack(pady=(5, 10), padx=20, anchor='w')
        
        self.create_parameter_control(
            control_frame,
            "x₀",
            self.x0_var,
            -10, 10, 0.5
        )
        
        self.create_parameter_control(
            control_frame,
            "y₀",
            self.y0_var,
            -10, 10, 0.5
        )
        
        self.create_parameter_control(
            control_frame,
            "z₀",
            self.z0_var,
            -10, 10, 0.5
        )
        
        # Parámetros del sistema
        params_label = tk.Label(
            control_frame,
            text="Parámetros del Sistema:",
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        params_label.pack(pady=(15, 10), padx=20, anchor='w')
        
        self.create_parameter_control(
            control_frame,
            "σ (sigma)",
            self.sigma_var,
            1, 20, 0.5
        )
        
        self.create_parameter_control(
            control_frame,
            "ρ (rho)",
            self.rho_var,
            1, 50, 1
        )
        
        self.create_parameter_control(
            control_frame,
            "β (beta)",
            self.beta_var,
            0.5, 5.0, 0.1
        )
        
        self.create_parameter_control(
            control_frame,
            "Tiempo Máximo",
            self.t_max_var,
            10, 100, 5
        )
        
        # Botones
        button_frame = tk.Frame(control_frame, bg=COLORS['header'])
        button_frame.pack(pady=20, padx=20, fill=tk.X)
        
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
        info_frame.pack(pady=15, padx=20, fill=tk.BOTH)
        
        info_title = tk.Label(
            info_frame,
            text="📋 Ecuaciones de Lorenz",
            font=FONTS['label'],
            bg='white',
            fg=COLORS['text_dark']
        )
        info_title.pack(pady=(10, 5))
        
        eq1 = tk.Label(
            info_frame,
            text="dx/dt = σ(y - x)",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq1.pack()
        
        eq2 = tk.Label(
            info_frame,
            text="dy/dt = x(ρ - z) - y",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq2.pack()
        
        eq3 = tk.Label(
            info_frame,
            text="dz/dt = xy - βz",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq3.pack(pady=(0, 10))
    
    def create_parameter_control(self, parent, label_text, variable, min_val, max_val, resolution):
        """Crea un control de parámetro con slider."""
        container = tk.Frame(parent, bg=COLORS['header'])
        container.pack(pady=6, padx=20, fill=tk.X)
        
        label = tk.Label(
            container,
            text=label_text,
            font=FONTS['small'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        label.pack(anchor='w')
        
        slider_frame = tk.Frame(container, bg=COLORS['header'])
        slider_frame.pack(fill=tk.X, pady=(3, 0))
        
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
        """Crea el panel del gráfico 3D."""
        graph_frame = tk.Frame(parent, bg='white', relief=tk.SUNKEN, borderwidth=2)
        graph_frame.grid(row=0, column=1, sticky="nsew")
        
        # Canvas 3D de Matplotlib
        self.graph = Graph3DCanvas(graph_frame, figsize=(9, 6))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.graph.set_labels(
            xlabel='X',
            ylabel='Y',
            zlabel='Z',
            title='Atractor de Lorenz'
        )
    
    def run_simulation(self):
        """Ejecuta la simulación del sistema de Lorenz."""
        # Obtener parámetros
        x0 = self.x0_var.get()
        y0 = self.y0_var.get()
        z0 = self.z0_var.get()
        sigma = self.sigma_var.get()
        rho = self.rho_var.get()
        beta = self.beta_var.get()
        t_max = self.t_max_var.get()
        
        # Simular
        t, x, y, z = LorenzSimulator.simulate(x0, y0, z0, sigma, rho, beta, t_max)
        
        # Graficar en 3D
        self.graph.clear()
        
        # Crear gradiente de color basado en el tiempo
        colors = t
        
        self.graph.ax.plot(x, y, z, linewidth=0.5, alpha=0.7, color='blue')
        scatter = self.graph.ax.scatter(x, y, z, c=colors, cmap='viridis', 
                                       s=1, alpha=0.6)
        
        # Marcar inicio y fin
        self.graph.ax.scatter([x[0]], [y[0]], [z[0]], color='green', 
                             s=100, marker='o', label='Inicio')
        self.graph.ax.scatter([x[-1]], [y[-1]], [z[-1]], color='red', 
                             s=100, marker='s', label='Final')
        
        self.graph.set_labels(
            xlabel='X',
            ylabel='Y',
            zlabel='Z',
            title=f'Atractor de Lorenz (σ={sigma}, ρ={rho}, β={beta:.2f})'
        )
        
        self.graph.legend()
        self.graph.tight_layout()
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
        self.graph.set_labels(
            xlabel='X',
            ylabel='Y',
            zlabel='Z',
            title='Atractor de Lorenz'
        )
