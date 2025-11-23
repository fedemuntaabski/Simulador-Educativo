import random
from typing import List, Dict, Any
from models.exercise import Exercise, Parameter, ParameterType, ActivityType, DifficultyLevel, ExerciseMetadata

def generate_exercise(topic: str) -> Exercise:
    """
    Genera un ejercicio educativo completo y válido para un tema específico.
    
    Args:
        topic: El tema del ejercicio (ej: "sir", "lorenz", "newton").
        
    Returns:
        Un objeto Exercise configurado.
        
    Raises:
        ValueError: Si el tema no es soportado.
    """
    generators = {
        'sir': _generate_sir,
        'lorenz': _generate_lorenz,
        'van_der_pol': _generate_van_der_pol,
        'hopf': _generate_hopf,
        'rlc': _generate_rlc,
        'logistica': _generate_logistic,
        'verhulst': _generate_verhulst,
        'orbitas': _generate_orbits,
        'amortiguadores': _generate_dampers,
        'newton': _generate_newton_cooling
    }
    
    normalized_topic = topic.lower().strip()
    if normalized_topic not in generators:
        # Try to match partial names or aliases if needed, or just raise error
        # Mapping some common aliases based on the prompt list
        aliases = {
            'enfriamiento de newton': 'newton',
            'amortiguador': 'amortiguadores',
            'orbital': 'orbitas',
            'logistico': 'logistica'
        }
        if normalized_topic in aliases:
            normalized_topic = aliases[normalized_topic]
        else:
            raise ValueError(f"Tema '{topic}' no soportado. Temas disponibles: {list(generators.keys())}")
            
    return generators[normalized_topic]()

def _generate_sir() -> Exercise:
    # Variaciones aleatorias
    beta = round(random.uniform(0.2, 0.8), 2)
    gamma = round(random.uniform(0.05, 0.3), 2)
    s0 = random.randint(900, 990)
    i0 = 1000 - s0
    
    r0_basic = beta / gamma
    
    description = (
        "El modelo SIR divide la población en tres compartimentos: Susceptibles (S), "
        "Infectados (I) y Recuperados (R). Este ejercicio explora cómo las tasas de "
        "transmisión y recuperación afectan la propagación de una epidemia."
    )
    
    parameters = [
        Parameter(
            name="beta",
            display_name="Tasa de transmisión (β)",
            description="Probabilidad de transmisión de la enfermedad por contacto.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=2.0,
            default_value=beta,
            step=0.01
        ),
        Parameter(
            name="gamma",
            display_name="Tasa de recuperación (γ)",
            description="Tasa a la que los infectados se recuperan.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=1.0,
            default_value=gamma,
            step=0.01
        ),
        Parameter(
            name="S0",
            display_name="Susceptibles iniciales",
            description="Número inicial de personas susceptibles.",
            param_type=ParameterType.INTEGER,
            min_value=0,
            max_value=1000,
            default_value=s0
        ),
        Parameter(
            name="I0",
            display_name="Infectados iniciales",
            description="Número inicial de personas infectadas.",
            param_type=ParameterType.INTEGER,
            min_value=0,
            max_value=1000,
            default_value=i0
        )
    ]
    
    questions = [
        f"Calcule el número reproductivo básico R₀ = β/γ. Con los valores actuales, ¿es R₀ > 1? (Valor esperado: {r0_basic:.2f})",
        "Observe el pico de la curva de infectados. ¿Cómo cambia si duplica la tasa de recuperación γ?",
        "¿Qué sucede con la población de Susceptibles a largo plazo? ¿Llega siempre a cero?"
    ]
    
    return Exercise(
        id=f"sir_{random.randint(1000, 9999)}",
        name="Dinámica de Epidemias SIR",
        main_topic="Modelo SIR",
        educational_objective="Comprender el concepto de umbral epidémico y R₀.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.SIMULACION,
        activity_description="Ajuste los parámetros β y γ para simular diferentes escenarios epidémicos.",
        analysis_questions=questions,
        expected_observation="Si R₀ > 1, se observará un brote epidémico (aumento inicial de I). Si R₀ < 1, la enfermedad desaparece sin brote.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.INTERMEDIO, category="Biología")
    )

