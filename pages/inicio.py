"""
Página de inicio - Diseño moderno y minimalista
Plataforma educativa para sistemas dinámicos
"""

import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS, ICONS
import random


class InicioPage(tk.Frame):
    """
    Página de inicio moderna y atractiva.
    """
    
    def __init__(self, parent):
        """
        Inicializa la página de inicio.
        
        Args:
            parent: Widget padre
        """
        super().__init__(parent, bg=COLORS['content_bg'])
        self.nav_callback = None
        self.create_widgets()
    
    def set_navigation_callback(self, callback):
        """Establece el callback de navegación."""
        self.nav_callback = callback
    
    def create_widgets(self):
        """Crea los widgets de la página de inicio."""
        # Canvas con scrollbar
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
        
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(
            canvas.find_withtag("all")[0], width=e.width))
        
        # Contenedor principal
        main_container = tk.Frame(scrollable_frame, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        
        # Banner principal
        self.create_main_banner(main_container)
        
        # Sección de sistemas destacados
        self.create_featured_systems(main_container)
        
        # Información del laboratorio
        self.create_lab_info(main_container)
        
        # Footer minimalista
        self.create_footer(main_container)
    
    def create_main_banner(self, parent):
        """Crea el banner principal con diseño moderno."""
        banner = tk.Frame(parent, bg=COLORS['card_bg'], relief=tk.FLAT, 
                         highlightbackground=COLORS['accent'], highlightthickness=3)
        banner.pack(fill=tk.X, pady=(0, 40))
        
        # Contenedor interno con padding
        inner = tk.Frame(banner, bg=COLORS['card_bg'])
        inner.pack(fill=tk.BOTH, expand=True, padx=50, pady=40)
        
        # Lado izquierdo - Texto
        left_frame = tk.Frame(inner, bg=COLORS['card_bg'])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Título grande
        title = tk.Label(
            left_frame,
            text="Simulador de\\nSistemas Dinámicos",
            font=('Segoe UI', 42, 'bold'),
            bg=COLORS['card_bg'],
            fg=COLORS['text_dark'],
            justify=tk.LEFT
        )
        title.pack(anchor='w', pady=(0, 15))
        
        # Subtítulo
        subtitle = tk.Label(
            left_frame,
            text="Plataforma educativa interactiva para el análisis\\ny visualización de sistemas dinámicos complejos.",
            font=('Segoe UI', 13),
            bg=COLORS['card_bg'],
            fg=COLORS['text_medium'],
            justify=tk.LEFT
        )
        subtitle.pack(anchor='w', pady=(0, 20))
        
        # Botón call-to-action
        self.cta_btn = tk.Button(
            left_frame,
            text="🧪 Ir al Laboratorio",
            font=('Segoe UI', 12, 'bold'),
            bg=COLORS['accent'],
            fg='white',
            activebackground=COLORS['accent_dark'],
            activeforeground='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=25,
            pady=12,
            command=self.go_to_lab
        )
        self.cta_btn.pack(anchor='w')
    
    def go_to_lab(self):
        """Navega al laboratorio."""
        if self.nav_callback:
            self.nav_callback('laboratorio')
        
        # Lado derecho - Icono grande
        right_frame = tk.Frame(inner, bg=COLORS['card_bg'])
        right_frame.pack(side=tk.RIGHT, padx=(40, 0))
        
        icon_bg = tk.Frame(right_frame, bg=COLORS['accent_light'], width=180, height=180)
        icon_bg.pack_propagate(False)
        icon_bg.pack()
        
        icon = tk.Label(
            icon_bg,
            text="📊",
            font=('Segoe UI', 80),
            bg=COLORS['accent_light']
        )
        icon.place(relx=0.5, rely=0.5, anchor='center')
    
    def create_featured_systems(self, parent):
        """Crea la sección de sistemas destacados."""
        # Título
        title_frame = tk.Frame(parent, bg=COLORS['content_bg'])
        title_frame.pack(fill=tk.X, pady=(0, 25))
        
        tk.Label(
            title_frame,
            text="Sistemas Disponibles",
            font=('Segoe UI', 24, 'bold'),
            bg=COLORS['content_bg'],
            fg=COLORS['text_dark']
        ).pack(side=tk.LEFT)
        
        # Grid de sistemas
        systems_grid = tk.Frame(parent, bg=COLORS['content_bg'])
        systems_grid.pack(fill=tk.BOTH, expand=True, pady=(0, 40))
        
        # Configurar columnas
        for i in range(3):
            systems_grid.grid_columnconfigure(i, weight=1, uniform='col')
        
        systems = [
            {'icon': '🌡️', 'name': 'Enfriamiento Newton', 'desc': 'Transferencia de calor', 'color': '#4299e1'},
            {'icon': '📈', 'name': 'Van der Pol', 'desc': 'Oscilador no lineal', 'color': '#48bb78'},
            {'icon': '🦠', 'name': 'Modelo SIR', 'desc': 'Epidemiología', 'color': '#f56565'},
            {'icon': '⚡', 'name': 'Circuito RLC', 'desc': 'Circuitos eléctricos', 'color': '#ed8936'},
            {'icon': '🌀', 'name': 'Sistema Lorenz', 'desc': 'Caos determinista', 'color': '#9f7aea'},
            {'icon': '🔄', 'name': 'Bifurcación Hopf', 'desc': 'Transiciones críticas', 'color': '#3d5a80'}
        ]
        
        row, col = 0, 0
        for system in systems:
            card = self.create_system_card(systems_grid, system)
            card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
            
            col += 1
            if col > 2:
                col = 0
                row += 1
    
    def create_system_card(self, parent, system):
        """Crea una tarjeta de sistema."""
        card = tk.Frame(parent, bg=COLORS['card_bg'], relief=tk.FLAT,
                       highlightbackground=COLORS['border'], highlightthickness=1)
        
        # Contenido
        content = tk.Frame(card, bg=COLORS['card_bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Icono
        tk.Label(
            content,
            text=system['icon'],
            font=('Segoe UI', 40),
            bg=COLORS['card_bg']
        ).pack(pady=(0, 10))
        
        # Nombre
        tk.Label(
            content,
            text=system['name'],
            font=('Segoe UI', 14, 'bold'),
            bg=COLORS['card_bg'],
            fg=COLORS['text_dark']
        ).pack()
        
        # Descripción
        tk.Label(
            content,
            text=system['desc'],
            font=('Segoe UI', 10),
            bg=COLORS['card_bg'],
            fg=COLORS['text_muted']
        ).pack(pady=(5, 0))
        
        # Efecto hover
        def on_enter(e):
            card.configure(highlightbackground=system['color'], highlightthickness=2)
        
        def on_leave(e):
            card.configure(highlightbackground=COLORS['border'], highlightthickness=1)
        
        card.bind('<Enter>', on_enter)
        card.bind('<Leave>', on_leave)
        content.bind('<Enter>', on_enter)
        content.bind('<Leave>', on_leave)
        
        return card
    
    def create_lab_info(self, parent):
        """Crea la sección de información del laboratorio."""
        lab_container = tk.Frame(parent, bg=COLORS['secondary'])
        lab_container.pack(fill=tk.X, pady=(0, 40))
        
        content = tk.Frame(lab_container, bg=COLORS['secondary'])
        content.pack(fill=tk.X, padx=50, pady=35)
        
        # Título
        tk.Label(
            content,
            text="🧪 Modo Laboratorio",
            font=('Segoe UI', 22, 'bold'),
            bg=COLORS['secondary'],
            fg='white'
        ).pack(anchor='w', pady=(0, 15))
        
        # Descripción
        desc_text = (
            "Experimenta con ejercicios generados automáticamente que se adaptan a tu nivel.\n"
            "Cada ejercicio incluye:\n\n"
            "• Parámetros aleatorios para práctica variada\n"
            "• Preguntas teóricas y prácticas\n"
            "• Evaluación automática con retroalimentación\n"
            "• Análisis cualitativo del comportamiento del sistema"
        )
        
        tk.Label(
            content,
            text=desc_text,
            font=('Segoe UI', 11),
            bg=COLORS['secondary'],
            fg='white',
            justify=tk.LEFT
        ).pack(anchor='w')
    
    def create_footer(self, parent):
        """Crea el footer minimalista."""
        footer = tk.Frame(parent, bg=COLORS['content_bg'])
        footer.pack(fill=tk.X, pady=(20, 0))
        
        # Separador
        tk.Frame(footer, height=1, bg=COLORS['border']).pack(fill=tk.X, pady=(0, 15))
        
        # Texto del footer
        tk.Label(
            footer,
            text="Plataforma Educativa de Sistemas Dinámicos • Universidad 2025",
            font=('Segoe UI', 9),
            bg=COLORS['content_bg'],
            fg=COLORS['text_muted']
        ).pack()
