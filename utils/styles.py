"""
Configuración de estilos, colores y fuentes para la aplicación.
Paleta moderna con enfoque en accesibilidad y experiencia de usuario.
"""

# Paleta de colores profesional - Azul y Grises
COLORS = {
    # Fondos principales
    'background': '#f8f9fa',          # Gris muy claro
    'sidebar': '#2c3e50',             # Azul oscuro profesional
    'sidebar_hover': '#34495e',       # Azul oscuro hover
    'header': '#f5f6f7',              # Gris muy claro
    'content_bg': '#f5f6f7',          # Gris muy claro
    
    # Botones y elementos interactivos
    'button': '#3498db',              # Azul profesional
    'button_active': '#2980b9',       # Azul oscuro activo
    'button_hover': '#5dade2',        # Azul claro hover
    
    # Acentos y destacados
    'accent': '#3498db',              # Azul principal
    'accent_light': '#85c1e9',        # Azul claro
    'accent_dark': '#2471a3',         # Azul oscuro
    'secondary': '#95a5a6',           # Gris azulado
    'secondary_light': '#bdc3c7',     # Gris claro
    
    # Textos
    'text_dark': '#2c3e50',           # Azul oscuro
    'text_medium': '#7f8c8d',         # Gris medio
    'text_light': '#ecf0f1',          # Gris muy claro
    'text_muted': '#95a5a6',          # Gris azulado
    
    # Estados y feedback
    'success': '#27ae60',             # Verde profesional
    'success_light': '#a9dfbf',       # Verde claro
    'danger': '#e74c3c',              # Rojo profesional
    'danger_light': '#f5b7b1',        # Rojo claro
    'warning': '#f39c12',             # Naranja advertencia
    'warning_light': '#fad7a0',       # Naranja claro
    'info': '#3498db',                # Azul información
    'info_light': '#d6eaf8',          # Azul muy claro
    
    # Elementos de UI
    'border': '#dee2e6',              # Borde sutil
    'border_dark': '#bdc3c7',         # Borde visible
    'graph_bg': '#fafbfc',            # Gris muy claro para gráficos
    'card_bg': '#fafbfc',             # Gris muy claro para tarjetas
    'card_shadow': '#e8e8e8',         # Sombra tarjetas
    'input_bg': '#fafbfc',            # Gris muy claro para inputs
    'input_border': '#ced4da',        # Borde inputs
    
    # Gradientes (representados como tuplas de colores)
    'gradient_primary': ('#3498db', '#2980b9'),
    'gradient_secondary': ('#5dade2', '#3498db'),
    'gradient_success': ('#58d68d', '#27ae60'),
}

# Fuentes optimizadas para legibilidad
FONTS = {
    # Títulos
    'title_large': ('Segoe UI', 32, 'bold'),      # Títulos principales
    'title': ('Segoe UI', 28, 'bold'),            # Títulos de página
    'header': ('Segoe UI', 24, 'bold'),           # Encabezados
    'section_title': ('Segoe UI', 18, 'bold'),    # Títulos de sección
    'subsection': ('Segoe UI', 14, 'bold'),       # Subtítulos
    
    # Navegación y botones
    'sidebar_title': ('Segoe UI', 13, 'bold'),    # Título sidebar
    'nav_button': ('Segoe UI', 11),               # Botones navegación
    'button': ('Segoe UI', 11, 'bold'),           # Botones generales
    'button_large': ('Segoe UI', 12, 'bold'),     # Botones grandes
    
    # Texto general
    'body': ('Segoe UI', 11),                     # Texto cuerpo
    'label': ('Segoe UI', 10),                    # Etiquetas
    'value': ('Segoe UI', 11, 'bold'),            # Valores
    'small': ('Segoe UI', 9),                     # Texto pequeño
    'small_bold': ('Segoe UI', 9, 'bold'),         # Texto pequeño en negrita
    'tiny': ('Segoe UI', 8),                      # Texto muy pequeño
    
    # Especiales
    'code': ('Consolas', 10),                     # Código
    'equation': ('Cambria Math', 11),             # Ecuaciones
    'icon': ('Segoe UI Emoji', 16),               # Iconos
    'icon_large': ('Segoe UI Emoji', 24),         # Iconos grandes
}

# Dimensiones y espaciado
DIMENSIONS = {
    # Contenedores principales
    'sidebar_width': 280,              # Ancho sidebar
    'header_height': 90,               # Alto header
    'footer_height': 60,               # Alto footer
    
    # Elementos interactivos
    'button_height': 45,               # Alto botones
    'button_height_small': 35,         # Botones pequeños
    'input_height': 40,                # Alto inputs
    'slider_length': 300,              # Largo sliders
    'slider_thickness': 20,            # Grosor sliders
    
    # Espaciado (siguiendo escala 4px)
    'space_xs': 4,                     # Extra pequeño
    'space_sm': 8,                     # Pequeño
    'space_md': 16,                    # Medio
    'space_lg': 24,                    # Grande
    'space_xl': 32,                    # Extra grande
    'space_xxl': 48,                   # Doble extra grande
    
    # Padding (legacy - mantener compatibilidad)
    'padding_small': 8,
    'padding_medium': 16,
    'padding_large': 24,
    
    # Bordes y sombras
    'border_radius': 8,                # Radio bordes
    'border_radius_large': 12,         # Radio grande
    'border_width': 1,                 # Ancho borde
    'shadow_offset': 2,                # Offset sombra
    
    # Tarjetas y paneles
    'card_min_width': 200,             # Ancho mínimo tarjeta
    'card_max_width': 350,             # Ancho máximo tarjeta
    'panel_min_height': 100,           # Alto mínimo panel
}

# Efectos visuales
EFFECTS = {
    'transition_speed': 200,           # ms para transiciones
    'hover_lift': 2,                   # px elevación en hover
    'shadow_blur': 10,                 # Radio desenfoque sombra
    'animation_duration': 300,         # ms para animaciones
}

# Iconos y emojis organizados por categoría
ICONS = {
    # Navegación
    'home': '🏠',
    'lab': '🧪',
    'settings': '⚙️',
    'info': 'ℹ️',
    'help': '❓',
    
    # Acciones
    'play': '▶',
    'pause': '⏸',
    'stop': '⏹',
    'reset': '🔄',
    'clear': '🗑️',
    'save': '💾',
    'load': '📁',
    'export': '📤',
    
    # Estados
    'success': '✅',
    'error': '❌',
    'warning': '⚠️',
    'pending': '⏳',
    'active': '🟢',
    
    # Sistemas dinámicos
    'newton': '🌡️',
    'van_der_pol': '📈',
    'sir': '🦠',
    'rlc': '⚡',
    'lorenz': '🌀',
    'hopf': '🔄',
    'logistic': '📊',
    'orbital': '🛰️',
    'butterfly': '🦋',
    'damper': '🔧',
    
    # Educación
    'book': '📚',
    'clipboard': '📋',
    'graph': '📊',
    'formula': '📐',
    'microscope': '🔬',
    'target': '🎯',
    'lightbulb': '💡',
    'star': '⭐',
    'time': '⏱️',
}