def _generate_lorenz() -> Exercise:
    sigma = 10.0
    beta = 8.0/3.0
    rho = round(random.uniform(20.0, 35.0), 1)
    
    description = (
        "El sistema de Lorenz es un modelo simplificado de convección atmosférica que exhibe "
        "comportamiento caótico. Es famoso por su atractor en forma de mariposa."
    )
    
    parameters = [
        Parameter(
            name="sigma",
            display_name="Número de Prandtl (σ)",
            description="Relación entre viscosidad y difusividad térmica.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=50.0,
            default_value=sigma,
            step=0.1
        ),
        Parameter(
            name="rho",
            display_name="Número de Rayleigh (ρ)",
            description="Parámetro de control relacionado con la diferencia de temperatura.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=100.0,
            default_value=rho,
            step=0.1
        ),
        Parameter(
            name="beta",
            display_name="Parámetro geométrico (β)",
            description="Relacionado con las dimensiones físicas de la capa de fluido.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=10.0,
            default_value=beta,
            step=0.01
        )
    ]
    
    questions = [
        "¿El sistema converge a un punto fijo o oscila indefinidamente?",
        f"Con ρ = {rho}, ¿observa el atractor de mariposa característico?",
        "Cambie ligeramente las condiciones iniciales. ¿Las trayectorias se mantienen juntas o divergen?"
    ]
    
    return Exercise(
        id=f"lorenz_{random.randint(1000, 9999)}",
        name="Caos en el Atractor de Lorenz",
        main_topic="Atractor de Lorenz",
        educational_objective="Identificar la sensibilidad a las condiciones iniciales (efecto mariposa).",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Explore el espacio de fases 3D variando el parámetro ρ.",
        analysis_questions=questions,
        expected_observation="Para ρ > 24.74, se espera observar un atractor extraño caótico donde las trayectorias nunca se repiten.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.AVANZADO, category="Física")
    )

def _generate_van_der_pol() -> Exercise:
    mu = round(random.uniform(0.5, 4.0), 1)
    
    description = (
        "El oscilador de Van der Pol es un sistema no conservativo con amortiguamiento no lineal. "
        "Exhibe oscilaciones de ciclo límite estables."
    )
    
    parameters = [
        Parameter(
            name="mu",
            display_name="Parámetro de amortiguamiento (μ)",
            description="Controla la no linealidad y la forma del ciclo límite.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=10.0,
            default_value=mu,
            step=0.1
        ),
        Parameter(
            name="x0",
            display_name="Posición inicial",
            description="Valor inicial de x.",
            param_type=ParameterType.FLOAT,
            min_value=-5.0,
            max_value=5.0,
            default_value=1.0,
            step=0.1
        )
    ]
    
    questions = [
        f"Con μ = {mu}, ¿la oscilación es sinusoidal o tiene forma de relajación?",
        "¿El sistema converge al mismo ciclo límite independientemente de la posición inicial?",
        "¿Qué sucede con el periodo de oscilación al aumentar μ?"
    ]
    
    return Exercise(
        id=f"vdp_{random.randint(1000, 9999)}",
        name="Ciclos Límite de Van der Pol",
        main_topic="Oscilador de Van der Pol",
        educational_objective="Comprender el concepto de ciclo límite y auto-oscilación.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Observe la convergencia de las trayectorias hacia el ciclo límite en el plano de fase.",
        analysis_questions=questions,
        expected_observation="Todas las trayectorias (excepto el origen) convergen a una órbita cerrada única (ciclo límite).",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.INTERMEDIO, category="Física")
    )

