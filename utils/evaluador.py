"""
Sistema de evaluación automática para ejercicios de laboratorio.
"""

import numpy as np
from utils.ejercicio_state import EjercicioState


class Evaluador:
    """
    Evalúa las respuestas de los estudiantes y proporciona feedback educativo.
    """
    
    def __init__(self):
        """Inicializa el evaluador."""
        self.respuestas_estudiante = {}
        self.puntuacion_total = 0
        self.puntuacion_maxima = 0
    
    def evaluar_ejercicio(self, ejercicio, respuestas):
        """
        Evalúa un ejercicio completo.
        
        Args:
            ejercicio: Diccionario con el ejercicio generado
            respuestas: Diccionario con las respuestas del estudiante
            
        Returns:
            Diccionario con resultados de evaluación
        """
        self.respuestas_estudiante = respuestas
        self.puntuacion_total = 0
        self.puntuacion_maxima = len(ejercicio['preguntas']) * 10
        
        resultados = {
            'preguntas': [],
            'puntuacion': 0,
            'puntuacion_maxima': self.puntuacion_maxima,
            'porcentaje': 0,
            'feedback_general': '',
            'aprobado': False
        }
        
        # Evaluar cada pregunta
        for i, pregunta in enumerate(ejercicio['preguntas']):
            pregunta_id = pregunta['id']
            respuesta = respuestas.get(pregunta_id, None)
            
            resultado_pregunta = self._evaluar_pregunta(pregunta, respuesta)
            resultados['preguntas'].append(resultado_pregunta)
            
            if resultado_pregunta['correcta']:
                self.puntuacion_total += 10
        
        # Calcular porcentaje
        resultados['puntuacion'] = self.puntuacion_total
        resultados['porcentaje'] = (self.puntuacion_total / self.puntuacion_maxima) * 100
        resultados['aprobado'] = resultados['porcentaje'] >= 70
        
        # Generar feedback general
        resultados['feedback_general'] = self._generar_feedback_general(
            resultados['porcentaje'],
            ejercicio['sistema']
        )
        
        return resultados
    
    def _evaluar_pregunta(self, pregunta, respuesta):
        """
        Evalúa una pregunta individual.
        
        Args:
            pregunta: Diccionario con la pregunta
            respuesta: Respuesta del estudiante
            
        Returns:
            Diccionario con el resultado de la pregunta
        """
        tipo = pregunta['tipo']
        
        if tipo == 'numerica':
            return self._evaluar_numerica(pregunta, respuesta)
        elif tipo == 'opcion_multiple':
            return self._evaluar_opcion_multiple(pregunta, respuesta)
        else:
            return {
                'id': pregunta['id'],
                'correcta': False,
                'feedback': 'Tipo de pregunta no reconocido',
                'puntos': 0
            }
    
    def _evaluar_numerica(self, pregunta, respuesta):
        """Evalúa una pregunta numérica."""
        if respuesta is None:
            return {
                'id': pregunta['id'],
                'correcta': False,
                'feedback': '❌ No se proporcionó respuesta',
                'puntos': 0,
                'respuesta_esperada': pregunta['respuesta_esperada']
            }
        
        try:
            respuesta_num = float(respuesta)
            esperada = pregunta['respuesta_esperada']
            tolerancia = pregunta.get('tolerancia', 0.1)
            
            diferencia = abs(respuesta_num - esperada)
            correcta = diferencia <= tolerancia
            
            if correcta:
                feedback = f'✅ ¡Correcto! Respuesta: {respuesta_num:.2f} {pregunta.get("unidad", "")}'
            else:
                porcentaje_error = (diferencia / esperada) * 100
                feedback = (f'❌ Incorrecto. Tu respuesta: {respuesta_num:.2f}. '
                           f'Respuesta esperada: {esperada:.2f} {pregunta.get("unidad", "")} '
                           f'(Error: {porcentaje_error:.1f}%)')
            
            return {
                'id': pregunta['id'],
                'correcta': correcta,
                'feedback': feedback,
                'puntos': 10 if correcta else 0,
                'respuesta_estudiante': respuesta_num,
                'respuesta_esperada': esperada,
                'error': diferencia
            }
        
        except (ValueError, TypeError):
            return {
                'id': pregunta['id'],
                'correcta': False,
                'feedback': f'❌ Respuesta inválida. Se esperaba un número.',
                'puntos': 0,
                'respuesta_esperada': pregunta['respuesta_esperada']
            }
    
    def _evaluar_opcion_multiple(self, pregunta, respuesta):
        """Evalúa una pregunta de opción múltiple."""
        if respuesta is None:
            return {
                'id': pregunta['id'],
                'correcta': False,
                'feedback': '❌ No se proporcionó respuesta',
                'puntos': 0,
                'respuesta_correcta': pregunta['opciones'][pregunta['respuesta_correcta']]
            }
        
        try:
            respuesta_idx = int(respuesta)
            correcta_idx = pregunta['respuesta_correcta']
            correcta = respuesta_idx == correcta_idx
            
            respuesta_texto = pregunta['opciones'][respuesta_idx]
            correcta_texto = pregunta['opciones'][correcta_idx]
            
            if correcta:
                feedback = f'✅ ¡Correcto! "{respuesta_texto}"'
            else:
                feedback = (f'❌ Incorrecto. Seleccionaste: "{respuesta_texto}". '
                           f'La respuesta correcta es: "{correcta_texto}"')
            
            return {
                'id': pregunta['id'],
                'correcta': correcta,
                'feedback': feedback,
                'puntos': 10 if correcta else 0,
                'respuesta_estudiante': respuesta_texto,
                'respuesta_correcta': correcta_texto
            }
        
        except (ValueError, TypeError, IndexError):
            return {
                'id': pregunta['id'],
                'correcta': False,
                'feedback': '❌ Respuesta inválida',
                'puntos': 0,
                'respuesta_correcta': pregunta['opciones'][pregunta['respuesta_correcta']]
            }
    
    def _generar_feedback_general(self, porcentaje, sistema):
        """
        Genera feedback general basado en el porcentaje de aciertos.
        
        Args:
            porcentaje: Porcentaje de respuestas correctas
            sistema: Nombre del sistema dinámico
            
        Returns:
            Mensaje de feedback
        """
        if porcentaje >= 90:
            nivel = "¡Excelente!"
            mensaje = (f"Has demostrado un dominio excepcional del sistema {sistema}. "
                      "Comprensión profunda de los conceptos fundamentales.")
        elif porcentaje >= 70:
            nivel = "¡Bien hecho!"
            mensaje = (f"Muestras un buen entendimiento del sistema {sistema}. "
                      "Continúa practicando para perfeccionar tu conocimiento.")
        elif porcentaje >= 50:
            nivel = "Aprobado con margen"
            mensaje = (f"Tienes conocimientos básicos del sistema {sistema}. "
                      "Te recomendamos revisar la teoría y practicar más ejercicios.")
        else:
            nivel = "Necesitas mejorar"
            mensaje = (f"Parece que hay dificultades con el sistema {sistema}. "
                      "Te sugerimos revisar los conceptos fundamentales y consultar el material de apoyo.")
        
        return f"{nivel}\n{mensaje}\n\nPuntuación: {porcentaje:.1f}%"
    
    def generar_reporte(self, ejercicio, resultados):
        """
        Genera un reporte detallado del ejercicio.
        
        Args:
            ejercicio: Ejercicio evaluado
            resultados: Resultados de la evaluación
            
        Returns:
            String con el reporte formateado
        """
        reporte = []
        reporte.append("=" * 60)
        reporte.append(f"REPORTE DE LABORATORIO: {ejercicio['titulo']}")
        reporte.append("=" * 60)
        reporte.append(f"Dificultad: {ejercicio['dificultad'].upper()}")
        reporte.append(f"Sistema: {ejercicio['sistema']}")
        reporte.append("")
        
        # Parámetros utilizados
        reporte.append("PARÁMETROS DEL EJERCICIO:")
        for param, valor in ejercicio['parametros'].items():
            reporte.append(f"  • {param} = {valor}")
        reporte.append("")
        
        # Resultados por pregunta
        reporte.append("RESULTADOS POR PREGUNTA:")
        for i, resultado in enumerate(resultados['preguntas'], 1):
            reporte.append(f"\nPregunta {i}:")
            reporte.append(f"  {resultado['feedback']}")
            reporte.append(f"  Puntos: {resultado['puntos']}/10")
        
        reporte.append("")
        reporte.append("-" * 60)
        
        # Resumen
        reporte.append(f"PUNTUACIÓN TOTAL: {resultados['puntuacion']}/{resultados['puntuacion_maxima']}")
        reporte.append(f"PORCENTAJE: {resultados['porcentaje']:.1f}%")
        reporte.append(f"ESTADO: {'APROBADO ✓' if resultados['aprobado'] else 'NO APROBADO ✗'}")
        reporte.append("")
        
        # Feedback general
        reporte.append("FEEDBACK:")
        reporte.append(resultados['feedback_general'])
        reporte.append("")
        
        # Análisis requerido
        if 'analisis_requerido' in ejercicio:
            reporte.append("ANÁLISIS REQUERIDO:")
            for analisis in ejercicio['analisis_requerido']:
                reporte.append(f"  • {analisis}")
        
        reporte.append("=" * 60)
        
        return "\n".join(reporte)
    
    def sugerencias_mejora(self, ejercicio, resultados):
        """
        Genera sugerencias personalizadas de mejora.
        
        Args:
            ejercicio: Ejercicio evaluado
            resultados: Resultados de la evaluación
            
        Returns:
            Lista de sugerencias
        """
        sugerencias = []
        sistema = ejercicio['sistema']
        
        # Sugerencias por sistema
        sugerencias_por_sistema = {
            'newton': [
                "Revisar la definición de constante de enfriamiento",
                "Practicar el cálculo de tiempo de enfriamiento",
                "Estudiar la aproximación asintótica a la temperatura ambiente"
            ],
            'van_der_pol': [
                "Comprender el concepto de ciclos límite",
                "Analizar el efecto del parámetro μ",
                "Estudiar sistemas no lineales"
            ],
            'sir': [
                "Calcular el número reproductivo básico R₀",
                "Comprender la dinámica de epidemias",
                "Analizar el pico de infectados"
            ],
            'hopf': [
                "Estudiar bifurcaciones en sistemas dinámicos",
                "Comprender la transición a ciclo límite",
                "Identificar valores críticos de parámetros"
            ],
            'logistico': [
                "Revisar el concepto de capacidad de carga",
                "Analizar el punto de inflexión",
                "Estudiar crecimiento logístico vs exponencial"
            ],
            'verhulst': [
                "Comprender el diagrama de bifurcación",
                "Estudiar el camino al caos",
                "Analizar sistemas discretos"
            ],
            'orbital': [
                "Revisar las leyes de Kepler",
                "Comprender la conservación de energía",
                "Estudiar órbitas elípticas"
            ],
            'mariposa': [
                "Comprender atractores extraños",
                "Estudiar sistemas caóticos",
                "Analizar la teoría del caos"
            ],
            'amortiguador': [
                "Calcular el factor de amortiguamiento",
                "Comprender tipos de amortiguamiento",
                "Analizar sistemas mecánicos"
            ]
        }
        
        # Agregar sugerencias generales si el porcentaje es bajo
        if resultados['porcentaje'] < 70:
            sugerencias.append("📚 Revisar la teoría fundamental del sistema")
            sugerencias.append("💻 Practicar con más ejercicios similares")
            sugerencias.append("📊 Analizar gráficos y resultados con más detalle")
        
        # Agregar sugerencias específicas del sistema
        if sistema in sugerencias_por_sistema:
            sugerencias.extend(sugerencias_por_sistema[sistema])
        
        # Sugerencias basadas en preguntas incorrectas
        for pregunta, resultado in zip(ejercicio['preguntas'], resultados['preguntas']):
            if not resultado['correcta']:
                if pregunta['tipo'] == 'numerica':
                    sugerencias.append(f"🔢 Revisar cálculos numéricos: {pregunta['texto']}")
                else:
                    sugerencias.append(f"💡 Reforzar concepto: {pregunta['texto']}")
        
        return list(set(sugerencias))  # Eliminar duplicados
