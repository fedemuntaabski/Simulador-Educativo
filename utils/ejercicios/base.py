"""
Clase base y helpers para generación de ejercicios.
Implementa métodos helper DRY usados por todos los generadores.
"""

import random
import numpy as np


class EjercicioBase:
    """
    Clase base con métodos helper para generar ejercicios.
    Implementa funcionalidad común siguiendo principios DRY.
    """
    
    # Niveles de dificultad
    DIFICULTAD = {
        'principiante': 1,
        'intermedio': 2,
        'avanzado': 3
    }
    
    # Preguntas por nivel
    PREGUNTAS_POR_NIVEL = {
        1: 3,
        2: 4,
        3: 5
    }
    
    @staticmethod
    def seleccionar_preguntas(pools_preguntas, nivel, cantidad=None):
        """
        Selecciona preguntas aleatorias del pool según nivel.
        
        Args:
            pools_preguntas: dict {1: [...], 2: [...], 3: [...]}
            nivel: int (1, 2, 3)
            cantidad: int opcional, usa PREGUNTAS_POR_NIVEL si None
            
        Returns:
            Lista de preguntas seleccionadas y renumeradas
        """
        pool = pools_preguntas.get(nivel, pools_preguntas.get(1, []))
        if cantidad is None:
            cantidad = EjercicioBase.PREGUNTAS_POR_NIVEL.get(nivel, 3)
        
        cantidad = min(cantidad, len(pool))
        preguntas = random.sample(pool, cantidad)
        
        # Renumerar
        for i, p in enumerate(preguntas, 1):
            p['id'] = i
        
        return preguntas
    
    @staticmethod
    def construir_ejercicio(sistema, titulo, dificultad, parametros,
                           objetivos, instrucciones, preguntas, analisis):
        """
        Construye diccionario de ejercicio con estructura estándar.
        """
        return {
            'sistema': sistema,
            'titulo': titulo,
            'dificultad': dificultad,
            'parametros': parametros,
            'objetivos': objetivos,
            'instrucciones': instrucciones,
            'preguntas': preguntas,
            'analisis_requerido': analisis
        }
    
    @staticmethod
    def param_aleatorio(nivel, config):
        """
        Obtiene parámetros según nivel de dificultad.
        
        Args:
            nivel: int (1, 2, 3)
            config: dict con configuración por nivel
                   {1: valor_o_funcion, 2: ..., 3: ...}
        """
        if nivel in config:
            val = config[nivel]
            return val() if callable(val) else val
        return config.get(1, {})
    
    @staticmethod
    def opcion(valores):
        """Selecciona un valor aleatorio de una lista."""
        return random.choice(valores)
    
    @staticmethod  
    def rango(minimo, maximo, decimales=2):
        """Genera valor aleatorio en rango con decimales."""
        return round(random.uniform(minimo, maximo), decimales)
    
    @staticmethod
    def entero(minimo, maximo):
        """Genera entero aleatorio en rango."""
        return random.randint(minimo, maximo)


class PreguntaBuilder:
    """Builder para crear preguntas de forma fluida."""
    
    @staticmethod
    def opcion_multiple(id_pregunta, texto, opciones, correcta):
        """Crea pregunta de opción múltiple."""
        return {
            'id': id_pregunta,
            'texto': texto,
            'tipo': 'opcion_multiple',
            'opciones': opciones,
            'respuesta_correcta': correcta
        }
    
    @staticmethod
    def numerica(id_pregunta, texto, esperada, tolerancia, unidad=''):
        """Crea pregunta numérica."""
        return {
            'id': id_pregunta,
            'texto': texto,
            'tipo': 'numerica',
            'respuesta_esperada': esperada,
            'tolerancia': tolerancia,
            'unidad': unidad
        }
