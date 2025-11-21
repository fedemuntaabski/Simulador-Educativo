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
            'amortiguador': self._generar_amortiguador
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
