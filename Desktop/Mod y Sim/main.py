"""
Sistema de Simulación de Sistemas Dinámicos
Aplicación principal con interfaz Tkinter
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Agregar el directorio raíz al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.styles import COLORS, FONTS
from utils.navigation import NavigationManager


class SimulatorApp:
    """
    Clase principal de la aplicación de simulación de sistemas dinámicos.
    Gestiona la ventana principal, navegación lateral y área de contenido.
    """
    
    def __init__(self, root):
        """
        Inicializa la aplicación principal.
        
        Args:
            root: Ventana raíz de Tkinter
        """
        self.root = root
        self.root.title("Simulador de Sistemas Dinámicos")
        self.root.geometry("1400x800")
        self.root.configure(bg=COLORS['background'])
        
        # Configurar el grid de la ventana principal
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Crear frames principales
        self.create_sidebar()
        self.create_main_area()
        
        # Inicializar gestor de navegación
        self.nav_manager = NavigationManager(self.content_frame, self.header_label)
        
        # Cargar la página de inicio por defecto
        self.nav_manager.show_page("inicio")
    
    def create_sidebar(self):
        """
        Crea la barra de navegación lateral con botones para cada sistema.
        """
        sidebar = tk.Frame(
            self.root,
            bg=COLORS['sidebar'],
            width=250,
            relief=tk.RAISED,
            borderwidth=2
        )
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        
        # Título de la barra lateral
        title_label = tk.Label(
            sidebar,
            text="SISTEMAS DINÁMICOS",
            font=FONTS['sidebar_title'],
            bg=COLORS['sidebar'],
            fg=COLORS['text_light'],
            pady=20
        )
        title_label.pack(fill=tk.X)
        
        # Separador
        separator = tk.Frame(sidebar, height=2, bg=COLORS['accent'])
        separator.pack(fill=tk.X, padx=10, pady=5)
        
        # Botones de navegación
        self.nav_buttons = {}
        nav_items = [
            ("🏠 Inicio", "inicio"),
            ("🌡️ Enfriamiento Newton", "newton"),
            ("📈 Van der Pol", "van_der_pol"),
            ("🦠 Modelo SIR", "sir"),
            ("⚡ Circuito RLC", "rlc"),
            ("🌀 Sistema Lorenz", "lorenz")
        ]
        
        for text, page_id in nav_items:
            btn = tk.Button(
                sidebar,
                text=text,
                font=FONTS['nav_button'],
                bg=COLORS['button'],
                fg=COLORS['text_light'],
                activebackground=COLORS['button_active'],
                activeforeground=COLORS['text_light'],
                relief=tk.FLAT,
                cursor="hand2",
                pady=15,
                command=lambda pid=page_id: self.navigate_to(pid)
            )
            btn.pack(fill=tk.X, padx=10, pady=5)
            self.nav_buttons[page_id] = btn
        
        # Información en la parte inferior
        info_frame = tk.Frame(sidebar, bg=COLORS['sidebar'])
        info_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        
        info_label = tk.Label(
            info_frame,
            text="Modelado y Simulación\nv1.0",
            font=FONTS['small'],
            bg=COLORS['sidebar'],
            fg=COLORS['text_muted'],
            justify=tk.CENTER
        )
        info_label.pack()
    
    def create_main_area(self):
        """
        Crea el área principal que contiene el encabezado y el área de contenido.
        """
        main_container = tk.Frame(self.root, bg=COLORS['background'])
        main_container.grid(row=0, column=1, sticky="nsew")
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Encabezado de sección
        header_frame = tk.Frame(
            main_container,
            bg=COLORS['header'],
            height=80,
            relief=tk.RAISED,
            borderwidth=1
        )
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_propagate(False)
        
        self.header_label = tk.Label(
            header_frame,
            text="Bienvenido",
            font=FONTS['header'],
            bg=COLORS['header'],
            fg=COLORS['text_dark'],
            anchor="w",
            padx=30
        )
        self.header_label.pack(fill=tk.BOTH, expand=True)
        
        # Área de contenido principal
        self.content_frame = tk.Frame(
            main_container,
            bg=COLORS['content_bg']
        )
        self.content_frame.grid(row=1, column=0, sticky="nsew")
    
    def navigate_to(self, page_id):
        """
        Navega a una página específica.
        
        Args:
            page_id: Identificador de la página
        """
        # Actualizar estilo de botones
        for btn_id, btn in self.nav_buttons.items():
            if btn_id == page_id:
                btn.configure(bg=COLORS['button_active'])
            else:
                btn.configure(bg=COLORS['button'])
        
        # Cambiar página
        self.nav_manager.show_page(page_id)
    
    def run(self):
        """
        Inicia el loop principal de la aplicación.
        """
        self.root.mainloop()


def main():
    """
    Función principal que crea y ejecuta la aplicación.
    """
    root = tk.Tk()
    app = SimulatorApp(root)
    app.run()


if __name__ == "__main__":
    main()
