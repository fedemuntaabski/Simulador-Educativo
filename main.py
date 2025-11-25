"""
Sistema de Simulación de Sistemas Dinámicos
Aplicación principal con interfaz Tkinter
"""

import tkinter as tk
from tkinter import ttk
import sys
import os
import subprocess

# Agregar el directorio raíz al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.styles import COLORS, FONTS, DIMENSIONS, ICONS
from utils.navigation import NavigationManager


def install_requirements():
    """
    Instala automáticamente las dependencias desde requirements.txt
    si no están instaladas.
    """
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')

    if not os.path.exists(requirements_file):
        print("⚠️  No se encontró requirements.txt")
        return

    try:
        print("🔄 Verificando e instalando dependencias...")

        # Instalar requirements usando pip
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', requirements_file,
            '--quiet', '--disable-pip-version-check'
        ], capture_output=True, text=True, timeout=300)

        if result.returncode == 0:
            print("✅ Dependencias instaladas correctamente")
        else:
            print("⚠️  Error instalando dependencias:")
            print(result.stderr)
            print("Continuando con la aplicación...")

    except subprocess.TimeoutExpired:
        print("⚠️  Timeout instalando dependencias. Continuando...")
    except Exception as e:
        print(f"⚠️  Error instalando dependencias: {e}")
        print("Continuando con la aplicación...")


