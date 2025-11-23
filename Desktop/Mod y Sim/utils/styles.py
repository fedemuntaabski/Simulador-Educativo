"""
Configuración de estilos, colores y fuentes para la aplicación.
Paleta moderna con enfoque en accesibilidad y experiencia de usuario.
"""

# Paleta de colores moderna y profesional
COLORS = {
    # Fondos principales
    'background': '#f5f7fa',          # Gris muy claro
    'sidebar': '#1e2a38',             # Azul oscuro profesional
    'sidebar_hover': '#2a3f54',       # Hover para sidebar
    'header': '#ffffff',              # Blanco puro
    'content_bg': '#ffffff',          # Blanco
    
    # Botones y elementos interactivos
    'button': '#3d5a80',              # Azul medio
    'button_active': '#ee6c4d',       # Naranja vibrante para activo
    'button_hover': '#98c1d9',        # Azul claro para hover
    
    # Acentos y destacados
    'accent': '#ee6c4d',              # Naranja principal
    'accent_light': '#ffa07a',        # Naranja claro
    'accent_dark': '#c9573d',         # Naranja oscuro
    'secondary': '#3d5a80',           # Azul secundario
    'secondary_light': '#98c1d9',     # Azul claro
    
    # Textos
    'text_dark': '#1e2a38',           # Casi negro azulado
    'text_medium': '#4a5568',         # Gris medio
    'text_light': '#ffffff',          # Blanco
    'text_muted': '#a0aec0',          # Gris claro
    
    # Estados y feedback
    'success': '#48bb78',             # Verde éxito
    'success_light': '#9ae6b4',       # Verde claro
    'danger': '#f56565',              # Rojo peligro
    'danger_light': '#fc8181',        # Rojo claro
    'warning': '#ed8936',             # Naranja advertencia
    'warning_light': '#fbd38d',       # Naranja claro
    'info': '#4299e1',                # Azul información
    'info_light': '#90cdf4',          # Azul claro
    
    # Elementos de UI
    'border': '#e2e8f0',              # Borde sutil
    'border_dark': '#cbd5e0',         # Borde más visible
    'graph_bg': '#ffffff',            # Fondo gráficos
    'card_bg': '#ffffff',             # Fondo tarjetas
    'card_shadow': '#e2e8f0',         # Sombra tarjetas
    'input_bg': '#f7fafc',            # Fondo inputs
    'input_border': '#cbd5e0',        # Borde inputs
    
    # Gradientes (representados como tuplas de colores)
    'gradient_primary': ('#ee6c4d', '#c9573d'),
    'gradient_secondary': ('#3d5a80', '#2a4365'),
    'gradient_success': ('#48bb78', '#38a169'),
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