def _generate_hopf() -> Exercise:
    mu_val = round(random.uniform(-1.0, 1.0), 1)
    
    description = (
        "La bifurcación de Hopf describe la aparición de una órbita periódica (ciclo límite) "
        "a partir de un punto de equilibrio cuando un parámetro varía."
    )
    
    parameters = [
        Parameter(
            name="mu",
            display_name="Parámetro de bifurcación (μ)",
            description="Controla la estabilidad del origen y la aparición del ciclo límite.",
            param_type=ParameterType.FLOAT,
            min_value=-2.0,
            max_value=2.0,
            default_value=mu_val,
            step=0.1
        ),
        Parameter(
            name="omega",
            display_name="Frecuencia (ω)",
            description="Frecuencia angular de la oscilación.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=5.0,
            default_value=1.0,
            step=0.1
        )
    ]
    
    questions = [
        f"Para el valor actual μ = {mu_val}, ¿el origen es estable o inestable?",
        "Encuentre el valor crítico de μ donde comienza la oscilación sostenida.",
        "¿Cómo varía la amplitud de la oscilación al aumentar μ por encima de cero?"
    ]
    
    return Exercise(
        id=f"hopf_{random.randint(1000, 9999)}",
        name="Bifurcación de Hopf",
        main_topic="Bifurcación de Hopf",
        educational_objective="Visualizar la transición de un punto fijo estable a un ciclo límite.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Varíe μ de negativo a positivo y observe el cambio cualitativo en el comportamiento.",
        analysis_questions=questions,
        expected_observation="Para μ < 0, las trayectorias espiralan hacia el origen. Para μ > 0, convergen a un ciclo límite circular.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.AVANZADO, category="Matemáticas")
    )

def _generate_rlc() -> Exercise:
    r_val = random.randint(5, 50)
    l_val = round(random.uniform(0.1, 1.0), 2)
    c_val = round(random.uniform(0.001, 0.01), 3)
    
    description = (
        "Un circuito RLC serie consta de una resistencia, un inductor y un capacitor. "
        "La energía oscila entre el campo magnético del inductor y el campo eléctrico del capacitor."
    )
    
    parameters = [
        Parameter(
            name="R",
            display_name="Resistencia (R)",
            description="Resistencia en Ohmios.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=100.0,
            default_value=r_val,
            unit="Ω"
        ),
        Parameter(
            name="L",
            display_name="Inductancia (L)",
            description="Inductancia en Henrios.",
            param_type=ParameterType.FLOAT,
            min_value=0.01,
            max_value=5.0,
            default_value=l_val,
            unit="H"
        ),
        Parameter(
            name="C",
            display_name="Capacitancia (C)",
            description="Capacitancia en Faradios.",
            param_type=ParameterType.FLOAT,
            min_value=0.0001,
            max_value=0.1,
            default_value=c_val,
            unit="F"
        )
    ]
    
    questions = [
        "¿El sistema está subamortiguado, críticamente amortiguado o sobreamortiguado?",
        "Calcule la frecuencia de resonancia teórica. ¿Coincide con la frecuencia de oscilación observada?",
        "¿Qué sucede con la amplitud de la corriente si reduce la resistencia R?"
    ]
    
    return Exercise(
        id=f"rlc_{random.randint(1000, 9999)}",
        name="Oscilaciones en Circuito RLC",
        main_topic="Circuito RLC",
        educational_objective="Analizar la respuesta transitoria de un circuito de segundo orden.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.SIMULACION,
        activity_description="Modifique R, L y C para observar diferentes regímenes de amortiguamiento.",
        analysis_questions=questions,
        expected_observation="Dependiendo de R, se observarán oscilaciones amortiguadas (subamortiguado) o un decaimiento exponencial sin oscilación (sobreamortiguado).",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.BASICO, category="Electrónica")
    )

