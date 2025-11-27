"""
Generador principal de ejercicios educativos.
Versión modularizada siguiendo DRY y KISS.
Incluye consignas contextualizadas y escenarios realistas.
"""

import random
import numpy as np

from .base import EjercicioBase
from .preguntas import PreguntasPool


class EjercicioGenerator(EjercicioBase):
    """
    Genera ejercicios automáticos con parámetros aleatorios,
    preguntas teóricas y objetivos de aprendizaje.
    Incluye contextos realistas y consignas detalladas.
    """
    
    # Mapeo de sistemas a simuladores
    SISTEMAS_DISPONIBLES = [
        'newton', 'van_der_pol', 'sir', 'rlc', 'lorenz', 
        'hopf', 'logistico', 'verhulst', 'orbital', 
        'mariposa', 'amortiguador'
    ]
    
    # Contextos realistas para cada sistema
    CONTEXTOS = {
        'newton': [
            {'objeto': 'taza de café', 'lugar': 'una oficina', 'T_tipica': (85, 95), 'T_amb_tipica': (20, 25)},
            {'objeto': 'sopa caliente', 'lugar': 'un restaurante', 'T_tipica': (75, 90), 'T_amb_tipica': (22, 26)},
            {'objeto': 'pieza de metal fundido', 'lugar': 'una fundición', 'T_tipica': (200, 400), 'T_amb_tipica': (25, 35)},
            {'objeto': 'termómetro clínico', 'lugar': 'un consultorio médico', 'T_tipica': (37, 40), 'T_amb_tipica': (20, 24)},
            {'objeto': 'pastel recién horneado', 'lugar': 'una panadería', 'T_tipica': (150, 180), 'T_amb_tipica': (22, 28)},
            {'objeto': 'componente electrónico', 'lugar': 'un laboratorio', 'T_tipica': (60, 85), 'T_amb_tipica': (18, 22)},
            {'objeto': 'vaso de leche caliente', 'lugar': 'una cocina', 'T_tipica': (65, 80), 'T_amb_tipica': (20, 25)},
        ],
        'sir': [
            {'enfermedad': 'gripe estacional', 'poblacion': 'una ciudad pequeña', 'N': 10000},
            {'enfermedad': 'COVID-19', 'poblacion': 'un campus universitario', 'N': 5000},
            {'enfermedad': 'sarampión', 'poblacion': 'una comunidad rural', 'N': 2000},
            {'enfermedad': 'varicela', 'poblacion': 'una escuela primaria', 'N': 500},
            {'enfermedad': 'influenza tipo A', 'poblacion': 'un crucero', 'N': 3000},
            {'enfermedad': 'resfriado común', 'poblacion': 'una empresa', 'N': 1000},
        ],
        'rlc': [
            {'aplicacion': 'filtro de radio AM', 'frecuencia': '530-1700 kHz'},
            {'aplicacion': 'sintonizador de TV', 'frecuencia': 'VHF/UHF'},
            {'aplicacion': 'fuente de alimentación', 'frecuencia': '50-60 Hz'},
            {'aplicacion': 'circuito de temporización', 'frecuencia': 'variable'},
            {'aplicacion': 'detector de metales', 'frecuencia': 'audio'},
        ],
        'van_der_pol': [
            {'aplicacion': 'oscilador de tubo de vacío', 'uso': 'radio transmisores antiguos'},
            {'aplicacion': 'marcapasos cardíaco', 'uso': 'regulación del ritmo cardíaco'},
            {'aplicacion': 'generador de señales', 'uso': 'instrumentación electrónica'},
            {'aplicacion': 'modelo neuronal', 'uso': 'neurociencia computacional'},
        ],
        'lorenz': [
            {'aplicacion': 'predicción meteorológica', 'fenomeno': 'convección atmosférica'},
            {'aplicacion': 'criptografía caótica', 'fenomeno': 'generación de claves'},
            {'aplicacion': 'dinámica de fluidos', 'fenomeno': 'células de convección'},
        ],
        'logistico': [
            {'poblacion': 'bacterias en un cultivo', 'recurso': 'nutrientes del medio'},
            {'poblacion': 'peces en un lago', 'recurso': 'alimento y espacio'},
            {'poblacion': 'árboles en un bosque', 'recurso': 'luz y agua'},
            {'poblacion': 'usuarios de una red social', 'recurso': 'atención del mercado'},
            {'poblacion': 'células tumorales', 'recurso': 'oxígeno y nutrientes'},
        ],
        'amortiguador': [
            {'sistema': 'suspensión de automóvil', 'proposito': 'absorber impactos del camino'},
            {'sistema': 'puerta automática', 'proposito': 'cierre suave sin golpes'},
            {'sistema': 'sismógrafo', 'proposito': 'registrar vibraciones del suelo'},
            {'sistema': 'edificio antisísmico', 'proposito': 'reducir oscilaciones'},
        ],
        'orbital': [
            {'mision': 'satélite de comunicaciones', 'destino': 'órbita geoestacionaria'},
            {'mision': 'estación espacial', 'destino': 'órbita baja terrestre'},
            {'mision': 'sonda interplanetaria', 'destino': 'Marte'},
            {'mision': 'telescopio espacial', 'destino': 'punto de Lagrange L2'},
        ],
    }
    
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
        
        # Mapeo de ejercicios avanzados a generadores base
        ejercicios_avanzados = {
            'equilibrio_logistico': ('logistico', 'avanzado'),
            'verhulst_transiciones': ('verhulst', 'avanzado'),
            'amortiguamiento_analisis': ('amortiguador', 'avanzado'),
            'ciclo_limite': ('van_der_pol', 'avanzado'),
            'hopf_aparicion': ('hopf', 'avanzado'),
            'rlc_resonancia': ('rlc', 'avanzado'),
            'sir_propagacion': ('sir', 'intermedio'),
            'lorenz_sensibilidad': ('lorenz', 'avanzado'),
            'orbital_kepler': ('orbital', 'intermedio'),
            'orbital_hohmann': ('orbital', 'avanzado'),
            'newton_enfriamiento': ('newton', 'intermedio'),
            'rc_carga': ('rlc', 'principiante'),
            'crecimiento_comparacion': ('logistico', 'intermedio'),
            'estabilidad_lineal': ('hopf', 'intermedio'),
            'sir_vacunacion': ('sir', 'avanzado'),
            'orbital_perturbaciones': ('orbital', 'avanzado'),
            'oscilador_forzado': ('amortiguador', 'avanzado'),
        }
        
        # Si es un ejercicio avanzado, usar el generador base correspondiente
        if sistema in ejercicios_avanzados:
            sistema_base, dificultad_forzada = ejercicios_avanzados[sistema]
            ejercicio = generadores[sistema_base](dificultad_forzada)
            # Personalizar el título según el ejercicio avanzado
            titulos_avanzados = {
                'equilibrio_logistico': 'Análisis de Equilibrio Poblacional',
                'verhulst_transiciones': 'Transiciones y Bifurcaciones en el Mapa de Verhulst',
                'amortiguamiento_analisis': 'Análisis Completo de Amortiguamiento',
                'ciclo_limite': 'Estudio de Ciclos Límite',
                'hopf_aparicion': 'Aparición de Bifurcaciones de Hopf',
                'rlc_resonancia': 'Resonancia en Circuitos RLC',
                'sir_propagacion': 'Dinámica de Propagación Epidémica',
                'lorenz_sensibilidad': 'Sensibilidad a Condiciones Iniciales (Caos)',
                'orbital_kepler': 'Verificación de las Leyes de Kepler',
                'orbital_hohmann': 'Transferencia Orbital de Hohmann',
                'newton_enfriamiento': 'Aplicaciones del Enfriamiento de Newton',
                'rc_carga': 'Carga y Descarga de Capacitor',
                'crecimiento_comparacion': 'Comparación de Modelos de Crecimiento',
                'estabilidad_lineal': 'Análisis de Estabilidad Lineal',
                'sir_vacunacion': 'Efectos de la Vacunación en Epidemias',
                'orbital_perturbaciones': 'Perturbaciones en Órbitas',
                'oscilador_forzado': 'Oscilador Armónico Forzado',
            }
            ejercicio['titulo'] = titulos_avanzados.get(sistema, ejercicio['titulo'])
            self.ejercicio_actual = ejercicio
            return ejercicio
        
        if sistema not in generadores:
            raise ValueError(f"Sistema '{sistema}' no soportado. Disponibles: {list(generadores.keys())}")
        
        ejercicio = generadores[sistema](dificultad)
        self.ejercicio_actual = ejercicio
        return ejercicio
    
    def _gen_newton(self, dificultad):
        """Genera ejercicio de enfriamiento de Newton con contexto realista."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['newton'])
        
        # Parámetros según nivel con mayor variabilidad
        if nivel == 1:
            T0 = self.entero(contexto['T_tipica'][0], contexto['T_tipica'][1])
            T_env = self.entero(contexto['T_amb_tipica'][0], contexto['T_amb_tipica'][1])
            k = self.rango(0.05, 0.15, 3)
        elif nivel == 2:
            T0 = self.entero(60, 150)
            T_env = self.entero(15, 30)
            k = self.rango(0.08, 0.30, 3)
        else:  # avanzado
            T0 = self.entero(50, 300)
            T_env = self.entero(10, 40)
            k = self.rango(0.05, 0.50, 3)
        
        # Cálculos auxiliares
        T_objetivo = T_env + (T0 - T_env) * 0.37
        t_esperado = -np.log((T_objetivo - T_env) / (T0 - T_env)) / k
        tau = 1 / k
        t_50 = tau * np.log(2)
        T_t2 = T_env + (T0 - T_env) * np.exp(-k * 2 * tau)
        
        # Tiempo específico para preguntas
        t_pregunta = self.entero(5, 20)
        T_en_t = T_env + (T0 - T_env) * np.exp(-k * t_pregunta)
        
        # Temperatura objetivo específica
        T_deseada = T_env + (T0 - T_env) * self.rango(0.2, 0.5, 2)
        t_para_T_deseada = -np.log((T_deseada - T_env) / (T0 - T_env)) / k
        
        # Obtener preguntas
        pools = PreguntasPool.newton(T0, T_env, k, tau, t_esperado, t_50, T_t2)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        # Construir consigna contextualizada
        consigna = self._construir_consigna_newton(contexto, T0, T_env, k, tau, t_pregunta, T_en_t, T_deseada, t_para_T_deseada, nivel)
        
        return self.construir_ejercicio(
            sistema='newton',
            titulo='Ley de Enfriamiento de Newton',
            dificultad=dificultad,
            parametros={'T0': T0, 'T_env': T_env, 'k': k},
            objetivos=[
                'Comprender el proceso de enfriamiento exponencial',
                'Analizar la influencia de la constante de enfriamiento k',
                'Predecir temperaturas en instantes específicos',
                'Calcular tiempos necesarios para alcanzar temperaturas objetivo',
                'Interpretar la constante de tiempo τ = 1/k'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _construir_consigna_newton(self, contexto, T0, T_env, k, tau, t_pregunta, T_en_t, T_deseada, t_para_T_deseada, nivel):
        """Construye la consigna contextualizada para Newton."""
        objeto = contexto['objeto']
        lugar = contexto['lugar']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"              ENFRIAMIENTO DE NEWTON - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 SITUACIÓN:",
            f"   Un/a {objeto} se encuentra en {lugar}.",
            "",
            f"📊 DATOS:",
            f"   • Temperatura inicial (T₀): {T0}°C",
            f"   • Temperatura ambiente (T_amb): {T_env}°C",
            f"   • Constante de enfriamiento (k): {k} min⁻¹",
            "",
            f"📐 MODELO MATEMÁTICO:",
            f"   La ley de enfriamiento de Newton establece:",
            f"   dT/dt = -k(T - T_amb)",
            "",
            f"🎯 SE PIDE:",
            f"   a) Determinar la constante de tiempo τ del sistema.",
            f"   b) Calcular la temperatura del objeto en t = {t_pregunta} minutos.",
            f"   c) Calcular cuánto tiempo tardará en alcanzar {T_deseada:.1f}°C.",
            f"   d) Determinar la temperatura de equilibrio del sistema.",
            f"   e) Analizar cómo afecta el valor de k a la velocidad de enfriamiento.",
            "",
            f"💡 SUGERENCIA: Utiliza el simulador para verificar tus cálculos.",
        ]
        
        datos = {
            't_pregunta': t_pregunta,
            'T_deseada': round(T_deseada, 1),
        }
        
        analisis = [
            'Graficar T(t) vs t y verificar el decaimiento exponencial',
            'Identificar gráficamente la constante de tiempo τ',
            'Comparar la simulación con la solución analítica',
            'Analizar qué sucede cuando t → ∞'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_van_der_pol(self, dificultad):
        """Genera ejercicio del oscilador Van der Pol con contexto realista."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['van_der_pol'])
        
        # Parámetros según nivel con mayor variabilidad
        if nivel == 1:
            mu = self.opcion([0.5, 1.0, 1.5, 2.0])
            x0 = self.rango(0.5, 2.0, 1)
            v0 = 0.0
        elif nivel == 2:
            mu = self.rango(0.5, 4.0, 2)
            x0 = self.rango(-2, 2, 1)
            v0 = self.rango(-1, 1, 1)
        else:  # avanzado
            mu = self.rango(0.2, 10.0, 2)
            x0 = self.rango(-3, 3, 1)
            v0 = self.rango(-2, 2, 1)
        
        # Determinar tipo de oscilación
        tipo_oscilacion = 'casi sinusoidal' if mu < 1.5 else ('transición' if mu < 3 else 'relajación')
        
        # Período aproximado (fórmula asintótica para μ grande)
        if mu > 2:
            T_aprox = (3 - 2*np.log(2)) * mu
        else:
            T_aprox = 2 * np.pi  # Aproximación para μ pequeño
        
        pools = PreguntasPool.van_der_pol(mu)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        # Construir consigna contextualizada
        consigna = self._construir_consigna_vdp(contexto, mu, x0, v0, tipo_oscilacion, T_aprox, nivel)
        
        return self.construir_ejercicio(
            sistema='van_der_pol',
            titulo='Oscilador de Van der Pol',
            dificultad=dificultad,
            parametros={'mu': mu, 'x0': x0, 'v0': v0},
            objetivos=[
                'Observar el comportamiento de ciclos límite',
                'Analizar el efecto del parámetro de no linealidad μ',
                'Estudiar el diagrama de fase (espacio x-ẋ)',
                'Comprender oscilaciones de relajación vs sinusoidales',
                'Verificar la independencia del ciclo límite respecto a condiciones iniciales'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _construir_consigna_vdp(self, contexto, mu, x0, v0, tipo_oscilacion, T_aprox, nivel):
        """Construye la consigna contextualizada para Van der Pol."""
        aplicacion = contexto['aplicacion']
        uso = contexto['uso']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"              OSCILADOR DE VAN DER POL - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 CONTEXTO:",
            f"   El oscilador de Van der Pol modela un {aplicacion},",
            f"   utilizado en {uso}.",
            "",
            f"📊 DATOS:",
            f"   • Parámetro de no linealidad (μ): {mu}",
            f"   • Posición inicial x(0): {x0}",
            f"   • Velocidad inicial ẋ(0): {v0}",
            "",
            f"📐 ECUACIÓN DE VAN DER POL:",
            f"   ẍ - μ(1 - x²)ẋ + x = 0",
            "",
            f"🎯 SE PIDE:",
            f"   a) Analizar el término -μ(1-x²)ẋ y explicar su efecto sobre",
            f"      la energía del sistema para |x| < 1 y |x| > 1.",
            f"   b) Determinar si existe un ciclo límite para μ = {mu}.",
            f"   c) Clasificar el tipo de oscilación (sinusoidal o de relajación).",
            f"   d) Medir el período aproximado de las oscilaciones.",
            f"   e) Verificar si el ciclo límite es independiente de las",
            f"      condiciones iniciales probando con valores diferentes.",
            "",
            f"💡 EXPERIMENTO: Prueba con x(0) = 0.1 y x(0) = 5 para verificar",
            f"   la convergencia al ciclo límite.",
        ]
        
        datos = {
            'mu': mu,
        }
        
        analisis = [
            'Graficar el diagrama de fase (x vs ẋ) e identificar el ciclo límite',
            'Graficar x(t) y caracterizar el tipo de oscilación',
            'Medir el período de las oscilaciones',
            'Observar la transición de oscilaciones sinusoidales a relajación'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_sir(self, dificultad):
        """Genera ejercicio del modelo SIR con contexto epidemiológico realista."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['sir'])
        N = contexto['N']
        
        # Parámetros según nivel con mayor variabilidad
        if nivel == 1:
            I0 = self.entero(5, 20)
            S0 = N - I0
            R0_val = 0
            beta = self.rango(0.25, 0.40, 3)
            gamma = self.rango(0.08, 0.12, 3)
        elif nivel == 2:
            I0 = self.entero(10, 50)
            R0_val = self.entero(0, 20)
            S0 = N - I0 - R0_val
            beta = self.rango(0.20, 0.50, 3)
            gamma = self.rango(0.05, 0.20, 3)
        else:  # avanzado
            I0 = self.entero(5, 100)
            R0_val = self.entero(0, int(N * 0.1))
            S0 = N - I0 - R0_val
            beta = self.rango(0.15, 0.70, 3)
            gamma = self.rango(0.04, 0.30, 3)
        
        # Cálculos epidemiológicos
        R0_basico = beta / gamma
        herd_immunity = 1 - 1/R0_basico if R0_basico > 1 else 0
        duracion_infeccion = 1 / gamma
        
        # Umbral epidémico
        S_umbral = gamma / beta * N
        habra_epidemia = S0 > S_umbral
        
        # Pico de infectados (aproximación)
        if habra_epidemia and R0_basico > 1:
            I_max_aprox = N * (1 - (1 + np.log(R0_basico)) / R0_basico)
        else:
            I_max_aprox = I0
        
        pools = PreguntasPool.sir(beta, gamma, R0_basico, herd_immunity)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        # Construir consigna contextualizada
        consigna = self._construir_consigna_sir(contexto, S0, I0, R0_val, beta, gamma, 
                                                 R0_basico, herd_immunity, duracion_infeccion,
                                                 habra_epidemia, I_max_aprox, nivel)
        
        return self.construir_ejercicio(
            sistema='sir',
            titulo='Modelo Epidemiológico SIR',
            dificultad=dificultad,
            parametros={'S0': S0, 'I0': I0, 'R0': R0_val, 'beta': beta, 'gamma': gamma, 'N': N},
            objetivos=[
                'Comprender la dinámica de propagación de epidemias',
                'Calcular e interpretar el número reproductivo básico R₀',
                'Predecir si ocurrirá un brote epidémico',
                'Estimar el pico de infectados y cuándo ocurre',
                'Calcular el umbral de inmunidad de rebaño'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _construir_consigna_sir(self, contexto, S0, I0, R0_val, beta, gamma, R0_basico, 
                                 herd_immunity, duracion_infeccion, habra_epidemia, I_max_aprox, nivel):
        """Construye la consigna contextualizada para SIR."""
        enfermedad = contexto['enfermedad']
        poblacion = contexto['poblacion']
        N = contexto['N']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"              MODELO EPIDEMIOLÓGICO SIR - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 SITUACIÓN:",
            f"   Se ha detectado un brote de {enfermedad} en {poblacion}.",
            "",
            f"📊 DATOS:",
            f"   • Población total: N = {N} personas",
            f"   • Susceptibles iniciales (S₀): {S0} personas",
            f"   • Infectados iniciales (I₀): {I0} personas",
            f"   • Recuperados iniciales (R₀): {R0_val} personas",
            f"   • Tasa de transmisión (β): {beta} día⁻¹",
            f"   • Tasa de recuperación (γ): {gamma} día⁻¹",
            "",
            f"📐 MODELO SIR:",
            f"   dS/dt = -βSI/N",
            f"   dI/dt = βSI/N - γI",
            f"   dR/dt = γI",
            "",
            f"🎯 SE PIDE:",
            f"   a) Calcular el número reproductivo básico R₀ = β/γ.",
            f"   b) Determinar si habrá brote epidémico (R₀ > 1) o no.",
            f"   c) Calcular la duración promedio de la infección.",
            f"   d) Estimar el pico de infectados y cuándo ocurrirá.",
            f"   e) Calcular el umbral de inmunidad de rebaño.",
            f"   f) Analizar qué pasaría si β se reduce a la mitad",
            f"      (ej: distanciamiento social).",
            "",
            f"💡 PREGUNTA CLAVE: ¿Cuántas personas deberían vacunarse para",
            f"   evitar la epidemia?",
        ]
        
        datos = {
            'N': N
        }
        
        analisis = [
            'Graficar S(t), I(t) y R(t) en el mismo gráfico',
            'Identificar el momento exacto del pico de I(t)',
            'Calcular el porcentaje final de infectados R(∞)/N',
            'Experimentar reduciendo β (simular cuarentena)'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_hopf(self, dificultad):
        """Genera ejercicio de bifurcación de Hopf."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Parámetros según nivel con mayor variabilidad
        if nivel == 1:
            mu = self.opcion([-0.5, -0.2, 0.0, 0.2, 0.5, 1.0])
        elif nivel == 2:
            mu = self.rango(-1.5, 2.5, 2)
        else:
            mu = self.rango(-2.0, 4.0, 2)
        
        # Condiciones iniciales variadas
        x0 = self.rango(0.05, 0.5, 2)
        y0 = self.rango(0.05, 0.5, 2)
        omega = self.rango(0.8, 1.5, 2)
        
        radio_ciclo = np.sqrt(mu) if mu > 0 else 0
        
        pools = PreguntasPool.hopf(mu, radio_ciclo)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        # Construir consigna detallada
        consigna = self._construir_consigna_hopf(mu, x0, y0, omega, radio_ciclo, nivel)
        
        return self.construir_ejercicio(
            sistema='hopf',
            titulo='Bifurcación de Hopf',
            dificultad=dificultad,
            parametros={'mu': mu, 'x0': x0, 'y0': y0, 'omega': omega},
            objetivos=[
                'Comprender qué es una bifurcación de Hopf',
                'Identificar el valor crítico del parámetro de bifurcación',
                'Observar la transición de punto fijo a ciclo límite',
                'Relacionar el radio del ciclo con el parámetro μ',
                'Distinguir entre bifurcación supercrítica y subcrítica'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            datos_adicionales=consigna['datos']
        )
    
    def _construir_consigna_hopf(self, mu, x0, y0, omega, radio_ciclo, nivel):
        """Construye la consigna detallada para bifurcación de Hopf."""
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"               BIFURCACIÓN DE HOPF - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 DESCRIPCIÓN:",
            f"   La bifurcación de Hopf es una transición donde un punto",
            f"   fijo puede perder estabilidad y emerger un ciclo límite.",
            "",
            f"📊 DATOS:",
            f"   • Parámetro de bifurcación (μ): {mu}",
            f"   • Frecuencia angular (ω): {omega}",
            f"   • Condición inicial: ({x0}, {y0})",
            "",
            f"📐 FORMA NORMAL:",
            f"   dx/dt = μx - ωy - x(x² + y²)",
            f"   dy/dt = ωx + μy - y(x² + y²)",
            "",
            f"   En coordenadas polares (r, θ):",
            f"   dr/dt = μr - r³",
            f"   dθ/dt = ω",
            "",
            f"🎯 SE PIDE:",
            f"   a) Analizar la estabilidad del origen (0,0) para μ = {mu}.",
            f"   b) Determinar el valor crítico de μ donde ocurre la bifurcación.",
            f"   c) Si existe ciclo límite, calcular su radio usando r* = √μ.",
            f"   d) Calcular el período del ciclo límite usando T = 2π/ω.",
            f"   e) Clasificar el tipo de comportamiento: punto fijo estable,",
            f"      ciclo límite, o punto de bifurcación.",
            f"   f) Variar μ entre -1 y +1 para observar la transición.",
            "",
            f"💡 EXPERIMENTO: Comienza con μ = -0.5 y aumenta gradualmente",
            f"   hasta μ = +0.5 para visualizar la bifurcación.",
        ]
        
        datos = {
            'mu': mu,
            'omega': omega,
        }
        
        analisis = [
            'Graficar el diagrama de fase (x vs y)',
            'Si μ > 0: medir el radio del ciclo y comparar con √μ',
            'Observar cómo cambia la dinámica al variar μ',
            'Identificar el punto exacto de bifurcación (μ = 0)'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_logistico(self, dificultad):
        """Genera ejercicio del modelo logístico con contexto ecológico realista."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['logistico'])
        
        # Parámetros según nivel con mayor variabilidad
        if nivel == 1:
            N0 = self.entero(10, 100)
            K = self.opcion([500, 1000, 2000, 5000])
            r = self.rango(0.1, 0.3, 2)
        elif nivel == 2:
            N0 = self.entero(5, 200)
            K = self.entero(500, 3000)
            r = self.rango(0.08, 0.5, 3)
        else:  # avanzado
            N0 = self.entero(1, 500)
            K = self.entero(200, 5000)
            r = self.rango(0.05, 0.8, 3)
        
        # Cálculos característicos
        t_inflexion = np.log((K - N0) / N0) / r if N0 < K and N0 > 0 else 0
        t_duplicacion = np.log(2) / r
        
        # Tiempo para alcanzar cierto porcentaje de K
        porcentaje_objetivo = self.opcion([0.5, 0.75, 0.9, 0.95])
        N_objetivo = K * porcentaje_objetivo
        t_objetivo = np.log((K - N0) * N_objetivo / (N0 * (K - N_objetivo))) / r if N0 < N_objetivo < K else float('inf')
        
        pools = PreguntasPool.logistico(K, t_inflexion, t_duplicacion)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        # Construir consigna contextualizada
        consigna = self._construir_consigna_logistico(contexto, N0, r, K, t_inflexion, 
                                                       t_duplicacion, porcentaje_objetivo, 
                                                       N_objetivo, t_objetivo, nivel)
        
        return self.construir_ejercicio(
            sistema='logistico',
            titulo='Modelo Logístico de Crecimiento',
            dificultad=dificultad,
            parametros={'N0': N0, 'r': r, 'K': K},
            objetivos=[
                'Comprender el crecimiento logístico y sus fases',
                'Identificar la capacidad de carga del ambiente',
                'Analizar el efecto de la tasa de crecimiento intrínseca',
                'Calcular el tiempo de duplicación inicial',
                'Localizar el punto de inflexión de la curva'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _construir_consigna_logistico(self, contexto, N0, r, K, t_inflexion, t_duplicacion,
                                       porcentaje_objetivo, N_objetivo, t_objetivo, nivel):
        """Construye la consigna contextualizada para modelo logístico."""
        poblacion = contexto['poblacion']
        recurso = contexto['recurso']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"            MODELO LOGÍSTICO DE CRECIMIENTO - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 SITUACIÓN:",
            f"   Se estudia una población de {poblacion}. El crecimiento está",
            f"   limitado por {recurso}.",
            "",
            f"📊 DATOS:",
            f"   • Población inicial (N₀): {N0} individuos",
            f"   • Capacidad de carga (K): {K} individuos",
            f"   • Tasa de crecimiento intrínseca (r): {r} por unidad de tiempo",
            "",
            f"📐 MODELO MATEMÁTICO:",
            f"   Ecuación diferencial logística:",
            f"   dN/dt = rN(1 - N/K)",
            "",
            f"🎯 SE PIDE:",
            f"   a) Calcular el tiempo de duplicación inicial: t₂ = ln(2)/r.",
            f"   b) Determinar en qué valor de N ocurre el punto de inflexión.",
            f"   c) Calcular el tiempo necesario para alcanzar {int(N_objetivo)} individuos",
            f"      ({porcentaje_objetivo*100:.0f}% de la capacidad de carga).",
            f"   d) Encontrar los puntos de equilibrio del sistema y",
            f"      analizar su estabilidad.",
            f"   e) Explicar qué ocurre si N₀ > K (sobrepoblación inicial).",
            "",
            f"💡 REFLEXIÓN: ¿Por qué las poblaciones no crecen indefinidamente?",
        ]
        
        datos = {
            'porcentaje_objetivo': porcentaje_objetivo,
            'N_objetivo': int(N_objetivo),
        }
        
        analisis = [
            'Graficar N(t) vs t e identificar las tres fases del crecimiento',
            'Localizar el punto de inflexión en la curva',
            'Medir el tiempo de duplicación inicial y comparar con ln(2)/r',
            'Experimentar con diferentes valores de r y K'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_verhulst(self, dificultad):
        """Genera ejercicio del mapa de Verhulst (logístico discreto) con análisis de bifurcaciones."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Parámetros según nivel - valores interesantes para bifurcaciones
        if nivel == 1:
            r = self.opcion([2.0, 2.5, 2.8, 3.0, 3.2, 3.5])
        elif nivel == 2:
            r = self.rango(1.5, 3.8, 2)
        else:
            r = self.rango(1.0, 4.0, 3)
        
        x0 = self.rango(0.1, 0.9, 2)
        
        # Análisis del comportamiento según r
        x_eq = 1 - 1/r if r > 1 else 0
        
        if r < 1:
            comportamiento = 'extinción (converge a 0)'
            periodo = 0
        elif r < 3:
            comportamiento = f'punto fijo estable x* = {x_eq:.4f}'
            periodo = 1
        elif r < 3.449:
            comportamiento = 'ciclo de período 2 (bifurcación)'
            periodo = 2
        elif r < 3.544:
            comportamiento = 'ciclo de período 4'
            periodo = 4
        elif r < 3.5699:
            comportamiento = 'ciclos de período 8, 16, ... (cascada)'
            periodo = 8
        elif r < 3.8284:
            comportamiento = 'caos con ventanas de periodicidad'
            periodo = -1  # caótico
        else:
            comportamiento = 'caos completamente desarrollado'
            periodo = -1
        
        # Preguntas específicas
        preguntas = self._crear_preguntas_verhulst(r, x_eq, comportamiento, periodo, nivel)
        
        # Construir consigna detallada
        consigna = self._construir_consigna_verhulst(r, x0, x_eq, comportamiento, periodo, nivel)
        
        return self.construir_ejercicio(
            sistema='verhulst',
            titulo='Mapa Logístico de Verhulst',
            dificultad=dificultad,
            parametros={'x0': x0, 'r': r},
            objetivos=[
                'Observar bifurcaciones de duplicación de período',
                'Comprender la ruta al caos determinista',
                'Analizar el diagrama de bifurcación',
                'Identificar ventanas de periodicidad en el caos',
                'Calcular puntos fijos y su estabilidad'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            datos_adicionales=consigna['datos']
        )
    
    def _crear_preguntas_verhulst(self, r, x_eq, comportamiento, periodo, nivel):
        """Crea preguntas específicas para el mapa de Verhulst."""
        preguntas = []
        
        if nivel == 1:
            preguntas = [
                {
                    'id': 1,
                    'texto': f'Para r = {r}, ¿el sistema converge a un punto fijo, oscila, o es caótico?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Converge a un punto fijo',
                        'Oscila con período definido',
                        'Es caótico (irregular)'
                    ],
                    'respuesta_correcta': 0 if periodo == 1 else (1 if periodo > 1 else 2)
                },
                {
                    'id': 2,
                    'texto': '¿En qué valor aproximado de r comienza la primera bifurcación (de punto fijo a período 2)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 3.0,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': '¿El mapa logístico xₙ₊₁ = r·xₙ(1-xₙ) es un sistema discreto o continuo?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Discreto (iteraciones)', 'Continuo (ecuación diferencial)'],
                    'respuesta_correcta': 0
                }
            ]
        elif nivel == 2:
            preguntas = [
                {
                    'id': 1,
                    'texto': f'Para r = {r}, el comportamiento del sistema es:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Punto fijo estable',
                        'Ciclo de período 2',
                        'Ciclo de período 4 o mayor',
                        'Caos'
                    ],
                    'respuesta_correcta': 0 if periodo == 1 else (1 if periodo == 2 else (2 if periodo > 2 else 3))
                },
                {
                    'id': 2,
                    'texto': f'Si r = {r} y r > 1, ¿cuál es el punto fijo no trivial x*?',
                    'tipo': 'numerica',
                    'respuesta_esperada': x_eq,
                    'tolerancia': 0.05,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': '¿A qué valor de r comienza aproximadamente el caos?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 3.57,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 4,
                    'texto': 'La constante de Feigenbaum δ ≈ 4.669 describe:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'El punto de inicio del caos',
                        'La razón entre intervalos sucesivos de bifurcación',
                        'El período máximo antes del caos',
                        'El exponente de Lyapunov'
                    ],
                    'respuesta_correcta': 1
                }
            ]
        else:  # avanzado
            preguntas = [
                {
                    'id': 1,
                    'texto': f'Para r = {r}, clasifique el comportamiento dinámico:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        f'Punto fijo estable x* = {x_eq:.4f}',
                        'Órbita de período 2',
                        'Órbita de período 4 o cascada',
                        'Caos determinista'
                    ],
                    'respuesta_correcta': 0 if periodo == 1 else (1 if periodo == 2 else (2 if periodo > 2 else 3))
                },
                {
                    'id': 2,
                    'texto': f'El punto fijo x* = 1 - 1/r = {x_eq:.4f} es estable si |f\'(x*)| < 1. Para r = {r}, ¿es estable?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Sí, es estable (r < 3)',
                        'No, es inestable (r > 3)',
                        'Es marginalmente estable (r = 3)'
                    ],
                    'respuesta_correcta': 0 if r < 3 else (1 if r > 3 else 2)
                },
                {
                    'id': 3,
                    'texto': '¿Qué valor tiene la derivada f\'(x) = r(1-2x) en el punto fijo x* = 1-1/r?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 2 - r,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 4,
                    'texto': 'En r ≈ 3.8284, existe una ventana de período 3. Esto es importante porque:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'El teorema de Sharkovskii garantiza todos los períodos',
                        'Es el inicio del caos',
                        'Es un error numérico',
                        'No tiene significado especial'
                    ],
                    'respuesta_correcta': 0
                },
                {
                    'id': 5,
                    'texto': '¿Cuántas bifurcaciones de duplicación hay entre r = 3 y r = 3.57?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Una (período 2)', 'Dos (períodos 2 y 4)', 'Infinitas', 'Ninguna'],
                    'respuesta_correcta': 2
                }
            ]
        
        return preguntas
    
    def _construir_consigna_verhulst(self, r, x0, x_eq, comportamiento, periodo, nivel):
        """Construye la consigna detallada para el mapa de Verhulst."""
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"           MAPA LOGÍSTICO DE VERHULST - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 DESCRIPCIÓN:",
            f"   El mapa logístico es un sistema discreto que exhibe la",
            f"   transición al caos a través de bifurcaciones.",
            "",
            f"📊 DATOS:",
            f"   • Parámetro de crecimiento (r): {r}",
            f"   • Condición inicial (x₀): {x0}",
            "",
            f"📐 MAPA LOGÍSTICO:",
            f"   xₙ₊₁ = r · xₙ · (1 - xₙ)",
            "",
            f"🎯 SE PIDE:",
            f"   a) Encontrar los puntos fijos del mapa resolviendo x = r·x(1-x).",
            f"   b) Analizar la estabilidad del punto fijo usando f'(x) = r(1-2x).",
            f"      Un punto fijo es estable si |f'(x*)| < 1.",
            f"   c) Para r = {r}, determinar si el sistema converge a un punto",
            f"      fijo, oscila periódicamente, o es caótico.",
            f"   d) Identificar los valores críticos de r donde ocurren",
            f"      bifurcaciones de duplicación de período.",
            f"   e) Explorar el diagrama de bifurcación variando r de 2.5 a 4.",
            "",
            f"📈 VALORES CLAVE:",
            f"   • r = 1: Transición de extinción a punto fijo",
            f"   • r = 3: Primera bifurcación (período 2)",
            f"   • r ≈ 3.449: Segunda bifurcación (período 4)",
            f"   • r ≈ 3.57: Inicio del caos",
            "",
            f"💡 EXPERIMENTO: Compara las trayectorias para x₀ = 0.2 y x₀ = 0.200001",
            f"   con r = 3.9 para observar sensibilidad a condiciones iniciales.",
        ]
        
        datos = {
            'r': r,
            'x0': x0,
        }
        
        analisis = [
            'Graficar xₙ vs n (serie temporal)',
            'Construir el diagrama de bifurcación variando r',
            'Identificar las primeras bifurcaciones',
            'Observar ventanas de periodicidad en la región caótica'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_orbital(self, dificultad):
        """Genera ejercicio de órbitas espaciales con contexto de misiones espaciales."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['orbital'])
        
        # Parámetros según nivel
        if nivel == 1:
            # Órbitas simples (circulares o casi circulares)
            r0 = self.rango(0.8, 1.5, 2)
            v_circular = 1 / np.sqrt(r0)  # Velocidad para órbita circular
            factor_v = self.rango(0.95, 1.05, 2)  # Pequeña desviación
            x0, y0 = r0, 0.0
            vx0, vy0 = 0.0, v_circular * factor_v
        elif nivel == 2:
            # Órbitas elípticas
            r0 = self.rango(0.5, 2.0, 2)
            v_circular = 1 / np.sqrt(r0)
            factor_v = self.rango(0.7, 1.3, 2)
            x0, y0 = r0, 0.0
            vx0, vy0 = 0.0, v_circular * factor_v
        else:
            # Órbitas variadas (incluye posibles escapes)
            r0 = self.rango(0.3, 2.5, 2)
            v_circular = 1 / np.sqrt(r0)
            factor_v = self.rango(0.5, 1.5, 2)
            x0 = r0
            y0 = self.rango(-0.3, 0.3, 2)
            vx0 = self.rango(-0.2, 0.2, 2)
            vy0 = v_circular * factor_v
        
        # Cálculos orbitales
        r0_mag = np.sqrt(x0**2 + y0**2)
        v0_mag = np.sqrt(vx0**2 + vy0**2)
        
        # Energía específica
        E = 0.5 * v0_mag**2 - 1.0/r0_mag
        
        # Momento angular específico
        L = x0 * vy0 - y0 * vx0
        
        # Semieje mayor
        if E < 0:
            a = -1 / (2 * E)
            # Excentricidad
            e = np.sqrt(1 + 2 * E * L**2)
            # Período (Kepler)
            T = 2 * np.pi * a**(3/2)
            tipo_orbita = 'elíptica' if e > 0.05 else 'circular'
        elif E == 0:
            a = float('inf')
            e = 1.0
            T = float('inf')
            tipo_orbita = 'parabólica'
        else:
            a = -1 / (2 * E)  # Negativo para hipérbola
            e = np.sqrt(1 + 2 * E * L**2)
            T = float('inf')
            tipo_orbita = 'hiperbólica (escape)'
        
        # Preguntas específicas
        preguntas = self._crear_preguntas_orbital(E, L, a, e, T, tipo_orbita, nivel)
        
        # Construir consigna
        consigna = self._construir_consigna_orbital(contexto, x0, y0, vx0, vy0, 
                                                     E, L, a, e, T, tipo_orbita, nivel)
        
        return self.construir_ejercicio(
            sistema='orbital',
            titulo='Órbitas Espaciales (Problema de Kepler)',
            dificultad=dificultad,
            parametros={'x0': x0, 'y0': y0, 'vx0': vx0, 'vy0': vy0, 'GM': 1.0},
            objetivos=[
                'Comprender las leyes de Kepler del movimiento planetario',
                'Analizar órbitas circulares, elípticas e hiperbólicas',
                'Verificar la conservación de energía y momento angular',
                'Clasificar órbitas según la energía total',
                'Aplicar conceptos de mecánica celeste'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _crear_preguntas_orbital(self, E, L, a, e, T, tipo_orbita, nivel):
        """Crea preguntas específicas para órbitas."""
        preguntas = []
        
        if nivel == 1:
            preguntas = [
                {
                    'id': 1,
                    'texto': '¿La energía total del sistema se conserva durante el movimiento?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, es una constante del movimiento', 'No, varía con el tiempo', 'Solo en órbitas circulares'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 2,
                    'texto': '¿El momento angular se conserva en una fuerza central?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, siempre para fuerzas centrales', 'No, nunca', 'Solo si la órbita es circular'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': '¿Qué relación cumple el período T con el semieje mayor a? (3ª Ley de Kepler)',
                    'tipo': 'opcion_multiple',
                    'opciones': ['T ∝ a', 'T² ∝ a³', 'T³ ∝ a²', 'T ∝ a²'],
                    'respuesta_correcta': 1
                }
            ]
        elif nivel == 2:
            preguntas = [
                {
                    'id': 1,
                    'texto': f'Dado que E = {E:.4f}, ¿qué tipo de órbita esperas?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Elíptica (E < 0, órbita ligada)',
                        'Parabólica (E = 0, escape límite)',
                        'Hiperbólica (E > 0, escape)'
                    ],
                    'respuesta_correcta': 0 if E < -0.001 else (1 if abs(E) < 0.001 else 2)
                },
                {
                    'id': 2,
                    'texto': '¿Cuál es la excentricidad de la órbita?',
                    'tipo': 'numerica',
                    'respuesta_esperada': e if e < 10 else 1.0,
                    'tolerancia': max(0.1, e * 0.15) if e < 10 else 0.5,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': '¿En qué punto de la órbita la velocidad es máxima?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Perihelio (punto más cercano)', 'Afelio (punto más lejano)', 'Es constante', 'En los nodos'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 4,
                    'texto': f'El momento angular L = {L:.4f} es constante porque:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'La fuerza es central (no hay torque)',
                        'La órbita es circular',
                        'La energía es negativa',
                        'El sistema es conservativo'
                    ],
                    'respuesta_correcta': 0
                }
            ]
        else:  # avanzado
            r_perihelio = a * (1 - e) if e < 1 else abs(a) * (e - 1)
            r_afelio = a * (1 + e) if e < 1 else float('inf')
            
            preguntas = [
                {
                    'id': 1,
                    'texto': f'Para E = {E:.4f} y L = {L:.4f}, calcula el semieje mayor a:',
                    'tipo': 'numerica',
                    'respuesta_esperada': abs(a) if abs(a) < 100 else 10.0,
                    'tolerancia': max(0.1, abs(a) * 0.15) if abs(a) < 100 else 2.0,
                    'unidad': 'unidades de distancia'
                },
                {
                    'id': 2,
                    'texto': f'La excentricidad e = √(1 + 2EL²) = ',
                    'tipo': 'numerica',
                    'respuesta_esperada': e if e < 5 else 1.5,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': f'Si la órbita es {tipo_orbita}, ¿cuál es el período (si existe)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': T if T < 100 else 50,
                    'tolerancia': T * 0.15 if T < 100 else 10,
                    'unidad': 'unidades de tiempo'
                } if E < 0 else {
                    'id': 3,
                    'texto': '¿Por qué no existe período orbital definido?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'La energía es positiva (escape)',
                        'El momento angular es cero',
                        'La órbita es inestable',
                        'Error en los cálculos'
                    ],
                    'respuesta_correcta': 0
                },
                {
                    'id': 4,
                    'texto': 'El vector de Laplace-Runge-Lenz es constante porque:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'El potencial es exactamente 1/r',
                        'El momento angular se conserva',
                        'La energía se conserva',
                        'La órbita es cerrada'
                    ],
                    'respuesta_correcta': 0
                },
                {
                    'id': 5,
                    'texto': 'Para una transferencia de Hohmann, necesitas:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Un solo impulso',
                        'Dos impulsos tangenciales',
                        'Impulso continuo',
                        'Cambio de plano orbital'
                    ],
                    'respuesta_correcta': 1
                }
            ]
        
        return preguntas
    
    def _construir_consigna_orbital(self, contexto, x0, y0, vx0, vy0, E, L, a, e, T, tipo_orbita, nivel):
        """Construye la consigna para órbitas espaciales."""
        mision = contexto['mision']
        destino = contexto['destino']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"              MECÁNICA ORBITAL - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 CONTEXTO:",
            f"   Se planea lanzar un {mision} hacia {destino}.",
            f"   Debes analizar la órbita resultante.",
            "",
            f"📊 CONDICIONES INICIALES:",
            f"   • Posición: r₀ = ({x0}, {y0})",
            f"   • Velocidad: v₀ = ({vx0}, {vy0})",
            f"   • GM = 1 (unidades normalizadas)",
            "",
            f"📐 ECUACIONES DEL MOVIMIENTO:",
            f"   Fuerza gravitatoria: F = -GMm/r² r̂",
            "",
            f"   Integrales del movimiento:",
            f"   • Energía: E = ½v² - GM/r",
            f"   • Momento angular: L = r × v",
            "",
            f"🎯 SE PIDE:",
            f"   a) Calcular la energía total E del sistema.",
            f"   b) Calcular el momento angular L.",
            f"   c) Clasificar el tipo de órbita según el signo de E:",
            f"      - E < 0: Elíptica (ligada)",
            f"      - E = 0: Parabólica (escape límite)",
            f"      - E > 0: Hiperbólica (escape)",
            f"   d) Si E < 0, calcular el semieje mayor a = -1/(2E).",
            f"   e) Calcular la excentricidad e = √(1 + 2EL²).",
            f"   f) Si la órbita es elíptica, calcular el período T = 2π·a^(3/2).",
            f"   g) Verificar que E y L se conservan durante el movimiento.",
            "",
            f"📈 LEYES DE KEPLER:",
            f"   1ª Ley: Las órbitas son cónicas con el Sol en un foco",
            f"   2ª Ley: El radio vector barre áreas iguales en tiempos iguales",
            f"   3ª Ley: T² ∝ a³",
            "",
            f"💡 EXPERIMENTO: Modifica ligeramente la velocidad inicial y observa",
            f"   cómo cambia la forma de la órbita.",
        ]
        
        datos = {
            'x0': x0,
            'y0': y0,
            'vx0': vx0,
            'vy0': vy0,
        }
        
        analisis = [
            'Graficar la trayectoria orbital (x vs y)',
            'Verificar conservación de E y L durante toda la simulación',
            'Medir perihelio y afelio si la órbita es elíptica',
            'Verificar la 3ª ley de Kepler: T² ∝ a³'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_mariposa(self, dificultad):
        """Genera ejercicio del atractor de Rössler con análisis de caos."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Parámetros según nivel
        if nivel == 1:
            a = 0.2
            b = 0.2
            c = self.opcion([4.0, 5.0, 5.7, 6.0])
        elif nivel == 2:
            a = self.rango(0.15, 0.25, 2)
            b = 0.2
            c = self.rango(4.0, 7.0, 1)
        else:
            a = self.rango(0.1, 0.35, 2)
            b = self.rango(0.1, 0.4, 2)
            c = self.rango(3.0, 9.0, 1)
        
        # Condiciones iniciales variadas
        x0 = self.rango(0.5, 2.0, 1)
        y0 = self.rango(0.5, 2.0, 1)
        z0 = self.rango(0.5, 2.0, 1)
        
        # Análisis del comportamiento
        # El sistema de Rössler muestra caos para a=0.2, b=0.2, c≈5.7
        if c < 4:
            comportamiento = 'punto fijo o ciclo simple'
        elif c < 5:
            comportamiento = 'ciclo límite'
        elif c < 6.5:
            comportamiento = 'atractor caótico'
        else:
            comportamiento = 'caos desarrollado o divergencia'
        
        preguntas = self._crear_preguntas_rossler(a, b, c, comportamiento, nivel)
        consigna = self._construir_consigna_rossler(a, b, c, x0, y0, z0, comportamiento, nivel)
        
        return self.construir_ejercicio(
            sistema='mariposa',
            titulo='Atractor de Rössler',
            dificultad=dificultad,
            parametros={'x0': x0, 'y0': y0, 'z0': z0, 'a': a, 'b': b, 'c': c},
            objetivos=[
                'Observar un atractor caótico tridimensional',
                'Comparar con el atractor de Lorenz',
                'Analizar la estructura del atractor de Rössler',
                'Entender la dependencia de los parámetros',
                'Visualizar sensibilidad a condiciones iniciales'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            datos_adicionales=consigna['datos']
        )
    
    def _crear_preguntas_rossler(self, a, b, c, comportamiento, nivel):
        """Crea preguntas específicas para el atractor de Rössler."""
        es_caotico = 'caótico' in comportamiento.lower()
        
        if nivel == 1:
            return [
                {
                    'id': 1,
                    'texto': '¿El sistema de Rössler es determinista o estocástico?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Determinista (ecuaciones fijas)', 'Estocástico (aleatorio)'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 2,
                    'texto': '¿Cuántas dimensiones tiene el sistema de Rössler?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 3,
                    'tolerancia': 0,
                    'unidad': ''
                },
                {
                    'id': 3,
                    'texto': f'Para los parámetros dados, el atractor parece ser:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Un punto fijo', 'Un ciclo límite simple', 'Un atractor caótico (extraño)'],
                    'respuesta_correcta': 0 if 'punto' in comportamiento else (1 if 'ciclo' in comportamiento else 2)
                }
            ]
        elif nivel == 2:
            return [
                {
                    'id': 1,
                    'texto': f'Con a={a}, b={b}, c={c}, el sistema exhibe:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Comportamiento periódico', 'Comportamiento caótico', 'Divergencia'],
                    'respuesta_correcta': 1 if es_caotico else 0
                },
                {
                    'id': 2,
                    'texto': '¿Qué diferencia principal hay entre Rössler y Lorenz?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Rössler tiene un solo lóbulo, Lorenz tiene dos',
                        'Rössler es 2D, Lorenz es 3D',
                        'Rössler es lineal, Lorenz es no lineal',
                        'No hay diferencia significativa'
                    ],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': 'El parámetro c controla principalmente:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'La frecuencia de rotación',
                        'La transición a caos',
                        'El tamaño del atractor',
                        'La estabilidad del origen'
                    ],
                    'respuesta_correcta': 1
                },
                {
                    'id': 4,
                    'texto': '¿Un atractor extraño tiene dimensión entera?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, siempre es entero', 'No, tiene dimensión fraccionaria'],
                    'respuesta_correcta': 1
                }
            ]
        else:  # avanzado
            return [
                {
                    'id': 1,
                    'texto': f'La proyección x-y del atractor de Rössler (c={c}) muestra:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Espirales convergentes a un punto',
                        'Un ciclo cerrado',
                        'Espirales que forman bandas caóticas',
                        'Trayectorias divergentes'
                    ],
                    'respuesta_correcta': 2 if es_caotico else (1 if 'ciclo' in comportamiento else 0)
                },
                {
                    'id': 2,
                    'texto': 'El atractor de Rössler tiene un exponente de Lyapunov positivo cuando:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Siempre',
                        'El sistema es caótico (c ≈ 5.7 con a=b=0.2)',
                        'Nunca (el sistema es estable)',
                        'Solo para c < 4'
                    ],
                    'respuesta_correcta': 1
                },
                {
                    'id': 3,
                    'texto': 'La bifurcación de período doble en Rössler ocurre al variar:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['El parámetro a', 'El parámetro b', 'El parámetro c', 'Las condiciones iniciales'],
                    'respuesta_correcta': 2
                },
                {
                    'id': 4,
                    'texto': '¿El sistema de Rössler fue diseñado para ser más simple que Lorenz. Por qué?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Solo un término no lineal (xz)',
                        'Menos ecuaciones',
                        'Parámetros más pequeños',
                        'Atractor más compacto'
                    ],
                    'respuesta_correcta': 0
                },
                {
                    'id': 5,
                    'texto': 'La dimensión de información del atractor de Rössler caótico es aproximadamente:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['~1.0', '~2.0', '~3.0', 'Mayor que 3'],
                    'respuesta_correcta': 1  # aproximadamente 2.0
                }
            ]
    
    def _construir_consigna_rossler(self, a, b, c, x0, y0, z0, comportamiento, nivel):
        """Construye la consigna para el atractor de Rössler."""
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"                  ATRACTOR DE RÖSSLER - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 DESCRIPCIÓN:",
            f"   El sistema de Rössler fue diseñado como el sistema más",
            f"   simple que exhibe caos. Tiene un solo término no lineal.",
            "",
            f"📊 DATOS:",
            f"   • a = {a}",
            f"   • b = {b}",
            f"   • c = {c}",
            f"   • Condición inicial: ({x0}, {y0}, {z0})",
            "",
            f"📐 ECUACIONES DE RÖSSLER:",
            f"   dx/dt = -y - z",
            f"   dy/dt = x + ay",
            f"   dz/dt = b + z(x - c)",
            "",
            f"🎯 SE PIDE:",
            f"   a) Identificar cuál es el único término no lineal del sistema.",
            f"   b) Determinar si el sistema presenta comportamiento:",
            f"      - Punto fijo estable",
            f"      - Ciclo límite",
            f"      - Atractor caótico",
            f"   c) Observar la proyección x-y y describir su forma.",
            f"   d) Variar el parámetro c entre 3 y 7 para observar",
            f"      cómo cambia el comportamiento del sistema.",
            f"   e) Comparar la estructura del atractor con el de Lorenz.",
            "",
            f"📈 REGIONES TÍPICAS (con a=b=0.2):",
            f"   • c < 4: Punto fijo o ciclo simple",
            f"   • c ≈ 4-5: Ciclo límite",
            f"   • c ≈ 5.7: Caos clásico de Rössler",
            "",
            f"💡 EXPERIMENTO: Inicia dos simulaciones con condiciones",
            f"   muy cercanas para observar la divergencia exponencial.",
        ]
        
        datos = {
            'a': a,
            'b': b,
            'c': c,
        }
        
        analisis = [
            'Visualizar el atractor en 3D',
            'Graficar la proyección x-y (plano de espirales)',
            'Comparar estructuralmente con Lorenz',
            'Observar la sensibilidad a condiciones iniciales'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_amortiguador(self, dificultad):
        """Genera ejercicio de sistema masa-resorte-amortiguador con contexto de ingeniería."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['amortiguador'])
        
        # Parámetros según nivel
        if nivel == 1:
            m = 1.0
            k = self.opcion([1.0, 4.0, 9.0, 16.0])
            c = self.rango(0.2, 2.0, 1)
        elif nivel == 2:
            m = self.rango(0.5, 2.0, 1)
            k = self.rango(1.0, 10.0, 1)
            c = self.rango(0.5, 6.0, 2)
        else:
            m = self.rango(0.2, 3.0, 2)
            k = self.rango(0.5, 15.0, 2)
            c = self.rango(0.1, 10.0, 2)
        
        # Condiciones iniciales variadas
        x0 = self.rango(0.5, 2.0, 1)
        v0 = self.rango(-1.0, 1.0, 1)
        
        # Forzamiento opcional para niveles avanzados
        if nivel >= 3 and random.random() > 0.5:
            F0 = self.rango(0.5, 2.0, 1)
            omega_f = self.rango(0.5, 3.0, 2)
        else:
            F0 = 0.0
            omega_f = 0.0
        
        # Cálculos característicos
        omega_n = np.sqrt(k / m)  # Frecuencia natural
        c_crit = 2 * np.sqrt(k * m)  # Amortiguamiento crítico
        zeta = c / c_crit  # Factor de amortiguamiento
        
        # Clasificación
        if zeta < 0.95:
            tipo = 'Subamortiguado'
            tipo_idx = 0
            omega_d = omega_n * np.sqrt(1 - zeta**2)  # Frecuencia amortiguada
        elif zeta < 1.05:
            tipo = 'Críticamente amortiguado'
            tipo_idx = 1
            omega_d = 0
        else:
            tipo = 'Sobreamortiguado'
            tipo_idx = 2
            omega_d = 0
        
        # Tiempo de establecimiento (2% criterion)
        if zeta < 1:
            t_settle = 4 / (zeta * omega_n) if zeta > 0.01 else float('inf')
        else:
            t_settle = 4 / omega_n
        
        preguntas = self._crear_preguntas_amortiguador(m, c, k, zeta, omega_n, omega_d, tipo, tipo_idx, F0, omega_f, nivel)
        consigna = self._construir_consigna_amortiguador(contexto, m, c, k, x0, v0, F0, omega_f,
                                                         zeta, omega_n, omega_d, c_crit, tipo, t_settle, nivel)
        
        return self.construir_ejercicio(
            sistema='amortiguador',
            titulo='Sistema Masa-Resorte-Amortiguador',
            dificultad=dificultad,
            parametros={'m': m, 'c': c, 'k': k, 'x0': x0, 'v0': v0, 'F0': F0, 'omega_f': omega_f},
            objetivos=[
                'Comprender los tres tipos de amortiguamiento',
                'Calcular el factor de amortiguamiento ζ',
                'Analizar la respuesta libre y forzada del sistema',
                'Identificar la frecuencia natural y amortiguada',
                'Determinar el tiempo de establecimiento'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _crear_preguntas_amortiguador(self, m, c, k, zeta, omega_n, omega_d, tipo, tipo_idx, F0, omega_f, nivel):
        """Crea preguntas específicas para el sistema amortiguado."""
        
        if nivel == 1:
            return [
                {
                    'id': 1,
                    'texto': '¿Qué tipo de amortiguamiento presenta el sistema?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado (oscila)', 'Críticamente amortiguado', 'Sobreamortiguado (no oscila)'],
                    'respuesta_correcta': tipo_idx
                },
                {
                    'id': 2,
                    'texto': '¿El sistema eventualmente regresa al equilibrio (x = 0)?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí, debido al amortiguamiento', 'No, oscila indefinidamente', 'Depende de x₀'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 3,
                    'texto': '¿Cuál es la frecuencia natural ωₙ = √(k/m)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': omega_n,
                    'tolerancia': omega_n * 0.1,
                    'unidad': 'rad/s'
                }
            ]
        elif nivel == 2:
            return [
                {
                    'id': 1,
                    'texto': f'¿Cuál es el factor de amortiguamiento ζ = c/(2√(km))?',
                    'tipo': 'numerica',
                    'respuesta_esperada': zeta,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 2,
                    'texto': '¿Qué tipo de amortiguamiento presenta el sistema?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado (ζ < 1)', 'Críticamente amortiguado (ζ = 1)', 'Sobreamortiguado (ζ > 1)'],
                    'respuesta_correcta': tipo_idx
                },
                {
                    'id': 3,
                    'texto': '¿El sistema oscila con amplitud decreciente?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Sí', 'No'],
                    'respuesta_correcta': 0 if zeta < 1 else 1
                },
                {
                    'id': 4,
                    'texto': f'La frecuencia natural es ωₙ = {omega_n:.3f} rad/s. ¿Cuál es el período natural Tₙ?',
                    'tipo': 'numerica',
                    'respuesta_esperada': 2*np.pi/omega_n,
                    'tolerancia': 0.2,
                    'unidad': 's'
                }
            ]
        else:  # avanzado
            preguntas = [
                {
                    'id': 1,
                    'texto': f'Dado m={m}, c={c}, k={k}, calcula el amortiguamiento crítico c_crit:',
                    'tipo': 'numerica',
                    'respuesta_esperada': 2*np.sqrt(k*m),
                    'tolerancia': 0.3,
                    'unidad': 'Ns/m'
                },
                {
                    'id': 2,
                    'texto': f'El factor ζ = {zeta:.3f}. El sistema es:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'],
                    'respuesta_correcta': tipo_idx
                },
            ]
            
            if zeta < 1:
                preguntas.append({
                    'id': 3,
                    'texto': f'La frecuencia amortiguada es ωd = ωₙ√(1-ζ²). Calcula ωd:',
                    'tipo': 'numerica',
                    'respuesta_esperada': omega_d,
                    'tolerancia': omega_d * 0.1 if omega_d > 0 else 0.1,
                    'unidad': 'rad/s'
                })
            else:
                preguntas.append({
                    'id': 3,
                    'texto': '¿Por qué no hay frecuencia de oscilación definida?',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'El sistema está sobreamortiguado (no oscila)',
                        'Error de cálculo',
                        'Falta fuerza externa',
                        'La masa es muy grande'
                    ],
                    'respuesta_correcta': 0
                })
            
            if F0 > 0:
                preguntas.extend([
                    {
                        'id': 4,
                        'texto': f'Con forzamiento F₀={F0}, ωf={omega_f}, ¿hay resonancia si ωf ≈ ωₙ?',
                        'tipo': 'opcion_multiple',
                        'opciones': ['Sí, la amplitud crece significativamente', 'No, el amortiguamiento lo impide totalmente', 'Solo si ζ = 0'],
                        'respuesta_correcta': 0 if abs(omega_f - omega_n) < 0.5 else 1
                    },
                    {
                        'id': 5,
                        'texto': 'La amplitud de resonancia depende de:',
                        'tipo': 'opcion_multiple',
                        'opciones': ['1/ζ (menor amortiguamiento = mayor amplitud)', 'ζ²', 'Solo de F₀', 'Solo de ωf'],
                        'respuesta_correcta': 0
                    }
                ])
            else:
                preguntas.extend([
                    {
                        'id': 4,
                        'texto': 'Para un sistema subamortiguado, la envolvente de decaimiento es:',
                        'tipo': 'opcion_multiple',
                        'opciones': ['e^(-ζωₙt)', 'e^(-t)', 't·e^(-t)', '1/t'],
                        'respuesta_correcta': 0
                    },
                    {
                        'id': 5,
                        'texto': 'El decremento logarítmico δ = 2πζ/√(1-ζ²) permite medir:',
                        'tipo': 'opcion_multiple',
                        'opciones': [
                            'El factor de amortiguamiento experimentalmente',
                            'La masa del sistema',
                            'La rigidez del resorte',
                            'La energía inicial'
                        ],
                        'respuesta_correcta': 0
                    }
                ])
            
            return preguntas
    
    def _construir_consigna_amortiguador(self, contexto, m, c, k, x0, v0, F0, omega_f,
                                          zeta, omega_n, omega_d, c_crit, tipo, t_settle, nivel):
        """Construye la consigna para el sistema masa-resorte-amortiguador."""
        sistema = contexto['sistema']
        proposito = contexto['proposito']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"          OSCILADOR AMORTIGUADO - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 CONTEXTO:",
            f"   Se analiza un {sistema} diseñado para {proposito}.",
            "",
            f"📊 DATOS:",
            f"   • Masa (m): {m} kg",
            f"   • Amortiguador (c): {c} Ns/m",
            f"   • Resorte (k): {k} N/m",
            f"   • Posición inicial (x₀): {x0} m",
            f"   • Velocidad inicial (v₀): {v0} m/s",
        ]
        
        if F0 > 0:
            instrucciones.append(f"   • Fuerza externa: F(t) = {F0}·cos({omega_f}t) N")
        
        instrucciones.extend([
            "",
            f"📐 ECUACIÓN DEL MOVIMIENTO:",
            f"   m·ẍ + c·ẋ + k·x = F(t)",
            "",
            f"🎯 SE PIDE:",
            f"   a) Calcular la frecuencia natural: ωₙ = √(k/m).",
            f"   b) Calcular el amortiguamiento crítico: c_crit = 2√(km).",
            f"   c) Calcular el factor de amortiguamiento: ζ = c/c_crit.",
            f"   d) Clasificar el sistema según ζ:",
            f"      - ζ < 1: Subamortiguado (oscila)",
            f"      - ζ = 1: Críticamente amortiguado",
            f"      - ζ > 1: Sobreamortiguado (no oscila)",
            f"   e) Si ζ < 1, calcular la frecuencia amortiguada: ωd = ωₙ√(1-ζ²).",
            f"   f) Estimar el tiempo de establecimiento del sistema.",
            "",
        ])
        
        instrucciones.extend([
            f"🔬 EXPERIMENTO:",
            f"   Varía c para observar la transición entre regímenes de",
            f"   amortiguamiento y determina el valor de c_crit experimentalmente.",
            "",
            f"💡 NOTA: El amortiguamiento crítico es óptimo para muchas aplicaciones",
            f"   (retorno rápido sin oscilaciones indeseadas).",
        ])
        
        datos = {
            'm': m,
            'c': c,
            'k': k,
        }
        
        analisis = [
            'Graficar x(t) y verificar el tipo de respuesta',
            'Medir el tiempo de establecimiento y comparar con la teoría',
            'Experimentar variando c para ver los tres regímenes'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_rlc(self, dificultad):
        """Genera ejercicio de circuito RLC con contexto de electrónica."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto aleatorio
        contexto = random.choice(self.CONTEXTOS['rlc'])
        
        # Parámetros según nivel
        if nivel == 1:
            R = self.opcion([5.0, 10.0, 20.0, 50.0])
            L = self.opcion([0.05, 0.1, 0.2])
            C = self.opcion([0.0005, 0.001, 0.002])
            V0 = self.opcion([5.0, 10.0, 12.0])
        elif nivel == 2:
            R = float(self.entero(5, 100))
            L = self.rango(0.02, 0.5, 3)
            C = self.rango(0.0002, 0.005, 5)
            V0 = float(self.entero(5, 24))
        else:
            R = float(self.entero(1, 200))
            L = self.rango(0.005, 1.0, 4)
            C = self.rango(0.00005, 0.01, 6)
            V0 = float(self.entero(1, 50))
        
        # Condiciones iniciales
        I0 = 0.0
        Q0 = C * V0  # Capacitor inicialmente cargado
        
        # Cálculos característicos
        omega_0 = 1 / np.sqrt(L * C)  # Frecuencia de resonancia
        f_0 = omega_0 / (2 * np.pi)   # En Hz
        Q_factor = omega_0 * L / R     # Factor de calidad
        
        # Factor de amortiguamiento
        alpha = R / (2 * L)
        zeta = alpha / omega_0
        
        # Clasificación
        if zeta < 0.95:
            tipo = 'Subamortiguado'
            tipo_idx = 0
            omega_d = omega_0 * np.sqrt(1 - zeta**2)
        elif zeta < 1.05:
            tipo = 'Críticamente amortiguado'
            tipo_idx = 1
            omega_d = 0
        else:
            tipo = 'Sobreamortiguado'
            tipo_idx = 2
            omega_d = 0
        
        preguntas = self._crear_preguntas_rlc(R, L, C, omega_0, f_0, Q_factor, zeta, tipo, tipo_idx, nivel)
        consigna = self._construir_consigna_rlc(contexto, R, L, C, V0, I0, Q0,
                                                 omega_0, f_0, Q_factor, zeta, omega_d, tipo, nivel)
        
        return self.construir_ejercicio(
            sistema='rlc',
            titulo='Circuito RLC Serie',
            dificultad=dificultad,
            parametros={'R': R, 'L': L, 'C': C, 'V0': V0, 'I0': I0, 'Q0': Q0},
            objetivos=[
                'Comprender la dinámica de circuitos RLC',
                'Analizar oscilaciones eléctricas amortiguadas',
                'Calcular la frecuencia de resonancia',
                'Determinar el factor de calidad Q',
                'Relacionar con sistemas mecánicos análogos'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _crear_preguntas_rlc(self, R, L, C, omega_0, f_0, Q_factor, zeta, tipo, tipo_idx, nivel):
        """Crea preguntas específicas para el circuito RLC."""
        
        if nivel == 1:
            return [
                {
                    'id': 1,
                    'texto': '¿Cuál es la frecuencia de resonancia ω₀ = 1/√(LC)?',
                    'tipo': 'numerica',
                    'respuesta_esperada': omega_0,
                    'tolerancia': omega_0 * 0.15,
                    'unidad': 'rad/s'
                },
                {
                    'id': 2,
                    'texto': '¿El circuito está subamortiguado, crítico o sobreamortiguado?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado (oscila)', 'Críticamente amortiguado', 'Sobreamortiguado (no oscila)'],
                    'respuesta_correcta': tipo_idx
                },
                {
                    'id': 3,
                    'texto': 'En un circuito RLC, la energía oscila entre:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Campo magnético (L) y campo eléctrico (C)',
                        'Resistencia y capacitor',
                        'Fuente y tierra',
                        'No hay oscilación de energía'
                    ],
                    'respuesta_correcta': 0
                }
            ]
        elif nivel == 2:
            return [
                {
                    'id': 1,
                    'texto': f'La frecuencia de resonancia ω₀ es:',
                    'tipo': 'numerica',
                    'respuesta_esperada': omega_0,
                    'tolerancia': omega_0 * 0.1,
                    'unidad': 'rad/s'
                },
                {
                    'id': 2,
                    'texto': f'La frecuencia en Hz (f₀ = ω₀/2π) es:',
                    'tipo': 'numerica',
                    'respuesta_esperada': f_0,
                    'tolerancia': f_0 * 0.15,
                    'unidad': 'Hz'
                },
                {
                    'id': 3,
                    'texto': f'El factor de calidad Q = ω₀L/R aproximado es:',
                    'tipo': 'numerica',
                    'respuesta_esperada': Q_factor,
                    'tolerancia': Q_factor * 0.2,
                    'unidad': ''
                },
                {
                    'id': 4,
                    'texto': '¿Qué sucede con Q si aumentamos R?',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Q aumenta', 'Q disminuye', 'Q permanece constante', 'Q se vuelve infinito'],
                    'respuesta_correcta': 1
                }
            ]
        else:  # avanzado
            return [
                {
                    'id': 1,
                    'texto': f'Calcula el factor de amortiguamiento ζ = R/(2√(L/C)):',
                    'tipo': 'numerica',
                    'respuesta_esperada': zeta,
                    'tolerancia': 0.1,
                    'unidad': ''
                },
                {
                    'id': 2,
                    'texto': f'El circuito con ζ = {zeta:.3f} es:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Subamortiguado', 'Críticamente amortiguado', 'Sobreamortiguado'],
                    'respuesta_correcta': tipo_idx
                },
                {
                    'id': 3,
                    'texto': 'El factor de calidad Q y el ancho de banda BW se relacionan por:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['BW = f₀/Q', 'BW = Q·f₀', 'BW = Q²/f₀', 'No hay relación'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 4,
                    'texto': 'La impedancia del circuito RLC a frecuencia de resonancia es:',
                    'tipo': 'opcion_multiple',
                    'opciones': ['Mínima e igual a R', 'Máxima', 'Cero', 'Infinita'],
                    'respuesta_correcta': 0
                },
                {
                    'id': 5,
                    'texto': 'El circuito RLC es análogo a qué sistema mecánico:',
                    'tipo': 'opcion_multiple',
                    'opciones': [
                        'Masa-resorte-amortiguador (L↔m, C↔1/k, R↔c)',
                        'Péndulo simple',
                        'Cuerda vibrante',
                        'Fluido en tubería'
                    ],
                    'respuesta_correcta': 0
                }
            ]
    
    def _construir_consigna_rlc(self, contexto, R, L, C, V0, I0, Q0, omega_0, f_0, Q_factor, zeta, omega_d, tipo, nivel):
        """Construye la consigna para el circuito RLC."""
        aplicacion = contexto['aplicacion']
        frecuencia = contexto['frecuencia']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"                 CIRCUITO RLC SERIE - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 CONTEXTO:",
            f"   Se diseña un {aplicacion} que opera en el rango de {frecuencia}.",
            "",
            f"📊 DATOS:",
            f"   • Resistencia (R): {R} Ω",
            f"   • Inductancia (L): {L*1000:.2f} mH ({L} H)",
            f"   • Capacitancia (C): {C*1e6:.2f} μF ({C} F)",
            f"   • Voltaje inicial en capacitor: V₀ = {V0} V",
            "",
            f"📐 ECUACIÓN DEL CIRCUITO:",
            f"   L·d²Q/dt² + R·dQ/dt + Q/C = 0",
            "",
            f"   Analogía con sistema mecánico:",
            f"   L ↔ m (masa), R ↔ c (amortiguador), 1/C ↔ k (resorte)",
            "",
            f"🎯 SE PIDE:",
            f"   a) Calcular la frecuencia de resonancia: ω₀ = 1/√(LC).",
            f"   b) Calcular la frecuencia en Hz: f₀ = ω₀/(2π).",
            f"   c) Calcular el factor de calidad: Q = ω₀L/R.",
            f"   d) Calcular el factor de amortiguamiento: ζ = R/(2ω₀L).",
            f"   e) Clasificar el circuito según ζ:",
            f"      - ζ < 1: Subamortiguado (oscila)",
            f"      - ζ = 1: Críticamente amortiguado",
            f"      - ζ > 1: Sobreamortiguado",
            f"   f) Calcular la energía inicial almacenada: E₀ = ½CV₀².",
            "",
            f"📈 RELACIONES IMPORTANTES:",
            f"   • Q alto → Oscilaciones duraderas, banda estrecha",
            f"   • Q bajo → Decaimiento rápido, banda ancha",
            f"   • Ancho de banda: BW = f₀/Q",
            "",
            f"💡 ANALOGÍA: Este circuito es equivalente a un sistema",
            f"   masa-resorte-amortiguador mecánico.",
        ]
        
        datos = {
            'R': R,
            'L': L,
            'C': C,
            'V0': V0,
        }
        
        analisis = [
            'Graficar I(t) y V_C(t) vs tiempo',
            'Medir la frecuencia de oscilación si el circuito es subamortiguado',
            'Medir Q experimentalmente contando oscilaciones',
            'Comparar con la analogía mecánica'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
    
    def _gen_lorenz(self, dificultad):
        """Genera ejercicio del sistema de Lorenz con análisis detallado del caos."""
        nivel = self.DIFICULTAD[dificultad]
        
        # Seleccionar contexto
        contexto = random.choice(self.CONTEXTOS['lorenz'])
        
        # Parámetros según nivel
        if nivel == 1:
            sigma = 10.0
            rho = self.opcion([15.0, 20.0, 24.0, 28.0, 35.0])
            beta = 8/3
        elif nivel == 2:
            sigma = 10.0
            rho = self.rango(18.0, 35.0, 1)
            beta = 8/3
        else:
            sigma = self.rango(8.0, 14.0, 1)
            rho = self.rango(15.0, 45.0, 1)
            beta = self.rango(2.0, 3.5, 2)
        
        # Condiciones iniciales variadas
        x0 = self.rango(0.5, 2.0, 1)
        y0 = self.rango(0.5, 2.0, 1)
        z0 = self.rango(0.5, 2.0, 1)
        
        # Análisis del comportamiento
        # Para σ=10, β=8/3: caos comienza en ρ ≈ 24.74
        rho_critico = sigma * (sigma + beta + 3) / (sigma - beta - 1) if sigma > beta + 1 else 24.74
        es_caotico = rho > 24.74
        
        # Puntos de equilibrio no triviales (si ρ > 1)
        if rho > 1:
            x_eq = np.sqrt(beta * (rho - 1))
            y_eq = x_eq
            z_eq = rho - 1
        else:
            x_eq = y_eq = z_eq = 0
        
        pools = PreguntasPool.lorenz(rho, es_caotico)
        preguntas = self.seleccionar_preguntas(pools, nivel)
        
        consigna = self._construir_consigna_lorenz(contexto, sigma, rho, beta, x0, y0, z0,
                                                   es_caotico, rho_critico, x_eq, y_eq, z_eq, nivel)
        
        return self.construir_ejercicio(
            sistema='lorenz',
            titulo='Sistema de Lorenz (Atractor Caótico)',
            dificultad=dificultad,
            parametros={'x0': x0, 'y0': y0, 'z0': z0, 'sigma': sigma, 'rho': rho, 'beta': beta},
            objetivos=[
                'Observar comportamiento caótico determinista',
                'Comprender la sensibilidad a condiciones iniciales (efecto mariposa)',
                'Analizar el atractor extraño de Lorenz',
                'Identificar el valor crítico de ρ para el caos',
                'Visualizar la estructura de dos lóbulos del atractor'
            ],
            instrucciones=consigna['instrucciones'],
            preguntas=preguntas,
            analisis=consigna['analisis'],
            contexto=contexto,
            datos_adicionales=consigna['datos']
        )
    
    def _construir_consigna_lorenz(self, contexto, sigma, rho, beta, x0, y0, z0, 
                                    es_caotico, rho_critico, x_eq, y_eq, z_eq, nivel):
        """Construye la consigna para el sistema de Lorenz."""
        aplicacion = contexto['aplicacion']
        fenomeno = contexto['fenomeno']
        
        instrucciones = [
            f"═══════════════════════════════════════════════════════════════",
            f"           SISTEMA DE LORENZ - CONSIGNA",
            f"═══════════════════════════════════════════════════════════════",
            "",
            f"📋 CONTEXTO:",
            f"   El sistema de Lorenz modela {fenomeno} para {aplicacion}.",
            "",
            f"📊 DATOS:",
            f"   • σ (sigma): {sigma}",
            f"   • ρ (rho): {rho}",
            f"   • β (beta): {beta:.4f}",
            f"   • Condición inicial: ({x0}, {y0}, {z0})",
            "",
            f"📐 ECUACIONES DE LORENZ:",
            f"   dx/dt = σ(y - x)",
            f"   dy/dt = x(ρ - z) - y",
            f"   dz/dt = xy - βz",
            "",
            f"🎯 SE PIDE:",
            f"   a) Encontrar los puntos de equilibrio del sistema:",
            f"      - ¿Qué condiciones deben cumplirse para que dx/dt = dy/dt = dz/dt = 0?",
            f"      - Demuestra que (0,0,0) siempre es punto de equilibrio.",
            f"      - Si ρ > 1, encuentra los otros puntos de equilibrio.",
            f"   b) Determinar el valor crítico de ρ donde el sistema se vuelve caótico",
            f"      (aproximadamente ρ_c ≈ 24.74 para σ=10, β=8/3).",
            f"   c) Para ρ = {rho}, determinar si el sistema es caótico o no.",
            f"   d) Visualizar el atractor y describir su estructura",
            f"      (un lóbulo, dos lóbulos, punto fijo, etc.).",
            f"   e) Realizar el experimento del 'efecto mariposa':",
            f"      - Ejecutar dos simulaciones con condiciones muy cercanas",
            f"      - Observar cómo divergen las trayectorias con el tiempo.",
            "",
            f"💡 EXPERIMENTO: Prueba con condiciones iniciales:",
            f"   Caso A: ({x0}, {y0}, {z0})",
            f"   Caso B: ({x0}, {y0 + 0.001}, {z0})",
            f"   Observa la divergencia exponencial.",
        ]
        
        datos = {
            'sigma': sigma,
            'rho': rho,
            'beta': round(beta, 4),
        }
        
        analisis = [
            'Visualizar el atractor en espacio 3D',
            'Identificar la estructura del atractor',
            'Probar sensibilidad cambiando ligeramente las condiciones iniciales',
            'Observar las transiciones entre lóbulos (si existen)'
        ]
        
        return {'instrucciones': instrucciones, 'datos': datos, 'analisis': analisis}
