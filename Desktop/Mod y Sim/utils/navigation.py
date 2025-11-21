"""
Gestor de navegación entre páginas de la aplicación.
"""

import tkinter as tk
from pages.inicio import InicioPage
from pages.newton import NewtonPage
from pages.van_der_pol import VanDerPolPage
from pages.sir import SIRPage
from pages.rlc import RLCPage
from pages.lorenz import LorenzPage


class NavigationManager:
    """
    Gestiona la navegación entre diferentes páginas de la aplicación.
    Implementa el patrón de cambio de frames para simular navegación multipágina.
    """
    
    def __init__(self, content_frame, header_label):
        """
        Inicializa el gestor de navegación.
        
        Args:
            content_frame: Frame donde se mostrará el contenido de las páginas
            header_label: Label del encabezado que se actualizará con el título de la página
        """
        self.content_frame = content_frame
        self.header_label = header_label
        self.current_page = None
        
        # Registro de páginas disponibles
        self.pages = {
            'inicio': {
                'class': InicioPage,
                'title': 'Bienvenido al Simulador de Sistemas Dinámicos'
            },
            'newton': {
                'class': NewtonPage,
                'title': 'Ley de Enfriamiento de Newton'
            },
            'van_der_pol': {
                'class': VanDerPolPage,
                'title': 'Oscilador de Van der Pol'
            },
            'sir': {
                'class': SIRPage,
                'title': 'Modelo Epidemiológico SIR'
            },
            'rlc': {
                'class': RLCPage,
                'title': 'Circuito RLC'
            },
            'lorenz': {
                'class': LorenzPage,
                'title': 'Sistema de Lorenz (Atractor Caótico)'
            }
        }
    
    def show_page(self, page_id):
        """
        Muestra la página especificada.
        
        Args:
            page_id: Identificador de la página a mostrar
        """
        if page_id not in self.pages:
            print(f"Advertencia: Página '{page_id}' no encontrada")
            return
        
        # Destruir página actual si existe
        if self.current_page is not None:
            self.current_page.destroy()
        
        # Actualizar encabezado
        page_info = self.pages[page_id]
        self.header_label.config(text=page_info['title'])
        
        # Crear y mostrar nueva página
        page_class = page_info['class']
        self.current_page = page_class(self.content_frame)
        self.current_page.pack(fill=tk.BOTH, expand=True)
