"""
Utilidades para la integración de gráficos de Matplotlib en Tkinter.
Versión mejorada con estilos modernos y formateo de valores.
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from utils.styles import COLORS, GRAPH_STYLE


class GraphCanvas:
    """
    Clase helper para crear y gestionar canvas de Matplotlib en Tkinter.
    Versión mejorada con estilos modernos.
    """
    
    def __init__(self, parent, figsize=(10, 6), dpi=100):
        """
        Inicializa el canvas de gráficos.
        
        Args:
            parent: Widget padre de Tkinter
            figsize: Tamaño de la figura (ancho, alto) en pulgadas
            dpi: Resolución de la figura
        """
        self.parent = parent
        self.figure = Figure(figsize=figsize, dpi=dpi, facecolor='#fafbfc')
        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas_widget = self.canvas.get_tk_widget()
        
        # Crear subplot principal con estilo mejorado
        self.ax = self.figure.add_subplot(111)
        self._apply_modern_style()
    
    def _apply_modern_style(self):
        """Aplica estilo moderno al gráfico."""
        self.ax.set_facecolor('#fafbfc')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_color('#bdc3c7')
        self.ax.spines['bottom'].set_color('#bdc3c7')
        self.ax.tick_params(colors='#2c3e50', labelsize=9)
        
    def get_widget(self):
        """Retorna el widget de Tkinter del canvas."""
        return self.canvas_widget
    
    def clear(self):
        """Limpia el gráfico actual."""
        self.ax.clear()
        self._apply_modern_style()
        self.canvas.draw()
    
    def plot(self, *args, **kwargs):
        """Crea un gráfico de línea con estilo mejorado."""
        if 'linewidth' not in kwargs:
            kwargs['linewidth'] = GRAPH_STYLE['linewidth']
        self.ax.plot(*args, **kwargs)
        self.canvas.draw()
    
    def scatter(self, *args, **kwargs):
        """Crea un gráfico de dispersión con estilo mejorado."""
        if 's' not in kwargs:
            kwargs['s'] = GRAPH_STYLE['marker_size']
        self.ax.scatter(*args, **kwargs)
        self.canvas.draw()
    
    def fill_between(self, *args, **kwargs):
        """Crea un área rellena entre curvas."""
        self.ax.fill_between(*args, **kwargs)
        self.canvas.draw()
    
    def axhline(self, *args, **kwargs):
        """Crea una línea horizontal."""
        self.ax.axhline(*args, **kwargs)
        self.canvas.draw()
    
    def axvline(self, *args, **kwargs):
        """Crea una línea vertical."""
        self.ax.axvline(*args, **kwargs)
        self.canvas.draw()
    
    def set_labels(self, xlabel='', ylabel='', title=''):
        """
        Configura las etiquetas de los ejes y título con estilo mejorado.
        
        Args:
            xlabel: Etiqueta del eje X
            ylabel: Etiqueta del eje Y
            title: Título del gráfico
        """
        if xlabel:
            self.ax.set_xlabel(xlabel, fontsize=GRAPH_STYLE['label_fontsize'], 
                             color='#2c3e50', fontweight='medium')
        if ylabel:
            self.ax.set_ylabel(ylabel, fontsize=GRAPH_STYLE['label_fontsize'], 
                             color='#2c3e50', fontweight='medium')
        if title:
            self.ax.set_title(title, fontsize=GRAPH_STYLE['title_fontsize'], 
                            color='#2c3e50', fontweight='bold', pad=15)
        self.canvas.draw()
    
    def grid(self, visible=True, **kwargs):
        """Activa o desactiva la grilla con estilo mejorado."""
        if 'alpha' not in kwargs:
            kwargs['alpha'] = GRAPH_STYLE['grid_alpha']
        if 'linestyle' not in kwargs:
            kwargs['linestyle'] = '--'
        if 'color' not in kwargs:
            kwargs['color'] = '#bdc3c7'
        self.ax.grid(visible, **kwargs)
        self.canvas.draw()
    
    def legend(self, *args, **kwargs):
        """Agrega una leyenda al gráfico con estilo mejorado."""
        if 'fontsize' not in kwargs:
            kwargs['fontsize'] = GRAPH_STYLE['legend_fontsize']
        if 'framealpha' not in kwargs:
            kwargs['framealpha'] = 0.9
        if 'edgecolor' not in kwargs:
            kwargs['edgecolor'] = '#bdc3c7'
        self.ax.legend(*args, **kwargs)
        self.canvas.draw()
    
    def tight_layout(self):
        """Ajusta el layout de la figura."""
        self.figure.tight_layout()
        self.canvas.draw()


class Graph3DCanvas(GraphCanvas):
    """
    Clase helper especializada para gráficos 3D.
    """
    
    def __init__(self, parent, figsize=(10, 6), dpi=100):
        """
        Inicializa el canvas de gráficos 3D.
        
        Args:
            parent: Widget padre de Tkinter
            figsize: Tamaño de la figura (ancho, alto) en pulgadas
            dpi: Resolución de la figura
        """
        self.parent = parent
        self.figure = Figure(figsize=figsize, dpi=dpi, facecolor='#fafbfc')
        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas_widget = self.canvas.get_tk_widget()
        
        # Crear subplot 3D
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.ax.set_facecolor('#fafbfc')
    
    def _apply_modern_style(self):
        """Override para 3D - estilo simplificado."""
        self.ax.set_facecolor('#fafbfc')
    
    def clear(self):
        """Limpia el gráfico 3D actual."""
        self.ax.clear()
        self.ax.set_facecolor('#fafbfc')
        self.canvas.draw()
    
    def set_labels(self, xlabel='', ylabel='', zlabel='', title=''):
        """
        Configura las etiquetas de los ejes y título para gráfico 3D.
        
        Args:
            xlabel: Etiqueta del eje X
            ylabel: Etiqueta del eje Y
            zlabel: Etiqueta del eje Z
            title: Título del gráfico
        """
        if xlabel:
            self.ax.set_xlabel(xlabel, fontsize=GRAPH_STYLE['label_fontsize'], 
                             color='#2c3e50')
        if ylabel:
            self.ax.set_ylabel(ylabel, fontsize=GRAPH_STYLE['label_fontsize'], 
                             color='#2c3e50')
        if zlabel:
            self.ax.set_zlabel(zlabel, fontsize=GRAPH_STYLE['label_fontsize'], 
                             color='#2c3e50')
        if title:
            self.ax.set_title(title, fontsize=GRAPH_STYLE['title_fontsize'], 
                            color='#2c3e50', fontweight='bold', pad=10)
        self.canvas.draw()
