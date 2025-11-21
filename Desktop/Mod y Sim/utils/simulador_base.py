"""
Componente base mejorado para páginas de simuladores con información educativa.
Incluye descripción teórica, ecuaciones, sliders interactivos y botones de ayuda.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from utils.styles import COLORS, FONTS
from utils.graph_helper import GraphCanvas
from utils.ejercicio_state import EjercicioState


class SimuladorBasePage(tk.Frame):
    """
    Clase base para páginas de simuladores con componentes educativos mejorados.
    """
    
    def __init__(self, parent, titulo, sistema_id):
        """
        Inicializa la página base del simulador.
        
        Args:
            parent: Frame padre
            titulo: Título del simulador
            sistema_id: ID del sistema (newton, sir, etc.)
        """
        super().__init__(parent, bg=COLORS['content_bg'])
        
        self.titulo = titulo
        self.sistema_id = sistema_id
        self.parametros = {}
        self.sliders = {}
        self.entries = {}
        
        # Verificar si hay ejercicio activo
        self.verificar_ejercicio_activo()
    
    def verificar_ejercicio_activo(self):
        """Verifica si hay un ejercicio activo y carga sus parámetros."""
        if EjercicioState.tiene_ejercicio():
            if EjercicioState.get_sistema_ejercicio() == self.sistema_id:
                self.parametros_ejercicio = EjercicioState.get_parametros_ejercicio()
                self.tiene_ejercicio = True
                return
        
        self.parametros_ejercicio = None
        self.tiene_ejercicio = False
    
    def create_layout(self, info_teorica, ecuaciones, parametros_config):
        """
        Crea el layout estándar del simulador educativo.
        
        Args:
            info_teorica: Diccionario con información teórica
            ecuaciones: Lista de ecuaciones LaTeX/texto
            parametros_config: Diccionario con configuración de parámetros
        """
        # Contenedor principal con scrollbar
        main_container = tk.Frame(self, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Canvas con scrollbar
        canvas = tk.Canvas(main_container, bg=COLORS['content_bg'])
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['content_bg'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido scrollable
        self.create_header(scrollable_frame)
        
        # Banner de ejercicio activo
        if self.tiene_ejercicio:
            self.create_ejercicio_banner(scrollable_frame)
        
        # Panel de información teórica (colapsable)
        self.create_info_panel(scrollable_frame, info_teorica, ecuaciones)
        
        # Panel de controles de parámetros
        self.create_controls_panel(scrollable_frame, parametros_config)
        
        # Gráfico de simulación
        self.create_graph_panel(scrollable_frame)
        
        # Panel de análisis cualitativo
        self.create_analysis_panel(scrollable_frame)
    
    def create_header(self, parent):
        """Crea el encabezado con título."""
        header_frame = tk.Frame(parent, bg=COLORS['accent'], height=70)
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text=f"🔬 {self.titulo}",
            font=('Segoe UI', 18, 'bold'),
            bg=COLORS['accent'],
            fg='white'
        ).pack(expand=True)
    
    def create_ejercicio_banner(self, parent):
        """Crea un banner indicando que hay un ejercicio activo."""
        banner_frame = tk.Frame(parent, bg='#4CAF50', relief=tk.RAISED, borderwidth=2)
        banner_frame.pack(fill=tk.X, padx=20, pady=10)
        
        info_container = tk.Frame(banner_frame, bg='#4CAF50')
        info_container.pack(fill=tk.X, padx=15, pady=10)
        
        tk.Label(
            info_container,
            text="📋 Ejercicio de Laboratorio Activo",
            font=('Segoe UI', 12, 'bold'),
            bg='#4CAF50',
            fg='white'
        ).pack(side=tk.LEFT)
        
        info = EjercicioState.get_info_ejercicio()
        tk.Label(
            info_container,
            text=f"  |  {info}",
            font=('Segoe UI', 10),
            bg='#4CAF50',
            fg='white'
        ).pack(side=tk.LEFT)
        
        # Botón para cargar parámetros del ejercicio
        tk.Button(
            info_container,
            text="⚙ Cargar Parámetros del Ejercicio",
            font=('Segoe UI', 9),
            bg='white',
            fg='#4CAF50',
            cursor="hand2",
            command=self.cargar_parametros_ejercicio,
            padx=10,
            pady=5
        ).pack(side=tk.RIGHT)
    
    def create_info_panel(self, parent, info_teorica, ecuaciones):
        """Crea el panel de información teórica colapsable."""
        info_frame = tk.LabelFrame(
            parent,
            text="📚 Información Teórica",
            font=FONTS['section_title'],
            bg='white',
            fg=COLORS['text_dark'],
            relief=tk.RAISED,
            borderwidth=2
        )
        info_frame.pack(fill=tk.X, padx=20, pady=15)
        
        # Frame interno con padding
        inner_frame = tk.Frame(info_frame, bg='white')
        inner_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # Descripción
        if 'descripcion' in info_teorica:
            desc_text = scrolledtext.ScrolledText(
                inner_frame,
                height=4,
                wrap=tk.WORD,
                font=FONTS['label'],
                bg='#f9f9f9',
                relief=tk.FLAT
            )
            desc_text.pack(fill=tk.X, pady=(0, 10))
            desc_text.insert('1.0', info_teorica['descripcion'])
            desc_text.config(state='disabled')
        
        # Ecuaciones
        if ecuaciones:
            tk.Label(
                inner_frame,
                text="📐 Ecuaciones Fundamentales:",
                font=('Segoe UI', 11, 'bold'),
                bg='white',
                anchor='w'
            ).pack(fill=tk.X, pady=(5, 5))
            
            ecuaciones_text = scrolledtext.ScrolledText(
                inner_frame,
                height=len(ecuaciones) + 1,
                wrap=tk.WORD,
                font=('Courier New', 10),
                bg='#f0f0f0',
                relief=tk.FLAT
            )
            ecuaciones_text.pack(fill=tk.X, pady=(0, 10))
            
            for ec in ecuaciones:
                ecuaciones_text.insert(tk.END, f"  {ec}\n")
            ecuaciones_text.config(state='disabled')
        
        # Aplicaciones
        if 'aplicaciones' in info_teorica:
            tk.Label(
                inner_frame,
                text="💡 Aplicaciones Prácticas:",
                font=('Segoe UI', 11, 'bold'),
                bg='white',
                anchor='w'
            ).pack(fill=tk.X, pady=(5, 5))
            
            for app in info_teorica['aplicaciones']:
                tk.Label(
                    inner_frame,
                    text=f"  • {app}",
                    font=FONTS['label'],
                    bg='white',
                    anchor='w',
                    wraplength=800,
                    justify=tk.LEFT
                ).pack(fill=tk.X, pady=2)
    
    def create_controls_panel(self, parent, parametros_config):
        """
        Crea el panel de controles con sliders interactivos.
        
        Args:
            parametros_config: Dict con configuración de cada parámetro
                Formato: {
                    'nombre_param': {
                        'label': 'Etiqueta visible',
                        'min': valor_min,
                        'max': valor_max,
                        'default': valor_default,
                        'resolution': paso,
                        'descripcion': 'Descripción del parámetro'
                    }
                }
        """
        controls_frame = tk.LabelFrame(
            parent,
            text="⚙️ Parámetros de Simulación",
            font=FONTS['section_title'],
            bg='white',
            fg=COLORS['text_dark'],
            relief=tk.RAISED,
            borderwidth=2
        )
        controls_frame.pack(fill=tk.X, padx=20, pady=15)
        
        # Frame interno
        inner_frame = tk.Frame(controls_frame, bg='white')
        inner_frame.pack(fill=tk.X, padx=15, pady=10)
        
        row = 0
        for param_name, config in parametros_config.items():
            # Frame para cada parámetro
            param_frame = tk.Frame(inner_frame, bg='white')
            param_frame.pack(fill=tk.X, pady=8)
            
            # Label con descripción
            label_frame = tk.Frame(param_frame, bg='white')
            label_frame.pack(fill=tk.X)
            
            tk.Label(
                label_frame,
                text=config['label'],
                font=('Segoe UI', 11, 'bold'),
                bg='white'
            ).pack(side=tk.LEFT)
            
            if 'descripcion' in config:
                tk.Label(
                    label_frame,
                    text=f"  ({config['descripcion']})",
                    font=('Segoe UI', 9),
                    bg='white',
                    fg=COLORS['text_muted']
                ).pack(side=tk.LEFT)
            
            # Frame para slider y entry
            control_frame = tk.Frame(param_frame, bg='white')
            control_frame.pack(fill=tk.X, pady=(5, 0))
            
            # Slider
            slider_var = tk.DoubleVar(value=config['default'])
            slider = tk.Scale(
                control_frame,
                from_=config['min'],
                to=config['max'],
                resolution=config.get('resolution', 0.1),
                orient=tk.HORIZONTAL,
                variable=slider_var,
                bg='white',
                length=400,
                command=lambda v, p=param_name: self.on_slider_change(p, v)
            )
            slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
            
            # Entry para valor numérico
            entry_var = tk.StringVar(value=str(config['default']))
            entry = tk.Entry(
                control_frame,
                textvariable=entry_var,
                font=FONTS['label'],
                width=10,
                justify=tk.CENTER
            )
            entry.pack(side=tk.LEFT)
            entry.bind('<Return>', lambda e, p=param_name: self.on_entry_change(p))
            
            # Guardar referencias
            self.sliders[param_name] = (slider_var, entry_var)
            self.parametros[param_name] = config['default']
            
            row += 1
        
        # Botón de simulación
        btn_frame = tk.Frame(controls_frame, bg='white')
        btn_frame.pack(fill=tk.X, padx=15, pady=(10, 15))
        
        tk.Button(
            btn_frame,
            text="▶ Ejecutar Simulación",
            font=('Segoe UI', 12, 'bold'),
            bg=COLORS['success'],
            fg='white',
            cursor="hand2",
            command=self.ejecutar_simulacion,
            pady=12,
            padx=30
        ).pack()
    
    def create_graph_panel(self, parent):
        """Crea el panel del gráfico."""
        graph_frame = tk.LabelFrame(
            parent,
            text="📊 Visualización",
            font=FONTS['section_title'],
            bg='white',
            fg=COLORS['text_dark'],
            relief=tk.RAISED,
            borderwidth=2
        )
        graph_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Crear canvas del gráfico
        self.graph = GraphCanvas(graph_frame, figsize=(10, 6))
        self.graph.get_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def create_analysis_panel(self, parent):
        """Crea el panel de análisis cualitativo."""
        analysis_frame = tk.LabelFrame(
            parent,
            text="🔍 Análisis Cualitativo",
            font=FONTS['section_title'],
            bg='white',
            fg=COLORS['text_dark'],
            relief=tk.RAISED,
            borderwidth=2
        )
        analysis_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        self.analysis_text = scrolledtext.ScrolledText(
            analysis_frame,
            height=6,
            wrap=tk.WORD,
            font=FONTS['label'],
            bg='#f9f9f9'
        )
        self.analysis_text.pack(fill=tk.X, padx=15, pady=10)
        self.analysis_text.insert('1.0', "Ejecuta la simulación para ver el análisis cualitativo del comportamiento.")
        self.analysis_text.config(state='disabled')
    
    def on_slider_change(self, param_name, value):
        """Callback cuando el slider cambia."""
        if param_name in self.sliders:
            slider_var, entry_var = self.sliders[param_name]
            entry_var.set(f"{float(value):.3f}")
            self.parametros[param_name] = float(value)
    
    def on_entry_change(self, param_name):
        """Callback cuando el entry cambia."""
        if param_name in self.sliders:
            slider_var, entry_var = self.sliders[param_name]
            try:
                value = float(entry_var.get())
                slider_var.set(value)
                self.parametros[param_name] = value
            except ValueError:
                # Restaurar valor anterior
                entry_var.set(f"{slider_var.get():.3f}")
    
    def cargar_parametros_ejercicio(self):
        """Carga los parámetros del ejercicio activo en los sliders."""
        if self.parametros_ejercicio:
            for param_name, value in self.parametros_ejercicio.items():
                if param_name in self.sliders:
                    slider_var, entry_var = self.sliders[param_name]
                    slider_var.set(value)
                    entry_var.set(str(value))
                    self.parametros[param_name] = value
    
    def ejecutar_simulacion(self):
        """Método a sobrescribir por las clases hijas."""
        raise NotImplementedError("Debe implementarse en la clase hija")
    
    def update_analysis(self, texto):
        """
        Actualiza el texto del análisis cualitativo.
        
        Args:
            texto: Texto del análisis
        """
        self.analysis_text.config(state='normal')
        self.analysis_text.delete('1.0', tk.END)
        self.analysis_text.insert('1.0', texto)
        self.analysis_text.config(state='disabled')
