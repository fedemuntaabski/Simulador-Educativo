"""
Pools de preguntas organizados por sistema y nivel.
Separados de la lógica para facilitar mantenimiento.
"""

import numpy as np


class PreguntasPool:
    """
    Repositorio centralizado de preguntas por sistema.
    Cada método retorna un dict {1: [...], 2: [...], 3: [...]} 
    con preguntas para cada nivel de dificultad.
    """
    
    @staticmethod
    def newton(T0, T_env, k, tau, t_esperado, t_50, T_t2):
        """Preguntas para enfriamiento de Newton."""
        principiante = [
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
                'texto': '¿Qué fracción de la diferencia inicial queda después de un tiempo τ=1/k?',
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
        
        T_objetivo = T_env + (T0 - T_env) * 0.37
        intermedio = [
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
                'texto': '¿Cuál es la constante de tiempo τ = 1/k del sistema?',
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
                'texto': '¿Cuánto tiempo se necesita para reducir la diferencia de temperatura a la mitad?',
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
        
        avanzado = [
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
                'texto': f'Si la temperatura inicial fuera {T0 + 20}°C, ¿cómo cambiaría la tasa inicial de enfriamiento?',
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
                'texto': f'¿Cuál es la energía disipada relativa después de τ = {tau:.2f} min?',
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
        
        return {1: principiante, 2: intermedio, 3: avanzado}
    
    @staticmethod
    def van_der_pol(mu):
        """Preguntas para oscilador Van der Pol."""
        principiante = [
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
        
        intermedio = [
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
        
        avanzado = [
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
        
        return {1: principiante, 2: intermedio, 3: avanzado}

    @staticmethod
    def sir(beta, gamma, R0_basico, herd_immunity):
        """Preguntas para modelo SIR."""
        principiante = [
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
        
        intermedio = [
            {
                'id': 1,
                'texto': '¿Cuál es el valor de R₀ (número reproductivo básico)?',
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
                'texto': '¿Qué fracción de la población debe vacunarse para inmunidad de rebaño?',
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
        
        avanzado = [
            {
                'id': 1,
                'texto': '¿Cuál es el valor de R₀?',
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
        
        return {1: principiante, 2: intermedio, 3: avanzado}

    @staticmethod
    def hopf(mu, radio_ciclo):
        """Preguntas para bifurcación de Hopf."""
        principiante = [
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
        
        intermedio = [
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
        
        avanzado = [
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
                'opciones': ['λ = μ ± iω (complejos con parte real μ)', 'λ = ±μ (reales)', 'λ = μ (degenerado)', 'λ = 0'],
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
        
        return {1: principiante, 2: intermedio, 3: avanzado}

    @staticmethod
    def logistico(K, t_inflexion, t_duplicacion):
        """Preguntas para modelo logístico."""
        principiante = [
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
        
        intermedio = [
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
                'texto': '¿Cuál es el tiempo de duplicación inicial aproximado (para N << K)?',
                'tipo': 'numerica',
                'respuesta_esperada': t_duplicacion,
                'tolerancia': t_duplicacion * 0.15,
                'unidad': 'unidades de tiempo'
            }
        ]
        
        avanzado = [
            {
                'id': 1,
                'texto': '¿En qué tiempo aproximado ocurre el punto de inflexión?',
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
        
        return {1: principiante, 2: intermedio, 3: avanzado}

    @staticmethod
    def lorenz(rho, es_caotico):
        """Preguntas para sistema de Lorenz."""
        principiante = [
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
        
        intermedio = [
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
        
        avanzado = [
            {
                'id': 1,
                'texto': f'Con ρ = {rho}, clasifique el comportamiento:',
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
                'texto': 'Para los parámetros dados, ¿los puntos fijos C+ y C- son estables?',
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
        
        return {1: principiante, 2: intermedio, 3: avanzado}
