"""
Página de inicio con información general de la aplicación.
Diseño moderno con tarjetas interactivas y estadísticas.
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS, ICONS


class InicioPage(tk.Frame):
    """
    Página de bienvenida con diseño moderno, tarjetas interactivas y guía rápida.
    """
    
    def __init__(self, parent):
        """
        Inicializa la página de inicio.
        
        Args:
            parent: Widget padre
        """
        super().__init__(parent, bg=COLORS['content_bg'])
        self.create_widgets()
    
    def create_widgets(self):
        """Crea los widgets de la página de inicio con diseño moderno."""
        # Canvas con scrollbar para contenido largo
        canvas = tk.Canvas(self, bg=COLORS['content_bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['content_bg'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=canvas.winfo_reqwidth())
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Actualizar ancho del frame interno cuando cambia el canvas
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(
            canvas.find_withtag("all")[0], width=e.width))
        
        # Contenedor principal con padding
        main_container = tk.Frame(scrollable_frame, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=DIMENSIONS['space_xxl'], pady=DIMENSIONS['space_xl'])
        
        # Hero Section - Banner de bienvenida
        self.create_hero_section(main_container)
        
        # Quick Stats - Estadísticas rápidas
        self.create_stats_section(main_container)
        
        # Systems Grid - Tarjetas de sistemas
        self.create_systems_grid(main_container)
        
        # Features Section - Características principales
        self.create_features_section(main_container)
        
        # Quick Start Guide
        self.create_quick_start(main_container)
        
        # Footer
        self.create_footer(main_container)
    
    def create_hero_section(self, parent):
        """Crea la sección hero con banner de bienvenida."""
        hero_frame = tk.Frame(parent, bg=COLORS['accent'], height=200)
        hero_frame.pack(fill=tk.X, pady=(0, DIMENSIONS['space_xxl']))
        hero_frame.pack_propagate(False)
        
        # Contenido centrado
        content_frame = tk.Frame(hero_frame, bg=COLORS['accent'])
        content_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Icono grande
        icon_label = tk.Label(
            content_frame,
            text="🎯",
            font=('Segoe UI', 48),
            bg=COLORS['accent'],
            fg='white'
        )
        icon_label.pack()
        
        # Título principal
        title_label = tk.Label(
            content_frame,
            text="Simulador de Sistemas Dinámicos",
            font=FONTS['title_large'],
            bg=COLORS['accent'],
            fg='white'
        )
        title_label.pack(pady=(DIMENSIONS['space_md'], DIMENSIONS['space_xs']))
        
        # Subtítulo
        subtitle_label = tk.Label(
            content_frame,
            text="Explora, Aprende y Simula • Plataforma Educativa Interactiva",
            font=FONTS['body'],
            bg=COLORS['accent'],
            fg='white'
        )
        subtitle_label.pack()
    
    def create_stats_section(self, parent):
        """Crea la sección de estadísticas rápidas."""
        stats_frame = tk.Frame(parent, bg=COLORS['content_bg'])
        stats_frame.pack(fill=tk.X, pady=(0, DIMENSIONS['space_xxl']))
        
        stats = [
            (ICONS['microscope'], "11", "Sistemas\nDisponibles"),
            (ICONS['graph'], "3", "Niveles de\nDificultad"),
            (ICONS['clipboard'], "∞", "Ejercicios\nGenerados"),
            (ICONS['star'], "100%", "Evaluación\nAutomática")
        ]
        
        for i, (icon, value, label) in enumerate(stats):
            stat_card = self.create_stat_card(stats_frame, icon, value, label)
            stat_card.grid(row=0, column=i, padx=DIMENSIONS['space_md'], sticky="ew")
            stats_frame.grid_columnconfigure(i, weight=1)
    
    def create_stat_card(self, parent, icon, value, label):
        """Crea una tarjeta de estadística."""
        card = tk.Frame(parent, bg='white', relief=tk.RAISED, borderwidth=1,
                       highlightbackground=COLORS['border'], highlightthickness=1)
        card.pack_propagate(False)
        card.configure(height=120)
        
        # Icono
        icon_label = tk.Label(card, text=icon, font=FONTS['icon'], bg='white')
        icon_label.pack(pady=(DIMENSIONS['space_md'], DIMENSIONS['space_xs']))
        
        # Valor
        value_label = tk.Label(card, text=value, font=FONTS['title'], bg='white', fg=COLORS['accent'])
        value_label.pack()
        
        # Label
        label_widget = tk.Label(card, text=label, font=FONTS['tiny'], bg='white', 
                               fg=COLORS['text_muted'], justify=tk.CENTER)
        label_widget.pack(pady=(0, DIMENSIONS['space_md']))
        
        return card
    
    def create_systems_grid(self, parent):
        """Crea la grid de tarjetas de sistemas."""
        # Título de sección
        section_title = tk.Label(
            parent,
            text="💡 Sistemas Dinámicos Disponibles",
            font=FONTS['section_title'],
            bg=COLORS['content_bg'],
            fg=COLORS['text_dark']
        )
        section_title.pack(anchor='w', pady=(0, DIMENSIONS['space_lg']))
        
        # Grid de tarjetas
        cards_frame = tk.Frame(parent, bg=COLORS['content_bg'])
        cards_frame.pack(fill=tk.BOTH, expand=True, pady=(0, DIMENSIONS['space_xxl']))
        
        # Configurar grid responsive
        for i in range(3):
            cards_frame.grid_columnconfigure(i, weight=1)
        
        # Sistemas disponibles con información mejorada
        systems = [
            {
                'icon': ICONS['newton'],
                'title': 'Enfriamiento de Newton',
                'description': 'Modelo de transferencia de calor que describe cómo un objeto se enfría exponencialmente.',
                'color': COLORS['info'],
                'level': 'Principiante'
            },
            {
                'icon': ICONS['van_der_pol'],
                'title': 'Oscilador Van der Pol',
                'description': 'Sistema no lineal con amortiguamiento que exhibe ciclos límite estables.',
                'color': COLORS['success'],
                'level': 'Intermedio'
            },
            {
                'icon': ICONS['sir'],
                'title': 'Modelo SIR',
                'description': 'Modelo epidemiológico para simular la propagación de enfermedades infecciosas.',
                'color': COLORS['danger'],
                'level': 'Intermedio'
            },
            {
                'icon': ICONS['rlc'],
                'title': 'Circuito RLC',
                'description': 'Circuito eléctrico serie con resistencia, inductancia y capacitancia.',
                'color': COLORS['warning'],
                'level': 'Intermedio'
            },
            {
                'icon': ICONS['lorenz'],
                'title': 'Sistema de Lorenz',
                'description': 'Sistema caótico tridimensional famoso por su atractor extraño ("Efecto Mariposa").',
                'color': COLORS['info_light'],
                'level': 'Avanzado'
            },
            {
                'icon': ICONS['hopf'],
                'title': 'Bifurcación de Hopf',
                'description': 'Transición entre punto fijo estable y ciclo límite mediante parámetro de control.',
                'color': COLORS['secondary'],
                'level': 'Avanzado'
            }
        ]
        
        # Crear tarjetas
        row, col = 0, 0
        for system in systems:
            card = self.create_system_card_modern(cards_frame, system)
            card.grid(row=row, column=col, padx=DIMENSIONS['space_md'], 
                     pady=DIMENSIONS['space_md'], sticky="nsew")
            
            col += 1
            if col > 2:
                col = 0
                row += 1
    
    def create_system_card_modern(self, parent, system_info):
        """Crea una tarjeta moderna de sistema con efectos hover."""
        card = tk.Frame(
            parent,
            bg='white',
            relief=tk.FLAT,
            highlightbackground=COLORS['border'],
            highlightthickness=1
        )
        
        # Header de la tarjeta con color
        header = tk.Frame(card, bg=system_info['color'], height=8)
        header.pack(fill=tk.X)
        
        # Contenido
        content = tk.Frame(card, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=DIMENSIONS['space_lg'], 
                    pady=DIMENSIONS['space_lg'])
        
        # Icono
        icon_label = tk.Label(
            content,
            text=system_info['icon'],
            font=FONTS['icon_large'],
            bg='white'
        )
        icon_label.pack()
        
        # Título
        title_label = tk.Label(
            content,
            text=system_info['title'],
            font=FONTS['subsection'],
            bg='white',
            fg=COLORS['text_dark']
        )
        title_label.pack(pady=(DIMENSIONS['space_sm'], DIMENSIONS['space_xs']))
        
        # Badge de nivel
        badge = tk.Label(
            content,
            text=system_info['level'],
            font=FONTS['tiny'],
            bg=system_info['color'],
            fg='white',
            padx=DIMENSIONS['space_sm'],
            pady=DIMENSIONS['space_xs']
        )
        badge.pack()
        
        # Descripción
        desc_label = tk.Label(
            content,
            text=system_info['description'],
            font=FONTS['small'],
            bg='white',
            fg=COLORS['text_medium'],
            wraplength=220,
            justify=tk.CENTER
        )
        desc_label.pack(pady=(DIMENSIONS['space_md'], 0))
        
        # Efecto hover
        def on_enter(e):
            card.configure(highlightbackground=system_info['color'], highlightthickness=2)
            header.configure(height=12)
        
        def on_leave(e):
            card.configure(highlightbackground=COLORS['border'], highlightthickness=1)
            header.configure(height=8)
        
        card.bind('<Enter>', on_enter)
        card.bind('<Leave>', on_leave)
        
        for widget in [card, content, icon_label, title_label, badge, desc_label]:
            widget.bind('<Enter>', on_enter)
            widget.bind('<Leave>', on_leave)
        
        return card
    
    def create_features_section(self, parent):
        """Crea la sección de características principales."""
        # Título
        section_title = tk.Label(
            parent,
            text="✨ Características Principales",
            font=FONTS['section_title'],
            bg=COLORS['content_bg'],
            fg=COLORS['text_dark']
        )
        section_title.pack(anchor='w', pady=(0, DIMENSIONS['space_lg']))
        
        features_frame = tk.Frame(parent, bg=COLORS['content_bg'])
        features_frame.pack(fill=tk.X, pady=(0, DIMENSIONS['space_xxl']))
        
        features = [
            (ICONS['lab'], "Modo Laboratorio", "Ejercicios automáticos con evaluación instantánea"),
            (ICONS['settings'], "Interfaz Intuitiva", "Diseño moderno y fácil de usar"),
            (ICONS['graph'], "Análisis Cualitativo", "Interpretación automática sin cálculo pesado"),
            (ICONS['book'], "Contenido Educativo", "Teoría completa y aplicaciones prácticas")
        ]
        
        for i, (icon, title, desc) in enumerate(features):
            feature_card = self.create_feature_card(features_frame, icon, title, desc)
            feature_card.grid(row=i//2, column=i%2, padx=DIMENSIONS['space_md'], 
                            pady=DIMENSIONS['space_sm'], sticky="ew")
            features_frame.grid_columnconfigure(0, weight=1)
            features_frame.grid_columnconfigure(1, weight=1)
    
    def create_feature_card(self, parent, icon, title, description):
        """Crea una tarjeta de característica."""
        card = tk.Frame(parent, bg=COLORS['input_bg'], relief=tk.FLAT)
        card.pack_propagate(False)
        card.configure(height=80)
        
        # Contenido horizontal
        content = tk.Frame(card, bg=COLORS['input_bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=DIMENSIONS['space_lg'], pady=DIMENSIONS['space_md'])
        
        # Icono a la izquierda
        icon_label = tk.Label(content, text=icon, font=FONTS['icon'], bg=COLORS['input_bg'])
        icon_label.pack(side=tk.LEFT, padx=(0, DIMENSIONS['space_md']))
        
        # Texto a la derecha
        text_container = tk.Frame(content, bg=COLORS['input_bg'])
        text_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        title_label = tk.Label(text_container, text=title, font=FONTS['subsection'],
                              bg=COLORS['input_bg'], fg=COLORS['text_dark'], anchor='w')
        title_label.pack(anchor='w')
        
        desc_label = tk.Label(text_container, text=description, font=FONTS['small'],
                             bg=COLORS['input_bg'], fg=COLORS['text_muted'], anchor='w')
        desc_label.pack(anchor='w')
        
        return card
    
    def create_quick_start(self, parent):
        """Crea la guía de inicio rápido."""
        # Contenedor con fondo
        quick_start_container = tk.Frame(parent, bg=COLORS['secondary'], relief=tk.FLAT)
        quick_start_container.pack(fill=tk.X, pady=(0, DIMENSIONS['space_xxl']))
        
        content = tk.Frame(quick_start_container, bg=COLORS['secondary'])
        content.pack(fill=tk.X, padx=DIMENSIONS['space_xxl'], pady=DIMENSIONS['space_xl'])
        
        # Título
        title = tk.Label(
            content,
            text=ICONS['target'] + " Guía de Inicio Rápido",
            font=FONTS['section_title'],
            bg=COLORS['secondary'],
            fg='white'
        )
        title.pack(anchor='w', pady=(0, DIMENSIONS['space_lg']))
        
        # Pasos
        steps = [
            "1. Selecciona un sistema dinámico desde el menú lateral",
            "2. Ajusta los parámetros usando los controles interactivos",
            "3. Presiona 'Ejecutar Simulación' para visualizar el comportamiento",
            "4. Analiza los gráficos y el análisis cualitativo automático",
            "5. Prueba el Modo Laboratorio para generar ejercicios educativos"
        ]
        
        for step in steps:
            step_label = tk.Label(
                content,
                text=step,
                font=FONTS['body'],
                bg=COLORS['secondary'],
                fg='white',
                anchor='w'
            )
            step_label.pack(anchor='w', pady=DIMENSIONS['space_xs'])
    
    def create_footer(self, parent):
        """Crea el footer de la página."""
        footer_frame = tk.Frame(parent, bg=COLORS['content_bg'])
        footer_frame.pack(fill=tk.X, pady=(DIMENSIONS['space_lg'], 0))
        
        # Separador
        separator = tk.Frame(footer_frame, height=1, bg=COLORS['border'])
        separator.pack(fill=tk.X, pady=(0, DIMENSIONS['space_md']))
        
        footer_text = tk.Label(
            footer_frame,
            text="🎓 Desarrollado para Modelado y Simulación • Universidad 2025\n"
                 "Plataforma Educativa Interactiva • v2.0",
            font=FONTS['small'],
            bg=COLORS['content_bg'],
            fg=COLORS['text_muted'],
            justify=tk.CENTER
        )
        footer_text.pack()
