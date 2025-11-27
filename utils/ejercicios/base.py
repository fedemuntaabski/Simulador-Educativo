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
                           objetivos, instrucciones, preguntas, analisis,
                           contexto=None, datos_adicionales=None):
        """
        Construye diccionario de ejercicio con estructura estándar.
        """
        ejercicio = {
            'sistema': sistema,
            'titulo': titulo,
            'dificultad': dificultad,
            'parametros': parametros,
            'objetivos': objetivos,
            'instrucciones': instrucciones,
            'preguntas': preguntas,
            'analisis_requerido': analisis
        }
        
        if contexto:
            ejercicio['contexto'] = contexto
        
        if datos_adicionales:
            ejercicio['datos_adicionales'] = datos_adicionales
        
        return ejercicio
    
    @staticmethod
    def param_aleatorio(nivel, config):
        """Obtiene parámetros según nivel de dificultad."""
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


class ConsignaBuilder:
    """
    Builder para construir consignas de forma estandarizada.
    Reduce duplicación en los métodos _construir_consigna_*.
    """
    
    SEPARADOR = "═" * 63
    
    @staticmethod
    def crear(titulo, contexto_texto, datos, modelo, se_pide, experimento=None, notas=None):
        """
        Crea una consigna estandarizada.
        
        Args:
            titulo: Título del ejercicio (ej: "ENFRIAMIENTO DE NEWTON")
            contexto_texto: Lista de líneas de contexto/situación
            datos: Lista de tuplas (nombre, valor, unidad) para la sección DATOS
            modelo: Dict con 'titulo' y 'ecuaciones' (lista de strings)
            se_pide: Lista de strings con los items a resolver
            experimento: String opcional con sugerencia de experimento
            notas: Lista opcional de strings con notas adicionales
            
        Returns:
            dict con 'instrucciones', 'datos', 'analisis'
        """
        instrucciones = [
            ConsignaBuilder.SEPARADOR,
            f"              {titulo} - CONSIGNA",
            ConsignaBuilder.SEPARADOR,
            "",
        ]
        
        # Sección contexto/situación
        if contexto_texto:
            instrucciones.append("📋 SITUACIÓN:")
            for linea in contexto_texto:
                instrucciones.append(f"   {linea}")
            instrucciones.append("")
        
        # Sección datos
        instrucciones.append("📊 DATOS:")
        for dato in datos:
            if len(dato) == 3:
                nombre, valor, unidad = dato
                instrucciones.append(f"   • {nombre}: {valor} {unidad}".strip())
            else:
                nombre, valor = dato
                instrucciones.append(f"   • {nombre}: {valor}")
        instrucciones.append("")
        
        # Sección modelo matemático
        if modelo:
            instrucciones.append(f"📐 {modelo.get('titulo', 'MODELO MATEMÁTICO')}:")
            for eq in modelo.get('ecuaciones', []):
                instrucciones.append(f"   {eq}")
            instrucciones.append("")
        
        # Sección se pide
        instrucciones.append("🎯 SE PIDE:")
        for i, item in enumerate(se_pide):
            letra = chr(ord('a') + i)
            instrucciones.append(f"   {letra}) {item}")
        instrucciones.append("")
        
        # Experimento sugerido
        if experimento:
            instrucciones.append(f"💡 EXPERIMENTO: {experimento}")
            instrucciones.append("")
        
        # Notas adicionales
        if notas:
            for nota in notas:
                instrucciones.append(f"📈 {nota}")
            instrucciones.append("")
        
        # Construir datos simplificados
        datos_dict = {}
        for dato in datos:
            if len(dato) >= 2:
                # Limpiar el nombre para usarlo como clave
                clave = dato[0].split('(')[0].strip().lower().replace(' ', '_')
                datos_dict[clave] = dato[1]
        
        return {
            'instrucciones': instrucciones,
            'datos': datos_dict,
            'analisis': []
        }