def _generate_logistic() -> Exercise:
    r = round(random.uniform(0.1, 0.5), 2)
    k = random.randint(500, 1500)
    n0 = random.randint(10, 100)
    
    description = (
        "El modelo logístico describe el crecimiento de una población limitada por recursos. "
        "Incluye una tasa de crecimiento y una capacidad de carga."
    )
    
    parameters = [
        Parameter(
            name="r",
            display_name="Tasa de crecimiento (r)",
            description="Tasa intrínseca de crecimiento poblacional.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=1.0,
            default_value=r
        ),
        Parameter(
            name="K",
            display_name="Capacidad de carga (K)",
            description="Población máxima que el entorno puede sostener.",
            param_type=ParameterType.INTEGER,
            min_value=100,
            max_value=2000,
            default_value=k
        ),
        Parameter(
            name="N0",
            display_name="Población inicial",
            description="Número inicial de individuos.",
            param_type=ParameterType.INTEGER,
            min_value=1,
            max_value=2000,
            default_value=n0
        )
    ]
    
    questions = [
        f"¿Hacia qué valor tiende la población cuando t → ∞? (Valor esperado: {k})",
        "¿Qué sucede si la población inicial N0 es mayor que la capacidad de carga K?",
        "¿Cómo afecta el valor de r a la velocidad con la que se alcanza el equilibrio?"
    ]
    
    return Exercise(
        id=f"log_{random.randint(1000, 9999)}",
        name="Crecimiento Poblacional Logístico",
        main_topic="Modelo Logístico",
        educational_objective="Entender el concepto de capacidad de carga y crecimiento limitado.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.GRAFICACION,
        activity_description="Simule el crecimiento poblacional y analice la curva sigmoidea.",
        analysis_questions=questions,
        expected_observation="La población crecerá (o decrecerá) hasta estabilizarse en el valor de K.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.BASICO, category="Biología")
    )

def _generate_verhulst() -> Exercise:
    r = round(random.uniform(2.5, 3.9), 2)
    
    description = (
        "El mapa logístico (o de Verhulst) es una ecuación en diferencias simple que puede "
        "exhibir comportamiento muy complejo, desde estabilidad hasta caos."
    )
    
    parameters = [
        Parameter(
            name="r",
            display_name="Parámetro de tasa (r)",
            description="Parámetro de control que determina el comportamiento del sistema.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=4.0,
            default_value=r,
            step=0.01
        ),
        Parameter(
            name="x0",
            display_name="Población inicial (x0)",
            description="Población inicial normalizada (entre 0 y 1).",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=1.0,
            default_value=0.5,
            step=0.01
        )
    ]
    
    questions = [
        f"Para r = {r}, ¿el sistema converge a un valor fijo, oscila o es caótico?",
        "Encuentre un valor de r para el cual la población oscile entre 2 valores (periodo 2).",
        "¿Qué sucede con el comportamiento del sistema cuando r supera 3.57?"
    ]
    
    return Exercise(
        id=f"verhulst_{random.randint(1000, 9999)}",
        name="Caos en el Mapa Logístico",
        main_topic="Mapa de Verhulst",
        educational_objective="Explorar el camino al caos mediante duplicación de periodo.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.SIMULACION,
        activity_description="Varíe r y observe el diagrama de bifurcación o la serie temporal.",
        analysis_questions=questions,
        expected_observation="Dependiendo de r, se verán puntos fijos, ciclos de periodo 2, 4, 8... o caos determinista.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.INTERMEDIO, category="Matemáticas")
    )

def _generate_orbits() -> Exercise:
    v_y = round(random.uniform(0.8, 1.3), 2)
    
    description = (
        "Simulación del movimiento de un cuerpo bajo la influencia gravitatoria de una masa central "
        "(Problema de los dos cuerpos/Kepler)."
    )
    
    parameters = [
        Parameter(
            name="vy0",
            display_name="Velocidad tangencial inicial",
            description="Velocidad inicial perpendicular al radio vector.",
            param_type=ParameterType.FLOAT,
            min_value=0.5,
            max_value=2.0,
            default_value=v_y,
            step=0.1
        ),
        Parameter(
            name="x0",
            display_name="Distancia inicial",
            description="Distancia inicial al centro de atracción.",
            param_type=ParameterType.FLOAT,
            min_value=0.5,
            max_value=2.0,
            default_value=1.0,
            step=0.1
        )
    ]
    
    questions = [
        f"Con la velocidad inicial dada, ¿la órbita es circular, elíptica o abierta?",
        "¿Se conserva la energía total del sistema durante la simulación?",
        "¿Qué sucede si la velocidad inicial es menor que la necesaria para una órbita circular?"
    ]
    
    return Exercise(
        id=f"orbit_{random.randint(1000, 9999)}",
        name="Órbitas Planetarias",
        main_topic="Mecánica Orbital",
        educational_objective="Visualizar las leyes de Kepler y la conservación de la energía.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.SIMULACION,
        activity_description="Ajuste la velocidad inicial para obtener diferentes tipos de órbitas.",
        analysis_questions=questions,
        expected_observation="Se observarán elipses cerradas para energías negativas y trayectorias abiertas para energías positivas.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.INTERMEDIO, category="Física")
    )

