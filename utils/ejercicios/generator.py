"""
Generador principal de ejercicios educativos.
Versión modularizada siguiendo DRY y KISS.
"""

import random
import numpy as np

from .base import EjercicioBase
from .preguntas import PreguntasPool


class EjercicioGenerator(EjercicioBase):
    """
    Genera ejercicios automáticos con parámetros aleatorios,
    preguntas teóricas y objetivos de aprendizaje.
    """
    
    # Mapeo de sistemas a simuladores
    SISTEMAS_DISPONIBLES = [
        'newton', 'van_der_pol', 'sir', 'rlc', 'lorenz', 
        'hopf', 'logistico', 'verhulst', 'orbital', 
        'mariposa', 'amortiguador'
    ]
    
    def __init__(self):
        """Inicializa el generador de ejercicios."""
        self.ejercicio_actual = None
        self.respuestas_esperadas = {}
    
    def generar_ejercicio(self, sistema, dificultad='intermedio'):
        """
        Genera un ejercicio completo para un sistema dinámico.
        
        Args:
            sistema: Nombre del sistema
            dificultad: 'principiante', 'intermedio', 'avanzado'
            
        Returns:
            dict con el ejercicio completo
        """
        generadores = {
            'newton': self._gen_newton,
            'van_der_pol': self._gen_van_der_pol,
            'sir': self._gen_sir,
            'rlc': self._gen_rlc,
            'lorenz': self._gen_lorenz,
            'hopf': self._gen_hopf,
            'logistico': self._gen_logistico,
            'verhulst': self._gen_verhulst,
            'orbital': self._gen_orbital,
            'mariposa': self._gen_mariposa,
            'amortiguador': self._gen_amortiguador,
        }
        
        if sistema not in generadores:
            raise ValueError(f"Sistema '{sistema}' no soportado. Disponibles: {list(generadores.keys())}")
        
        ejercicio = generadores[sistema](dificultad)
        self.ejercicio_actual = ejercicio
        return ejercicio
    
    def _gen_newton(self, dificultad):
        """Genera ejercicio de enfriamiento de Newton."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Parámetros según nivel
        config = {
            1: {'T0': self.opcion([100, 90, 80]), 'T_env': self.opcion([20, 25]), 'k': self.rango(0.05, 0.15)},
            2: {'T0': self.entero(70, 120), 'T_env': self.entero(15, 30), 'k': self.rango(0.08, 0.25, 3)},
            3: {'T0': self.entero(60, 150), 'T_env': self.entero(10, 35), 'k': self.rango(0.05, 0.4, 3)}
        }
        params = self.param_aleatorio(nivel, config)
        T0, T_env, k = params['T0'], params['T_env'], params['k']
        
        # Cálculos auxiliares
        T_objetivo = T_env + (T0 - T_env) * 0.37
        t_esperado = -np.log((T_objetivo - T_env) / (T0 - T_env)) / k
        tau = 1 / k
        t_50 = tau * np.log(2)
        T_t2 = T_env + (T0 - T_env) * np.exp(-k * 2 * tau)
        
        # Obtener preguntas
        pools = PreguntasPool.newton(T0, T_env, k, tau, t_esperado, t_50, T_t2)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        return self.construir_ejercicio(
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
    
    def _gen_van_der_pol(self, dificultad):
        """Genera ejercicio del oscilador Van der Pol."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'mu': self.opcion([0.5, 1.0, 1.5]), 'x0': 1.0, 'v0': 0.0},
            2: {'mu': self.rango(0.5, 3.0, 1), 'x0': self.rango(-2, 2, 1), 'v0': self.rango(-1, 1, 1)},
            3: {'mu': self.rango(0.2, 8.0), 'x0': self.rango(-3, 3, 1), 'v0': self.rango(-2, 2, 1)}
        }
        params = self.param_aleatorio(nivel, config)
        mu, x0, v0 = params['mu'], params['x0'], params['v0']
        
        pools = PreguntasPool.van_der_pol(mu)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        return self.construir_ejercicio(
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
                'Comparar trayectorias desde diferentes condiciones iniciales'
            ]
        )
    
    def _gen_sir(self, dificultad):
        """Genera ejercicio del modelo SIR."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'S0': 990, 'I0': 10, 'R0': 0, 'beta': 0.3, 'gamma': 0.1},
            2: lambda: {
                'S0': self.entero(900, 990), 'I0': 1000 - self.entero(900, 990), 'R0': 0,
                'beta': self.rango(0.2, 0.5), 'gamma': self.rango(0.05, 0.2)
            },
            3: lambda: {
                'S0': self.entero(800, 990), 'I0': self.entero(5, 50), 
                'R0': 1000 - self.entero(800, 990) - self.entero(5, 50),
                'beta': self.rango(0.15, 0.7), 'gamma': self.rango(0.05, 0.3)
            }
        }
        params = self.param_aleatorio(nivel, config)
        S0, I0, R0 = params['S0'], params['I0'], params['R0']
        beta, gamma = params['beta'], params['gamma']
        
        R0_basico = beta / gamma
        herd_immunity = 1 - 1/R0_basico if R0_basico > 1 else 0
        
        pools = PreguntasPool.sir(beta, gamma, R0_basico, herd_immunity)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        return self.construir_ejercicio(
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
                '5. Observe la evolución de las poblaciones'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar las tres poblaciones S(t), I(t), R(t)',
                'Calcular R₀ = β/γ',
                'Determinar el día del pico de infectados'
            ]
        )
    
    def _gen_hopf(self, dificultad):
        """Genera ejercicio de bifurcación de Hopf."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'mu': self.opcion([-0.5, 0.0, 0.5, 1.0])},
            2: {'mu': self.rango(-1.0, 2.0, 1)},
            3: {'mu': self.rango(-2.0, 3.0)}
        }
        params = self.param_aleatorio(nivel, config)
        mu = params['mu']
        
        radio_ciclo = np.sqrt(mu) if mu > 0 else 0
        
        pools = PreguntasPool.hopf(mu, radio_ciclo)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        return self.construir_ejercicio(
            sistema='hopf',
            titulo='Bifurcación de Hopf',
            dificultad=dificultad,
            parametros={'mu': mu, 'x0': 0.1, 'y0': 0.1, 'omega': 1.0},
            objetivos=[
                'Comprender la bifurcación de Hopf',
                'Identificar el valor crítico del parámetro',
                'Observar la transición de punto fijo a ciclo límite'
            ],
            instrucciones=[
                f'1. Configure μ = {mu}',
                f'2. Radio esperado del ciclo (si μ > 0): √μ = {radio_ciclo:.3f}',
                '3. Observe el comportamiento del sistema',
                '4. Identifique el punto de bifurcación en μ = 0'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar el diagrama de fase (x vs y)',
                'Variar μ y observar la transición',
                'Verificar que radio ∝ √μ'
            ]
        )
    
    def _gen_logistico(self, dificultad):
        """Genera ejercicio del modelo logístico."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'N0': self.opcion([10, 20, 50]), 'K': 1000, 'r': self.opcion([0.1, 0.2, 0.3])},
            2: {'N0': self.entero(10, 100), 'K': self.entero(500, 1500), 'r': self.rango(0.1, 0.5)},
            3: {'N0': self.entero(5, 200), 'K': self.entero(300, 2000), 'r': self.rango(0.05, 0.8, 3)}
        }
        params = self.param_aleatorio(nivel, config)
        N0, r, K = params['N0'], params['r'], params['K']
        
        t_inflexion = np.log((K - N0) / N0) / r if N0 < K else 0
        t_duplicacion = np.log(2) / r
        
        pools = PreguntasPool.logistico(K, t_inflexion, t_duplicacion)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        return self.construir_ejercicio(
            sistema='logistico',
            titulo='Modelo Logístico de Crecimiento',
            dificultad=dificultad,
            parametros={'N0': N0, 'r': r, 'K': K},
            objetivos=[
                'Comprender el crecimiento logístico',
                'Identificar la capacidad de carga',
                'Analizar el efecto de la tasa de crecimiento'
            ],
            instrucciones=[
                f'1. Configure N(0) = {N0}',
                f'2. Configure r = {r}, K = {K}',
                f'3. Punto de inflexión esperado en N = K/2 = {K/2}',
                '4. Ejecute la simulación'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar N(t) vs t',
                'Identificar la capacidad de carga K',
                'Calcular el punto de inflexión'
            ]
        )
    
    def _gen_verhulst(self, dificultad):
        """Genera ejercicio del mapa de Verhulst (logístico discreto)."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'r': self.opcion([2.5, 2.8, 3.2, 3.5])},
            2: {'r': self.rango(2.0, 3.8, 1)},
            3: {'r': self.rango(1.5, 4.0)}
        }
        params = self.param_aleatorio(nivel, config)
        r = params['r']
        
        x_eq = 1 - 1/r if r > 1 else 0
        
        # Preguntas simplificadas
        preguntas = [
            {
                'id': 1,
                'texto': f'¿Para r = {r}, el sistema converge a un punto fijo?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí (r < 3)', 'No, oscila o es caótico'],
                'respuesta_correcta': 0 if r < 3.0 else 1
            },
            {
                'id': 2,
                'texto': '¿En qué valor de r aparece la primera bifurcación?',
                'tipo': 'numerica',
                'respuesta_esperada': 3.0,
                'tolerancia': 0.2,
                'unidad': ''
            },
            {
                'id': 3,
                'texto': '¿A partir de qué r comienza el caos?',
                'tipo': 'numerica',
                'respuesta_esperada': 3.57,
                'tolerancia': 0.1,
                'unidad': ''
            }
        ]
        
        return self.construir_ejercicio(
            sistema='verhulst',
            titulo='Mapa Logístico de Verhulst',
            dificultad=dificultad,
            parametros={'x0': 0.5, 'r': r},
            objetivos=[
                'Observar bifurcaciones en sistemas discretos',
                'Comprender el camino al caos',
                'Analizar el diagrama de bifurcación'
            ],
            instrucciones=[
                f'1. Configure r = {r}',
                f'2. Punto fijo teórico: x* = 1 - 1/r = {x_eq:.4f}',
                '3. Ejecute la simulación',
                '4. Referencia: caos comienza en r ≈ 3.57'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar la serie temporal',
                'Identificar regiones periódicas y caóticas'
            ]
        )
    
    def _gen_orbital(self, dificultad):
        """Genera ejercicio de órbitas espaciales."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'x0': 1.0, 'y0': 0.0, 'vx0': 0.0, 'vy0': 1.0, 'tipo': 'circular'},
            2: lambda: {'x0': 1.0, 'y0': 0.0, 'vx0': 0.0, 'vy0': self.rango(0.7, 1.3), 'tipo': 'elíptica'},
            3: lambda: {'x0': self.rango(0.5, 2.0), 'y0': 0.0, 'vx0': 0.0, 'vy0': self.rango(0.5, 1.5), 'tipo': 'variada'}
        }
        params = self.param_aleatorio(nivel, config)
        x0, y0, vx0, vy0 = params['x0'], params['y0'], params['vx0'], params['vy0']
        
        # Calcular energía
        r0 = np.sqrt(x0**2 + y0**2)
        v0 = np.sqrt(vx0**2 + vy0**2)
        E = 0.5 * v0**2 - 1.0/r0
        
        preguntas = [
            {
                'id': 1,
                'texto': '¿La energía total del sistema se conserva?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No'],
                'respuesta_correcta': 0
            },
            {
                'id': 2,
                'texto': '¿El momento angular se conserva?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí (fuerza central)', 'No'],
                'respuesta_correcta': 0
            },
            {
                'id': 3,
                'texto': '¿Qué relación cumple T con a? (3ª Ley Kepler)',
                'tipo': 'opcion_multiple',
                'opciones': ['T ∝ a', 'T² ∝ a³', 'T³ ∝ a²'],
                'respuesta_correcta': 1
            }
        ]
        
        return self.construir_ejercicio(
            sistema='orbital',
            titulo='Órbitas Espaciales (Problema de Kepler)',
            dificultad=dificultad,
            parametros={'x0': x0, 'y0': y0, 'vx0': vx0, 'vy0': vy0, 'GM': 1.0},
            objetivos=[
                'Comprender las leyes de Kepler',
                'Analizar órbitas circulares y elípticas',
                'Verificar conservación de energía y momento angular'
            ],
            instrucciones=[
                f'1. Posición inicial: ({x0}, {y0})',
                f'2. Velocidad inicial: ({vx0}, {vy0})',
                f'3. Energía calculada: E = {E:.4f}',
                '4. Ejecute la simulación'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar la trayectoria orbital',
                'Verificar las leyes de Kepler'
            ]
        )
    
    def _gen_mariposa(self, dificultad):
        """Genera ejercicio del atractor de Rössler."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'a': 0.2, 'b': 0.2, 'c': 5.7},
            2: {'a': 0.2, 'b': 0.2, 'c': self.rango(4.0, 6.5, 1)},
            3: {'a': self.rango(0.1, 0.3), 'b': self.rango(0.1, 0.4), 'c': self.rango(3.0, 8.0, 1)}
        }
        params = self.param_aleatorio(nivel, config)
        a, b, c = params['a'], params['b'], params['c']
        
        preguntas = [
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
        ]
        
        return self.construir_ejercicio(
            sistema='mariposa',
            titulo='Atractor de Rössler (Mariposa)',
            dificultad=dificultad,
            parametros={'x0': 1.0, 'y0': 1.0, 'z0': 1.0, 'a': a, 'b': b, 'c': c},
            objetivos=[
                'Observar un atractor caótico',
                'Comparar con el atractor de Lorenz',
                'Analizar la estructura del atractor'
            ],
            instrucciones=[
                f'1. Configure a = {a}, b = {b}, c = {c}',
                '2. Ejecute la simulación',
                '3. Observe el atractor en 3D'
            ],
            preguntas=preguntas,
            analisis=[
                'Visualizar el atractor en 3D',
                'Comparar con Lorenz'
            ]
        )
    
    def _gen_amortiguador(self, dificultad):
        """Genera ejercicio de sistema masa-resorte-amortiguador."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'m': 1.0, 'k': 1.0, 'c': self.opcion([0.2, 1.0, 2.0])},
            2: {'m': 1.0, 'k': 4.0, 'c': self.rango(0.5, 6.0, 1)},
            3: {'m': self.rango(0.5, 2.0, 1), 'k': self.rango(1.0, 10.0, 1), 'c': self.rango(0.1, 8.0)}
        }
        params = self.param_aleatorio(nivel, config)
        m, c, k = params['m'], params['c'], params['k']
        
        c_crit = 2 * np.sqrt(k * m)
        zeta = c / c_crit
        
        tipo_idx = 0 if zeta < 0.95 else (1 if zeta < 1.05 else 2)
        tipo = ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'][tipo_idx]
        
        preguntas = [
            {
                'id': 1,
                'texto': '¿Qué tipo de amortiguamiento presenta el sistema?',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado (oscila)', 'Críticamente amortiguado', 'Sobreamortiguado (no oscila)'],
                'respuesta_correcta': tipo_idx
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
                'texto': '¿El sistema oscila con amplitud decreciente?',
                'tipo': 'opcion_multiple',
                'opciones': ['Sí', 'No'],
                'respuesta_correcta': 0 if zeta < 1 else 1
            }
        ]
        
        return self.construir_ejercicio(
            sistema='amortiguador',
            titulo='Sistema Masa-Resorte-Amortiguador',
            dificultad=dificultad,
            parametros={'m': m, 'c': c, 'k': k, 'x0': 1.0, 'v0': 0.0, 'F0': 0.0, 'omega_f': 0.0},
            objetivos=[
                'Comprender los tipos de amortiguamiento',
                'Calcular el factor de amortiguamiento ζ',
                'Analizar la respuesta del sistema'
            ],
            instrucciones=[
                f'1. Configure m = {m} kg, c = {c} Ns/m, k = {k} N/m',
                f'2. Amortiguamiento crítico: c_crit = {c_crit:.3f}',
                f'3. Factor ζ = {zeta:.3f} → {tipo}',
                '4. Ejecute la simulación'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar x(t) y v(t)',
                'Determinar el tipo de amortiguamiento'
            ]
        )
    
    def _gen_rlc(self, dificultad):
        """Genera ejercicio de circuito RLC."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'R': 10.0, 'L': 0.1, 'C': 0.001, 'V0': 10.0},
            2: {'R': float(self.entero(5, 50)), 'L': self.rango(0.05, 0.5), 'C': self.rango(0.0005, 0.005, 4), 'V0': float(self.entero(5, 20))},
            3: {'R': float(self.entero(1, 100)), 'L': self.rango(0.01, 1.0), 'C': self.rango(0.0001, 0.01, 4), 'V0': float(self.entero(1, 50))}
        }
        params = self.param_aleatorio(nivel, config)
        R, L, C, V0 = params['R'], params['L'], params['C'], params['V0']
        
        omega_0 = 1 / np.sqrt(L * C)
        Q = omega_0 * L / R
        zeta = R / (2 * np.sqrt(L / C))
        
        tipo_idx = 0 if zeta < 0.95 else (1 if zeta < 1.05 else 2)
        
        preguntas = [
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
                'texto': '¿El circuito está sub, crítico o sobreamortiguado?',
                'tipo': 'opcion_multiple',
                'opciones': ['Subamortiguado (oscila)', 'Críticamente amortiguado', 'Sobreamortiguado'],
                'respuesta_correcta': tipo_idx
            },
            {
                'id': 3,
                'texto': f'¿Cuál es el factor de calidad Q aproximado?',
                'tipo': 'numerica',
                'respuesta_esperada': Q,
                'tolerancia': Q * 0.15,
                'unidad': ''
            }
        ]
        
        return self.construir_ejercicio(
            sistema='rlc',
            titulo='Circuito RLC Serie',
            dificultad=dificultad,
            parametros={'R': R, 'L': L, 'C': C, 'V0': V0, 'I0': 0.0, 'Q0': 0.0},
            objetivos=[
                'Comprender circuitos RLC',
                'Analizar oscilaciones eléctricas',
                'Calcular la frecuencia de resonancia'
            ],
            instrucciones=[
                f'1. Configure R = {R}Ω, L = {L}H, C = {C}F',
                f'2. Frecuencia natural: ω₀ = {omega_0:.2f} rad/s',
                f'3. Factor Q = {Q:.2f}',
                '4. Ejecute la simulación'
            ],
            preguntas=preguntas,
            analisis=[
                'Graficar I(t) y V_C(t)',
                'Clasificar el tipo de amortiguamiento'
            ]
        )
    
    def _gen_lorenz(self, dificultad):
        """Genera ejercicio del sistema de Lorenz."""
        nivel = self.DIFICULTAD[dificultad]
        
        config = {
            1: {'sigma': 10.0, 'rho': 28.0, 'beta': 8/3},
            2: {'sigma': 10.0, 'rho': self.rango(20.0, 35.0, 1), 'beta': 8/3},
            3: {'sigma': self.rango(8.0, 15.0, 1), 'rho': self.rango(15.0, 40.0, 1), 'beta': self.rango(2.0, 3.5)}
        }
        params = self.param_aleatorio(nivel, config)
        sigma, rho, beta = params['sigma'], params['rho'], params['beta']
        
        es_caotico = rho > 24.74
        
        pools = PreguntasPool.lorenz(rho, es_caotico)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        return self.construir_ejercicio(
            sistema='lorenz',
            titulo='Sistema de Lorenz (Atractor Caótico)',
            dificultad=dificultad,
            parametros={'x0': 1.0, 'y0': 1.0, 'z0': 1.0, 'sigma': sigma, 'rho': rho, 'beta': beta},
            objetivos=[
                'Observar comportamiento caótico determinista',
                'Comprender la teoría del caos',
                'Analizar el atractor extraño'
            ],
            instrucciones=[
                f'1. Configure σ = {sigma}, ρ = {rho}, β = {beta:.2f}',
                f'2. Valor crítico de ρ para caos: ~24.74',
                '3. Ejecute la simulación',
                '4. Observe el atractor en 3D'
            ],
            preguntas=preguntas,
            analisis=[
                'Visualizar el atractor en espacio 3D',
                'Identificar los dos lóbulos del atractor'
            ]
        )
