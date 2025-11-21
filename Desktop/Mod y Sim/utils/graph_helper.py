"""
Utilidades para la integración de gráficos de Matplotlib en Tkinter.
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from utils.styles import COLORS


class GraphCanvas:
    """
    Clase helper para crear y gestionar canvas de Matplotlib en Tkinter.
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
        self.figure = Figure(figsize=figsize, dpi=dpi, facecolor=COLORS['graph_bg'])
        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas_widget = self.canvas.get_tk_widget()
        
        # Crear subplot principal
        self.ax = self.figure.add_subplot(111)
        
    def get_widget(self):
        """Retorna el widget de Tkinter del canvas."""
        return self.canvas_widget
    
    def clear(self):
        """Limpia el gráfico actual."""
        self.ax.clear()
        self.canvas.draw()
    
    def plot(self, *args, **kwargs):
        """Crea un gráfico de línea."""
        self.ax.plot(*args, **kwargs)
        self.canvas.draw()
    
    def scatter(self, *args, **kwargs):
        """Crea un gráfico de dispersión."""
        self.ax.scatter(*args, **kwargs)
        self.canvas.draw()
    
    def set_labels(self, xlabel='', ylabel='', title=''):
        """
        Configura las etiquetas de los ejes y título.
        
        Args:
            xlabel: Etiqueta del eje X
            ylabel: Etiqueta del eje Y
            title: Título del gráfico
        """
        if xlabel:
            self.ax.set_xlabel(xlabel)
        if ylabel:
            self.ax.set_ylabel(ylabel)
        if title:
            self.ax.set_title(title)
        self.canvas.draw()
    
    def grid(self, visible=True):
        """Activa o desactiva la grilla."""
        self.ax.grid(visible, alpha=0.3)
        self.canvas.draw()
    
    def legend(self, *args, **kwargs):
        """Agrega una leyenda al gráfico."""
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
        self.figure = Figure(figsize=figsize, dpi=dpi, facecolor=COLORS['graph_bg'])
        self.canvas = FigureCanvasTkAgg(self.figure, parent)
        self.canvas_widget = self.canvas.get_tk_widget()
        
        # Crear subplot 3D
        self.ax = self.figure.add_subplot(111, projection='3d')
    
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
            self.ax.set_xlabel(xlabel)
        if ylabel:
            self.ax.set_ylabel(ylabel)
        if zlabel:
            self.ax.set_zlabel(zlabel)
        if title:
            self.ax.set_title(title)
        self.canvas.draw()
