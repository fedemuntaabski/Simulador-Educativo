"""
Clase base para páginas de simulación.
Aplica DRY extrayendo código común de todas las páginas de simuladores.
"""

import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from utils.styles import COLORS, FONTS, DIMENSIONS, GRAPH_STYLE


class BaseSimulatorPage(tk.Frame, ABC):
    """
    Clase base abstracta para todas las páginas de simuladores.
    Implementa el patrón Template Method para estandarizar la estructura.
    """
    
    # Subclases deben definir estos atributos
    TITLE = "Simulador Base"
    ICON = "📊"
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        self.display_vars = {}
        self.param_vars = {}
        self._init_parameters()
        self._create_widgets()
    
    @abstractmethod
    def _init_parameters(self):
        """
        Inicializa los parámetros del simulador.
        Las subclases deben definir self.parameters como lista de tuplas:
        (param_id, label, min_val, max_val, resolution, default, decimals)
        """
        pass
    
    @abstractmethod
    def _get_equations_info(self):
        """
        Retorna información de las ecuaciones del modelo.
        Returns:
            dict: {'title': str, 'equations': list[str]}
        """
        pass
    
    @abstractmethod
    def run_simulation(self):
        """Ejecuta la simulación específica del sistema."""
        pass
    
    def _create_widgets(self):
        """Template method para crear la estructura de widgets."""
        main_container = tk.Frame(self, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        self._create_control_panel(main_container)
        self._create_graph_panel(main_container)
    
    def _create_control_panel(self, parent):
        """Crea el panel de controles estandarizado."""
        control_frame = tk.Frame(parent, bg=COLORS['header'], relief=tk.RAISED, borderwidth=2)
        control_frame.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        
        # Título del panel
        tk.Label(
            control_frame,
            text="⚙️ Parámetros",
            font=FONTS['section_title'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        ).pack(pady=(15, 20), padx=20)
        
        # Crear controles para cada parámetro
        for param_config in self.parameters:
            self._create_parameter_control(control_frame, *param_config)
        
        # Botones de acción
        self._create_action_buttons(control_frame)
        
        # Panel de información/ecuaciones
        self._create_info_panel(control_frame)
    
    def _create_parameter_control(self, parent, param_id, label_text, min_val, max_val, 
                                   resolution, default, decimals=2):
        """Crea un control de parámetro con slider y valor formateado."""
        container = tk.Frame(parent, bg=COLORS['header'])
        container.pack(pady=8, padx=20, fill=tk.X)
        
        tk.Label(
            container,
            text=label_text,
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        ).pack(anchor='w')
        
        slider_frame = tk.Frame(container, bg=COLORS['header'])
        slider_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Variable para el slider
        var = tk.DoubleVar(value=default)
        self.param_vars[param_id] = var
        
        # Variable para mostrar valor formateado
        display_var = tk.StringVar(value=f"{default:.{decimals}f}")
        self.display_vars[param_id] = display_var
        
        slider = ttk.Scale(
            slider_frame,
            from_=min_val,
            to=max_val,
            variable=var,
            orient=tk.HORIZONTAL,
            length=DIMENSIONS['slider_length'],
            command=lambda v, dv=display_var, d=decimals: dv.set(f"{float(v):.{d}f}")
        )
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(
            slider_frame,
            textvariable=display_var,
            font=FONTS['value'],
            bg=COLORS['header'],
            fg=COLORS['accent'],
            width=10
        ).pack(side=tk.LEFT, padx=(10, 0))
    
    def _create_action_buttons(self, parent):
        """Crea los botones de acción (simular, limpiar)."""
        button_frame = tk.Frame(parent, bg=COLORS['header'])
        button_frame.pack(pady=20, padx=20, fill=tk.X)
        
        tk.Button(
            button_frame,
            text="▶ Ejecutar Simulación",
            font=FONTS['button'],
            bg=COLORS['success'],
            fg='white',
            cursor="hand2",
            command=self.run_simulation,
            pady=10
        ).pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(
            button_frame,
            text="🗑️ Limpiar Gráfico",
            font=FONTS['button'],
            bg=COLORS['danger'],
            fg='white',
            cursor="hand2",
            command=self.clear_graph,
            pady=10
        ).pack(fill=tk.X)
    
    def _create_info_panel(self, parent):
        """Crea el panel de información con ecuaciones."""
        info = self._get_equations_info()
        
        info_frame = tk.Frame(parent, bg='white', relief=tk.SUNKEN, borderwidth=1)
        info_frame.pack(pady=15, padx=20, fill=tk.BOTH)
        
        tk.Label(
            info_frame,
            text=f"📋 {info['title']}",
            font=FONTS['label'],
            bg='white',
            fg=COLORS['text_dark']
        ).pack(pady=(10, 5))
        
        for eq in info['equations']:
            tk.Label(
                info_frame,
                text=eq,
                font=('Courier New', 9, 'bold'),
                bg='white',
                fg=COLORS['accent']
            ).pack()
        
        # Nota adicional si existe
        if 'note' in info:
            tk.Label(
                info_frame,
                text=info['note'],
                font=FONTS['small'],
                bg='white',
                fg=COLORS['text_muted'],
                wraplength=250,
                justify=tk.CENTER
            ).pack(pady=(5, 10))
    
    def _create_graph_panel(self, parent):
        """Crea el panel del gráfico. Puede ser sobrescrito para gráficos 3D."""
        from utils.graph_helper import GraphCanvas
        
        graph_frame = tk.Frame(parent, bg='white', relief=tk.SUNKEN, borderwidth=2)
        graph_frame.grid(row=0, column=1, sticky="nsew")
        
        self.graph = GraphCanvas(graph_frame, figsize=(9, 6))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self._setup_initial_graph()
    
    def _setup_initial_graph(self):
        """Configura el estado inicial del gráfico."""
        self.graph.set_labels(
            xlabel='X',
            ylabel='Y',
            title=f'{self.ICON} {self.TITLE}'
        )
        self.graph.grid(True)
    
    def clear_graph(self):
        """Limpia el gráfico y restaura configuración inicial."""
        self.graph.clear()
        self._setup_initial_graph()
    
    def get_param(self, param_id):
        """Obtiene el valor actual de un parámetro."""
        return self.param_vars[param_id].get()