def _generate_dampers() -> Exercise:
    m = round(random.uniform(0.5, 2.0), 1)
    k = round(random.uniform(1.0, 5.0), 1)
    c = round(random.uniform(0.1, 3.0), 1)
    
    description = (
        "Sistema masa-resorte-amortiguador. Estudia cómo la fricción (amortiguamiento) "
        "afecta el movimiento oscilatorio."
    )
    
    parameters = [
        Parameter(
            name="m",
            display_name="Masa (m)",
            description="Masa del objeto oscilante.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=10.0,
            default_value=m,
            unit="kg"
        ),
        Parameter(
            name="k",
            display_name="Constante del resorte (k)",
            description="Rigidez del resorte.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=20.0,
            default_value=k,
            unit="N/m"
        ),
        Parameter(
            name="c",
            display_name="Coeficiente de amortiguamiento (c)",
            description="Resistencia viscosa al movimiento.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=10.0,
            default_value=c,
            unit="Ns/m"
        )
    ]
    
    questions = [
        "Calcule el coeficiente de amortiguamiento crítico c_crit = 2√(km).",
        f"¿El sistema está subamortiguado (c < c_crit) o sobreamortiguado (c > c_crit)?",
        "¿Cómo cambia la frecuencia de oscilación al aumentar la masa m?"
    ]
    
    return Exercise(
        id=f"damper_{random.randint(1000, 9999)}",
        name="Oscilador Amortiguado",
        main_topic="Mecánica Clásica",
        educational_objective="Distinguir entre movimiento subamortiguado, crítico y sobreamortiguado.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.GRAFICACION,
        activity_description="Encuentre el valor de c que produce el retorno al equilibrio más rápido (amortiguamiento crítico).",
        analysis_questions=questions,
        expected_observation="La amplitud de las oscilaciones decaerá exponencialmente con el tiempo.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.BASICO, category="Física")
    )

def _generate_newton_cooling() -> Exercise:
    t_env = random.randint(15, 25)
    t0 = random.randint(70, 95)
    k = round(random.uniform(0.05, 0.2), 3)
    
    description = (
        "La Ley de Enfriamiento de Newton establece que la tasa de cambio de temperatura de un objeto "
        "es proporcional a la diferencia de temperatura con el ambiente."
    )
    
    parameters = [
        Parameter(
            name="T_env",
            display_name="Temperatura ambiente",
            description="Temperatura del entorno constante.",
            param_type=ParameterType.FLOAT,
            min_value=-20.0,
            max_value=40.0,
            default_value=float(t_env),
            unit="°C"
        ),
        Parameter(
            name="T0",
            display_name="Temperatura inicial",
            description="Temperatura inicial del objeto.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=100.0,
            default_value=float(t0),
            unit="°C"
        ),
        Parameter(
            name="k",
            display_name="Constante de enfriamiento (k)",
            description="Constante de proporcionalidad que depende del material y geometría.",
            param_type=ParameterType.FLOAT,
            min_value=0.01,
            max_value=1.0,
            default_value=k,
            step=0.01
        )
    ]
    
    questions = [
        f"¿Cuánto tiempo tomará aproximadamente para que la temperatura baje a la mitad de la diferencia inicial?",
        "¿La temperatura del objeto llegará a ser menor que la temperatura ambiente?",
        "Si duplica k, ¿el objeto se enfría más rápido o más lento?"
    ]
    
    return Exercise(
        id=f"newton_{random.randint(1000, 9999)}",
        name="Ley de Enfriamiento de Newton",
        main_topic="Termodinámica",
        educational_objective="Modelar procesos de decaimiento exponencial.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.GRAFICACION,
        activity_description="Simule el enfriamiento y determine la constante de tiempo del sistema.",
        analysis_questions=questions,
        expected_observation="La temperatura decaerá exponencialmente acercándose asintóticamente a la temperatura ambiente.",
        metadata=ExerciseMetadata(difficulty=DifficultyLevel.BASICO, category="Física")
    )
