"""
Página de simulación del Circuito RLC.
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS, GRAPH_STYLE
from utils.graph_helper import GraphCanvas
from utils.simulator import RLCSimulator


class RLCPage(tk.Frame):
    """
    Página para simular un circuito RLC serie.
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        # Variables de parámetros
        self.R_var = tk.DoubleVar(value=10.0)
        self.L_var = tk.DoubleVar(value=0.1)
        self.C_var = tk.DoubleVar(value=0.001)
        self.V0_var = tk.DoubleVar(value=10.0)
        self.I0_var = tk.DoubleVar(value=0.0)
        self.Q0_var = tk.DoubleVar(value=0.0)
        self.t_max_var = tk.DoubleVar(value=0.5)
        
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
        
        # Resistencia
        self.create_parameter_control(
            control_frame, "Resistencia R (Ω)",
            self.R_var, 1, 100, 1, 'R'
        )
        
        # Inductancia
        self.create_parameter_control(
            control_frame, "Inductancia L (H)",
            self.L_var, 0.01, 1.0, 0.01, 'L'
        )
        
        # Capacitancia
        self.create_parameter_control(
            control_frame, "Capacitancia C (F)",
            self.C_var, 0.0001, 0.01, 0.0001, 'C', decimals=4
        )
        
        # Voltaje
        self.create_parameter_control(
            control_frame, "Voltaje V₀ (V)",
            self.V0_var, 0, 50, 1, 'V0'
        )
        
        # Corriente inicial
        self.create_parameter_control(
            control_frame, "Corriente Inicial I₀ (A)",
            self.I0_var, 0, 5, 0.1, 'I0'
        )
        
        # Carga inicial
        self.create_parameter_control(
            control_frame, "Carga Inicial Q₀ (C)",
            self.Q0_var, 0, 0.1, 0.001, 'Q0', decimals=3
        )
        
        # Tiempo máximo
        self.create_parameter_control(
            control_frame, "Tiempo Máximo (s)",
            self.t_max_var, 0.1, 2.0, 0.1, 't_max'
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
            text="📋 Ecuaciones",
            font=FONTS['label'],
            bg='white',
            fg=COLORS['text_dark']
        )
        info_title.pack(pady=(10, 5))
        
        eq1 = tk.Label(
            info_frame,
            text="L(dI/dt) + RI + Q/C = V₀",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq1.pack()
        
        eq2 = tk.Label(
            info_frame,
            text="dQ/dt = I",
            font=('Courier New', 9, 'bold'),
            bg='white',
            fg=COLORS['accent']
        )
        eq2.pack(pady=(0, 10))
    
    def create_parameter_control(self, parent, label_text, variable, min_val, max_val, resolution, param_id, decimals=2):
        """Crea un control de parámetro con slider y valor formateado."""
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
        
        # Variable para mostrar valor formateado
        display_var = tk.StringVar(value=f"{variable.get():.{decimals}f}")
        self.display_vars[param_id] = display_var
        
        slider = ttk.Scale(
            slider_frame,
            from_=min_val,
            to=max_val,
            variable=variable,
            orient=tk.HORIZONTAL,
            length=DIMENSIONS['slider_length'],
            command=lambda v, dv=display_var, d=decimals: dv.set(f"{float(v):.{d}f}")
        )
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        value_label = tk.Label(
            slider_frame,
            textvariable=display_var,
            font=FONTS['value'],
            bg=COLORS['header'],
            fg=COLORS['accent'],
            width=10
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
            xlabel='Tiempo (s)',
            ylabel='Corriente (A)',
            title='Circuito RLC Serie'
        )
        self.graph.grid(True)
    
    def run_simulation(self):
        """Ejecuta la simulación del circuito RLC."""
        # Obtener parámetros
        R = self.R_var.get()
        L = self.L_var.get()
        C = self.C_var.get()
        V0 = self.V0_var.get()
        I0 = self.I0_var.get()
        Q0 = self.Q0_var.get()
        t_max = self.t_max_var.get()
        
        # Simular
        t, I, Q, V = RLCSimulator.simulate(I0, Q0, R, L, C, V0, t_max)
        
        # Graficar corriente y voltaje con estilo mejorado
        self.graph.clear()
        
        # Crear dos ejes Y
        ax1 = self.graph.ax
        ax2 = ax1.twinx()
        
        # Aplicar estilo a ax1
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_color(GRAPH_STYLE['colors']['primary'])
        ax1.spines['bottom'].set_color('#bdc3c7')
        
        # Graficar corriente en eje izquierdo
        line1 = ax1.plot(t, I, color=GRAPH_STYLE['colors']['primary'], 
                        linewidth=GRAPH_STYLE['linewidth'], label='Corriente I(t)')
        ax1.set_xlabel('Tiempo (s)', fontsize=GRAPH_STYLE['label_fontsize'], 
                      color='#2c3e50', fontweight='medium')
        ax1.set_ylabel('Corriente (A)', color=GRAPH_STYLE['colors']['primary'],
                      fontsize=GRAPH_STYLE['label_fontsize'], fontweight='medium')
        ax1.tick_params(axis='y', labelcolor=GRAPH_STYLE['colors']['primary'])
        
        # Graficar voltaje en eje derecho
        line2 = ax2.plot(t, V, color=GRAPH_STYLE['colors']['secondary'], 
                        linewidth=GRAPH_STYLE['linewidth'], label='Voltaje V_C(t)')
        ax2.set_ylabel('Voltaje (V)', color=GRAPH_STYLE['colors']['secondary'],
                      fontsize=GRAPH_STYLE['label_fontsize'], fontweight='medium')
        ax2.tick_params(axis='y', labelcolor=GRAPH_STYLE['colors']['secondary'])
        ax2.spines['right'].set_color(GRAPH_STYLE['colors']['secondary'])
        ax2.spines['top'].set_visible(False)
        
        # Combinar leyendas
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='upper right', fontsize=GRAPH_STYLE['legend_fontsize'],
                  framealpha=0.9, edgecolor='#bdc3c7')
        
        ax1.set_title(f'Circuito RLC (R = {R:.2f}Ω, L = {L:.2f}H, C = {C:.4f}F)', 
                     fontsize=GRAPH_STYLE['title_fontsize'], color='#2c3e50', fontweight='bold')
        ax1.grid(True, alpha=GRAPH_STYLE['grid_alpha'], linestyle='--', color='#bdc3c7')
        
        self.graph.tight_layout()
        self.graph.canvas.draw()
    
    def clear_graph(self):
        """Limpia el gráfico."""
        self.graph.clear()
        self.graph.set_labels(
            xlabel='Tiempo (s)',
            ylabel='Corriente (A)',
            title='Circuito RLC Serie'
        )
        self.graph.grid(True)
