"""
Generador automático de ejercicios educacionales para sistemas dinámicos.
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
    
    def __init__(self):
        """Inicializa el generador de ejercicios."""
        self.ejercicio_actual = None
        self.respuestas_esperadas = {}
    
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
        """Genera ejercicio de enfriamiento de Newton."""
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
        
        # Calcular tiempo esperado para llegar a cierta temperatura
        T_objetivo = T_env + (T0 - T_env) * 0.37  # Aproximadamente 1 constante de tiempo
        t_esperado = -np.log((T_objetivo - T_env) / (T0 - T_env)) / k
        
        ejercicio = {
            'sistema': 'newton',
            'titulo': 'Ley de Enfriamiento de Newton',
            'dificultad': dificultad,
            'parametros': {
                'T0': T0,
                'T_env': T_env,
                'k': k
            },
            'objetivos': [
                'Comprender el proceso de enfriamiento exponencial',
                'Analizar la influencia de la constante k',
                'Predecir el tiempo de enfriamiento'
            ],
            'instrucciones': [
                f'1. Configure la temperatura inicial en {T0}°C',
                f'2. Configure la temperatura ambiente en {T_env}°C',
                f'3. Configure la constante k en {k}',
                '4. Ejecute la simulación y observe el comportamiento',
                '5. Responda las preguntas basándose en los resultados'
            ],
            'preguntas': [
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
                    'texto': '¿La temperatura alcanza exactamente la temperatura ambiente?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No, se aproxima asintóticamente', 'Depende de k'],
                    'respuesta_correcta': 1
                },
                {
                    'id': 3,
                    'texto': f'Si k fuera el doble ({2*k}), ¿el enfriamiento sería más rápido o más lento?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Más rápido', 'Más lento', 'Igual'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar la curva de temperatura vs tiempo',
                'Identificar la constante de tiempo del sistema',
                'Comparar con la solución analítica'
            ]
        }
        
        self.respuestas_esperadas['newton'] = ejercicio
        return ejercicio
    
    def _generar_van_der_pol(self, dificultad):
        """Genera ejercicio del oscilador de Van der Pol."""
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
        
        ejercicio = {
            'sistema': 'van_der_pol',
            'titulo': 'Oscilador de Van der Pol',
            'dificultad': dificultad,
            'parametros': {
                'mu': mu,
                'x0': x0,
                'v0': v0
            },
            'objetivos': [
                'Observar el comportamiento de ciclos límite',
                'Analizar el efecto del parámetro μ',
                'Estudiar el diagrama de fase'
            ],
            'instrucciones': [
                f'1. Configure μ = {mu}',
                f'2. Configure x(0) = {x0}, dx/dt(0) = {v0}',
                '3. Ejecute la simulación',
                '4. Observe el diagrama de fase',
                '5. Analice si existe un ciclo límite'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿El sistema converge a un ciclo límite?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No', 'Depende de las condiciones iniciales'],
                    'respuesta_correcta': 0 if mu > 0 else 1
                },
                {
                    'id': 2,
                    'texto': f'Con μ = {mu}, ¿qué tipo de comportamiento exhibe?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Oscilación amortiguada', 'Oscilación sostenida (ciclo límite)', 'Divergente'],
                    'respuesta_correcta': 1 if mu > 0 else 0
                },
                {
                    'id': 3,
                    'texto': '¿El sistema es lineal o no lineal?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Lineal', 'No lineal'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar el diagrama de fase',
                'Identificar puntos de equilibrio',
                'Analizar la estabilidad del ciclo límite'
            ]
        }
        
        return ejercicio
    
    def _generar_sir(self, dificultad):
        """Genera ejercicio del modelo SIR."""
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
        
        ejercicio = {
            'sistema': 'sir',
            'titulo': 'Modelo Epidemiológico SIR',
            'dificultad': dificultad,
            'parametros': {
                'S0': S0,
                'I0': I0,
                'R0': R0,
                'beta': beta,
                'gamma': gamma
            },
            'objetivos': [
                'Comprender la dinámica de epidemias',
                'Calcular el número reproductivo básico R₀',
                'Predecir el pico de infectados'
            ],
            'instrucciones': [
                f'1. Configure S(0) = {S0}, I(0) = {I0}, R(0) = {R0}',
                f'2. Configure β = {beta}, γ = {gamma}',
                '3. Ejecute la simulación',
                '4. Observe la evolución de las poblaciones',
                '5. Identifique el pico de infectados'
            ],
            'preguntas': [
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
                    'opciones': ['Sí, porque R₀ > 1', 'No, porque R₀ < 1', 'No se puede determinar'],
                    'respuesta_correcta': 0 if R0_basico > 1 else 1
                },
                {
                    'id': 3,
                    'texto': '¿Qué población nunca aumenta en el modelo SIR?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Susceptibles', 'Infectados', 'Recuperados', 'Todas pueden aumentar'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar las tres poblaciones',
                'Calcular R₀ = β/γ',
                'Determinar el día del pico de infectados'
            ]
        }
        
        return ejercicio
    
    def _generar_hopf(self, dificultad):
        """Genera ejercicio de bifurcación de Hopf."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            mu = random.choice([-0.5, 0.0, 0.5, 1.0])
        elif nivel == 2:
            mu = round(random.uniform(-1.0, 2.0), 1)
        else:
            mu = round(random.uniform(-2.0, 3.0), 2)
        
        ejercicio = {
            'sistema': 'hopf',
            'titulo': 'Bifurcación de Hopf',
            'dificultad': dificultad,
            'parametros': {
                'mu': mu,
                'x0': 0.1,
                'y0': 0.1,
                'omega': 1.0
            },
            'objetivos': [
                'Comprender la bifurcación de Hopf',
                'Identificar el valor crítico del parámetro',
                'Observar la transición a ciclo límite'
            ],
            'instrucciones': [
                f'1. Configure μ = {mu}',
                '2. Observe el comportamiento del sistema',
                '3. Experimente con valores de μ negativos y positivos',
                '4. Identifique el punto de bifurcación'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'Con μ = {mu}, ¿qué comportamiento exhibe el sistema?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Punto fijo estable', 'Ciclo límite estable', 'Comportamiento caótico'],
                    'respuesta_correcta': 0 if mu < 0 else 1
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
                    'texto': 'Para μ > 0, ¿el ciclo límite es estable o inestable?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Estable', 'Inestable'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar el diagrama de fase',
                'Variar μ y observar cambios',
                'Identificar el punto de bifurcación'
            ]
        }
        
        return ejercicio
    
    def _generar_logistico(self, dificultad):
        """Genera ejercicio del modelo logístico."""
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
        
        ejercicio = {
            'sistema': 'logistico',
            'titulo': 'Modelo Logístico de Crecimiento',
            'dificultad': dificultad,
            'parametros': {
                'N0': N0,
                'r': r,
                'K': K
            },
            'objetivos': [
                'Comprender el crecimiento logístico',
                'Identificar la capacidad de carga',
                'Analizar el efecto de la tasa de crecimiento'
            ],
            'instrucciones': [
                f'1. Configure N(0) = {N0}',
                f'2. Configure r = {r}, K = {K}',
                '3. Ejecute la simulación',
                '4. Observe cómo la población se estabiliza'
            ],
            'preguntas': [
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
                    'texto': '¿En qué valor de N la tasa de crecimiento es máxima?',
                    'tipo': 'numerica',
                    'respuesta_esperada': K / 2,
                    'tolerancia': K * 0.1,
                    'unidad': 'individuos'
                },
                {
                    'id': 3,
                    'texto': 'Si r se duplica, ¿la población alcanza K más rápido o más lento?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Más rápido', 'Más lento', 'Igual'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar N(t) vs t',
                'Identificar la capacidad de carga K',
                'Calcular el punto de inflexión'
            ]
        }
        
        return ejercicio
    
    def _generar_verhulst(self, dificultad):
        """Genera ejercicio del mapa de Verhulst."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            r = random.choice([2.5, 3.0, 3.2])
        elif nivel == 2:
            r = round(random.uniform(2.8, 3.6), 1)
        else:
            r = round(random.uniform(3.4, 4.0), 2)
        
        ejercicio = {
            'sistema': 'verhulst',
            'titulo': 'Mapa Logístico de Verhulst',
            'dificultad': dificultad,
            'parametros': {
                'x0': 0.5,
                'r': r
            },
            'objetivos': [
                'Observar bifurcaciones en sistemas discretos',
                'Comprender el camino al caos',
                'Analizar el diagrama de bifurcación'
            ],
            'instrucciones': [
                f'1. Configure r = {r}',
                '2. Ejecute la simulación',
                '3. Observe el comportamiento a largo plazo',
                '4. Experimente con diferentes valores de r'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': f'Con r = {r}, ¿qué comportamiento exhibe el sistema?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Punto fijo', 'Oscilación periódica', 'Comportamiento caótico'],
                    'respuesta_correcta': 0 if r < 3 else (1 if r < 3.57 else 2)
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
                    'texto': 'El mapa de Verhulst es un ejemplo de:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sistema continuo', 'Sistema discreto', 'Sistema híbrido'],
                    'respuesta_correcta': 1
                }
            ],
            'analisis_requerido': [
                'Graficar la serie temporal',
                'Construir el diagrama de bifurcación',
                'Identificar las regiones periódicas y caóticas'
            ]
        }
        
        return ejercicio
    
    def _generar_orbital(self, dificultad):
        """Genera ejercicio de órbitas espaciales."""
        nivel = self.DIFICULTAD[dificultad]
        
        if nivel == 1:
            # Órbita circular
            x0, y0 = 1.0, 0.0
            vx0, vy0 = 0.0, 1.0
        elif nivel == 2:
            # Órbita elíptica
            x0 = 1.0
            y0 = 0.0
            vx0 = 0.0
            vy0 = round(random.uniform(0.7, 1.3), 2)
        else:
            # Órbita variada
            x0 = round(random.uniform(0.5, 2.0), 2)
            y0 = 0.0
            vx0 = 0.0
            vy0 = round(random.uniform(0.5, 1.5), 2)
        
        ejercicio = {
            'sistema': 'orbital',
            'titulo': 'Órbitas Espaciales (Problema de Kepler)',
            'dificultad': dificultad,
            'parametros': {
                'x0': x0,
                'y0': y0,
                'vx0': vx0,
                'vy0': vy0,
                'mu': 1.0
            },
            'objetivos': [
                'Comprender las leyes de Kepler',
                'Analizar órbitas circulares y elípticas',
                'Verificar la conservación de energía'
            ],
            'instrucciones': [
                f'1. Configure posición inicial: ({x0}, {y0})',
                f'2. Configure velocidad inicial: ({vx0}, {vy0})',
                '3. Ejecute la simulación',
                '4. Observe la trayectoria orbital'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Qué tipo de órbita se forma?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Circular', 'Elíptica', 'Hiperbólica', 'Parabólica'],
                    'respuesta_correcta': 0 if abs(vy0 - 1.0) < 0.1 else 1
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
                    'opciones': ['Gravitacional', 'Electromagnética', 'Nuclear'],
                    'respuesta_correcta': 0
                }
            ],
            'analisis_requerido': [
                'Graficar la trayectoria orbital',
                'Calcular la energía total',
                'Verificar las leyes de Kepler'
            ]
        }
        
        return ejercicio
    
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
        """Genera ejercicio de sistema masa-resorte-amortiguador."""
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
        
        # Calcular tipo de amortiguamiento
        c_crit = 2 * np.sqrt(k * m)
        zeta = c / c_crit
        
        if zeta < 1:
            tipo = "Subamortiguado"
        elif abs(zeta - 1) < 0.1:
            tipo = "Críticamente amortiguado"
        else:
            tipo = "Sobreamortiguado"
        
        ejercicio = {
            'sistema': 'amortiguador',
            'titulo': 'Sistema Masa-Resorte-Amortiguador',
            'dificultad': dificultad,
            'parametros': {
                'm': m,
                'c': c,
                'k': k,
                'x0': 1.0,
                'v0': 0.0,
                'F0': 0.0,
                'omega_f': 0.0
            },
            'objetivos': [
                'Comprender los tipos de amortiguamiento',
                'Calcular el factor de amortiguamiento ζ',
                'Analizar la respuesta del sistema'
            ],
            'instrucciones': [
                f'1. Configure m = {m}, c = {c}, k = {k}',
                '2. Configure x(0) = 1.0, v(0) = 0.0',
                '3. Ejecute la simulación',
                '4. Observe el comportamiento'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Qué tipo de amortiguamiento presenta el sistema?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'],
                    'respuesta_correcta': 0 if zeta < 0.9 else (1 if zeta < 1.1 else 2)
                },
                {
                    'id': 2,
                    'texto': f'¿Cuál es el factor de amortiguamiento ζ?',
                    'tipo': 'numerica',
                    'respuesta_esperada': zeta,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': '¿El sistema oscila?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No'],
                    'respuesta_correcta': 0 if zeta < 1 else 1
                }
            ],
            'analisis_requerido': [
                'Graficar x(t) y v(t)',
                'Calcular ζ = c / (2√(km))',
                'Determinar el tipo de amortiguamiento'
            ]
        }
        
        return ejercicio
    
    def _generar_rlc(self, dificultad):
        """Genera ejercicio de circuito RLC."""
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
        
        return {
            'sistema': 'rlc',
            'titulo': 'Circuito RLC Serie',
            'dificultad': dificultad,
            'parametros': {
                'R': R,
                'L': L,
                'C': C,
                'V0': V0,
                'I0': 0.0,
                'Q0': 0.0
            },
            'objetivos': [
                'Comprender circuitos RLC',
                'Analizar oscilaciones eléctricas',
                'Calcular la frecuencia de resonancia'
            ],
            'instrucciones': [
                f'1. Configure R = {R}Ω, L = {L}H, C = {C}F',
                f'2. Configure V₀ = {V0}V',
                '3. Ejecute la simulación',
                '4. Observe corriente y voltaje'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿Cuál es la frecuencia de resonancia ω₀ = 1/√(LC)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 1 / np.sqrt(L * C),
                    'tolerancia': 5.0,
                    'unidad': 'rad/s'
                },
                {
                    'id': 2,
                    'texto': '¿El circuito está subamortiguado, críticamente amortiguado o sobreamortiguado?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'],
                    'respuesta_correcta': 0 if R < 2 * np.sqrt(L / C) else 2
                }
            ],
            'analisis_requerido': [
                'Graficar I(t) y V_C(t)',
                'Calcular ω₀ = 1/√(LC)',
                'Determinar el factor de calidad Q'
            ]
        }
    
    def _generar_lorenz(self, dificultad):
        """Genera ejercicio del sistema de Lorenz."""
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
        
        return {
            'sistema': 'lorenz',
            'titulo': 'Sistema de Lorenz (Atractor Caótico)',
            'dificultad': dificultad,
            'parametros': {
                'x0': 1.0,
                'y0': 1.0,
                'z0': 1.0,
                'sigma': sigma,
                'rho': rho,
                'beta': beta
            },
            'objetivos': [
                'Observar comportamiento caótico',
                'Comprender la teoría del caos',
                'Analizar el atractor extraño'
            ],
            'instrucciones': [
                f'1. Configure σ = {sigma}, ρ = {rho}, β = {beta:.2f}',
                '2. Ejecute la simulación',
                '3. Observe el atractor en 3D',
                '4. Analice la sensibilidad a condiciones iniciales'
            ],
            'preguntas': [
                {
                    'id': 1,
                    'texto': '¿El sistema de Lorenz es determinista o estocástico?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Determinista', 'Estocástico'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 2,
                    'texto': 'Para ρ > 24.74, ¿qué comportamiento exhibe?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Punto fijo', 'Ciclo límite', 'Comportamiento caótico'],
                    'respuesta_correcta': 2 if rho > 24.74 else 0
                }
            ],
            'analisis_requerido': [
                'Visualizar el atractor en 3D',
                'Probar diferentes condiciones iniciales',
                'Observar la sensibilidad al caos'
            ]
        }
    
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
            'parametros': {'x0': r0, 'y0': 0.0, 'vx0': 0.0, 'vy0': v0, 'mu': GM},
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
            'parametros': {'x0': r1, 'y0': 0.0, 'vx0': 0.0, 'vy0': 1.0/np.sqrt(r1), 'mu': 1.0},
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
            'parametros': {'x0': r0, 'y0': 0.0, 'vx0': delta_v, 'vy0': v_circ, 'mu': 1.0},
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
