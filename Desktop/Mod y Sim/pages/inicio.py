"""
Página de inicio con información general de la aplicación.
"""

import tkinter as tk
from utils.styles import COLORS, FONTS


class InicioPage(tk.Frame):
    """
    Página de bienvenida con descripción de la aplicación y sistemas disponibles.
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
        """Crea los widgets de la página de inicio."""
        # Contenedor principal con padding
        main_container = tk.Frame(self, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        
        # Título de bienvenida
        welcome_title = tk.Label(
            main_container,
            text="🎯 Simulador de Sistemas Dinámicos",
            font=('Segoe UI', 28, 'bold'),
            bg=COLORS['content_bg'],
            fg=COLORS['accent']
        )
        welcome_title.pack(pady=(0, 20))
        
        # Descripción general
        description = tk.Label(
            main_container,
            text="Esta aplicación permite simular y visualizar diferentes sistemas dinámicos\n"
                 "mediante la resolución numérica de ecuaciones diferenciales ordinarias.",
            font=FONTS['label'],
            bg=COLORS['content_bg'],
            fg=COLORS['text_dark'],
            justify=tk.CENTER
        )
        description.pack(pady=(0, 30))
        
        # Frame para tarjetas de sistemas
        cards_frame = tk.Frame(main_container, bg=COLORS['content_bg'])
        cards_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar grid para las tarjetas
        for i in range(3):
            cards_frame.grid_columnconfigure(i, weight=1)
        
        # Sistemas disponibles
        systems = [
            {
                'icon': '🌡️',
                'title': 'Enfriamiento de Newton',
                'description': 'Modelo de transferencia de calor que describe cómo un objeto se enfría en un ambiente.'
            },
            {
                'icon': '📈',
                'title': 'Oscilador Van der Pol',
                'description': 'Sistema no lineal con amortiguamiento que exhibe ciclos límite y oscilaciones.'
            },
            {
                'icon': '🦠',
                'title': 'Modelo SIR',
                'description': 'Modelo epidemiológico que simula la propagación de enfermedades infecciosas.'
            },
            {
                'icon': '⚡',
                'title': 'Circuito RLC',
                'description': 'Circuito eléctrico con resistencia, inductancia y capacitancia en serie.'
            },
            {
                'icon': '🌀',
                'title': 'Sistema de Lorenz',
                'description': 'Sistema caótico tridimensional que exhibe un atractor extraño.'
            },
            {
                'icon': '📚',
                'title': 'Más sistemas',
                'description': 'Próximamente se agregarán más sistemas dinámicos interesantes.'
            }
        ]
        
        # Crear tarjetas
        row = 0
        col = 0
        for system in systems:
            card = self.create_system_card(cards_frame, system)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Instrucciones
        instructions_frame = tk.Frame(main_container, bg=COLORS['header'], relief=tk.RAISED, borderwidth=1)
        instructions_frame.pack(fill=tk.X, pady=(30, 0))
        
        instructions_title = tk.Label(
            instructions_frame,
            text="📖 Cómo usar la aplicación",
            font=FONTS['section_title'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        )
        instructions_title.pack(pady=(15, 10), padx=20, anchor='w')
        
        instructions_text = tk.Label(
            instructions_frame,
            text="1. Selecciona un sistema dinámico desde el menú lateral\n"
                 "2. Ajusta los parámetros usando los controles deslizantes\n"
                 "3. Presiona 'Ejecutar Simulación' para ver el resultado\n"
                 "4. Experimenta con diferentes valores para explorar el comportamiento del sistema",
            font=FONTS['label'],
            bg=COLORS['header'],
            fg=COLORS['text_dark'],
            justify=tk.LEFT
        )
        instructions_text.pack(pady=(0, 15), padx=40, anchor='w')
        
        # Pie de página
        footer = tk.Label(
            main_container,
            text="Desarrollado para el curso de Modelado y Simulación • 2025",
            font=FONTS['small'],
            bg=COLORS['content_bg'],
            fg=COLORS['text_muted']
        )
        footer.pack(side=tk.BOTTOM, pady=(20, 0))
    
    def create_system_card(self, parent, system_info):
        """
        Crea una tarjeta de información para un sistema.
        
        Args:
            parent: Widget padre
            system_info: Diccionario con información del sistema
            
        Returns:
            Frame de la tarjeta
        """
        card = tk.Frame(
            parent,
            bg='white',
            relief=tk.RAISED,
            borderwidth=1,
            highlightbackground=COLORS['accent'],
            highlightthickness=1
        )
        
        # Icono
        icon_label = tk.Label(
            card,
            text=system_info['icon'],
            font=('Segoe UI', 36),
            bg='white'
        )
        icon_label.pack(pady=(15, 5))
        
        # Título
        title_label = tk.Label(
            card,
            text=system_info['title'],
            font=('Segoe UI', 12, 'bold'),
            bg='white',
            fg=COLORS['text_dark']
        )
        title_label.pack(pady=(0, 5))
        
        # Descripción
        desc_label = tk.Label(
            card,
            text=system_info['description'],
            font=FONTS['small'],
            bg='white',
            fg=COLORS['text_muted'],
            wraplength=200,
            justify=tk.CENTER
        )
        desc_label.pack(pady=(0, 15), padx=10)
        
        return card
