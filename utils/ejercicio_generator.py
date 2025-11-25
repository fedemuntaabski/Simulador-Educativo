"""
Generador automático de ejercicios educacionales para sistemas dinámicos.

Principios de diseño:
- DRY: Métodos helper para evitar repetición
- KISS: Lógica simple y clara
- Separación: Datos de preguntas separados de lógica
"""

import random
import numpy as np


class EjercicioGenerator:
    """
    Genera ejercicios automáticos con parámetros aleatorios,
    preguntas teóricas y objetivos de aprendizaje.
    """
    
    # Niveles de dificultad
    DIFICULTAD = {
        'principiante': 1,
        'intermedio': 2,
        'avanzado': 3
    }
    
    # Configuración de cantidad de preguntas por nivel
    PREGUNTAS_POR_NIVEL = {
        1: 3,  # principiante
        2: 4,  # intermedio
        3: 5   # avanzado
    }
    
    def __init__(self):
        """Inicializa el generador de ejercicios."""
        self.ejercicio_actual = None
        self.respuestas_esperadas = {}
    
    # ==================== MÉTODOS HELPER (DRY) ====================
    
    def _seleccionar_preguntas(self, pools_preguntas, nivel):
        """
        Selecciona preguntas aleatorias del pool correspondiente al nivel.
        
        Args:
            pools_preguntas: dict con claves 1, 2, 3 para cada nivel
            nivel: int (1, 2, o 3)
            
        Returns:
            Lista de preguntas seleccionadas y renumeradas
        """
        pool = pools_preguntas.get(nivel, pools_preguntas[1])
        cantidad = min(self.PREGUNTAS_POR_NIVEL[nivel], len(pool))
        preguntas = random.sample(pool, cantidad)
        
        # Renumerar las preguntas
        for i, p in enumerate(preguntas, 1):
            p['id'] = i
        
        return preguntas
    
    def _construir_ejercicio(self, sistema, titulo, dificultad, parametros, 
                             objetivos, instrucciones, preguntas, analisis):
        """
        Construye el diccionario del ejercicio con estructura estándar.
        
        Returns:
            dict con la estructura completa del ejercicio
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
    
    def _param_por_nivel(self, nivel, config):
        """
        Obtiene parámetros según el nivel de dificultad.
        
        Args:
            nivel: int (1, 2, o 3)
            config: dict con claves 1, 2, 3 conteniendo dicts de parámetros
                    o funciones que generan parámetros
            
        Returns:
            dict de parámetros para ese nivel
        """
        if nivel in config:
            val = config[nivel]
            return val() if callable(val) else val
        return config.get(1, {})
    
    def generar_ejercicio(self, sistema, dificultad='intermedio'):
        """
        Genera un ejercicio completo para un sistema dinámico.
        
        Args:
            sistema: Nombre del sistema ('newton', 'van_der_pol', 'sir', etc.)
            dificultad: Nivel de dificultad
            
        Returns:
            Diccionario con el ejercicio completo
        """
        generadores = {
            'newton': self._generar_newton,
            'van_der_pol': self._generar_van_der_pol,
            'sir': self._generar_sir,
            'rlc': self._generar_rlc,
            'lorenz': self._generar_lorenz,
            'hopf': self._generar_hopf,
            'logistico': self._generar_logistico,
            'verhulst': self._generar_verhulst,
            'orbital': self._generar_orbital,
            'mariposa': self._generar_mariposa,
            'amortiguador': self._generar_amortiguador,
            'equilibrio_logistico': self._generar_equilibrio_logistico,
            'verhulst_transiciones': self._generar_verhulst_transiciones,
            'amortiguamiento_analisis': self._generar_amortiguamiento_analisis,
            'ciclo_limite': self._generar_ciclo_limite,
            'hopf_aparicion': self._generar_hopf_aparicion,
            'rlc_resonancia': self._generar_rlc_resonancia,
            'sir_propagacion': self._generar_sir_propagacion,
            'lorenz_sensibilidad': self._generar_lorenz_sensibilidad,
            'orbital_kepler': self._generar_orbital_kepler,
            'orbital_hohmann': self._generar_orbital_hohmann,
            'newton_enfriamiento': self._generar_newton_enfriamiento,
            'rc_carga': self._generar_rc_carga,
            'crecimiento_comparacion': self._generar_crecimiento_comparacion,
            'estabilidad_lineal': self._generar_estabilidad_lineal,
            'sir_vacunacion': self._generar_sir_vacunacion,
            'orbital_perturbaciones': self._generar_orbital_perturbaciones,
            'oscilador_forzado': self._generar_oscilador_forzado
        }
        
        if sistema not in generadores:
            raise ValueError(f"Sistema '{sistema}' no soportado")
        
        ejercicio = generadores[sistema](dificultad)
        self.ejercicio_actual = ejercicio
        return ejercicio
    
    def _generar_newton(self, dificultad):
        """Genera ejercicio de enfriamiento de Newton con preguntas variadas por dificultad."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Parámetros según dificultad
        if nivel == 1:
            T0 = random.choice([100, 90, 80])
            T_env = random.choice([20, 25])
            k = round(random.uniform(0.05, 0.15), 2)
        elif nivel == 2:
            T0 = random.randint(70, 120)
            T_env = random.randint(15, 30)
            k = round(random.uniform(0.08, 0.25), 3)
        else:
            T0 = random.randint(60, 150)
            T_env = random.randint(10, 35)
            k = round(random.uniform(0.05, 0.4), 3)
        
        # Calcular valores para preguntas
        T_objetivo = T_env + (T0 - T_env) * 0.37  # ~1 constante de tiempo
        t_esperado = -np.log((T_objetivo - T_env) / (T0 - T_env)) / k
        tau = 1 / k  # Constante de tiempo
        t_50 = tau * np.log(2)  # Tiempo para 50%
        T_t2 = T_env + (T0 - T_env) * np.exp(-k * 2 * tau)  # Temp en 2τ
        
        # Pool de preguntas según dificultad
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿La temperatura alcanza exactamente la temperatura ambiente?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, eventualmente', 'No, se aproxima asintóticamente', 'Depende de k'],
                'respuesta_correcta': 1
            },
            {
                'id': 2,
                'texto': f'Si k fuera el doble ({2*k:.3f}), ¿el enfriamiento sería?',
                'tipo': 'opcion_multiple',
                'opciones': ['Más rápido', 'Más lento', 'Igual velocidad'],
                'respuesta_correcta': 0
            },
            {
                'id': 3,
                'texto': '¿Qué representa la constante k en la ecuación de Newton?',
                'tipo': 'opcion_multiple',
                'opciones': ['Temperatura final', 'Velocidad de enfriamiento', 'Masa del objeto', 'Calor específico'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': f'¿Qué fracción de la diferencia inicial (T₀-Tₐₘ) queda después de un tiempo τ=1/k?',
                'tipo': 'opcion_multiple',
                'opciones': ['~37% (1/e)', '~50%', '~63%', '~90%'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': '¿El enfriamiento de Newton es un proceso lineal o exponencial?',
                'tipo': 'opcion_multiple',
                'opciones': ['Lineal', 'Exponencial decreciente', 'Cuadrático', 'Logarítmico'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'¿Cuánto tiempo aproximado tarda en llegar a {T_objetivo:.1f}°C?',
                'tipo': 'numerica',
                'respuesta_esperada': t_esperado,
                'tolerancia': 2.0,
                'unidad': 'minutos'
            },
            {
                'id': 2,
                'texto': f'¿Cuál es la constante de tiempo τ = 1/k del sistema?',
                'tipo': 'numerica',
                'respuesta_esperada': tau,
                'tolerancia': tau * 0.1,
                'unidad': 'minutos'
            },
            {
                'id': 3,
                'texto': '¿Qué tipo de ecuación diferencial describe el enfriamiento de Newton?',
                'tipo': 'opcion_multiple',
                'opciones': ['Lineal de primer orden', 'No lineal de primer orden', 'Lineal de segundo orden', 'No lineal de segundo orden'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': f'¿Cuánto tiempo se necesita para reducir la diferencia de temperatura a la mitad?',
                'tipo': 'numerica',
                'respuesta_esperada': t_50,
                'tolerancia': t_50 * 0.15,
                'unidad': 'minutos'
            },
            {
                'id': 5,
                'texto': 'Si duplicamos la diferencia inicial de temperatura, el tiempo para alcanzar T_amb:',
                'tipo': 'opcion_multiple',
                'opciones': ['Se duplica', 'No cambia (asintótico)', 'Se reduce a la mitad', 'Aumenta logarítmicamente'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': '¿Cuál es la solución analítica de la ecuación dT/dt = -k(T - Tₐₘ)?',
                'tipo': 'opcion_multiple',
                'opciones': ['T(t) = T₀·e^(-kt)', 'T(t) = Tₐₘ + (T₀-Tₐₘ)·e^(-kt)', 'T(t) = T₀ - kt', 'T(t) = Tₐₘ·(1 - e^(-kt))'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'¿Cuánto tiempo aproximado tarda en llegar a {T_objetivo:.1f}°C?',
                'tipo': 'numerica',
                'respuesta_esperada': t_esperado,
                'tolerancia': 1.5,
                'unidad': 'minutos'
            },
            {
                'id': 2,
                'texto': f'¿Cuál será la temperatura después de 2 constantes de tiempo (t = 2τ)?',
                'tipo': 'numerica',
                'respuesta_esperada': T_t2,
                'tolerancia': 2.0,
                'unidad': '°C'
            },
            {
                'id': 3,
                'texto': f'Si la temperatura inicial fuera {T0 + 20}°C, ¿cómo cambiaría la tasa inicial de enfriamiento dT/dt|₀?',
                'tipo': 'opcion_multiple',
                'opciones': ['Aumentaría en magnitud', 'Disminuiría en magnitud', 'Permanecería igual', 'Se invertiría'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': 'En el espacio de fases (T, dT/dt), la trayectoria del sistema es:',
                'tipo': 'opcion_multiple',
                'opciones': ['Una elipse', 'Una recta con pendiente -k', 'Una parábola', 'Un ciclo límite'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': f'¿Cuál es la energía disipada relativa E(t)/E₀ después de τ = {tau:.2f} min?',
                'tipo': 'opcion_multiple',
                'opciones': ['1 - e⁻¹ ≈ 0.63', 'e⁻¹ ≈ 0.37', '0.50', '0.25'],
                'respuesta_correcta': 0
            },
            {
                'id': 6,
                'texto': '¿Cómo afecta la convección forzada (mayor k) comparada con convección natural?',
                'tipo': 'opcion_multiple',
                'opciones': ['Enfriamiento más lento', 'Enfriamiento más rápido', 'No hay diferencia', 'Depende de T₀'],
                'respuesta_correcta': 1
            },
            {
                'id': 7,
                'texto': 'El número de Biot (Bi) determina si el enfriamiento de Newton es aplicable. ¿Cuándo es válido?',
                'tipo': 'opcion_multiple',
                'opciones': ['Bi >> 1', 'Bi << 1', 'Bi = 1', 'Siempre es válido'],
                'respuesta_correcta': 1
            }
        ]
        
        # Usar helper para seleccionar preguntas
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        # Usar helper para construir ejercicio
        return self._construir_ejercicio(
            sistema='newton',
            titulo='Ley de Enfriamiento de Newton',
            dificultad=dificultad,
            parametros={'T0': T0, 'T_env': T_env, 'k': k},
            objetivos=[
                'Comprender el proceso de enfriamiento exponencial',
                'Analizar la influencia de la constante k',
                'Predecir el tiempo de enfriamiento',
                'Calcular la constante de tiempo τ'
            ],
            instrucciones=[
                f'1. Configure la temperatura inicial en {T0}°C',
                f'2. Configure la temperatura ambiente en {T_env}°C',
                f'3. Configure la constante k en {k}',
                f'4. Constante de tiempo: τ = 1/k = {tau:.2f} min',
                '5. Ejecute la simulación y observe el comportamiento',
                '6. Responda las preguntas basándose en los resultados'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar la curva de temperatura vs tiempo',
                'Identificar la constante de tiempo del sistema',
                'Comparar con la solución analítica'
            ]
        )
    
    def _generar_van_der_pol(self, dificultad):
        """Genera ejercicio del oscilador de Van der Pol con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            mu = random.choice([0.5, 1.0, 1.5])
            x0, v0 = 1.0, 0.0
        elif nivel == 2:
            mu = round(random.uniform(0.5, 3.0), 1)
            x0 = round(random.uniform(-2, 2), 1)
            v0 = round(random.uniform(-1, 1), 1)
        else:
            mu = round(random.uniform(0.2, 8.0), 2)
            x0 = round(random.uniform(-3, 3), 1)
            v0 = round(random.uniform(-2, 2), 1)
        
        # Pool de preguntas por dificultad
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿El sistema de Van der Pol es lineal o no lineal?',
                'tipo': 'opcion_multiple',
                'opciones': ['Lineal', 'No lineal'],
                'respuesta_correcta': 1
            },
            {
                'id': 2,
                'texto': f'¿El sistema converge a un ciclo límite cuando μ = {mu}?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, para μ > 0', 'No', 'Solo si μ < 0'],
                'respuesta_correcta': 0 if mu > 0 else 1
            },
            {
                'id': 3,
                'texto': '¿Qué representa un ciclo límite en el espacio de fases?',
                'tipo': 'opcion_multiple',
                'opciones': ['Un punto de equilibrio', 'Una oscilación autosostenida periódica', 'Un comportamiento caótico', 'Una trayectoria divergente'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿Cuántos puntos de equilibrio tiene el oscilador de Van der Pol?',
                'tipo': 'opcion_multiple',
                'opciones': ['Ninguno', 'Uno (el origen)', 'Dos', 'Infinitos'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'Con μ = {mu}, ¿qué tipo de comportamiento exhibe el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Oscilación amortiguada', 'Oscilación autosostenida (ciclo límite)', 'Divergencia', 'Punto fijo estable'],
                'respuesta_correcta': 1 if mu > 0 else 0
            },
            {
                'id': 2,
                'texto': '¿El ciclo límite depende de las condiciones iniciales?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, cada condición inicial genera un ciclo diferente', 'No, todas convergen al mismo ciclo límite', 'Solo depende de x₀', 'Solo depende de v₀'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': '¿Qué sucede con la forma del ciclo límite cuando μ aumenta?',
                'tipo': 'opcion_multiple',
                'opciones': ['Se vuelve más circular', 'Se distorsiona (relajación)', 'Desaparece', 'Se vuelve caótico'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': 'El término μ(1-x²)dx/dt en la ecuación representa:',
                'tipo': 'opcion_multiple',
                'opciones': ['Amortiguamiento constante', 'Amortiguamiento negativo no lineal', 'Fuerza externa', 'Resorte no lineal'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': '¿El punto de equilibrio (0,0) es estable o inestable para μ > 0?',
                'tipo': 'opcion_multiple',
                'opciones': ['Estable', 'Inestable (las trayectorias se alejan)', 'Marginalmente estable', 'Depende de las condiciones iniciales'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'Con μ = {mu}, ¿qué tipo de oscilación se observa?',
                'tipo': 'opcion_multiple',
                'opciones': ['Oscilaciones de relajación (μ grande)', 'Oscilaciones casi sinusoidales (μ pequeño)', 'No hay oscilaciones', 'Oscilaciones caóticas'],
                'respuesta_correcta': 0 if mu > 2.0 else 1
            },
            {
                'id': 2,
                'texto': '¿Cuál es el comportamiento del período T cuando μ → 0?',
                'tipo': 'opcion_multiple',
                'opciones': ['T → 0', 'T → 2π (oscilador armónico)', 'T → ∞', 'T permanece constante'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': 'Para μ >> 1, el período aproximado es T ≈ (3 - 2ln2)μ. Esto indica:',
                'tipo': 'opcion_multiple',
                'opciones': ['Período independiente de μ', 'Período crece linealmente con μ', 'Período decrece con μ', 'Período oscila'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿El teorema de Poincaré-Bendixson garantiza la existencia del ciclo límite?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, porque es un sistema plano con región anular invariante', 'No, solo funciona en 3D', 'Solo para μ < 1', 'Nunca se aplica'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': f'Dado μ = {mu}, clasifique el punto fijo del sistema linealizado:',
                'tipo': 'opcion_multiple',
                'opciones': ['Foco inestable', 'Foco estable', 'Nodo inestable', 'Silla'],
                'respuesta_correcta': 0 if mu > 0 else 1
            },
            {
                'id': 6,
                'texto': 'El oscilador de Van der Pol fue originalmente diseñado para modelar:',
                'tipo': 'opcion_multiple',
                'opciones': ['Péndulos', 'Circuitos con tubos de vacío', 'Poblaciones biológicas', 'Órbitas planetarias'],
                'respuesta_correcta': 1
            }
        ]
        
        # Usar helpers para seleccionar preguntas y construir ejercicio
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='van_der_pol',
            titulo='Oscilador de Van der Pol',
            dificultad=dificultad,
            parametros={'mu': mu, 'x0': x0, 'v0': v0},
            objetivos=[
                'Observar el comportamiento de ciclos límite',
                'Analizar el efecto del parámetro μ',
                'Estudiar el diagrama de fase',
                'Comprender oscilaciones de relajación'
            ],
            instrucciones=[
                f'1. Configure μ = {mu}',
                f'2. Configure x(0) = {x0}, dx/dt(0) = {v0}',
                '3. Ejecute la simulación',
                '4. Observe el diagrama de fase (x vs dx/dt)',
                '5. Analice la convergencia al ciclo límite'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar el diagrama de fase',
                'Identificar el ciclo límite',
                'Comparar trayectorias desde diferentes condiciones iniciales',
                'Analizar la estabilidad del punto de equilibrio'
            ]
        )
    
    def _generar_sir(self, dificultad):
        """Genera ejercicio del modelo SIR con preguntas variadas por dificultad."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            S0, I0, R0 = 990, 10, 0
            beta = 0.3
            gamma = 0.1
        elif nivel == 2:
            S0 = random.randint(900, 990)
            I0 = 1000 - S0
            R0 = 0
            beta = round(random.uniform(0.2, 0.5), 2)
            gamma = round(random.uniform(0.05, 0.2), 2)
        else:
            S0 = random.randint(800, 990)
            I0 = random.randint(5, 50)
            R0 = 1000 - S0 - I0
            beta = round(random.uniform(0.15, 0.7), 2)
            gamma = round(random.uniform(0.05, 0.3), 2)
        
        R0_basico = beta / gamma
        N = S0 + I0 + R0
        # Umbral de inmunidad de rebaño
        herd_immunity = 1 - 1/R0_basico if R0_basico > 1 else 0
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿Qué representa S(t) en el modelo SIR?',
                'tipo': 'opcion_multiple',
                'opciones': ['Personas sanas', 'Personas susceptibles a infectarse', 'Personas sintomáticas', 'Personas seguras'],
                'respuesta_correcta': 1
            },
            {
                'id': 2,
                'texto': '¿Qué población nunca disminuye en el modelo SIR?',
                'tipo': 'opcion_multiple',
                'opciones': ['Susceptibles (S)', 'Infectados (I)', 'Recuperados (R)', 'Ninguna'],
                'respuesta_correcta': 2
            },
            {
                'id': 3,
                'texto': f'Con β = {beta} y γ = {gamma}, ¿cuál es R₀ = β/γ?',
                'tipo': 'numerica',
                'respuesta_esperada': R0_basico,
                'tolerancia': 0.3,
                'unidad': ''
            },
            {
                'id': 4,
                'texto': '¿Qué significa R₀ > 1?',
                'tipo': 'opcion_multiple',
                'opciones': ['No habrá epidemia', 'Habrá un brote epidémico', 'La enfermedad desaparecerá', 'Todos se recuperarán'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': '¿El modelo SIR considera nacimientos y muertes?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No, la población es constante', 'Solo nacimientos', 'Solo muertes'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'¿Cuál es el valor de R₀ (número reproductivo básico)?',
                'tipo': 'numerica',
                'respuesta_esperada': R0_basico,
                'tolerancia': 0.2,
                'unidad': ''
            },
            {
                'id': 2,
                'texto': f'Con R₀ = {R0_basico:.2f}, ¿habrá epidemia?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, porque R₀ > 1', 'No, porque R₀ < 1', 'Solo si I₀ es grande'],
                'respuesta_correcta': 0 if R0_basico > 1 else 1
            },
            {
                'id': 3,
                'texto': '¿Cuándo alcanza I(t) su máximo?',
                'tipo': 'opcion_multiple',
                'opciones': ['Cuando S = γ/β', 'Cuando S = 0', 'Cuando R = N', 'Al inicio'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': '¿Por qué la curva de susceptibles nunca llega a cero?',
                'tipo': 'opcion_multiple',
                'opciones': ['Error numérico', 'La epidemia termina antes de infectar a todos', 'El modelo está mal', 'Siempre nacen nuevos susceptibles'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': f'¿Qué fracción de la población debe vacunarse para inmunidad de rebaño?',
                'tipo': 'numerica',
                'respuesta_esperada': herd_immunity,
                'tolerancia': 0.1,
                'unidad': ''
            },
            {
                'id': 6,
                'texto': '¿Cómo se puede reducir R₀ en la práctica?',
                'tipo': 'opcion_multiple',
                'opciones': ['Aumentar β', 'Reducir β (distanciamiento) o aumentar γ (tratamiento)', 'Aumentar S₀', 'No se puede modificar'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'¿Cuál es el valor de R₀?',
                'tipo': 'numerica',
                'respuesta_esperada': R0_basico,
                'tolerancia': 0.15,
                'unidad': ''
            },
            {
                'id': 2,
                'texto': f'¿Cuál es el umbral de inmunidad de rebaño p_c = 1 - 1/R₀?',
                'tipo': 'numerica',
                'respuesta_esperada': herd_immunity,
                'tolerancia': 0.08,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': 'La ecuación dI/dt = βSI - γI implica que I crece cuando:',
                'tipo': 'opcion_multiple',
                'opciones': ['S > γ/β', 'S < γ/β', 'I > S', 'R < S'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': '¿El modelo SIR puede exhibir oscilaciones periódicas (endémicas)?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, siempre', 'No, converge a un equilibrio', 'Solo con dinámica vital', 'Solo en 3D'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': 'El tamaño final de la epidemia R(∞) satisface una ecuación trascendental. Para R₀ = 2:',
                'tipo': 'opcion_multiple',
                'opciones': ['~20% se infectará', '~80% se infectará eventualmente', '100% se infectará', '50% se infectará'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': '¿El sistema SIR tiene puntos de equilibrio endémicos (I > 0)?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No, solo existe el equilibrio libre de enfermedad', 'Solo si γ = 0', 'Solo si β = 0'],
                'respuesta_correcta': 1
            },
            {
                'id': 7,
                'texto': 'Si duplicamos β manteniendo γ constante, el pico de infectados:',
                'tipo': 'opcion_multiple',
                'opciones': ['Se duplica', 'Más que se duplica', 'Menos que se duplica', 'No cambia'],
                'respuesta_correcta': 1
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='sir',
            titulo='Modelo Epidemiológico SIR',
            dificultad=dificultad,
            parametros={'S0': S0, 'I0': I0, 'R0': R0, 'beta': beta, 'gamma': gamma},
            objetivos=[
                'Comprender la dinámica de epidemias',
                'Calcular el número reproductivo básico R₀',
                'Predecir el pico de infectados',
                'Analizar el umbral de inmunidad de rebaño'
            ],
            instrucciones=[
                f'1. Configure S(0) = {S0}, I(0) = {I0}, R(0) = {R0}',
                f'2. Configure β = {beta}, γ = {gamma}',
                f'3. Calcule R₀ = β/γ = {R0_basico:.2f}',
                '4. Ejecute la simulación',
                '5. Observe la evolución de las poblaciones',
                '6. Identifique el pico de infectados'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar las tres poblaciones S(t), I(t), R(t)',
                'Calcular R₀ = β/γ',
                'Determinar el día del pico de infectados',
                'Calcular la fracción final de afectados'
            ]
        )
    
    def _generar_hopf(self, dificultad):
        """Genera ejercicio de bifurcación de Hopf con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            mu = random.choice([-0.5, 0.0, 0.5, 1.0])
        elif nivel == 2:
            mu = round(random.uniform(-1.0, 2.0), 1)
        else:
            mu = round(random.uniform(-2.0, 3.0), 2)
        
        # Radio del ciclo límite para mu > 0
        radio_ciclo = np.sqrt(mu) if mu > 0 else 0
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': f'Con μ = {mu}, ¿qué comportamiento exhibe el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Punto fijo estable (espiral)', 'Ciclo límite estable', 'Comportamiento caótico', 'Divergencia'],
                'respuesta_correcta': 0 if mu < 0 else 1
            },
            {
                'id': 2,
                'texto': '¿Qué es una bifurcación de Hopf?',
                'tipo': 'opcion_multiple',
                'opciones': ['Nacimiento de un punto fijo', 'Nacimiento de un ciclo límite desde un punto fijo', 'Duplicación de período', 'Transición al caos'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': '¿En qué valor de μ ocurre la bifurcación de Hopf en este sistema?',
                'tipo': 'numerica',
                'respuesta_esperada': 0.0,
                'tolerancia': 0.1,
                'unidad': ''
            },
            {
                'id': 4,
                'texto': '¿El sistema tiene dimensión 2 o 3?',
                'tipo': 'opcion_multiple',
                'opciones': ['1', '2', '3', '4'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'Con μ = {mu}, ¿las trayectorias convergen al origen o a un ciclo límite?',
                'tipo': 'opcion_multiple',
                'opciones': ['Convergen al origen (μ < 0)', 'Ciclo límite (μ > 0)', 'Punto crítico (μ ≈ 0)'],
                'respuesta_correcta': 0 if mu < -0.05 else (1 if mu > 0.05 else 2)
            },
            {
                'id': 2,
                'texto': '¿En qué valor de μ ocurre la bifurcación de Hopf?',
                'tipo': 'numerica',
                'respuesta_esperada': 0.0,
                'tolerancia': 0.1,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': '¿Cómo crece el radio del ciclo límite con μ (para μ > 0)?',
                'tipo': 'opcion_multiple',
                'opciones': ['Proporcional a μ', 'Proporcional a √μ', 'Proporcional a μ²', 'Constante'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': 'Para μ > 0, ¿el ciclo límite es estable o inestable?',
                'tipo': 'opcion_multiple',
                'opciones': ['Estable (atractor)', 'Inestable (repulsor)'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': 'Esta bifurcación se llama supercrítica porque:',
                'tipo': 'opcion_multiple',
                'opciones': ['El ciclo nace de forma estable para μ > 0', 'El ciclo es muy grande', 'Ocurre a alta frecuencia', 'El sistema diverge'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'Con μ = {mu}, ¿cuál es el radio aproximado del ciclo límite?',
                'tipo': 'numerica',
                'respuesta_esperada': radio_ciclo,
                'tolerancia': max(radio_ciclo * 0.15, 0.1),
                'unidad': ''
            },
            {
                'id': 2,
                'texto': '¿Los valores propios del sistema linealizado en el origen son?',
                'tipo': 'opcion_multiple',
                'opciones': [f'λ = μ ± iω (complejos con parte real μ)', 'λ = ±μ (reales)', 'λ = μ (degenerado)', 'λ = 0'],
                'respuesta_correcta': 0
            },
            {
                'id': 3,
                'texto': 'En la bifurcación de Hopf subcrítica, ¿qué ocurre?',
                'tipo': 'opcion_multiple',
                'opciones': ['El ciclo límite es estable', 'El ciclo límite es inestable y existe para μ < 0', 'No hay ciclo límite', 'El sistema diverge'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿La forma normal de la bifurcación de Hopf en coordenadas polares es?',
                'tipo': 'opcion_multiple',
                'opciones': ['dr/dt = μr - r³, dθ/dt = ω', 'dr/dt = r², dθ/dt = 1', 'dr/dt = μr, dθ/dt = r', 'dr/dt = -r, dθ/dt = μ'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': '¿El teorema del centro manifiesto es relevante para bifurcaciones de Hopf porque?',
                'tipo': 'opcion_multiple',
                'opciones': ['Reduce la dimensionalidad del análisis', 'Calcula valores propios', 'Determina el período', 'Elimina no linealidades'],
                'respuesta_correcta': 0
            },
            {
                'id': 6,
                'texto': f'Para μ = {mu}, ¿el punto fijo (0,0) es estable o inestable?',
                'tipo': 'opcion_multiple',
                'opciones': ['Estable (μ < 0)', 'Inestable (μ > 0)', 'Marginalmente estable (μ = 0)'],
                'respuesta_correcta': 0 if mu < -0.05 else (1 if mu > 0.05 else 2)
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='hopf',
            titulo='Bifurcación de Hopf',
            dificultad=dificultad,
            parametros={'mu': mu, 'x0': 0.1, 'y0': 0.1, 'omega': 1.0},
            objetivos=[
                'Comprender la bifurcación de Hopf',
                'Identificar el valor crítico del parámetro',
                'Observar la transición de punto fijo a ciclo límite',
                'Analizar cómo crece el radio del ciclo'
            ],
            instrucciones=[
                f'1. Configure μ = {mu}',
                f'2. Radio esperado del ciclo (si μ > 0): √μ = {radio_ciclo:.3f}',
                '3. Observe el comportamiento del sistema',
                '4. Experimente con valores de μ negativos y positivos',
                '5. Identifique el punto de bifurcación en μ = 0'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar el diagrama de fase (x vs y)',
                'Variar μ y observar la transición',
                'Medir el radio del ciclo límite vs μ',
                'Verificar que radio ∝ √μ'
            ]
        )
    
    def _generar_logistico(self, dificultad):
        """Genera ejercicio del modelo logístico con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            N0 = random.choice([10, 20, 50])
            K = 1000
            r = random.choice([0.1, 0.2, 0.3])
        elif nivel == 2:
            N0 = random.randint(10, 100)
            K = random.randint(500, 1500)
            r = round(random.uniform(0.1, 0.5), 2)
        else:
            N0 = random.randint(5, 200)
            K = random.randint(300, 2000)
            r = round(random.uniform(0.05, 0.8), 3)
        
        # Cálculos auxiliares
        t_inflexion = np.log((K - N0) / N0) / r if N0 < K else 0
        t_duplicacion = np.log(2) / r
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿Hacia qué valor tiende la población a largo plazo?',
                'tipo': 'numerica',
                'respuesta_esperada': K,
                'tolerancia': K * 0.05,
                'unidad': 'individuos'
            },
            {
                'id': 2,
                'texto': '¿Qué representa K en el modelo logístico?',
                'tipo': 'opcion_multiple',
                'opciones': ['Tasa de crecimiento', 'Capacidad de carga del ambiente', 'Población inicial', 'Tiempo de duplicación'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': '¿Por qué el crecimiento no es infinito como en el modelo exponencial?',
                'tipo': 'opcion_multiple',
                'opciones': ['Por errores numéricos', 'Por la limitación de recursos (K)', 'Por la muerte de individuos', 'El modelo está mal'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿La curva logística tiene forma de S (sigmoide)?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No, es exponencial', 'No, es lineal', 'Depende de r'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': '¿Hacia qué valor tiende la población a largo plazo?',
                'tipo': 'numerica',
                'respuesta_esperada': K,
                'tolerancia': K * 0.03,
                'unidad': 'individuos'
            },
            {
                'id': 2,
                'texto': '¿En qué valor de N la tasa de crecimiento dN/dt es máxima?',
                'tipo': 'numerica',
                'respuesta_esperada': K / 2,
                'tolerancia': K * 0.1,
                'unidad': 'individuos'
            },
            {
                'id': 3,
                'texto': 'Si r se duplica, ¿la población alcanza K más rápido o más lento?',
                'tipo': 'opcion_multiple',
                'opciones': ['Más rápido', 'Más lento', 'Igual velocidad', 'Nunca alcanza K'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': '¿Cuántos puntos de equilibrio tiene el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Uno (N = 0)', 'Uno (N = K)', 'Dos (N = 0 y N = K)', 'Infinitos'],
                'respuesta_correcta': 2
            },
            {
                'id': 5,
                'texto': '¿El equilibrio N = 0 es estable o inestable?',
                'tipo': 'opcion_multiple',
                'opciones': ['Estable', 'Inestable', 'Marginalmente estable', 'Depende de r'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': f'¿Cuál es el tiempo de duplicación inicial aproximado (para N << K)?',
                'tipo': 'numerica',
                'respuesta_esperada': t_duplicacion,
                'tolerancia': t_duplicacion * 0.15,
                'unidad': 'unidades de tiempo'
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'¿En qué tiempo aproximado ocurre el punto de inflexión?',
                'tipo': 'numerica',
                'respuesta_esperada': t_inflexion,
                'tolerancia': max(t_inflexion * 0.2, 1),
                'unidad': 'unidades de tiempo'
            },
            {
                'id': 2,
                'texto': '¿La ecuación logística dN/dt = rN(1-N/K) es lineal o no lineal?',
                'tipo': 'opcion_multiple',
                'opciones': ['Lineal', 'No lineal (término N²)'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': 'La solución analítica N(t) = K/(1 + ((K-N₀)/N₀)e^(-rt)) es una función:',
                'tipo': 'opcion_multiple',
                'opciones': ['Exponencial', 'Logística (sigmoide)', 'Hiperbólica', 'Trigonométrica'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': 'Si N₀ > K (sobrepoblación inicial), ¿qué sucede?',
                'tipo': 'opcion_multiple',
                'opciones': ['N crece más', 'N decrece hacia K', 'N oscila', 'El modelo falla'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': '¿Cuál es el valor propio del sistema linealizado cerca de N = K?',
                'tipo': 'opcion_multiple',
                'opciones': ['λ = r (inestable)', 'λ = -r (estable)', 'λ = 0 (neutral)', 'λ = rK'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': 'El modelo logístico es caso particular del modelo de Verhulst-Pearl. ¿Qué asume?',
                'tipo': 'opcion_multiple',
                'opciones': ['Recursos infinitos', 'Competencia intraespecífica proporcional a N²', 'No hay nacimientos', 'Tasa de muerte constante'],
                'respuesta_correcta': 1
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='logistico',
            titulo='Modelo Logístico de Crecimiento',
            dificultad=dificultad,
            parametros={'N0': N0, 'r': r, 'K': K},
            objetivos=[
                'Comprender el crecimiento logístico',
                'Identificar la capacidad de carga',
                'Analizar el efecto de la tasa de crecimiento',
                'Localizar el punto de inflexión'
            ],
            instrucciones=[
                f'1. Configure N(0) = {N0}',
                f'2. Configure r = {r}, K = {K}',
                f'3. Punto de inflexión esperado en N = K/2 = {K/2}',
                '4. Ejecute la simulación',
                '5. Observe cómo la población se estabiliza'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar N(t) vs t',
                'Identificar la capacidad de carga K',
                'Calcular el punto de inflexión',
                'Comparar con crecimiento exponencial'
            ]
        )
    
    def _generar_verhulst(self, dificultad):
        """Genera ejercicio del mapa de Verhulst con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            r = random.choice([2.5, 2.8, 3.2, 3.5])
        elif nivel == 2:
            r = round(random.uniform(2.0, 3.8), 1)
        else:
            r = round(random.uniform(1.5, 4.0), 2)
        
        # Determinar comportamiento según r
        if r < 3.0:
            comportamiento = "punto_fijo"
        elif r < 3.449:
            comportamiento = "periodo_2"
        elif r < 3.544:
            comportamiento = "periodo_4"
        elif r < 3.5699:
            comportamiento = "periodo_alto"
        else:
            comportamiento = "caotico"
        
        # Punto fijo estable (si existe)
        x_eq = 1 - 1/r if r > 1 else 0
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': 'El mapa de Verhulst xₙ₊₁ = r·xₙ(1-xₙ) es un sistema:',
                'tipo': 'opcion_multiple',
                'opciones': ['Continuo', 'Discreto (iterativo)', 'Híbrido', 'Estocástico'],
                'respuesta_correcta': 1
            },
            {
                'id': 2,
                'texto': f'¿Para r = {r}, el sistema converge a un único punto fijo?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, si r < 3', 'No, siempre oscila', 'Depende de x₀'],
                'respuesta_correcta': 0 if r < 3.0 else 1
            },
            {
                'id': 3,
                'texto': '¿Qué sucede cuando r > 4 en el mapa logístico?',
                'tipo': 'opcion_multiple',
                'opciones': ['Converge más rápido', 'Las iteraciones escapan de [0,1]', 'Se vuelve periódico', 'No hay cambio'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿El valor inicial x₀ debe estar en qué rango?',
                'tipo': 'opcion_multiple',
                'opciones': ['[-1, 1]', '[0, 1]', '[0, ∞)', 'Cualquier valor'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'Con r = {r}, ¿qué tipo de comportamiento asintótico exhibe el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Punto fijo (r < 3)', 'Órbita periódica (3 < r < 3.57)', 'Comportamiento caótico (r > 3.57)'],
                'respuesta_correcta': 0 if r < 3.0 else (1 if r < 3.57 else 2)
            },
            {
                'id': 2,
                'texto': '¿A partir de qué valor aproximado de r comienza el comportamiento caótico?',
                'tipo': 'numerica',
                'respuesta_esperada': 3.57,
                'tolerancia': 0.1,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': '¿Qué es la constante de Feigenbaum δ ≈ 4.669?',
                'tipo': 'opcion_multiple',
                'opciones': ['Tasa de duplicación de período', 'Límite de r', 'Exponente de Lyapunov', 'Dimensión fractal'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': f'El punto fijo no trivial x* = 1 - 1/r = {x_eq:.3f} es estable cuando:',
                'tipo': 'opcion_multiple',
                'opciones': ['1 < r < 3', 'r > 3', 'r < 1', 'Siempre'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': '¿Qué son las "ventanas periódicas" en el diagrama de bifurcación?',
                'tipo': 'opcion_multiple',
                'opciones': ['Regiones de comportamiento periódico dentro del caos', 'Puntos fijos inestables', 'Errores numéricos', 'Bifurcaciones inversas'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'Con r = {r}, clasifique el comportamiento del sistema:',
                'tipo': 'opcion_multiple',
                'opciones': ['Punto fijo estable', 'Ciclo de período 2', 'Ciclo de período 4+', 'Caos'],
                'respuesta_correcta': 0 if r < 3.0 else (1 if r < 3.449 else (2 if r < 3.57 else 3))
            },
            {
                'id': 2,
                'texto': '¿Cuál es el valor de r donde ocurre la primera bifurcación (período 1 → 2)?',
                'tipo': 'numerica',
                'respuesta_esperada': 3.0,
                'tolerancia': 0.05,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': 'La distancia entre bifurcaciones sucesivas δₙ = (rₙ - rₙ₋₁)/(rₙ₊₁ - rₙ) converge a:',
                'tipo': 'numerica',
                'respuesta_esperada': 4.669,
                'tolerancia': 0.1,
                'unidad': ''
            },
            {
                'id': 4,
                'texto': '¿El exponente de Lyapunov λ indica caos cuando?',
                'tipo': 'opcion_multiple',
                'opciones': ['λ > 0', 'λ < 0', 'λ = 0', 'λ → ∞'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': 'La secuencia de duplicación de período 2ⁿ se llama:',
                'tipo': 'opcion_multiple',
                'opciones': ['Cascada de Hopf', 'Ruta de duplicación de período (Feigenbaum)', 'Intermitencia', 'Cuasiperiodicidad'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': '¿Qué indica la "isla de período 3" cerca de r ≈ 3.83?',
                'tipo': 'opcion_multiple',
                'opciones': ['El teorema de Li-Yorke: período 3 implica caos', 'Error numérico', 'Fin del caos', 'Nueva ruta al caos'],
                'respuesta_correcta': 0
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='verhulst',
            titulo='Mapa Logístico de Verhulst',
            dificultad=dificultad,
            parametros={'x0': 0.5, 'r': r},
            objetivos=[
                'Observar bifurcaciones en sistemas discretos',
                'Comprender el camino al caos',
                'Analizar el diagrama de bifurcación',
                'Identificar la constante de Feigenbaum'
            ],
            instrucciones=[
                f'1. Configure r = {r}',
                f'2. Punto fijo teórico: x* = 1 - 1/r = {x_eq:.4f}',
                '3. Ejecute la simulación (iteraciones)',
                '4. Observe el comportamiento a largo plazo',
                '5. Referencia: caos comienza en r ≈ 3.5699'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar la serie temporal xₙ vs n',
                'Construir el diagrama de bifurcación',
                'Identificar las regiones periódicas y caóticas',
                'Localizar ventanas periódicas en el caos'
            ]
        )
    
    def _generar_orbital(self, dificultad):
        """Genera ejercicio de órbitas espaciales con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            # Órbita circular
            x0, y0 = 1.0, 0.0
            vx0, vy0 = 0.0, 1.0
            tipo_orbita = "circular"
        elif nivel == 2:
            # Órbita elíptica
            x0 = 1.0
            y0 = 0.0
            vx0 = 0.0
            vy0 = round(random.uniform(0.7, 1.3), 2)
            tipo_orbita = "circular" if abs(vy0 - 1.0) < 0.1 else "elíptica"
        else:
            # Órbita variada
            x0 = round(random.uniform(0.5, 2.0), 2)
            y0 = 0.0
            vx0 = 0.0
            vy0 = round(random.uniform(0.5, 1.5), 2)
            v_circ = 1.0 / np.sqrt(x0)
            if abs(vy0 - v_circ) < 0.1:
                tipo_orbita = "circular"
            elif vy0 < np.sqrt(2) * v_circ:
                tipo_orbita = "elíptica"
            else:
                tipo_orbita = "hiperbólica"
        
        # Calcular energía y momento angular
        r0 = np.sqrt(x0**2 + y0**2)
        v0_mag = np.sqrt(vx0**2 + vy0**2)
        E = 0.5 * v0_mag**2 - 1.0/r0  # Energía específica (GM=1)
        L = x0 * vy0 - y0 * vx0  # Momento angular específico
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿Qué tipo de órbita se forma con estos parámetros?',
                'tipo': 'opcion_multiple',
                'opciones': ['Circular', 'Elíptica', 'Hiperbólica', 'Parabólica'],
                'respuesta_correcta': 0 if tipo_orbita == "circular" else (1 if tipo_orbita == "elíptica" else 2)
            },
            {
                'id': 2,
                'texto': '¿La energía total del sistema se conserva?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No'],
                'respuesta_correcta': 0
            },
            {
                'id': 3,
                'texto': '¿Qué fuerza actúa sobre el cuerpo orbital?',
                'tipo': 'opcion_multiple',
                'opciones': ['Gravitacional', 'Electromagnética', 'Nuclear', 'Fricción'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': '¿La velocidad del satélite es constante en una órbita circular?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No, varía según la posición'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'Con r₀ = {x0} y v₀ = {vy0}, ¿qué tipo de órbita se forma?',
                'tipo': 'opcion_multiple',
                'opciones': ['Circular (v = √(GM/r))', 'Elíptica', 'Hiperbólica/Parabólica'],
                'respuesta_correcta': 0 if tipo_orbita == "circular" else (1 if tipo_orbita == "elíptica" else 2)
            },
            {
                'id': 2,
                'texto': '¿El momento angular se conserva en el problema de Kepler?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, siempre (fuerza central)', 'No', 'Solo en órbitas circulares'],
                'respuesta_correcta': 0
            },
            {
                'id': 3,
                'texto': f'¿La energía total E = v²/2 - GM/r es positiva, negativa o cero?',
                'tipo': 'opcion_multiple',
                'opciones': ['Negativa (órbita ligada)', 'Cero (parabólica)', 'Positiva (hiperbólica)'],
                'respuesta_correcta': 0 if E < -0.01 else (1 if abs(E) < 0.01 else 2)
            },
            {
                'id': 4,
                'texto': '¿Qué relación cumple el período T con el semieje mayor a?',
                'tipo': 'opcion_multiple',
                'opciones': ['T ∝ a', 'T² ∝ a³ (3ª Ley de Kepler)', 'T³ ∝ a²', 'T ∝ √a'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': '¿En una órbita elíptica, dónde es máxima la velocidad?',
                'tipo': 'opcion_multiple',
                'opciones': ['En el perihelio (punto más cercano)', 'En el afelio (punto más lejano)', 'Es constante', 'En los puntos intermedios'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'¿Cuál es la energía específica E = v²/2 - 1/r del sistema?',
                'tipo': 'numerica',
                'respuesta_esperada': E,
                'tolerancia': abs(E) * 0.15 + 0.05,
                'unidad': ''
            },
            {
                'id': 2,
                'texto': f'¿Cuál es el momento angular específico L = r × v?',
                'tipo': 'numerica',
                'respuesta_esperada': L,
                'tolerancia': L * 0.1,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': '¿Cómo se relaciona la excentricidad e con E y L?',
                'tipo': 'opcion_multiple',
                'opciones': ['e = √(1 + 2EL²)', 'e = E/L', 'e = L²/E', 'e = 1/(EL)'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': '¿Cuántas integrales de movimiento tiene el problema de Kepler?',
                'tipo': 'opcion_multiple',
                'opciones': ['3 (E, L)', '5 (E, L⃗, vector de Laplace-Runge-Lenz)', '7', '1'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': 'Para cambiar de una órbita circular a otra circular más alta, la maniobra más eficiente es:',
                'tipo': 'opcion_multiple',
                'opciones': ['Empuje continuo', 'Transferencia de Hohmann (2 impulsos)', 'Transferencia bi-elíptica', 'Asistencia gravitatoria'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': '¿Qué sucede si la velocidad de escape v_esc = √(2GM/r) se alcanza?',
                'tipo': 'opcion_multiple',
                'opciones': ['Órbita circular', 'Órbita elíptica cerrada', 'Trayectoria parabólica (E = 0)', 'El satélite cae'],
                'respuesta_correcta': 2
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='orbital',
            titulo='Órbitas Espaciales (Problema de Kepler)',
            dificultad=dificultad,
            parametros={'x0': x0, 'y0': y0, 'vx0': vx0, 'vy0': vy0, 'GM': 1.0},
            objetivos=[
                'Comprender las leyes de Kepler',
                'Analizar órbitas circulares y elípticas',
                'Verificar la conservación de energía y momento angular',
                'Clasificar órbitas según su energía'
            ],
            instrucciones=[
                f'1. Configure posición inicial: ({x0}, {y0})',
                f'2. Configure velocidad inicial: ({vx0}, {vy0})',
                f'3. Velocidad circular en r = {x0}: v_circ = 1/√r = {1/np.sqrt(x0):.3f}',
                f'4. Energía calculada: E = {E:.4f}',
                '5. Ejecute la simulación',
                '6. Observe la trayectoria orbital'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar la trayectoria orbital',
                'Calcular la energía total y momento angular',
                'Verificar las leyes de Kepler',
                'Determinar el tipo de órbita'
            ]
        )
    
    def _generar_mariposa(self, dificultad):
        """Genera ejercicio del atractor de Rössler (mariposa)."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            a, b, c = 0.2, 0.2, 5.7
        elif nivel == 2:
            a, b = 0.2, 0.2
            c = round(random.uniform(4.0, 6.5), 1)
        else:
            a = round(random.uniform(0.1, 0.3), 2)
            b = round(random.uniform(0.1, 0.4), 2)
            c = round(random.uniform(3.0, 8.0), 1)
        
        ejercicio = {
            'sistema': 'mariposa',
            'titulo': 'Atractor de Rössler (Mariposa)',
            'dificultad': dificultad,
            'parametros': {
                'x0': 1.0,
                'y0': 1.0,
                'z0': 1.0,
                'a': a,
                'b': b,
                'c': c
            },
            'objetivos': [
                'Observar un atractor caótico',
                'Comparar con el atractor de Lorenz',
                'Analizar la estructura del atractor'
            ],
            'instrucciones': [
                f'1. Configure a = {a}, b = {b}, c = {c}',
                '2. Ejecute la simulación',
                '3. Observe el atractor en 3D',
                '4. Identifique la forma de mariposa'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿El sistema de Rössler es caótico?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No', 'Depende de los parámetros'],
                    'respuesta_correcta': 2
                },
                {
                    'id': 2,
                    'texto': '¿Cuántas dimensiones tiene el sistema?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 3,
                    'tolerancia': 0,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': 'El atractor de Rössler es:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Un punto fijo', 'Un ciclo límite', 'Un atractor extraño'],
                    'respuesta_correcta': 2
                }
            ],
            'analisis_requerido': [
                'Visualizar el atractor en 3D',
                'Comparar con Lorenz',
                'Analizar la sensibilidad a condiciones iniciales'
            ]
        }
        
        return ejercicio
    
    def _generar_amortiguador(self, dificultad):
        """Genera ejercicio de sistema masa-resorte-amortiguador con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            m, k = 1.0, 1.0
            c = random.choice([0.2, 1.0, 2.0])  # Sub, crítico, sobre
        elif nivel == 2:
            m, k = 1.0, 4.0
            c = round(random.uniform(0.5, 6.0), 1)
        else:
            m = round(random.uniform(0.5, 2.0), 1)
            k = round(random.uniform(1.0, 10.0), 1)
            c = round(random.uniform(0.1, 8.0), 2)
        
        # Calcular parámetros del sistema
        c_crit = 2 * np.sqrt(k * m)
        zeta = c / c_crit
        omega_n = np.sqrt(k / m)
        omega_d = omega_n * np.sqrt(1 - zeta**2) if zeta < 1 else 0
        T_d = 2 * np.pi / omega_d if omega_d > 0 else float('inf')
        
        if zeta < 1:
            tipo = "Subamortiguado"
            tipo_idx = 0
        elif abs(zeta - 1) < 0.1:
            tipo = "Críticamente amortiguado"
            tipo_idx = 1
        else:
            tipo = "Sobreamortiguado"
            tipo_idx = 2
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿Qué tipo de amortiguamiento presenta el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado (oscila)', 'Críticamente amortiguado', 'Sobreamortiguado (no oscila)'],
                'respuesta_correcta': tipo_idx
            },
            {
                'id': 2,
                'texto': '¿El sistema masa-resorte-amortiguador es lineal o no lineal?',
                'tipo': 'opcion_multiple',
                'opciones': ['Lineal', 'No lineal', 'Depende de los parámetros'],
                'respuesta_correcta': 0
            },
            {
                'id': 3,
                'texto': '¿Qué hace el amortiguador c en el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Almacena energía', 'Disipa energía (fricción)', 'Genera oscilaciones', 'Aumenta la frecuencia'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿El sistema oscila cuando ζ < 1?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': '¿Qué tipo de amortiguamiento presenta el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado (ζ < 1)', 'Críticamente amortiguado (ζ = 1)', 'Sobreamortiguado (ζ > 1)'],
                'respuesta_correcta': tipo_idx
            },
            {
                'id': 2,
                'texto': f'¿Cuál es el factor de amortiguamiento ζ = c/(2√(km))?',
                'tipo': 'numerica',
                'respuesta_esperada': zeta,
                'tolerancia': 0.1,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': f'¿Cuál es la frecuencia natural ωₙ = √(k/m)?',
                'tipo': 'numerica',
                'respuesta_esperada': omega_n,
                'tolerancia': omega_n * 0.1,
                'unidad': 'rad/s'
            },
            {
                'id': 4,
                'texto': '¿Cuál régimen retorna al equilibrio más rápido sin oscilar?',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': '¿El sistema oscila con amplitud decreciente?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, si ζ < 1', 'No, nunca oscila', 'Solo si ζ > 1'],
                'respuesta_correcta': 0 if zeta < 1 else 1
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'¿Cuál es el factor de amortiguamiento ζ?',
                'tipo': 'numerica',
                'respuesta_esperada': zeta,
                'tolerancia': 0.08,
                'unidad': ''
            },
            {
                'id': 2,
                'texto': f'¿Cuál es la frecuencia de oscilación amortiguada ωd = ωₙ√(1-ζ²)?',
                'tipo': 'numerica',
                'respuesta_esperada': omega_d if omega_d > 0 else omega_n,
                'tolerancia': max(omega_d * 0.1, 0.1) if omega_d > 0 else omega_n * 0.1,
                'unidad': 'rad/s'
            },
            {
                'id': 3,
                'texto': '¿Cuáles son los valores propios del sistema para ζ < 1?',
                'tipo': 'opcion_multiple',
                'opciones': ['Reales y negativos', 'Complejos conjugados con parte real negativa', 'Imaginarios puros', 'Reales y positivos'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': 'El decremento logarítmico δ = ln(xₙ/xₙ₊₁) está relacionado con ζ por:',
                'tipo': 'opcion_multiple',
                'opciones': ['δ = 2πζ/√(1-ζ²)', 'δ = ζ', 'δ = 1/ζ', 'δ = πζ'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': f'El amortiguamiento crítico c_crit = 2√(km) = {c_crit:.3f}. El actual c = {c} es:',
                'tipo': 'opcion_multiple',
                'opciones': ['Menor que c_crit (subamortiguado)', 'Igual a c_crit (crítico)', 'Mayor que c_crit (sobreamortiguado)'],
                'respuesta_correcta': tipo_idx
            },
            {
                'id': 6,
                'texto': '¿Por qué el amortiguamiento crítico es importante en ingeniería?',
                'tipo': 'opcion_multiple',
                'opciones': ['Máxima oscilación', 'Retorno más rápido sin sobrepaso', 'Mínima energía', 'Máxima frecuencia'],
                'respuesta_correcta': 1
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='amortiguador',
            titulo='Sistema Masa-Resorte-Amortiguador',
            dificultad=dificultad,
            parametros={'m': m, 'c': c, 'k': k, 'x0': 1.0, 'v0': 0.0, 'F0': 0.0, 'omega_f': 0.0},
            objetivos=[
                'Comprender los tipos de amortiguamiento',
                'Calcular el factor de amortiguamiento ζ',
                'Analizar la respuesta del sistema',
                'Identificar frecuencias naturales y amortiguadas'
            ],
            instrucciones=[
                f'1. Configure m = {m} kg, c = {c} Ns/m, k = {k} N/m',
                '2. Configure x(0) = 1.0 m, v(0) = 0.0 m/s',
                f'3. Amortiguamiento crítico: c_crit = 2√(km) = {c_crit:.3f}',
                f'4. Factor ζ = c/c_crit = {zeta:.3f} → {tipo}',
                '5. Ejecute la simulación',
                '6. Observe el comportamiento temporal'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar x(t) y v(t)',
                'Calcular ζ = c / (2√(km))',
                'Determinar el tipo de amortiguamiento',
                'Medir el decremento logarítmico si ζ < 1'
            ]
        )
    
    def _generar_rlc(self, dificultad):
        """Genera ejercicio de circuito RLC con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            R, L, C = 10.0, 0.1, 0.001
            V0 = 10.0
        elif nivel == 2:
            R = random.randint(5, 50)
            L = round(random.uniform(0.05, 0.5), 2)
            C = round(random.uniform(0.0005, 0.005), 4)
            V0 = random.randint(5, 20)
        else:
            R = random.randint(1, 100)
            L = round(random.uniform(0.01, 1.0), 2)
            C = round(random.uniform(0.0001, 0.01), 4)
            V0 = random.randint(1, 50)
        
        # Cálculos auxiliares
        omega_0 = 1 / np.sqrt(L * C)
        Q = omega_0 * L / R
        zeta = R / (2 * np.sqrt(L / C))
        omega_d = omega_0 * np.sqrt(1 - zeta**2) if zeta < 1 else 0
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿Qué componente almacena energía en un campo magnético?',
                'tipo': 'opcion_multiple',
                'opciones': ['Resistor (R)', 'Inductor (L)', 'Capacitor (C)', 'Ninguno'],
                'respuesta_correcta': 1
            },
            {
                'id': 2,
                'texto': '¿El resistor disipa o almacena energía?',
                'tipo': 'opcion_multiple',
                'opciones': ['Almacena', 'Disipa', 'Ambos', 'Ninguno'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': '¿La corriente y voltaje en un circuito RLC pueden oscilar?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, si el amortiguamiento es bajo', 'No, siempre son constantes', 'Solo el voltaje', 'Solo la corriente'],
                'respuesta_correcta': 0
            },
            {
                'id': 4,
                'texto': '¿Qué sucede cuando R = 0 (circuito LC ideal)?',
                'tipo': 'opcion_multiple',
                'opciones': ['No hay oscilación', 'Oscilación perpetua', 'Cortocircuito', 'El capacitor explota'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': '¿Cuál es la frecuencia de resonancia ω₀ = 1/√(LC)?',
                'tipo': 'numerica',
                'respuesta_esperada': omega_0,
                'tolerancia': omega_0 * 0.1,
                'unidad': 'rad/s'
            },
            {
                'id': 2,
                'texto': '¿El circuito está subamortiguado, críticamente amortiguado o sobreamortiguado?',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado (oscila)', 'Críticamente amortiguado', 'Sobreamortiguado (no oscila)'],
                'respuesta_correcta': 0 if zeta < 0.95 else (1 if zeta < 1.05 else 2)
            },
            {
                'id': 3,
                'texto': f'¿Cuál es el factor de calidad Q = ω₀L/R aproximado?',
                'tipo': 'numerica',
                'respuesta_esperada': Q,
                'tolerancia': Q * 0.15,
                'unidad': ''
            },
            {
                'id': 4,
                'texto': '¿Qué indica un factor Q alto?',
                'tipo': 'opcion_multiple',
                'opciones': ['Mucha disipación', 'Oscilaciones sostenidas (bajo amortiguamiento)', 'Frecuencia alta', 'Capacitancia grande'],
                'respuesta_correcta': 1
            },
            {
                'id': 5,
                'texto': 'El circuito RLC serie es análogo mecánico a:',
                'tipo': 'opcion_multiple',
                'opciones': ['Péndulo simple', 'Sistema masa-resorte-amortiguador', 'Resorte sin fricción', 'Péndulo doble'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': '¿Cuál es la frecuencia de resonancia ω₀?',
                'tipo': 'numerica',
                'respuesta_esperada': omega_0,
                'tolerancia': omega_0 * 0.08,
                'unidad': 'rad/s'
            },
            {
                'id': 2,
                'texto': f'El factor de amortiguamiento ζ = R/(2√(L/C)) = {zeta:.3f} indica:',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado (ζ < 1)', 'Crítico (ζ ≈ 1)', 'Sobreamortiguado (ζ > 1)'],
                'respuesta_correcta': 0 if zeta < 0.95 else (1 if zeta < 1.05 else 2)
            },
            {
                'id': 3,
                'texto': 'Si ζ < 1, ¿cuál es la frecuencia de oscilación amortiguada ωd = ω₀√(1-ζ²)?',
                'tipo': 'numerica',
                'respuesta_esperada': omega_d if omega_d > 0 else omega_0,
                'tolerancia': max(omega_d * 0.1, 1) if omega_d > 0 else omega_0 * 0.1,
                'unidad': 'rad/s'
            },
            {
                'id': 4,
                'texto': 'El ancho de banda del circuito RLC es BW = R/L. Si R aumenta:',
                'tipo': 'opcion_multiple',
                'opciones': ['BW aumenta, Q disminuye', 'BW disminuye, Q aumenta', 'Ambos aumentan', 'Ambos disminuyen'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': '¿Los valores propios del sistema son complejos conjugados cuando?',
                'tipo': 'opcion_multiple',
                'opciones': ['ζ < 1 (subamortiguado)', 'ζ > 1 (sobreamortiguado)', 'Siempre', 'Nunca'],
                'respuesta_correcta': 0
            },
            {
                'id': 6,
                'texto': 'En resonancia (ω = ω₀), la impedancia del circuito es:',
                'tipo': 'opcion_multiple',
                'opciones': ['Mínima e igual a R', 'Máxima', 'Cero', 'Infinita'],
                'respuesta_correcta': 0
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='rlc',
            titulo='Circuito RLC Serie',
            dificultad=dificultad,
            parametros={'R': R, 'L': L, 'C': C, 'V0': V0, 'I0': 0.0, 'Q0': 0.0},
            objetivos=[
                'Comprender circuitos RLC',
                'Analizar oscilaciones eléctricas',
                'Calcular la frecuencia de resonancia',
                'Determinar el tipo de amortiguamiento'
            ],
            instrucciones=[
                f'1. Configure R = {R}Ω, L = {L}H, C = {C}F',
                f'2. Configure V₀ = {V0}V',
                f'3. Frecuencia natural: ω₀ = 1/√(LC) = {omega_0:.2f} rad/s',
                f'4. Factor de amortiguamiento: ζ = {zeta:.3f}',
                '5. Ejecute la simulación',
                '6. Observe corriente y voltaje'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar I(t) y V_C(t)',
                'Calcular ω₀ = 1/√(LC)',
                'Determinar el factor de calidad Q',
                'Clasificar el tipo de amortiguamiento'
            ]
        )
    
    def _generar_lorenz(self, dificultad):
        """Genera ejercicio del sistema de Lorenz con preguntas variadas."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            sigma, rho, beta = 10.0, 28.0, 8/3
        elif nivel == 2:
            sigma = 10.0
            rho = round(random.uniform(20.0, 35.0), 1)
            beta = 8/3
        else:
            sigma = round(random.uniform(8.0, 15.0), 1)
            rho = round(random.uniform(15.0, 40.0), 1)
            beta = round(random.uniform(2.0, 3.5), 2)
        
        # Puntos críticos para rho > 1
        rho_critico = 24.74
        es_caotico = rho > rho_critico
        
        preguntas_principiante = [
            {
                'id': 1,
                'texto': '¿El sistema de Lorenz es determinista o estocástico?',
                'tipo': 'opcion_multiple',
                'opciones': ['Determinista (ecuaciones fijas)', 'Estocástico (aleatorio)', 'Híbrido', 'Depende de los parámetros'],
                'respuesta_correcta': 0
            },
            {
                'id': 2,
                'texto': '¿Cuántas dimensiones tiene el sistema de Lorenz?',
                'tipo': 'numerica',
                'respuesta_esperada': 3,
                'tolerancia': 0,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': '¿Qué forma tiene el atractor de Lorenz?',
                'tipo': 'opcion_multiple',
                'opciones': ['Esférica', 'Mariposa con dos lóbulos', 'Toroidal', 'Lineal'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': '¿El sistema de Lorenz fue desarrollado para modelar?',
                'tipo': 'opcion_multiple',
                'opciones': ['Circuitos eléctricos', 'Convección atmosférica', 'Poblaciones', 'Reacciones químicas'],
                'respuesta_correcta': 1
            }
        ]
        
        preguntas_intermedio = [
            {
                'id': 1,
                'texto': f'Para ρ = {rho}, ¿el sistema exhibe comportamiento caótico?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí (ρ > 24.74)', 'No (ρ < 24.74)', 'Solo si σ > 10'],
                'respuesta_correcta': 0 if es_caotico else 1
            },
            {
                'id': 2,
                'texto': '¿Qué significa "sensibilidad a condiciones iniciales"?',
                'tipo': 'opcion_multiple',
                'opciones': ['Pequeños cambios en CI no afectan', 'Pequeños cambios en CI causan grandes diferencias', 'El sistema es inestable', 'El sistema diverge'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': '¿A partir de qué valor aproximado de ρ aparece el caos?',
                'tipo': 'numerica',
                'respuesta_esperada': 24.74,
                'tolerancia': 1.0,
                'unidad': ''
            },
            {
                'id': 4,
                'texto': '¿Cuántos puntos de equilibrio no triviales tiene el sistema para ρ > 1?',
                'tipo': 'numerica',
                'respuesta_esperada': 2,
                'tolerancia': 0,
                'unidad': ''
            },
            {
                'id': 5,
                'texto': '¿El atractor de Lorenz es un atractor extraño?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí, tiene dimensión fractal', 'No, es un ciclo límite', 'No, es un punto fijo', 'Depende de σ'],
                'respuesta_correcta': 0
            }
        ]
        
        preguntas_avanzado = [
            {
                'id': 1,
                'texto': f'Con σ = {sigma}, ρ = {rho}, β = {beta:.2f}, clasifique el comportamiento:',
                'tipo': 'opcion_multiple',
                'opciones': ['Punto fijo estable', 'Ciclo límite', 'Atractor caótico', 'Trayectorias divergentes'],
                'respuesta_correcta': 2 if es_caotico else 0
            },
            {
                'id': 2,
                'texto': 'El exponente de Lyapunov positivo indica:',
                'tipo': 'opcion_multiple',
                'opciones': ['Estabilidad', 'Divergencia exponencial de trayectorias cercanas', 'Convergencia', 'Periodicidad'],
                'respuesta_correcta': 1
            },
            {
                'id': 3,
                'texto': '¿Cuál es la dimensión fractal aproximada del atractor de Lorenz?',
                'tipo': 'opcion_multiple',
                'opciones': ['~1.0', '~2.06', '~3.0', '~4.5'],
                'respuesta_correcta': 1
            },
            {
                'id': 4,
                'texto': f'Para los parámetros dados, ¿los puntos fijos C+ y C- son estables?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí para ρ < 24.74', 'No, siempre son inestables', 'Solo C+ es estable', 'Depende de β'],
                'respuesta_correcta': 0
            },
            {
                'id': 5,
                'texto': 'El teorema de Takens permite reconstruir el atractor desde:',
                'tipo': 'opcion_multiple',
                'opciones': ['Las tres variables', 'Una sola serie temporal con retardos', 'Solo x(t)', 'La derivada'],
                'respuesta_correcta': 1
            },
            {
                'id': 6,
                'texto': '¿Por qué el sistema de Lorenz ilustra el "efecto mariposa"?',
                'tipo': 'opcion_multiple',
                'opciones': ['Por la forma del atractor', 'Por la sensibilidad extrema a CI', 'Por el aleteo de trayectorias', 'Todas las anteriores'],
                'respuesta_correcta': 3
            }
        ]
        
        # Usar helpers
        pools = {1: preguntas_principiante, 2: preguntas_intermedio, 3: preguntas_avanzado}
        preguntas = self._seleccionar_preguntas(pools, nivel)
        
        return self._construir_ejercicio(
            sistema='lorenz',
            titulo='Sistema de Lorenz (Atractor Caótico)',
            dificultad=dificultad,
            parametros={'x0': 1.0, 'y0': 1.0, 'z0': 1.0, 'sigma': sigma, 'rho': rho, 'beta': beta},
            objetivos=[
                'Observar comportamiento caótico determinista',
                'Comprender la teoría del caos',
                'Analizar el atractor extraño',
                'Verificar sensibilidad a condiciones iniciales'
            ],
            instrucciones=[
                f'1. Configure σ = {sigma}, ρ = {rho}, β = {beta:.2f}',
                f'2. Valor crítico de ρ para caos: ~24.74',
                '3. Ejecute la simulación',
                '4. Observe el atractor en 3D',
                '5. Pruebe con condiciones iniciales ligeramente diferentes'
            ],
            preguntas=preguntas,
            analisis=[
                'Visualizar el atractor en espacio 3D',
                'Comparar trayectorias con CI cercanas',
                'Identificar los dos lóbulos del atractor',
                'Observar el comportamiento aperiódico'
            ]
        )
    
    # ==================== EJERCICIOS EDUCATIVOS AVANZADOS ====================
    
    def _generar_equilibrio_logistico(self, dificultad):
        """Ejercicio 1: Estabilidad de Puntos de Equilibrio en el Sistema Logístico."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            r = random.choice([0.5, 1.0, 1.5])
            K = 500
            N0 = 50
        elif nivel == 2:
            r = round(random.uniform(0.3, 2.0), 2)
            K = random.randint(300, 1000)
            N0 = random.randint(20, 200)
        else:
            r = round(random.uniform(0.1, 2.5), 2)
            K = random.randint(100, 1500)
            N0 = random.randint(10, 500)
        
        return {
            'sistema': 'logistico',
            'titulo': 'Ejercicio 1: Estabilidad de Puntos de Equilibrio en el Sistema Logístico',
            'dificultad': dificultad,
            'parametros': {'N0': N0, 'r': r, 'K': K},
            'objetivos': [
                'Comprender cómo la tasa de crecimiento y la capacidad de carga afectan la evolución temporal',
                'Determinar condiciones de equilibrio',
                'Analizar el tiempo de convergencia'
            ],
            'instrucciones': [
                f'1. Configure población inicial N0 = {N0}, tasa r = {r}, capacidad K = {K}',
                '2. Simule la evolución temporal de la población',
                '3. Grafique N(t) versus tiempo',
                '4. Identifique visualmente los puntos de equilibrio estables'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Hacia qué valor converge la población independientemente de N0?',
                    'tipo': 'numerica',
                    'respuesta_esperada': K,
                    'tolerancia': K * 0.05,
                    'unidad': 'individuos'
                },
                {
                    'id': 2,
                    'texto': 'Si la población inicial N0 es mayor que K, ¿cómo evoluciona el sistema?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Decrece hacia K', 'Crece indefinidamente', 'Oscila alrededor de K'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': f'Con r = {r}, ¿el sistema presenta oscilaciones antes de estabilizarse?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, para valores altos de r', 'No, convergencia suave', 'Depende de N0'],
                    'respuesta_correcta': 0 if r > 1.5 else 1
                }
            ],
            'analisis_requerido': [
                'Graficar N(t) para diferentes valores de r',
                'Medir el tiempo de convergencia al equilibrio',
                'Comparar curvas con diferentes N0'
            ]
        }
    
    def _generar_verhulst_transiciones(self, dificultad):
        """Ejercicio 2: Transiciones de Fase en el Modelo de Verhulst Discreto."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            r = random.choice([2.5, 2.8, 3.2, 3.5])
        elif nivel == 2:
            r = round(random.uniform(2.0, 3.8), 1)
        else:
            r = round(random.uniform(1.5, 4.0), 2)
        
        return {
            'sistema': 'verhulst',
            'titulo': 'Ejercicio 2: Transiciones de Fase en el Modelo de Verhulst Discreto',
            'dificultad': dificultad,
            'parametros': {'x0': 0.4, 'r': r},
            'objetivos': [
                'Explorar comportamientos complejos en sistemas discretos simples',
                'Identificar ciclos periódicos y caos',
                'Comprender el diagrama de bifurcación'
            ],
            'instrucciones': [
                f'1. Configure parámetro r = {r}',
                '2. Ejecute el mapa logístico discreto',
                '3. Observe el comportamiento asintótico',
                '4. Identifique si es punto fijo, periódico o caótico'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿Para r = {r}, el sistema converge a un único punto fijo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No, oscila periódicamente', 'Comportamiento caótico'],
                    'respuesta_correcta': 0 if r < 3.0 else (1 if r < 3.57 else 2)
                },
                {
                    'id': 2,
                    'texto': '¿Aproximadamente en qué valor de r aparece la primera bifurcación?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 3.0,
                    'tolerancia': 0.2,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': '¿El mapa de Verhulst exhibe comportamiento caótico para r ≈ 3.7?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No', 'Solo en ventanas periódicas'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Generar diagramas de bifurcación',
                'Identificar regiones de comportamiento periódico',
                'Observar duplicaciones de período'
            ]
        }
    
    def _generar_amortiguamiento_analisis(self, dificultad):
        """Ejercicio 3: Análisis de Amortiguamiento en Osciladores Mecánicos."""
        nivel = self.DIFICULTAD[dificultad]
        
        m = 1.0  # masa fija para simplicidad
        k = 25.0  # constante fija
        
        if nivel == 1:
            c = random.choice([2.0, 10.0, 20.0])  # Sub, crítico, sobre
        elif nivel == 2:
            c = round(random.uniform(1.0, 25.0), 1)
        else:
            c = round(random.uniform(0.5, 30.0), 2)
        
        c_crit = 2 * np.sqrt(k * m)
        zeta = c / c_crit
        
        return {
            'sistema': 'amortiguador',
            'titulo': 'Ejercicio 3: Análisis de Amortiguamiento en Osciladores Mecánicos',
            'dificultad': dificultad,
            'parametros': {'m': m, 'c': c, 'k': k, 'x0': 1.0, 'v0': 0.0, 'F0': 0.0, 'omega_f': 0.0},
            'objetivos': [
                'Comprender cómo el coeficiente de amortiguamiento afecta la respuesta dinámica',
                'Clasificar regímenes: subamortiguado, crítico y sobreamortiguado',
                'Medir el decremento logarítmico'
            ],
            'instrucciones': [
                f'1. Configure m = {m} kg, k = {k} N/m, c = {c} Ns/m',
                '2. Configure x(0) = 1.0 m, v(0) = 0.0 m/s',
                '3. Simule la respuesta temporal',
                f'4. Calcule ζ = c/(2√(mk)) = {zeta:.3f}'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿El sistema con ζ = {zeta:.3f} está subamortiguado, críticamente amortiguado o sobreamortiguado?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado (ζ < 1)', 'Críticamente amortiguado (ζ = 1)', 'Sobreamortiguado (ζ > 1)'],
                    'respuesta_correcta': 0 if zeta < 0.95 else (1 if zeta < 1.05 else 2)
                },
                {
                    'id': 2,
                    'texto': '¿Cuál régimen retorna al equilibrio más rápido sin oscilar?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'],
                    'respuesta_correcta': 1
                },
                {
                    'id': 3,
                    'texto': '¿El sistema oscila con amplitud decreciente?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No'],
                    'respuesta_correcta': 0 if zeta < 1 else 1
                }
            ],
            'analisis_requerido': [
                'Graficar x(t) versus tiempo',
                'Calcular el factor de amortiguamiento ζ',
                'Medir el decremento logarítmico si ζ < 1'
            ]
        }
    
    def _generar_ciclo_limite(self, dificultad):
        """Ejercicio 4: Ciclos Límite en el Oscilador de Van der Pol."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            mu = random.choice([0.5, 1.0, 2.0])
        elif nivel == 2:
            mu = round(random.uniform(0.2, 4.0), 1)
        else:
            mu = round(random.uniform(0.1, 6.0), 2)
        
        x0 = round(random.uniform(-2, 2), 1)
        v0 = round(random.uniform(-2, 2), 1)
        
        return {
            'sistema': 'van_der_pol',
            'titulo': 'Ejercicio 4: Ciclos Límite en el Oscilador de Van der Pol',
            'dificultad': dificultad,
            'parametros': {'mu': mu, 'x0': x0, 'v0': v0},
            'objetivos': [
                'Identificar la existencia de ciclos límite en sistemas no lineales',
                'Comprender cómo μ afecta la forma y amplitud del ciclo',
                'Verificar independencia de condiciones iniciales'
            ],
            'instrucciones': [
                f'1. Configure μ = {mu}',
                f'2. Pruebe diferentes condiciones iniciales: x(0) = {x0}, v(0) = {v0}',
                '3. Grafique el espacio de fases (x vs dx/dt)',
                '4. Observe la convergencia al ciclo límite'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿El ciclo límite depende de las condiciones iniciales?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, cada condición inicial genera un ciclo diferente', 'No, todas convergen al mismo ciclo'],
                    'respuesta_correcta': 1
                },
                {
                    'id': 2,
                    'texto': f'Con μ = {mu}, ¿el ciclo límite es más circular o más distorsionado?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Circular (μ pequeño)', 'Distorsionado (μ grande)'],
                    'respuesta_correcta': 0 if mu < 1.5 else 1
                },
                {
                    'id': 3,
                    'texto': '¿Qué representa físicamente el ciclo límite?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Equilibrio inestable', 'Oscilación autosostenida', 'Comportamiento caótico'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar espacio de fases para varias condiciones iniciales',
                'Comparar forma del ciclo para μ pequeño vs grande',
                'Medir el período de oscilación'
            ]
        }
    
    def _generar_hopf_aparicion(self, dificultad):
        """Ejercicio 5: Aparición de Oscilaciones por Bifurcación de Hopf."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            mu = random.choice([-0.5, 0.0, 0.5])
        elif nivel == 2:
            mu = round(random.uniform(-0.8, 1.0), 1)
        else:
            mu = round(random.uniform(-1.5, 1.5), 2)
        
        return {
            'sistema': 'hopf',
            'titulo': 'Ejercicio 5: Aparición de Oscilaciones por Bifurcación de Hopf',
            'dificultad': dificultad,
            'parametros': {'mu': mu, 'x0': 0.1, 'y0': 0.1, 'omega': 1.0},
            'objetivos': [
                'Observar transición de punto fijo estable a ciclo límite',
                'Determinar el valor crítico de bifurcación',
                'Medir cómo crece la amplitud del ciclo con μ'
            ],
            'instrucciones': [
                f'1. Configure μ = {mu}',
                '2. Grafique trayectorias en el plano de fases (x, y)',
                '3. Determine hacia dónde convergen las trayectorias',
                '4. Pruebe valores de μ negativos, cero y positivos'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'Con μ = {mu}, ¿las trayectorias convergen al origen o a un ciclo límite?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Convergen al origen (μ < 0)', 'Ciclo límite (μ > 0)', 'Punto crítico (μ = 0)'],
                    'respuesta_correcta': 0 if mu < -0.05 else (1 if mu > 0.05 else 2)
                },
                {
                    'id': 2,
                    'texto': '¿En qué valor de μ ocurre la bifurcación de Hopf?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 0.0,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': '¿Cómo crece el radio del ciclo límite con μ?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Proporcional a μ', 'Proporcional a √μ', 'Proporcional a μ²'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar plano de fases para diferentes μ',
                'Medir el radio del ciclo límite vs μ',
                'Identificar el tipo de bifurcación (supercrítica/subcrítica)'
            ]
        }
    
    def _generar_rlc_resonancia(self, dificultad):
        """Ejercicio 6: Circuito RLC - Resonancia y Factor de Calidad."""
        nivel = self.DIFICULTAD[dificultad]
        
        L = 0.1  # Henrios
        C = 0.001  # Faradios
        
        if nivel == 1:
            R = random.choice([5.0, 10.0, 20.0])
        elif nivel == 2:
            R = round(random.uniform(3.0, 30.0), 1)
        else:
            R = round(random.uniform(1.0, 50.0), 1)
        
        omega_0 = 1 / np.sqrt(L * C)
        Q = omega_0 * L / R
        
        return {
            'sistema': 'rlc',
            'titulo': 'Ejercicio 6: Circuito RLC - Resonancia y Factor de Calidad',
            'dificultad': dificultad,
            'parametros': {'R': R, 'L': L, 'C': C, 'V0': 10.0, 'I0': 0.0, 'Q0': 0.0},
            'objetivos': [
                'Analizar la respuesta en frecuencia de un circuito RLC',
                'Identificar la frecuencia de resonancia',
                'Calcular el factor de calidad Q'
            ],
            'instrucciones': [
                f'1. Configure R = {R} Ω, L = {L} H, C = {C} F',
                f'2. Calcule ω₀ = 1/√(LC) = {omega_0:.2f} rad/s',
                f'3. Calcule Q = ω₀L/R = {Q:.2f}',
                '4. Observe la respuesta del circuito'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Cuál es la frecuencia de resonancia ω₀?',
                    'tipo': 'numerica',
                    'respuesta_esperada': omega_0,
                    'tolerancia': omega_0 * 0.1,
                    'unidad': 'rad/s'
                },
                {
                    'id': 2,
                    'texto': f'Con R = {R} Ω, ¿el circuito tiene alta o baja selectividad?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Alta (Q > 5)', 'Media (1 < Q < 5)', 'Baja (Q < 1)'],
                    'respuesta_correcta': 0 if Q > 5 else (1 if Q > 1 else 2)
                },
                {
                    'id': 3,
                    'texto': '¿Cómo afecta aumentar R a la altura del pico de resonancia?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Aumenta', 'Disminuye', 'No cambia'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar I(t) y V_C(t)',
                'Calcular frecuencia de resonancia',
                'Determinar el ancho de banda'
            ]
        }
    
    def _generar_sir_propagacion(self, dificultad):
        """Ejercicio 7: Propagación de Epidemias - Modelo SIR Básico."""
        nivel = self.DIFICULTAD[dificultad]
        
        N = 10000
        
        if nivel == 1:
            beta = 0.3
            gamma = 0.1
            I0 = 10
        elif nivel == 2:
            beta = round(random.uniform(0.2, 0.6), 2)
            gamma = round(random.uniform(0.05, 0.2), 2)
            I0 = random.randint(5, 50)
        else:
            beta = round(random.uniform(0.15, 0.8), 2)
            gamma = round(random.uniform(0.03, 0.3), 2)
            I0 = random.randint(1, 100)
        
        S0 = N - I0
        R0_basico = beta / gamma
        
        return {
            'sistema': 'sir',
            'titulo': 'Ejercicio 7: Propagación de Epidemias - Modelo SIR Básico',
            'dificultad': dificultad,
            'parametros': {'S0': S0, 'I0': I0, 'R0': 0, 'beta': beta, 'gamma': gamma},
            'objetivos': [
                'Comprender la dinámica de propagación de enfermedades infecciosas',
                'Calcular el número reproductivo básico R₀',
                'Determinar la severidad de un brote'
            ],
            'instrucciones': [
                f'1. Configure población: S(0) = {S0}, I(0) = {I0}, R(0) = 0',
                f'2. Configure β = {beta}, γ = {gamma}',
                f'3. Calcule R₀ = β/γ = {R0_basico:.2f}',
                '4. Simule y observe el pico de infectados'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Cuál es el número reproductivo básico R₀?',
                    'tipo': 'numerica',
                    'respuesta_esperada': R0_basico,
                    'tolerancia': 0.2,
                    'unidad': ''
                },
                {
                    'id': 2,
                    'texto': f'Con R₀ = {R0_basico:.2f}, ¿habrá un brote epidémico significativo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí (R₀ > 1)', 'No (R₀ < 1)', 'Incierto'],
                    'respuesta_correcta': 0 if R0_basico > 1 else 1
                },
                {
                    'id': 3,
                    'texto': '¿Por qué el número de infectados eventualmente disminuye?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Por intervención externa', 'La población susceptible cae bajo el umbral crítico', 'El virus muta'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar S(t), I(t), R(t)',
                'Identificar el pico de infectados',
                'Calcular la fracción final de población afectada'
            ]
        }
    
    def _generar_lorenz_sensibilidad(self, dificultad):
        """Ejercicio 8: Atractor de Lorenz - Sensibilidad a Condiciones Iniciales."""
        nivel = self.DIFICULTAD[dificultad]
        
        sigma = 10.0
        rho = 28.0
        beta = 8.0/3.0
        
        if nivel == 1:
            epsilon = 0.01
        elif nivel == 2:
            epsilon = 0.001
        else:
            epsilon = 0.0001
        
        return {
            'sistema': 'lorenz',
            'titulo': 'Ejercicio 8: Atractor de Lorenz - Sensibilidad a Condiciones Iniciales',
            'dificultad': dificultad,
            'parametros': {'x0': 1.0, 'y0': 1.0, 'z0': 1.0, 'sigma': sigma, 'rho': rho, 'beta': beta},
            'objetivos': [
                'Visualizar el atractor extraño de Lorenz',
                'Demostrar sensibilidad a condiciones iniciales (caos determinista)',
                'Comprender la forma de mariposa del atractor'
            ],
            'instrucciones': [
                f'1. Configure σ = {sigma}, ρ = {rho}, β = {beta:.2f}',
                f'2. Simule con condiciones iniciales (1, 1, 1) y (1+{epsilon}, 1, 1)',
                '3. Compare ambas trayectorias',
                '4. Visualice el atractor en 3D'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿Las trayectorias con diferencia inicial de {epsilon} divergen con el tiempo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, exponencialmente', 'No, permanecen cercanas', 'Depende'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 2,
                    'texto': '¿Cuántos lóbulos tiene el atractor de Lorenz?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 2,
                    'tolerancia': 0,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': 'Para ρ < 24.74, ¿qué ocurre con el atractor?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Se mantiene caótico', 'Converge a puntos fijos estables', 'Desaparece'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Visualizar el atractor en espacio 3D',
                'Calcular la separación entre trayectorias',
                'Identificar la forma de mariposa'
            ]
        }
    
    def _generar_orbital_kepler(self, dificultad):
        """Ejercicio 9: Órbitas Planetarias - Leyes de Kepler."""
        nivel = self.DIFICULTAD[dificultad]
        
        GM = 1.0  # Unidades normalizadas
        r0 = 1.0
        
        if nivel == 1:
            # Órbita circular
            v0 = 1.0
            theta = 90
        elif nivel == 2:
            # Órbita elíptica moderada
            v0 = round(random.uniform(0.7, 1.2), 2)
            theta = 90
        else:
            # Órbita variada
            v0 = round(random.uniform(0.5, 1.5), 2)
            theta = random.randint(45, 135)
        
        return {
            'sistema': 'orbital',
            'titulo': 'Ejercicio 9: Órbitas Planetarias - Leyes de Kepler',
            'dificultad': dificultad,
            'parametros': {'x0': r0, 'y0': 0.0, 'vx0': 0.0, 'vy0': v0, 'GM': GM},
            'objetivos': [
                'Verificar las leyes de Kepler mediante simulación',
                'Comprender cómo la energía determina el tipo de órbita',
                'Analizar la conservación del momento angular'
            ],
            'instrucciones': [
                f'1. Configure distancia inicial r0 = {r0}',
                f'2. Configure velocidad inicial v0 = {v0}, ángulo = {theta}°',
                '3. Simule la órbita',
                '4. Verifique si es circular, elíptica o hiperbólica'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'Con v0 = {v0} (v_circular = 1.0), ¿qué tipo de órbita se forma?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Circular', 'Elíptica', 'Hiperbólica'],
                    'respuesta_correcta': 0 if abs(v0 - 1.0) < 0.1 else (1 if v0 < 1.4 else 2)
                },
                {
                    'id': 2,
                    'texto': '¿El momento angular se conserva en todas las órbitas?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No', 'Solo en órbitas circulares'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': '¿Qué relación cumple el período T con el semieje mayor a? (3ª Ley de Kepler)',
                    'tipo': 'opcion_multiple',
                    'opciones': ['T ∝ a', 'T² ∝ a³', 'T³ ∝ a²'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar la trayectoria orbital',
                'Calcular energía total y momento angular',
                'Verificar la tercera ley de Kepler'
            ]
        }
    
    def _generar_orbital_hohmann(self, dificultad):
        """Ejercicio 10: Transferencia Orbital de Hohmann."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            r1 = 1.0
            r2 = 2.0
        elif nivel == 2:
            r1 = 1.0
            r2 = round(random.uniform(1.5, 4.0), 1)
        else:
            r1 = round(random.uniform(0.5, 2.0), 1)
            r2 = round(random.uniform(r1 + 1.0, r1 + 6.0), 1)
        
        a_t = (r1 + r2) / 2
        
        return {
            'sistema': 'orbital',
            'titulo': 'Ejercicio 10: Transferencia Orbital de Hohmann',
            'dificultad': dificultad,
            'parametros': {'x0': r1, 'y0': 0.0, 'vx0': 0.0, 'vy0': 1.0/np.sqrt(r1), 'GM': 1.0},
            'objetivos': [
                'Diseñar una transferencia de Hohmann entre dos órbitas circulares',
                'Calcular los cambios de velocidad requeridos (Δv)',
                'Determinar el tiempo de transferencia'
            ],
            'instrucciones': [
                f'1. Órbita inicial de radio r1 = {r1}',
                f'2. Órbita final de radio r2 = {r2}',
                f'3. Semieje mayor de transferencia a_t = {a_t}',
                '4. Calcule Δv1 y Δv2'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿Cuál es el semieje mayor de la órbita de transferencia?',
                    'tipo': 'numerica',
                    'respuesta_esperada': a_t,
                    'tolerancia': 0.1,
                    'unidad': 'UA'
                },
                {
                    'id': 2,
                    'texto': 'En una transferencia a órbita superior, ¿cuál Δv es generalmente mayor?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Δv1 (primer impulso)', 'Δv2 (segundo impulso)', 'Son iguales'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': '¿Por qué la transferencia de Hohmann es más eficiente que empuje continuo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Usa menos combustible', 'Es más rápida', 'Es más segura'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Calcular velocidades orbitales en r1 y r2',
                'Determinar Δv total requerido',
                'Calcular tiempo de transferencia'
            ]
        }
    
    def _generar_newton_enfriamiento(self, dificultad):
        """Ejercicio 11: Enfriamiento de un Cuerpo - Ley de Newton."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            T0 = 80
            T_amb = 20
            k = 0.1
        elif nivel == 2:
            T0 = random.randint(60, 100)
            T_amb = random.randint(15, 30)
            k = round(random.uniform(0.05, 0.3), 2)
        else:
            T0 = random.randint(40, 120)
            T_amb = random.randint(10, 35)
            k = round(random.uniform(0.02, 0.5), 3)
        
        tau = 1 / k
        t_half = tau * np.log(2)
        
        return {
            'sistema': 'newton',
            'titulo': 'Ejercicio 11: Enfriamiento de un Cuerpo - Ley de Newton',
            'dificultad': dificultad,
            'parametros': {'T0': T0, 'T_env': T_amb, 'k': k},
            'objetivos': [
                'Aplicar la ley de enfriamiento de Newton',
                'Determinar constantes de tiempo térmicas',
                'Predecir tiempo de enfriamiento'
            ],
            'instrucciones': [
                f'1. Configure T(0) = {T0}°C, T_amb = {T_amb}°C',
                f'2. Configure constante k = {k} min⁻¹',
                f'3. Calcule tiempo de relajación τ = 1/k = {tau:.2f} min',
                '4. Simule la evolución temporal'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Qué fracción de la diferencia inicial permanece después de un tiempo τ?',
                    'tipo': 'numerica',
                    'respuesta_esperada': np.exp(-1),
                    'tolerancia': 0.05,
                    'unidad': ''
                },
                {
                    'id': 2,
                    'texto': f'¿Cuál es el tiempo de medio enfriamiento (reducción al 50%)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': t_half,
                    'tolerancia': t_half * 0.1,
                    'unidad': 'min'
                },
                {
                    'id': 3,
                    'texto': '¿El cuerpo alcanza exactamente T_amb en tiempo finito?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No, se aproxima asintóticamente'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar T(t) versus tiempo',
                'Calcular constante de tiempo τ',
                'Ajustar curva exponencial'
            ]
        }
    
    def _generar_rc_carga(self, dificultad):
        """Ejercicio 12: Dinámica de Carga de un Capacitor."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            R = 1000  # Ohmios
            C = 0.001  # Faradios
            V0 = 10
        elif nivel == 2:
            R = random.randint(500, 5000)
            C = round(random.uniform(0.0001, 0.01), 4)
            V0 = random.randint(5, 20)
        else:
            R = random.randint(100, 10000)
            C = round(random.uniform(0.00001, 0.1), 5)
            V0 = random.randint(3, 50)
        
        tau = R * C
        
        return {
            'sistema': 'rlc',
            'titulo': 'Ejercicio 12: Dinámica de Carga de un Capacitor (RC)',
            'dificultad': dificultad,
            'parametros': {'R': R, 'L': 0.0, 'C': C, 'V0': V0, 'I0': 0.0, 'Q0': 0.0},
            'objetivos': [
                'Analizar proceso de carga y descarga de un capacitor',
                'Comprender el concepto de constante de tiempo RC',
                'Calcular tiempos de carga'
            ],
            'instrucciones': [
                f'1. Configure R = {R} Ω, C = {C} F, V0 = {V0} V',
                f'2. Calcule τ = RC = {tau:.4f} s',
                '3. Simule la carga del capacitor',
                '4. Verifique que en τ se alcanza ~63% de V0'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Cuántas constantes de tiempo se requieren para alcanzar 95% del voltaje final?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 3,
                    'tolerancia': 0.5,
                    'unidad': 'τ'
                },
                {
                    'id': 2,
                    'texto': '¿Cómo afecta duplicar R a la constante de tiempo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Se duplica', 'Se reduce a la mitad', 'No cambia'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': '¿Por qué la corriente inicial de carga es máxima?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Máxima diferencia de voltaje', 'Capacitor vacío', 'Resistencia mínima'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar V_C(t) y I(t)',
                'Verificar V_C(τ) ≈ 0.63·V0',
                'Medir tiempo para alcanzar 99% de carga'
            ]
        }
    
    def _generar_crecimiento_comparacion(self, dificultad):
        """Ejercicio 13: Comparación de Modelos de Crecimiento Poblacional."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            N0 = 20
            r = 0.2
            K = 1000
        elif nivel == 2:
            N0 = random.randint(10, 100)
            r = round(random.uniform(0.1, 0.5), 2)
            K = random.randint(500, 1500)
        else:
            N0 = random.randint(5, 200)
            r = round(random.uniform(0.05, 0.8), 3)
            K = random.randint(300, 2000)
        
        return {
            'sistema': 'logistico',
            'titulo': 'Ejercicio 13: Comparación de Modelos de Crecimiento Poblacional',
            'dificultad': dificultad,
            'parametros': {'N0': N0, 'r': r, 'K': K},
            'objetivos': [
                'Contrastar crecimiento exponencial vs logístico',
                'Identificar cuándo cada modelo es aplicable',
                'Comprender limitaciones del modelo exponencial'
            ],
            'instrucciones': [
                f'1. Configure N(0) = {N0}, r = {r}, K = {K}',
                '2. Simule modelo logístico',
                '3. Compare mentalmente con crecimiento exponencial',
                '4. Identifique momento de divergencia significativa'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿En qué rango de N las predicciones de ambos modelos son similares?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['N << K', 'N ≈ K', 'N >> K'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 2,
                    'texto': f'¿En qué valor de N ocurre la tasa de crecimiento máxima del modelo logístico?',
                    'tipo': 'numerica',
                    'respuesta_esperada': K / 2,
                    'tolerancia': K * 0.1,
                    'unidad': 'individuos'
                },
                {
                    'id': 3,
                    'texto': '¿Por qué el modelo exponencial no es realista a largo plazo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Predice crecimiento infinito', 'Es muy lento', 'No considera nacimientos'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar ambos modelos en la misma figura',
                'Calcular tiempo de duplicación',
                'Identificar punto de inflexión del modelo logístico'
            ]
        }
    
    def _generar_estabilidad_lineal(self, dificultad):
        """Ejercicio 14: Estabilidad en Sistemas Lineales de Segundo Orden."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            # Sistema estable simple
            a11, a12 = -1.0, 1.0
            a21, a22 = -1.0, -1.0
        elif nivel == 2:
            # Sistema aleatorio
            a11 = round(random.uniform(-3, 1), 1)
            a12 = round(random.uniform(-2, 2), 1)
            a21 = round(random.uniform(-2, 2), 1)
            a22 = round(random.uniform(-3, 1), 1)
        else:
            # Sistema más complejo
            a11 = round(random.uniform(-5, 2), 1)
            a12 = round(random.uniform(-3, 3), 1)
            a21 = round(random.uniform(-3, 3), 1)
            a22 = round(random.uniform(-5, 2), 1)
        
        traza = a11 + a22
        det = a11 * a22 - a12 * a21
        discriminante = traza**2 - 4*det
        
        return {
            'sistema': 'hopf',
            'titulo': 'Ejercicio 14: Estabilidad en Sistemas Lineales de Segundo Orden',
            'dificultad': dificultad,
            'parametros': {'mu': traza/2, 'x0': 1.0, 'y0': 0.5, 'omega': 1.0},
            'objetivos': [
                'Clasificar estabilidad mediante análisis de valores propios',
                'Relacionar traza y determinante con el comportamiento',
                'Identificar nodos, espirales, sillas y centros'
            ],
            'instrucciones': [
                f'1. Matriz A: [[{a11}, {a12}], [{a21}, {a22}]]',
                f'2. Calcule traza = {traza:.2f}, determinante = {det:.2f}',
                f'3. Discriminante Δ = tr² - 4·det = {discriminante:.2f}',
                '4. Clasifique el punto de equilibrio'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'Con tr(A) = {traza:.2f} y det(A) = {det:.2f}, ¿el sistema es estable?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí (tr < 0, det > 0)', 'No (tr > 0 o det < 0)', 'Marginalmente estable'],
                    'respuesta_correcta': 0 if (traza < 0 and det > 0) else 1
                },
                {
                    'id': 2,
                    'texto': f'Con Δ = {discriminante:.2f}, ¿el sistema exhibe oscilaciones?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí (Δ < 0, valores propios complejos)', 'No (Δ > 0, valores propios reales)'],
                    'respuesta_correcta': 0 if discriminante < 0 else 1
                },
                {
                    'id': 3,
                    'texto': 'Si det(A) < 0, ¿qué tipo de punto fijo es?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Nodo', 'Espiral', 'Silla (inestable)', 'Centro'],
                    'respuesta_correcta': 2
                }
            ],
            'analisis_requerido': [
                'Calcular valores propios',
                'Graficar plano de fases',
                'Clasificar el punto de equilibrio'
            ]
        }
    
    def _generar_sir_vacunacion(self, dificultad):
        """Ejercicio 15: Transiciones en el Modelo SIR con Vacunación."""
        nivel = self.DIFICULTAD[dificultad]
        
        N = 10000
        beta = 0.4
        gamma = 0.15
        R0_basico = beta / gamma
        
        if nivel == 1:
            p = 0.5  # 50% vacunados
        elif nivel == 2:
            p = round(random.uniform(0.3, 0.8), 2)
        else:
            p = round(random.uniform(0.1, 0.95), 2)
        
        p_critico = 1 - 1/R0_basico if R0_basico > 1 else 0
        S0 = int(N * (1 - p))
        
        return {
            'sistema': 'sir',
            'titulo': 'Ejercicio 15: Modelo SIR con Vacunación',
            'dificultad': dificultad,
            'parametros': {'S0': S0, 'I0': 10, 'R0': N - S0 - 10, 'beta': beta, 'gamma': gamma},
            'objetivos': [
                'Evaluar el efecto de la vacunación en la dinámica epidémica',
                'Determinar el umbral de vacunación (inmunidad de rebaño)',
                'Calcular R_efectivo'
            ],
            'instrucciones': [
                f'1. R₀ básico = β/γ = {R0_basico:.2f}',
                f'2. Fracción vacunada p = {p:.2f}',
                f'3. Umbral crítico p_c = 1 - 1/R₀ = {p_critico:.2f}',
                f'4. Susceptibles iniciales S(0) = N(1-p) = {S0}'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿Cuál es el umbral de vacunación p_c para lograr inmunidad de rebaño?',
                    'tipo': 'numerica',
                    'respuesta_esperada': p_critico,
                    'tolerancia': 0.05,
                    'unidad': ''
                },
                {
                    'id': 2,
                    'texto': f'Con p = {p:.2f} y p_c = {p_critico:.2f}, ¿se previene el brote?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí (p > p_c)', 'No (p < p_c)', 'Límite (p ≈ p_c)'],
                    'respuesta_correcta': 0 if p > p_critico + 0.05 else (1 if p < p_critico - 0.05 else 2)
                },
                {
                    'id': 3,
                    'texto': '¿Es necesario vacunar al 100% para eliminar brotes?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No, alcanza con superar p_c'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar pico de infectados vs p',
                'Calcular R_efectivo = R₀(1-p)',
                'Identificar p crítico visualmente'
            ]
        }
    
    def _generar_orbital_perturbaciones(self, dificultad):
        """Ejercicio 16: Análisis de Perturbaciones en Órbitas Circulares."""
        nivel = self.DIFICULTAD[dificultad]
        
        r0 = 1.0
        v_circ = 1.0  # velocidad circular normalizada
        
        if nivel == 1:
            delta_v = 0.1  # 10% de perturbación
        elif nivel == 2:
            delta_v = round(random.uniform(0.05, 0.2), 2)
        else:
            delta_v = round(random.uniform(0.01, 0.3), 3)
        
        return {
            'sistema': 'orbital',
            'titulo': 'Ejercicio 16: Análisis de Perturbaciones en Órbitas Circulares',
            'dificultad': dificultad,
            'parametros': {'x0': r0, 'y0': 0.0, 'vx0': delta_v, 'vy0': v_circ, 'GM': 1.0},
            'objetivos': [
                'Estudiar cómo perturbaciones afectan órbitas circulares',
                'Analizar diferencias entre perturbaciones radiales y tangenciales',
                'Comprender la estabilidad orbital'
            ],
            'instrucciones': [
                f'1. Órbita circular perfecta: r0 = {r0}, v = {v_circ}',
                f'2. Perturbación de velocidad: Δv = {delta_v}',
                '3. Simule la nueva órbita',
                '4. Determine la excentricidad resultante'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿La órbita con perturbación Δv = {delta_v} sigue siendo circular?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No, se vuelve elíptica'],
                    'respuesta_correcta': 1
                },
                {
                    'id': 2,
                    'texto': '¿Qué tipo de perturbación produce mayor cambio en excentricidad?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Radial', 'Tangencial', 'Son equivalentes'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': '¿La energía orbital cambia con una perturbación tangencial?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar la trayectoria perturbada',
                'Calcular excentricidad e',
                'Medir cambio en energía total'
            ]
        }
    
    def _generar_oscilador_forzado(self, dificultad):
        """Ejercicio 17: Oscilaciones Forzadas y Resonancia en Sistemas Mecánicos."""
        nivel = self.DIFICULTAD[dificultad]
        
        m = 1.0
        k = 25.0
        omega_0 = np.sqrt(k / m)
        
        if nivel == 1:
            c = 2.0
            omega = omega_0  # En resonancia
            F0 = 5.0
        elif nivel == 2:
            c = round(random.uniform(1.0, 5.0), 1)
            omega = round(omega_0 * random.uniform(0.5, 1.5), 2)
            F0 = round(random.uniform(3.0, 10.0), 1)
        else:
            c = round(random.uniform(0.5, 10.0), 2)
            omega = round(omega_0 * random.uniform(0.3, 2.0), 2)
            F0 = round(random.uniform(1.0, 15.0), 1)
        
        return {
            'sistema': 'amortiguador',
            'titulo': 'Ejercicio 17: Oscilaciones Forzadas y Resonancia en Sistemas Mecánicos',
            'dificultad': dificultad,
            'parametros': {'m': m, 'c': c, 'k': k, 'x0': 0.0, 'v0': 0.0, 'F0': F0, 'omega_f': omega},
            'objetivos': [
                'Analizar respuesta de oscilador forzado a fuerzas periódicas',
                'Identificar condiciones de resonancia',
                'Comprender el papel del amortiguamiento en resonancia'
            ],
            'instrucciones': [
                f'1. Configure m = {m} kg, k = {k} N/m, c = {c} Ns/m',
                f'2. Frecuencia natural ω₀ = √(k/m) = {omega_0:.2f} rad/s',
                f'3. Fuerza: F(t) = {F0}·cos({omega}t)',
                '4. Observe la amplitud de oscilación en estado estacionario'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'¿En qué frecuencia ω/ω₀ se alcanza la amplitud máxima (resonancia)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 1.0,
                    'tolerancia': 0.15,
                    'unidad': ''
                },
                {
                    'id': 2,
                    'texto': '¿Cómo afecta aumentar c a la altura del pico de resonancia?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Aumenta', 'Disminuye', 'No cambia'],
                    'respuesta_correcta': 1
                },
                {
                    'id': 3,
                    'texto': '¿Por qué sistemas con poco amortiguamiento son susceptibles a daños por resonancia?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Amplitudes muy grandes', 'Frecuencia muy alta', 'Energía negativa'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar amplitud vs frecuencia (curva de resonancia)',
                'Medir desfase entre fuerza y desplazamiento',
                'Identificar frecuencia de resonancia'
            ]
        }