class SimulatorApp:
    """
    Clase principal de la aplicación de simulación de sistemas dinámicos.
    Gestiona la ventana principal, navegación lateral y área de contenido.
    Interfaz moderna con efectos visuales mejorados.
    """
    
    def __init__(self, root):
        """
        Inicializa la aplicación principal.
        
        Args:
            root: Ventana raíz de Tkinter
        """
        self.root = root
        self.root.title("Simulador de Sistemas Dinámicos")
        self.root.geometry("1450x850")
        self.root.configure(bg=COLORS['background'])
        
        # Estado del sidebar
        self.sidebar_visible = True
        
        # Centrar ventana en la pantalla
        self.center_window()
        
        # Configurar el grid de la ventana principal
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Crear frames principales
        self.create_sidebar()
        self.create_main_area()
        
        # Crear botón flotante de toggle sidebar (siempre visible)
        self.create_toggle_button()
        
        # Inicializar gestor de navegación
        self.nav_manager = NavigationManager(self.content_frame, self.header_label)
        
        # Cargar la página de inicio por defecto
        self.nav_manager.show_page("inicio")
    
    def center_window(self):
        """Centra la ventana en la pantalla."""
        self.root.update_idletasks()
        width = 1450
        height = 850
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_sidebar(self):
        """
        Crea la barra de navegación lateral con botones para cada sistema.
        Diseño moderno con efectos hover y animaciones.
        """
        self.sidebar = tk.Frame(
            self.root,
            bg=COLORS['sidebar'],
            width=DIMENSIONS['sidebar_width']
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        
        # Header del sidebar con logo/título
        header_sidebar = tk.Frame(self.sidebar, bg=COLORS['sidebar'])
        header_sidebar.pack(fill=tk.X, pady=(DIMENSIONS['space_lg'], DIMENSIONS['space_md']))
        
        # Logo/Icono principal
        logo_label = tk.Label(
            header_sidebar,
            text="🎯",
            font=FONTS['icon_large'],
            bg=COLORS['sidebar'],
            fg=COLORS['accent']
        )
        logo_label.pack()
        
        # Título de la barra lateral
        title_label = tk.Label(
            header_sidebar,
            text="SISTEMAS\nDINÁMICOS",
            font=FONTS['sidebar_title'],
            bg=COLORS['sidebar'],
            fg=COLORS['text_light'],
            justify=tk.CENTER
        )
        title_label.pack(pady=(DIMENSIONS['space_sm'], 0))
        
        # Separador con gradiente visual
        separator_frame = tk.Frame(self.sidebar, bg=COLORS['sidebar'], height=DIMENSIONS['space_md'])
        separator_frame.pack(fill=tk.X)
        
        separator = tk.Frame(separator_frame, height=2, bg=COLORS['accent'])
        separator.pack(fill=tk.X, padx=DIMENSIONS['space_lg'])
        
        # Container para botones con scroll (si es necesario en el futuro)
        buttons_container = tk.Frame(self.sidebar, bg=COLORS['sidebar'])
        buttons_container.pack(fill=tk.BOTH, expand=True, pady=DIMENSIONS['space_md'])
        
        # Botones de navegación
        self.nav_buttons = {}
        nav_items = [
            (ICONS['home'] + " Inicio", "inicio", False),
            (ICONS['lab'] + " Laboratorio", "laboratorio", True),
            ("", "separator", False),  # Separador visual
            (ICONS['newton'] + " Enfriamiento Newton", "newton", False),
            (ICONS['van_der_pol'] + " Van der Pol", "van_der_pol", False),
            (ICONS['sir'] + " Modelo SIR", "sir", False),
            (ICONS['rlc'] + " Circuito RLC", "rlc", False),
            (ICONS['lorenz'] + " Sistema Lorenz", "lorenz", False),
            (ICONS['hopf'] + " Bifurcación Hopf", "hopf", False)
        ]
        
        for text, page_id, is_featured in nav_items:
            if page_id == "separator":
                # Agregar un separador visual sutil
                sep_container = tk.Frame(buttons_container, bg=COLORS['sidebar'], height=DIMENSIONS['space_md'])
                sep_container.pack(fill=tk.X, pady=DIMENSIONS['space_sm'])
                
                sep = tk.Frame(sep_container, height=1, bg=COLORS['sidebar_hover'])
                sep.pack(fill=tk.X, padx=DIMENSIONS['space_xxl'])
                continue
            
            # Destacar botón especial (Laboratorio)
            if is_featured:
                btn = self.create_featured_button(buttons_container, text, page_id)
            else:
                btn = self.create_nav_button(buttons_container, text, page_id)
            
            self.nav_buttons[page_id] = btn
        
        # Footer del sidebar
        footer_frame = tk.Frame(self.sidebar, bg=COLORS['sidebar'])
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=DIMENSIONS['space_lg'])
        
        # Separador footer
        footer_sep = tk.Frame(footer_frame, height=1, bg=COLORS['sidebar_hover'])
        footer_sep.pack(fill=tk.X, padx=DIMENSIONS['space_lg'], pady=(0, DIMENSIONS['space_md']))
    
    def create_nav_button(self, parent, text, page_id):
        """Crea un botón de navegación estándar con efectos hover."""
        btn_frame = tk.Frame(parent, bg=COLORS['sidebar'])
        btn_frame.pack(fill=tk.X, padx=DIMENSIONS['space_md'], pady=DIMENSIONS['space_xs'])
        
        btn = tk.Button(
            btn_frame,
            text=text,
            font=FONTS['nav_button'],
            bg=COLORS['button'],
            fg=COLORS['text_light'],
            activebackground=COLORS['button_active'],
            activeforeground=COLORS['text_light'],
            relief=tk.FLAT,
            cursor="hand2",
            anchor='w',
            padx=DIMENSIONS['space_lg'],
            pady=DIMENSIONS['space_md'],
            command=lambda: self.navigate_to(page_id)
        )
        btn.pack(fill=tk.X)
        
        # Efectos hover
        btn.bind('<Enter>', lambda e: self.on_button_hover(btn, True))
        btn.bind('<Leave>', lambda e: self.on_button_hover(btn, False))
        
        return btn
    
    def create_featured_button(self, parent, text, page_id):
        """Crea un botón destacado (ej: Laboratorio) con estilo especial."""
        btn_frame = tk.Frame(parent, bg=COLORS['sidebar'])
        btn_frame.pack(fill=tk.X, padx=DIMENSIONS['space_md'], pady=DIMENSIONS['space_sm'])
        
        btn = tk.Button(
            btn_frame,
            text=text,
            font=FONTS['button'],
            bg=COLORS['accent'],
            fg=COLORS['text_light'],
            activebackground=COLORS['accent_dark'],
            activeforeground=COLORS['text_light'],
            relief=tk.FLAT,
            cursor="hand2",
            anchor='w',
            padx=DIMENSIONS['space_lg'],
            pady=DIMENSIONS['space_md'] + 2,
            command=lambda: self.navigate_to(page_id)
        )
        btn.pack(fill=tk.X)
        
        # Efectos hover especiales
        btn.bind('<Enter>', lambda e: btn.configure(bg=COLORS['accent_light']))
        btn.bind('<Leave>', lambda e: self.reset_featured_button(btn, page_id))
        
        return btn
    
    def on_button_hover(self, button, entering):
        """Maneja el efecto hover de botones normales."""
        if entering:
            button.configure(bg=COLORS['button_hover'], fg=COLORS['text_dark'])
        else:
            # Restaurar color original o activo
            current_page = getattr(self.nav_manager, 'current_page', None)
            is_active = False
            
            for page_id, btn in self.nav_buttons.items():
                if btn == button and current_page == page_id:
                    is_active = True
                    break
            
            if is_active:
                button.configure(bg=COLORS['button_active'], fg=COLORS['text_light'])
            else:
                button.configure(bg=COLORS['button'], fg=COLORS['text_light'])
    
    def reset_featured_button(self, button, page_id):
        """Resetea el botón destacado a su estado original."""
        current_page = getattr(self.nav_manager, 'current_page', None)
        if current_page == page_id:
            button.configure(bg=COLORS['accent_dark'])
        else:
            button.configure(bg=COLORS['accent'])
    
    def create_main_area(self):
        """
        Crea el área principal con header moderno y área de contenido.
        """
        main_container = tk.Frame(self.root, bg=COLORS['background'])
        main_container.grid(row=0, column=1, sticky="nsew")
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Encabezado moderno con sombra sutil
        header_frame = tk.Frame(
            main_container,
            bg=COLORS['header'],
            height=DIMENSIONS['header_height']
        )
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_propagate(False)
        
        # Container interno para el header
        header_inner = tk.Frame(header_frame, bg=COLORS['header'])
        header_inner.pack(fill=tk.BOTH, expand=True, padx=DIMENSIONS['space_xl'], pady=DIMENSIONS['space_md'])
        
        # Frame para título y breadcrumb
        title_container = tk.Frame(header_inner, bg=COLORS['header'])
        title_container.pack(side=tk.LEFT, fill=tk.Y)
        
        self.header_label = tk.Label(
            title_container,
            text="Bienvenido",
            font=FONTS['header'],
            bg=COLORS['header'],
            fg=COLORS['text_dark'],
            anchor="w"
        )
        self.header_label.pack(anchor='w')
        
        # Breadcrumb/subtítulo
        self.breadcrumb_label = tk.Label(
            title_container,
            text="Inicio • Panel Principal",
            font=FONTS['small'],
            bg=COLORS['header'],
            fg=COLORS['text_muted'],
            anchor="w"
        )
        self.breadcrumb_label.pack(anchor='w', pady=(DIMENSIONS['space_xs'], 0))
        
        # Frame para acciones rápidas (derecha)
        actions_frame = tk.Frame(header_inner, bg=COLORS['header'])
        actions_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botón de ayuda rápida
        help_btn = tk.Button(
            actions_frame,
            text=ICONS['help'] + " Ayuda",
            font=FONTS['small'],
            bg=COLORS['info'],
            fg=COLORS['text_light'],
            relief=tk.FLAT,
            cursor="hand2",
            padx=DIMENSIONS['space_md'],
            pady=DIMENSIONS['space_sm'],
            command=self.show_help
        )
        help_btn.pack(side=tk.RIGHT, padx=DIMENSIONS['space_xs'])
        
        # Línea separadora sutil debajo del header
        separator_line = tk.Frame(main_container, height=1, bg=COLORS['border'])
        separator_line.grid(row=0, column=0, sticky="ews")
        
        # Área de contenido principal con padding
        content_container = tk.Frame(main_container, bg=COLORS['background'])
        content_container.grid(row=1, column=0, sticky="nsew")
        content_container.grid_rowconfigure(0, weight=1)
        content_container.grid_columnconfigure(0, weight=1)
        
        self.content_frame = tk.Frame(
            content_container,
            bg=COLORS['content_bg']
        )
        self.content_frame.grid(row=0, column=0, sticky="nsew", 
                               padx=DIMENSIONS['space_md'], 
                               pady=DIMENSIONS['space_md'])
    
    def navigate_to(self, page_id):
        """
        Navega a una página específica con actualización visual.
        
        Args:
            page_id: Identificador de la página
        """
        # Actualizar estilo de botones
        for btn_id, btn in self.nav_buttons.items():
            if btn_id == page_id:
                # Botón activo
                if btn_id == "laboratorio":
                    btn.configure(bg=COLORS['accent_dark'])
                else:
                    btn.configure(bg=COLORS['button_active'])
            else:
                # Botón inactivo
                if btn_id == "laboratorio":
                    btn.configure(bg=COLORS['accent'])
                else:
                    btn.configure(bg=COLORS['button'])
        
        # Actualizar breadcrumb
        page_names = {
            'inicio': 'Inicio • Panel Principal',
            'laboratorio': 'Laboratorio • Modo Educativo',
            'newton': 'Simuladores • Enfriamiento de Newton',
            'van_der_pol': 'Simuladores • Van der Pol',
            'sir': 'Simuladores • Modelo SIR',
            'rlc': 'Simuladores • Circuito RLC',
            'lorenz': 'Simuladores • Sistema de Lorenz',
            'hopf': 'Simuladores • Bifurcación de Hopf'
        }
        
        self.breadcrumb_label.config(text=page_names.get(page_id, 'Navegación'))
        
        # Cambiar página
        self.nav_manager.show_page(page_id)
    
    def show_help(self):
        """Muestra ventana de ayuda rápida."""
        from tkinter import messagebox
        messagebox.showinfo(
            "Ayuda Rápida",
            "🎯 Simulador de Sistemas Dinámicos\n\n"
            "📚 Cómo usar:\n"
            "1. Selecciona un sistema del menú lateral\n"
            "2. Ajusta los parámetros con los sliders\n"
            "3. Presiona 'Ejecutar Simulación'\n"
            "4. Analiza los resultados\n\n"
            "🧪 Modo Laboratorio:\n"
            "• Genera ejercicios automáticos\n"
            "• Responde preguntas\n"
            "• Recibe feedback personalizado\n\n"
            "💡 Los ejercicios se guardan automáticamente"
        )
    
    def create_toggle_button(self):
        """Crea un botón flotante siempre visible para toggle del sidebar."""
        self.toggle_btn = tk.Button(
            self.root,
            text="☰",
            font=('Segoe UI', 18, 'bold'),
            bg=COLORS['accent'],  # Naranja
            fg='white',
            activebackground=COLORS['accent_dark'],
            activeforeground='white',
            relief=tk.FLAT,
            cursor="hand2",
            command=self.toggle_sidebar,
            width=3,
            height=1
        )
        # Posicionar en la esquina superior izquierda
        self.toggle_btn.place(x=10, y=10)
        
        # Efecto hover
        self.toggle_btn.bind('<Enter>', lambda e: self.toggle_btn.configure(bg=COLORS['accent_light']))
        self.toggle_btn.bind('<Leave>', lambda e: self.toggle_btn.configure(bg=COLORS['accent']))
    
    def toggle_sidebar(self):
        """Alterna la visibilidad del sidebar."""
        if self.sidebar_visible:
            # Ocultar sidebar
            self.sidebar.grid_remove()
            self.toggle_btn.config(text="☰")
            self.sidebar_visible = False
        else:
            # Mostrar sidebar
            self.sidebar.grid()
            self.toggle_btn.config(text="☰")
            self.sidebar_visible = True
    
    def run(self):
        """
        Inicia el loop principal de la aplicación.
        """
        self.root.mainloop()


def main():
    """
    Función principal que crea y ejecuta la aplicación.
    """
    # Instalar dependencias automáticamente
    install_requirements()

    root = tk.Tk()
    app = SimulatorApp(root)
    app.run()


if __name__ == "__main__":
    main()
