import random
import numpy as np
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
        'newton': _generate_newton_cooling,
        # Nuevos ejercicios adicionales
        'sir_avanzado': _generate_sir_advanced,
        'sir_control': _generate_sir_control,
        'lorenz_comparacion': _generate_lorenz_comparison,
        'lorenz_lyapunov': _generate_lorenz_lyapunov,
        'vdp_forzado': _generate_vdp_forced,
        'vdp_acoplado': _generate_vdp_coupled,
        'hopf_subcritico': _generate_hopf_subcritical,
        'hopf_variaciones': _generate_hopf_variations,
        'rlc_forzado': _generate_rlc_forced,
        'rlc_paralelo': _generate_rlc_parallel,
        'logistica_cosecha': _generate_logistic_harvesting,
        'logistica_allee': _generate_logistic_allee,
        'verhulst_ventanas': _generate_verhulst_windows,
        'verhulst_feigenbaum': _generate_verhulst_feigenbaum,
        'orbitas_elipticas': _generate_orbits_elliptical,
        'orbitas_transferencia': _generate_orbits_transfer,
        'amortiguador_forzado': _generate_damper_forced,
        'amortiguador_doble': _generate_damper_double,
        'newton_calentamiento': _generate_newton_heating,
        'newton_multicuerpo': _generate_newton_multibody
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
    # Variaciones aleatorias para mayor diversidad
    scenario = random.choice(['epidemic', 'endemic', 'vaccination', 'seasonal'])
    
    if scenario == 'epidemic':
        beta = round(random.uniform(0.4, 0.8), 2)
        gamma = round(random.uniform(0.05, 0.2), 2)
        s0 = random.randint(9500, 9900)
        i0 = random.randint(10, 100)
        description = (
            "Simulación de un brote epidémico agudo. El modelo SIR divide la población en tres "
            "compartimentos: Susceptibles (S), Infectados (I) y Recuperados (R). En este escenario, "
            "una pequeña cantidad de infectados puede generar un gran brote si R₀ > 1."
        )
    elif scenario == 'endemic':
        beta = round(random.uniform(0.2, 0.4), 2)
        gamma = round(random.uniform(0.15, 0.3), 2)
        s0 = random.randint(8000, 9000)
        i0 = random.randint(50, 200)
        description = (
            "Simulación de una enfermedad endémica con presencia constante en la población. "
            "Este escenario explora cómo la enfermedad persiste cuando hay un equilibrio entre "
            "nuevos casos y recuperaciones."
        )
    elif scenario == 'vaccination':
        beta = round(random.uniform(0.5, 0.7), 2)
        gamma = round(random.uniform(0.1, 0.2), 2)
        vac_rate = random.uniform(0.3, 0.7)
        s0 = int(random.randint(9000, 9800) * (1 - vac_rate))
        i0 = random.randint(20, 50)
        description = (
            f"Escenario con vacunación previa (~{vac_rate*100:.0f}% de la población inmunizada). "
            "Observe cómo la inmunidad de rebaño puede prevenir brotes masivos incluso con "
            "tasas de transmisión relativamente altas."
        )
    else:  # seasonal
        beta = round(random.uniform(0.3, 0.6), 2)
        gamma = round(random.uniform(0.1, 0.25), 2)
        s0 = random.randint(9200, 9700)
        i0 = random.randint(15, 60)
        description = (
            "Simulación de una enfermedad estacional. Analice cómo pequeños cambios en la "
            "tasa de transmisión pueden alterar significativamente la magnitud del brote."
        )
    
    r0_basic = beta / gamma
    peak_time_estimate = (1/gamma) * np.log(s0 * beta / gamma) if r0_basic > 1 else 0
    
    parameters = [
        Parameter(
            name="beta",
            display_name="Tasa de transmisión (β)",
            description="Probabilidad de transmisión de la enfermedad por contacto entre susceptibles e infectados.",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=2.0,
            default_value=beta,
            step=0.01,
            unit="1/día"
        ),
        Parameter(
            name="gamma",
            display_name="Tasa de recuperación (γ)",
            description="Tasa a la que los infectados se recuperan (inverso del período infeccioso).",
            param_type=ParameterType.FLOAT,
            min_value=0.0,
            max_value=1.0,
            default_value=gamma,
            step=0.01,
            unit="1/día"
        ),
        Parameter(
            name="S0",
            display_name="Susceptibles iniciales (S₀)",
            description="Número inicial de personas susceptibles a la enfermedad.",
            param_type=ParameterType.INTEGER,
            min_value=0,
            max_value=10000,
            default_value=s0
        ),
        Parameter(
            name="I0",
            display_name="Infectados iniciales (I₀)",
            description="Número inicial de personas infectadas (casos índice).",
            param_type=ParameterType.INTEGER,
            min_value=1,
            max_value=1000,
            default_value=i0
        ),
        Parameter(
            name="R0",
            display_name="Recuperados iniciales (R₀)",
            description="Número inicial de personas recuperadas o inmunes.",
            param_type=ParameterType.INTEGER,
            min_value=0,
            max_value=10000,
            default_value=10000 - s0 - i0
        )
    ]
    
    questions = [
        f"Calcule el número reproductivo básico R₀ = β/γ. Con β={beta} y γ={gamma}, obtenemos R₀≈{r0_basic:.2f}. ¿Habrá epidemia?",
        "Identifique el momento del pico de infectados. ¿Cuántos días después del inicio ocurre?",
        "¿Qué fracción de la población susceptible nunca se infecta? Compare S(∞) con S(0).",
        f"Si el período infeccioso promedio es 1/γ = {1/gamma:.1f} días, ¿cuántos días dura la fase epidémica activa?",
        "Explique por qué la curva de susceptibles es siempre decreciente mientras que la de infectados tiene un máximo.",
        "¿Qué estrategia sería más efectiva: reducir β (medidas de distanciamiento) o aumentar γ (mejor tratamiento)?"
    ]
    
    return Exercise(
        id=f"sir_{random.randint(1000, 9999)}",
        name=f"Dinámica de Epidemias SIR - {scenario.capitalize()}",
        main_topic="Modelo SIR Epidemiológico",
        educational_objective="Comprender el concepto de umbral epidémico R₀, dinámica de brotes y el impacto de parámetros en la propagación de enfermedades.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.SIMULACION,
        activity_description="Simule la evolución temporal de las tres poblaciones (S, I, R) y analice cómo diferentes valores de β y γ afectan la severidad y duración del brote epidémico.",
        analysis_questions=questions,
        expected_observation=f"Si R₀ = {r0_basic:.2f} > 1, se observará un brote epidémico con un pico de infectados alrededor del día {peak_time_estimate:.0f}. Si R₀ < 1, la enfermedad desaparece exponencialmente sin generar epidemia. La fracción final de susceptibles S(∞)/N depende de R₀ y S₀.",
        metadata=ExerciseMetadata(
            difficulty=DifficultyLevel.INTERMEDIO,
            category="Epidemiología",
            tags=["SIR", "epidemia", "R₀", "salud pública", "enfermedades infecciosas"],
            estimated_time=30
        )
    )

def _generate_lorenz() -> Exercise:
    regime = random.choice(['periodic', 'transient', 'chaotic', 'butterfly'])
    
    sigma = 10.0
    beta = 8.0/3.0
    
    if regime == 'periodic':
        rho = round(random.uniform(10.0, 20.0), 1)
        description = (
            "Sistema de Lorenz en régimen periódico o convergente. Para valores bajos de ρ, "
            "el sistema converge a puntos fijos estables o exhibe oscilaciones periódicas simples. "
            "Este ejercicio demuestra que no todo sistema no-lineal es caótico."
        )
    elif regime == 'transient':
        rho = round(random.uniform(22.0, 25.0), 1)
        description = (
            "Sistema de Lorenz cerca de la transición al caos (ρ ≈ 24.74). En esta zona crítica, "
            "el sistema exhibe comportamiento intermitente alternando entre períodos casi-periódicos "
            "y episodios caóticos."
        )
    elif regime == 'butterfly':
        rho = 28.0
        description = (
            "El clásico atractor de Lorenz con parámetros de Edward Lorenz (1963). Este es el caso "
            "más famoso que reveló el comportamiento caótico en sistemas deterministas. El atractor "
            "tiene forma de mariposa con dos lóbulos en el espacio tridimensional."
        )
    else:  # chaotic
        rho = round(random.uniform(26.0, 40.0), 1)
        description = (
            "Sistema de Lorenz en régimen caótico completo. Las trayectorias nunca se repiten y "
            "exhiben sensibilidad exponencial a las condiciones iniciales (efecto mariposa). Ideal "
            "para estudiar la teoría del caos y atractores extraños."
        )
    
    x0 = round(random.uniform(-2.0, 2.0), 2)
    y0 = round(random.uniform(-2.0, 2.0), 2)
    z0 = round(random.uniform(-2.0, 2.0), 2)
    
    parameters = [
        Parameter(
            name="sigma",
            display_name="Número de Prandtl (σ)",
            description="Relación entre viscosidad cinemática y difusividad térmica del fluido.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=50.0,
            default_value=sigma,
            step=0.1,
            unit=None
        ),
        Parameter(
            name="rho",
            display_name="Número de Rayleigh (ρ)",
            description="Parámetro de control proporcional a la diferencia de temperatura entre placas.",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=100.0,
            default_value=rho,
            step=0.1,
            unit=None
        ),
        Parameter(
            name="beta",
            display_name="Parámetro geométrico (β)",
            description="Relacionado con la razón de aspecto de la capa de fluido (típicamente 8/3).",
            param_type=ParameterType.FLOAT,
            min_value=0.1,
            max_value=10.0,
            default_value=beta,
            step=0.01,
            unit=None
        ),
        Parameter(
            name="x0",
            display_name="Condición inicial x₀",
            description="Valor inicial de la variable de estado x.",
            param_type=ParameterType.FLOAT,
            min_value=-10.0,
            max_value=10.0,
            default_value=x0,
            step=0.1,
            unit=None
        ),
        Parameter(
            name="y0",
            display_name="Condición inicial y₀",
            description="Valor inicial de la variable de estado y.",
            param_type=ParameterType.FLOAT,
            min_value=-10.0,
            max_value=10.0,
            default_value=y0,
            step=0.1,
            unit=None
        ),
        Parameter(
            name="z0",
            display_name="Condición inicial z₀",
            description="Valor inicial de la variable de estado z.",
            param_type=ParameterType.FLOAT,
            min_value=-10.0,
            max_value=10.0,
            default_value=z0,
            step=0.1,
            unit=None
        )
    ]
    
    questions = [
        f"¿Con ρ = {rho}, el sistema exhibe comportamiento periódico, transiente o caótico?",
        "Modifique ligeramente una condición inicial (ej. x₀ → x₀ + 0.001) y compare las trayectorias. ¿Divergen exponencialmente?",
        "¿Cuál es la forma geométrica del atractor en el espacio (x, y, z)?",
        "Identifique el valor crítico ρ_c ≈ 24.74 donde aparece el caos. ¿Qué ocurre por debajo y por encima de este valor?",
        "¿Por qué el sistema de Lorenz, siendo completamente determinista (sin aleatoriedad), produce comportamiento impredecible?",
        "Compare la tasa de separación de trayectorias cercanas. ¿Es constante, lineal o exponencial?"
    ]
    
    return Exercise(
        id=f"lorenz_{random.randint(1000, 9999)}",
        name=f"Atractor de Lorenz - Régimen {regime.capitalize()}",
        main_topic="Sistemas Caóticos y Atractor de Lorenz",
        educational_objective="Comprender el comportamiento caótico, sensibilidad a condiciones iniciales (efecto mariposa), y la estructura de atractores extraños en sistemas deterministas.",
        description=description,
        parameters=parameters,
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Simule el sistema en el espacio de fases tridimensional, visualice el atractor, y experimente con diferentes valores de ρ para observar la transición de comportamiento periódico a caótico.",
        analysis_questions=questions,
        expected_observation=f"Para ρ = {rho}: " + ("el sistema converge a puntos fijos estables" if rho < 13.9 else ("comportamiento periódico o transiente" if rho < 24.74 else "atractor caótico en forma de mariposa con dos lóbulos")),
        metadata=ExerciseMetadata(
            difficulty=DifficultyLevel.AVANZADO,
            category="Física Matemática",
            tags=["caos", "lorenz", "atractor extraño", "convección", "sensibilidad"],
            estimated_time=40
        )
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

# ==================== EJERCICIOS ADICIONALES AVANZADOS ====================

def _generate_sir_advanced() -> Exercise:
    """SIR con tasa de mortalidad y natalidad"""
    beta = round(random.uniform(0.3, 0.6), 2)
    gamma = round(random.uniform(0.1, 0.2), 2)
    mu = round(random.uniform(0.01, 0.05), 3)  # tasa de natalidad/mortalidad
    s0, i0 = random.randint(8000, 9500), random.randint(20, 100)
    
    return Exercise(
        id=f"sir_adv_{random.randint(1000, 9999)}",
        name="Modelo SIR con Demografía (Natalidad/Mortalidad)",
        main_topic="Modelos Epidemiológicos Extendidos",
        educational_objective="Comprender cómo la dinámica poblacional afecta la propagación de enfermedades endémicas a largo plazo.",
        description=f"Extensión del modelo SIR que incluye tasa de natalidad y mortalidad natural (μ={mu}). Permite estudiar equilibrios endémicos donde la enfermedad persiste indefinidamente en la población.",
        parameters=[
            Parameter(
            name="beta",
            display_name="Tasa de transmisión β",
            description="Transmisión",
            param_type=ParameterType.FLOAT,
            default_value=beta,
            min_value=0.0,
            max_value=1.0,
            step=0.01,
            unit="1/día"
        ),
            Parameter(
            name="gamma",
            display_name="Tasa de recuperación γ",
            description="Recuperación",
            param_type=ParameterType.FLOAT,
            default_value=gamma,
            min_value=0.0,
            max_value=0.5,
            step=0.01,
            unit="1/día"
        ),
            Parameter(
            name="mu",
            display_name="Tasa natalidad/mortalidad μ",
            description="Demografía",
            param_type=ParameterType.FLOAT,
            default_value=mu,
            min_value=0.0,
            max_value=0.1,
            step=0.001,
            unit="1/día"
        ),
            Parameter(name="S0", display_name="Susceptibles iniciales", description="", param_type=ParameterType.INTEGER, default_value=s0, min_value=0, max_value=10000),
            Parameter(name="I0", display_name="Infectados iniciales", description="", param_type=ParameterType.INTEGER, default_value=i0, min_value=0, max_value=1000)
        ],
        activity_type=ActivityType.SIMULACION,
        activity_description="Simule a largo plazo y observe si se alcanza un equilibrio endémico (I* > 0) o la enfermedad desaparece.",
        analysis_questions=[
            f"¿Existe equilibrio endémico? Calcule I* = N(1 - γ/β - μ/β) con N=10000",
            "Compare la dinámica con y sin demografía (μ=0 vs μ>0). ¿Cómo cambia el comportamiento a largo plazo?",
            "¿Qué condición sobre β, γ, μ garantiza persistencia endémica?"
        ],
        expected_observation=f"Con μ={mu}, el sistema puede alcanzar equilibrio endémico si R₀=(β/(γ+μ)) > 1. La población se renueva continuamente.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Epidemiología", ["SIR", "endémico", "demografía"], 40)
    )

def _generate_sir_control() -> Exercise:
    """SIR con estrategias de control"""
    beta = round(random.uniform(0.4, 0.7), 2)
    gamma = round(random.uniform(0.1, 0.2), 2)
    control_type = random.choice(['vaccination', 'isolation', 'treatment'])
    control_rate = round(random.uniform(0.1, 0.5), 2)
    
    desc_map = {
        'vaccination': f"Vacunación continua a tasa {control_rate}/día",
        'isolation': f"Aislamiento de infectados reduciendo β efectivo en {control_rate*100}%",
        'treatment': f"Tratamiento aumentando γ en {control_rate}/día"
    }
    
    return Exercise(
        id=f"sir_ctrl_{random.randint(1000, 9999)}",
        name=f"Control de Epidemias - {control_type.title()}",
        main_topic="Estrategias de Control Epidemiológico",
        educational_objective="Evaluar la efectividad de diferentes intervenciones de salud pública.",
        description=f"Modelo SIR con intervención: {desc_map[control_type]}. Analice cómo las estrategias de control alteran la dinámica epidémica.",
        parameters=[
            Parameter(name="beta", display_name="Tasa transmisión β", description="", param_type=ParameterType.FLOAT, default_value=beta, min_value=0.1, max_value=1.0, step=0.01),
            Parameter(name="gamma", display_name="Tasa recuperación γ", description="", param_type=ParameterType.FLOAT, default_value=gamma, min_value=0.05, max_value=0.5, step=0.01),
            Parameter(name="control_rate", display_name=f"Tasa de {control_type}", description="", param_type=ParameterType.FLOAT, default_value=control_rate, min_value=0.0, max_value=1.0, step=0.01),
            Parameter(name="S0", display_name="Susceptibles", description="", param_type=ParameterType.INTEGER, default_value=9500, min_value=7000, max_value=9900),
            Parameter(name="I0", display_name="Infectados", description="", param_type=ParameterType.INTEGER, default_value=50, min_value=10, max_value=200)
        ],
        activity_type=ActivityType.COMPARACION,
        activity_description=f"Compare la evolución con y sin {control_type}. Mida reducción en pico de infectados y tiempo de epidemia.",
        analysis_questions=[
            f"¿Cuánto reduce el pico de infectados la estrategia de {control_type}?",
            "¿Es posible eliminar completamente el brote con esta intervención?",
            "Compare costo-efectividad: ¿qué tasa mínima se necesita para reducir el pico a la mitad?"
        ],
        expected_observation=f"La intervención de {control_type} reduce R₀ efectivo, disminuyendo la severidad del brote.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Salud Pública", ["control", "intervención", "SIR"], 35)
    )

def _generate_lorenz_comparison() -> Exercise:
    """Comparación de trayectorias con CI cercanas"""
    epsilon = round(random.uniform(0.0001, 0.01), 4)
    return Exercise(
        id=f"lorenz_comp_{random.randint(1000, 9999)}",
        name="Sensibilidad Extrema a Condiciones Iniciales",
        main_topic="Teoría del Caos - Efecto Mariposa",
        educational_objective="Cuantificar la divergencia exponencial característica de sistemas caóticos.",
        description=f"Dos trayectorias con condiciones iniciales que difieren en solo ε={epsilon}. Mida cómo la separación crece exponencialmente en el tiempo.",
        parameters=[
            Parameter(name="x0_1", display_name="Primera trayectoria x₀", description="", param_type=ParameterType.FLOAT, default_value=1.0, min_value=-5, max_value=5, step=0.1),
            Parameter(name="x0_2", display_name="Segunda trayectoria x₀", description="", param_type=ParameterType.FLOAT, default_value=1.0+epsilon, min_value=-5, max_value=5, step=0.0001),
            Parameter(name="sigma", display_name="σ", description="", param_type=ParameterType.FLOAT, default_value=10.0, min_value=5, max_value=15, step=0.5),
            Parameter(name="rho", display_name="ρ", description="", param_type=ParameterType.FLOAT, default_value=28.0, min_value=20, max_value=40, step=1.0),
            Parameter(name="beta", display_name="β", description="", param_type=ParameterType.FLOAT, default_value=8/3, min_value=1, max_value=5, step=0.1)
        ],
        activity_type=ActivityType.COMPARACION,
        activity_description="Grafique ambas trayectorias y la distancia entre ellas versus tiempo. Ajuste d(t) ≈ d₀·exp(λt) para estimar el exponente de Lyapunov λ.",
        analysis_questions=[
            f"¿A partir de qué tiempo las trayectorias son completamente diferentes a pesar de iniciar con diferencia ε={epsilon}?",
            "Estime el exponente de Lyapunov λ (para Lorenz clásico: λ ≈ 0.9). ¿Qué significa físicamente?",
            "¿Por qué este fenómeno hace imposible pronósticos del clima a largo plazo?"
        ],
        expected_observation="La separación crece exponencialmente: d(t) ~ e^(λt) con λ>0, demostrando caos determinista.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Caos", ["lyapunov", "divergencia", "mariposa"], 45)
    )

def _generate_lorenz_lyapunov() -> Exercise:
    """Cálculo del espectro de Lyapunov"""
    return Exercise(
        id=f"lorenz_lyap_{random.randint(1000, 9999)}",
        name="Espectro de Exponentes de Lyapunov",
        main_topic="Caracterización Cuantitativa del Caos",
        educational_objective="Calcular los exponentes de Lyapunov para clasificar el comportamiento dinámico.",
        description="El espectro de Lyapunov caracteriza tasas de expansión/contracción en diferentes direcciones. Para Lorenz (σ=10, ρ=28, β=8/3): λ₁≈0.9, λ₂≈0, λ₃≈-14.6.",
        parameters=[
            Parameter(name="sigma", display_name="σ", description="", param_type=ParameterType.FLOAT, default_value=10.0, min_value=5, max_value=20, step=0.5),
            Parameter(name="rho", display_name="ρ", description="", param_type=ParameterType.FLOAT, default_value=28.0, min_value=10, max_value=50, step=1.0),
            Parameter(name="beta", display_name="β", description="", param_type=ParameterType.FLOAT, default_value=8/3, min_value=1, max_value=10, step=0.1),
            Parameter(name="t_transient", display_name="Tiempo transitorio", description="", param_type=ParameterType.FLOAT, default_value=50, min_value=10, max_value=100, step=5),
            Parameter(
            name="t_measure",
            display_name="Tiempo medición",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=500,
            min_value=100,
            max_value=1000,
            step=50
        )
        ],
        activity_type=ActivityType.INTERPRETACION,
        activity_description="Implemente el algoritmo de Benettin et al. para calcular los 3 exponentes de Lyapunov. Verifique λ₁+λ₂+λ₃ = -σ-β-1.",
        analysis_questions=[
            "¿Cuántos exponentes son positivos, cero y negativos? ¿Qué implica para la dimensionalidad del atractor?",
            "Calcule la dimensión de Lyapunov: D_L = 2 + λ₁/|λ₃|. ¿Es fraccionaria?",
            "¿Qué ocurre con el espectro cuando ρ < 24.74 (régimen no-caótico)?"
        ],
        expected_observation="λ₁>0 confirma caos, λ₂≈0 indica dirección neutral (flujo), λ₃<0 contracción disipativa.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Teoría del Caos", ["lyapunov", "atractor", "dimensión"], 60)
    )

def _generate_vdp_forced() -> Exercise:
    """Van der Pol forzado - sincronización"""
    mu = round(random.uniform(1.0, 5.0), 1)
    A = round(random.uniform(0.5, 2.0), 1)
    omega_f = round(random.uniform(0.5, 2.0), 1)
    
    return Exercise(
        id=f"vdp_forced_{random.randint(1000, 9999)}",
        name="Oscilador de Van der Pol Forzado - Sincronización",
        main_topic="Sincronización No-lineal",
        educational_objective="Estudiar el fenómeno de 'entrainment' donde un oscilador auto-sostenido se sincroniza con fuerza externa.",
        description=f"Van der Pol con fuerza externa F(t)={A}·cos({omega_f}t). Dependiendo de A y ω_f, el sistema puede sincronizarse (1:1), exhibir cuasi-periodicidad o caos.",
        parameters=[
            Parameter(name="mu", display_name="μ (no-linealidad)", description="", param_type=ParameterType.FLOAT, default_value=mu, min_value=0.1, max_value=10, step=0.1),
            Parameter(name="A", display_name="Amplitud fuerza", description="", param_type=ParameterType.FLOAT, default_value=A, min_value=0, max_value=5, step=0.1),
            Parameter(name="omega_f", display_name="Frecuencia fuerza ω_f", description="", param_type=ParameterType.FLOAT, default_value=omega_f, min_value=0.1, max_value=5, step=0.1),
            Parameter(name="x0", display_name="x₀", description="", param_type=ParameterType.FLOAT, default_value=0.5, min_value=-3, max_value=3, step=0.1),
            Parameter(
            name="v0",
            display_name="v₀",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=0.0,
            min_value=-3,
            max_value=3,
            step=0.1
        )
        ],
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Grafique x(t), diagrama de fase, y sección de Poincaré. Observe transición de sincronización 1:1 a toro cuasi-periódico a caos.",
        analysis_questions=[
            f"¿El sistema se sincroniza 1:1 con la frecuencia externa ω_f={omega_f}?",
            "Construya diagrama Arnold tongues: regiones (A, ω_f) con sincronización m:n",
            "Identifique ruta al caos: ¿duplicación de período o cuasi-periodicidad?"
        ],
        expected_observation="Para A pequeña: sincronización. A moderada: cuasi-periodicidad (dos frecuencias inconmensurables). A grande: posible caos.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Oscilaciones No-lineales", ["sincronización", "forzado", "arnold"], 50)
    )

def _generate_vdp_coupled() -> Exercise:
    """Dos osciladores Van der Pol acoplados"""
    mu1 = round(random.uniform(1.0, 3.0), 1)
    mu2 = round(random.uniform(1.0, 3.0), 1)
    k = round(random.uniform(0.1, 1.0), 2)
    
    return Exercise(
        id=f"vdp_coup_{random.randint(1000, 9999)}",
        name="Osciladores de Van der Pol Acoplados",
        main_topic="Sincronización Mutua",
        educational_objective="Analizar sincronización espontánea entre osciladores mediante acoplamiento débil.",
        description=f"Dos osciladores Van der Pol (μ₁={mu1}, μ₂={mu2}) acoplados con fuerza k={k}·(x₂-x₁). Demuestra sincronización de Huygens.",
        parameters=[
            Parameter(name="mu1", display_name="μ₁", description="", param_type=ParameterType.FLOAT, default_value=mu1, min_value=0.5, max_value=5, step=0.1),
            Parameter(name="mu2", display_name="μ₂", description="", param_type=ParameterType.FLOAT, default_value=mu2, min_value=0.5, max_value=5, step=0.1),
            Parameter(name="k", display_name="Acoplamiento k", description="", param_type=ParameterType.FLOAT, default_value=k, min_value=0, max_value=2, step=0.05),
            Parameter(name="x1_0", display_name="x₁(0)", description="", param_type=ParameterType.FLOAT, default_value=1.0, min_value=-2, max_value=2, step=0.1),
            Parameter(
            name="x2_0",
            display_name="x₂(0)",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=-0.5,
            min_value=-2,
            max_value=2,
            step=0.1
        )
        ],
        activity_type=ActivityType.SIMULACION,
        activity_description="Grafique x₁(t) y x₂(t), diferencia de fase Δφ(t), y plano (x₁, x₂). Observe transición a sincronización al aumentar k.",
        analysis_questions=[
            "¿Existe un valor crítico k_c por encima del cual los osciladores se sincronizan?",
            f"Con μ₁={mu1} y μ₂={mu2}, ¿los osciladores tienen frecuencias naturales iguales o diferentes?",
            "Mida el tiempo de sincronización τ_sync. ¿Cómo depende de k?"
        ],
        expected_observation="Para k < k_c: desincronizados. Para k > k_c: sincronización en fase y frecuencia (state locking).",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Sistemas Acoplados", ["sincronización", "acoplamiento", "huygens"], 45)
    )

def _generate_hopf_subcritical() -> Exercise:
    """Hopf subcrítica - ciclo límite inestable"""
    return Exercise(
        id=f"hopf_sub_{random.randint(1000, 9999)}",
        name="Bifurcación de Hopf Subcrítica",
        main_topic="Bifurcaciones No-lineales",
        educational_objective="Distinguir entre bifurcaciones supercríticas (suaves) y subcríticas (catastróficas).",
        description="En Hopf subcrítica, al cruzar μ=0 aparece ciclo límite INESTABLE. Coexiste con foco estable, generando bistabilidad y saltos catastróficos.",
        parameters=[
            Parameter(name="mu", display_name="μ", description="", param_type=ParameterType.FLOAT, default_value=0.2, min_value=-1, max_value=1, step=0.05),
            Parameter(name="a", display_name="Parámetro a (no-linealidad)", description="", param_type=ParameterType.FLOAT, default_value=-1, min_value=-5, max_value=0, step=0.1),
            Parameter(name="r0", display_name="Radio inicial", description="", param_type=ParameterType.FLOAT, default_value=0.5, min_value=0, max_value=3, step=0.1),
            Parameter(
            name="theta0",
            display_name="Ángulo inicial",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=0,
            min_value=0,
            max_value=6.28,
            step=0.1
        )
        ],
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Grafique plano de fase para μ<0 y μ>0. Identifique ciclo límite inestable (curva separatriz) y región de atracción del foco.",
        analysis_questions=[
            "¿Qué ocurre con condiciones iniciales dentro vs fuera del ciclo límite inestable?",
            "Compare con Hopf supercrítica: ¿cuál es más 'peligrosa' desde perspectiva de control?",
            "Experimente con perturbaciones: ¿el sistema retorna suavemente o salta abruptamente?"
        ],
        expected_observation="Para μ>0: bistabilidad entre foco estable (r≈0) y ciclo grande estable. Transiciones abruptas (histeresis).",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Bifurcaciones", ["subcrítica", "bistabilidad", "catástrofe"], 50)
    )

def _generate_hopf_variations() -> Exercise:
    """Variaciones del sistema de Hopf"""
    variation = random.choice(['normal', 'detuning', 'parametric'])
    
    desc_map = {
        'normal': "Forma canónica estándar de bifurcación de Hopf",
        'detuning': "Con desintonía: diferentes frecuencias en cada eje",
        'parametric': "Hopf paramétrico: frecuencia depende de amplitud"
    }
    
    return Exercise(
        id=f"hopf_var_{random.randint(1000, 9999)}",
        name=f"Variante de Hopf - {variation.title()}",
        main_topic="Formas Normales de Bifurcaciones",
        educational_objective="Explorar variaciones de la bifurcación de Hopf y sus aplicaciones.",
        description=desc_map[variation],
        parameters=[
            Parameter(name="mu", display_name="μ", description="", param_type=ParameterType.FLOAT, default_value=0.5, min_value=-1.5, max_value=1.5, step=0.1),
            Parameter(name="omega", display_name="ω₀", description="", param_type=ParameterType.FLOAT, default_value=1.0, min_value=0.5, max_value=3, step=0.1),
            Parameter(name="delta", display_name="δ (desintonía)", description="", param_type=ParameterType.FLOAT, default_value=0.0, min_value=-0.5, max_value=0.5, step=0.05),
            Parameter(
            name="c",
            display_name="c (no-linealidad)",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=-1,
            min_value=-2,
            max_value=2,
            step=0.1
        )
        ],
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Analice cómo las variaciones afectan forma y estabilidad del ciclo límite.",
        analysis_questions=[
            "¿El ciclo límite es perfectamente circular o tiene deformación?",
            "¿Cómo afecta la desintonía δ a la frecuencia de oscilación?",
            "Mida dependencia de frecuencia con amplitud: ω(A) = ω₀ + c·A²"
        ],
        expected_observation=f"Variante {variation} modifica la forma canónica, introduciendo nuevos fenómenos dinámicos.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Análisis No-lineal", ["hopf", "formas normales"], 40)
    )

def _generate_rlc_forced() -> Exercise:
    """RLC con fuerza externa - resonancia"""
    L, C = 0.1, 0.001
    omega_0 = 1/np.sqrt(L*C)
    R = round(random.uniform(5, 20), 1)
    V_ac = round(random.uniform(5, 15), 1)
    omega_drive = round(omega_0 * random.uniform(0.5, 1.5), 1)
    
    return Exercise(
        id=f"rlc_forced_{random.randint(1000, 9999)}",
        name="Resonancia en Circuito RLC Forzado",
        main_topic="Resonancia Eléctrica",
        educational_objective="Estudiar curvas de resonancia, factor Q, y ancho de banda en circuitos RLC.",
        description=f"Circuito RLC excitado por voltaje AC: V(t)={V_ac}·sin({omega_drive}t). Frecuencia natural ω₀={omega_0:.1f} rad/s.",
        parameters=[
            Parameter(
            name="R",
            display_name="R",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=R,
            min_value=1,
            max_value=50,
            step=1,
            unit="Ω"
        ),
            Parameter(
            name="L",
            display_name="L",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=L,
            min_value=0.01,
            max_value=1,
            step=0.01,
            unit="H"
        ),
            Parameter(
            name="C",
            display_name="C",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=C,
            min_value=0.0001,
            max_value=0.01,
            step=0.0001,
            unit="F"
        ),
            Parameter(
            name="V_ac",
            display_name="V_AC",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=V_ac,
            min_value=1,
            max_value=30,
            step=1,
            unit="V"
        ),
            Parameter(
            name="omega_drive",
            display_name="ω_drive",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=omega_drive,
            min_value=10,
            max_value=200,
            step=5,
            unit="rad/s"
        )
        ],
        activity_type=ActivityType.GRAFICACION,
        activity_description="Grafique amplitud de corriente vs frecuencia (curva de resonancia). Identifique pico en ω₀ y mida ancho de banda Δω.",
        analysis_questions=[
            f"¿En qué frecuencia ocurre resonancia? Compare con ω₀={omega_0:.1f}",
            f"Calcule Q = ω₀L/R = {omega_0*L/R:.1f}. ¿Es resonador de alta o baja calidad?",
            "Mida ancho de banda Δω (entre puntos a 1/√2 del máximo). Verifique Q ≈ ω₀/Δω"
        ],
        expected_observation="Pico de corriente en ω≈ω₀. Mayor Q implica pico más agudo y mayor selectividad frecuencial.",
        metadata=ExerciseMetadata(DifficultyLevel.INTERMEDIO, "Circuitos AC", ["resonancia", "Q", "filtros"], 35)
    )

def _generate_rlc_parallel() -> Exercise:
    """Circuito RLC paralelo"""
    R = round(random.uniform(100, 1000), 0)
    L = round(random.uniform(0.01, 0.5), 3)
    C = round(random.uniform(0.001, 0.01), 4)
    I0 = round(random.uniform(0.1, 1.0), 2)
    
    return Exercise(
        id=f"rlc_par_{random.randint(1000, 9999)}",
        name="Circuito RLC Paralelo",
        main_topic="Circuitos Resonantes Paralelos",
        educational_objective="Contrastar comportamiento serie vs paralelo. Circuito tanque.",
        description=f"Configuración paralela: R, L, C en paralelo con fuente de corriente I₀={I0}A. Dual del circuito serie.",
        parameters=[
            Parameter(
            name="R",
            display_name="R",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=R,
            min_value=10,
            max_value=2000,
            step=10,
            unit="Ω"
        ),
            Parameter(
            name="L",
            display_name="L",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=L,
            min_value=0.001,
            max_value=1,
            step=0.001,
            unit="H"
        ),
            Parameter(
            name="C",
            display_name="C",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=C,
            min_value=0.0001,
            max_value=0.1,
            step=0.0001,
            unit="F"
        ),
            Parameter(
            name="I0",
            display_name="I₀",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=I0,
            min_value=0.01,
            max_value=2,
            step=0.01,
            unit="A"
        )
        ],
        activity_type=ActivityType.COMPARACION,
        activity_description="Compare respuesta en frecuencia: serie (mínima impedancia en resonancia) vs paralelo (máxima impedancia).",
        analysis_questions=[
            "¿En resonancia, la impedancia es mínima o máxima?",
            "Aplicación: ¿por qué circuitos tanque se usan en osciladores RF?",
            "Calcule impedancia compleja Z(ω) y grafique |Z| vs ω"
        ],
        expected_observation="En ω₀: Z_paralelo → máximo (circuito tanque). Energía oscila entre L y C con mínima disipación en R.",
        metadata=ExerciseMetadata(DifficultyLevel.INTERMEDIO, "Electrónica", ["paralelo", "tanque", "oscilador"], 30)
    )

def _generate_logistic_harvesting() -> Exercise:
    """Modelo logístico con cosecha"""
    r = round(random.uniform(0.2, 0.5), 2)
    K = random.randint(500, 1500)
    h = round(random.uniform(10, 100), 1)
    
    return Exercise(
        id=f"log_harv_{random.randint(1000, 9999)}",
        name="Crecimiento Logístico con Cosecha Constante",
        main_topic="Manejo de Recursos Renovables",
        educational_objective="Determinar niveles de cosecha sostenible y detectar colapso poblacional.",
        description=f"Población con crecimiento logístico sometida a cosecha constante h={h} individuos/año. Modelo fundamental en pesca y silvicultura.",
        parameters=[
            Parameter(
            name="r",
            display_name="Tasa crecimiento r",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=r,
            min_value=0.05,
            max_value=1,
            step=0.01
        ),
            Parameter(name="K", display_name="Capacidad carga K", description="", param_type=ParameterType.INTEGER, default_value=K, min_value=100, max_value=2000),
            Parameter(
            name="h",
            display_name="Cosecha h",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=h,
            min_value=0,
            max_value=200,
            step=1
        ),
            Parameter(name="N0", display_name="Población inicial", description="", param_type=ParameterType.INTEGER, default_value=int(K*0.7), min_value=50, max_value=1500)
        ],
        activity_type=ActivityType.SIMULACION,
        activity_description="Varíe h y observe: h pequeña (sostenible), h=h_max (inestable), h>h_max (extinción).",
        analysis_questions=[
            f"Calcule h_max = rK/4 = {r*K/4:.1f}. ¿Qué ocurre si h > h_max?",
            "Identifique dos equilibrios N* cuando h < h_max. ¿Cuál es estable?",
            "¿Cuál es la estrategia óptima: cosechar cerca de K o cerca de K/2?"
        ],
        expected_observation="h_max es rendimiento máximo sostenible (MSY). Por encima: colapso catastrófico a extinción.",
        metadata=ExerciseMetadata(DifficultyLevel.INTERMEDIO, "Ecología", ["cosecha", "sostenibilidad", "MSY"], 35)
    )

def _generate_logistic_allee() -> Exercise:
    """Efecto Allee - crecimiento deprimido a baja densidad"""
    r = round(random.uniform(0.3, 0.6), 2)
    K = random.randint(800, 1500)
    A = round(random.uniform(0.1, 0.4), 2) * K  # umbral Allee
    
    return Exercise(
        id=f"log_allee_{random.randint(1000, 9999)}",
        name="Efecto Allee en Dinámica Poblacional",
        main_topic="Crecimiento con Umbral Crítico",
        educational_objective="Comprender crecimiento negativo a bajas densidades (cooperación, apareamiento).",
        description=f"Modelo con efecto Allee: umbral A={A:.0f}. Por debajo, crecimiento negativo → extinción. Arriba, crecimiento hacia K={K}.",
        parameters=[
            Parameter(
            name="r",
            display_name="Tasa r",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=r,
            min_value=0.1,
            max_value=1,
            step=0.05
        ),
            Parameter(name="K", display_name="Capacidad K", description="", param_type=ParameterType.INTEGER, default_value=K, min_value=500, max_value=2000),
            Parameter(name="A", display_name="Umbral Allee A", description="", param_type=ParameterType.FLOAT, default_value=A, min_value=50, max_value=K*0.5, step=10),
            Parameter(name="N0", display_name="N₀", description="", param_type=ParameterType.INTEGER, default_value=int(A*1.2), min_value=10, max_value=K)
        ],
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Grafique dN/dt vs N. Identifique tres equilibrios: 0 (estable), A (inestable), K (estable).",
        analysis_questions=[
            "¿Qué ocurre si N₀ < A versus N₀ > A?",
            "Aplicación: ¿por qué especies en peligro pueden extinguirse incluso si N>0?",
            "Compare con logístico estándar (sin Allee): ¿cuál es más resiliente?"
        ],
        expected_observation="Bistabilidad: atracción hacia N=0 si N<A, hacia N=K si N>A. Explica extinciones en especies raras.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Biología de Conservación", ["allee", "extinción", "umbral"], 40)
    )

# Funciones auxiliares para ejercicios restantes
def _generate_verhulst_windows():
    """Ventanas periódicas en el mapa logístico"""
    r = round(random.uniform(3.6, 3.9), 3)
    return Exercise(
        id=f"verh_wind_{random.randint(1000, 9999)}",
        name="Ventanas Periódicas en Régimen Caótico",
        main_topic="Estructura Fina del Caos",
        educational_objective="Descubrir islas de periodicidad dentro del régimen caótico del mapa logístico.",
        description=f"Para r={r} (zona caótica), busque 'ventanas' periódicas: valores de r donde reaparece comportamiento regular (período 3, 5, etc.).",
        parameters=[
            Parameter(
            name="r",
            display_name="Parámetro r",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=r,
            min_value=3.5,
            max_value=4.0,
            step=0.001
        ),
            Parameter(
            name="x0",
            display_name="x₀",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=0.5,
            min_value=0,
            max_value=1,
            step=0.01
        ),
            Parameter(name="n_iterations", display_name="Iteraciones", description="", param_type=ParameterType.INTEGER, default_value=500, min_value=100, max_value=1000)
        ],
        activity_type=ActivityType.INTERPRETACION,
        activity_description="Construya diagrama de bifurcación fino cerca de r≈3.83 (ventana de período 3). Teorema de Sharkovskii predice orden de aparición.",
        analysis_questions=[
            "¿Encuentra ventanas periódicas dentro del caos?",
            "La ventana período-3 (r≈3.83): ¿es estable?",
            "¿Qué fracción del intervalo [3.57, 4] corresponde a caos vs periodicidad?"
        ],
        expected_observation="Estructura fractal: ventanas periódicas embebidas en caos. Cada ventana tiene su propia cascada de bifurcaciones.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Caos Discreto", ["ventanas", "sharkovskii", "fractal"], 50)
    )

def _generate_verhulst_feigenbaum():
    """Constante de Feigenbaum - universalidad"""
    return Exercise(
        id=f"verh_feig_{random.randint(1000, 9999)}",
        name="Constante de Feigenbaum y Universalidad",
        main_topic="Ruta al Caos por Duplicación de Período",
        educational_objective="Medir la constante de Feigenbaum δ≈4.669 que caracteriza duplicaciones de período en sistemas no-lineales.",
        description="Secuencia de bifurcaciones período 1→2→4→8→16... Razón entre intervalos sucesivos converge a δ (constante universal).",
        parameters=[
            Parameter(
            name="precision",
            display_name="Precisión r",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=0.001,
            min_value=0.0001,
            max_value=0.01,
            step=0.0001
        ),
            Parameter(name="max_period", display_name="Período máximo", description="", param_type=ParameterType.INTEGER, default_value=128, min_value=16, max_value=512)
        ],
        activity_type=ActivityType.GRAFICACION,
        activity_description="Detecte r_n donde ocurren bifurcaciones período-2^n. Calcule δ_n = (r_n-1 - r_n-2)/(r_n - r_n-1). Verifique convergencia a δ≈4.669.",
        analysis_questions=[
            "Mida r₁ (bifurcación 1→2), r₂ (2→4), r₃ (4→8). Calcule δ₂ y δ₃.",
            "¿Por qué δ es universal (mismo valor para distintas funciones unimodales)?",
            "Estime r_∞ (acumulación de bifurcaciones). Compare con r_∞≈3.5699"
        ],
        expected_observation="δ_n → δ ≈ 4.6692... (constante de Feigenbaum). Demuestra universalidad en transición al caos.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Universalidad", ["feigenbaum", "bifurcación", "scaling"], 60)
    )

def _generate_orbits_elliptical():
    """Órbitas elípticas - elementos orbitales"""
    e = round(random.uniform(0.1, 0.7), 2)  # excentricidad
    a = round(random.uniform(1.0, 2.5), 1)  # semieje mayor
    
    return Exercise(
        id=f"orbit_ellip_{random.randint(1000, 9999)}",
        name="Elementos Orbitales y Órbitas Elípticas",
        main_topic="Mecánica Orbital Kepleriana",
        educational_objective="Calcular y visualizar elementos orbitales: semieje mayor a, excentricidad e, período T.",
        description=f"Órbita elíptica con a={a} AU, e={e}. Calcule perihelio, afelio, período orbital, y verifique 3ª Ley de Kepler.",
        parameters=[
            Parameter(
            name="a",
            display_name="Semieje mayor a",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=a,
            min_value=0.5,
            max_value=10,
            step=0.1,
            unit="AU"
        ),
            Parameter(
            name="e",
            display_name="Excentricidad e",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=e,
            min_value=0,
            max_value=0.95,
            step=0.01
        ),
            Parameter(
            name="theta0",
            display_name="Anomalía verdadera θ₀",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=0,
            min_value=0,
            max_value=6.28,
            step=0.1,
            unit="rad"
        ),
            Parameter(
            name="GM",
            display_name="GM (μ)",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=1.0,
            min_value=0.5,
            max_value=2,
            step=0.1
        )
        ],
        activity_type=ActivityType.SIMULACION,
        activity_description="Grafique la órbita, marque perihelio (r_min) y afelio (r_max). Verifique r_min + r_max = 2a y T² ∝ a³.",
        analysis_questions=[
            f"Calcule perihelio r_p = a(1-e) = {a*(1-e):.2f} AU",
            f"Calcule afelio r_a = a(1+e) = {a*(1+e):.2f} AU",
            "Verifique 3ª Ley: T² = (4π²/GM)·a³. ¿Cuál es el período orbital en años?"
        ],
        expected_observation=f"Órbita elíptica con e={e}. Velocidad máxima en perihelio, mínima en afelio (2ª Ley de Kepler).",
        metadata=ExerciseMetadata(DifficultyLevel.INTERMEDIO, "Astrodinámica", ["kepler", "elipse", "elementos"], 35)
    )

def _generate_orbits_transfer():
    """Transferencia de Hohmann"""
    r1 = 1.0
    r2 = round(random.uniform(1.5, 4.0), 1)
    
    return Exercise(
        id=f"orbit_hoh_{random.randint(1000, 9999)}",
        name="Transferencia Orbital de Hohmann",
        main_topic="Maniobras Orbitales",
        educational_objective="Diseñar transferencia de mínima energía entre órbitas circulares.",
        description=f"Transferencia de r₁={r1} AU a r₂={r2} AU mediante elipse de transferencia. Calcule Δv total requerido.",
        parameters=[
            Parameter(
            name="r1",
            display_name="Radio órbita inicial",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=r1,
            min_value=0.5,
            max_value=2,
            step=0.1,
            unit="AU"
        ),
            Parameter(
            name="r2",
            display_name="Radio órbita final",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=r2,
            min_value=1,
            max_value=10,
            step=0.1,
            unit="AU"
        ),
            Parameter(
            name="GM",
            display_name="GM",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=1.0,
            min_value=0.5,
            max_value=2,
            step=0.1
        )
        ],
        activity_type=ActivityType.INTERPRETACION,
        activity_description="Calcule v_circular en r₁ y r₂, velocidades en elipse de transferencia, y Δv₁, Δv₂.",
        analysis_questions=[
            f"Semieje mayor transferencia: a_t = (r₁+r₂)/2 = {(r1+r2)/2:.2f} AU",
            "Calcule Δv₁ (impulso en r₁) y Δv₂ (impulso en r₂). ¿Cuál es mayor?",
            "Tiempo de transferencia: T_transfer = T_elipse/2. Calcule en días."
        ],
        expected_observation="Transferencia de Hohmann minimiza Δv total. Usado en misiones interplanetarias (ej: Tierra→Marte).",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Astronáutica", ["hohmann", "delta-v", "misiones"], 45)
    )

def _generate_damper_forced():
    """Oscilador forzado - resonancia mecánica"""
    m = 1.0
    k = 25.0
    omega_0 = np.sqrt(k/m)
    c = round(random.uniform(1.0, 5.0), 1)
    F0 = round(random.uniform(5.0, 15.0), 1)
    omega_f = round(omega_0 * random.uniform(0.7, 1.3), 1)
    
    return Exercise(
        id=f"damp_forced_{random.randint(1000, 9999)}",
        name="Resonancia en Oscilador Mecánico Forzado",
        main_topic="Respuesta en Frecuencia",
        educational_objective="Analizar resonancia mecánica, factor Q, y fenómenos de amplificación dinámica.",
        description=f"Masa-resorte-amortiguador forzado: F(t)={F0}·cos({omega_f}t). Frecuencia natural ω₀={omega_0:.1f} rad/s.",
        parameters=[
            Parameter(
            name="m",
            display_name="Masa m",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=m,
            min_value=0.5,
            max_value=5,
            step=0.1,
            unit="kg"
        ),
            Parameter(
            name="c",
            display_name="Amortiguamiento c",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=c,
            min_value=0.5,
            max_value=20,
            step=0.5,
            unit="Ns/m"
        ),
            Parameter(
            name="k",
            display_name="Rigidez k",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=k,
            min_value=10,
            max_value=100,
            step=5,
            unit="N/m"
        ),
            Parameter(
            name="F0",
            display_name="Amplitud fuerza",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=F0,
            min_value=1,
            max_value=30,
            step=1,
            unit="N"
        ),
            Parameter(
            name="omega_f",
            display_name="Frecuencia fuerza",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=omega_f,
            min_value=1,
            max_value=20,
            step=0.5,
            unit="rad/s"
        )
        ],
        activity_type=ActivityType.GRAFICACION,
        activity_description="Grafique amplitud estado estacionario vs ω_f. Identifique pico de resonancia y mida factor de amplificación.",
        analysis_questions=[
            f"¿En qué frecuencia ocurre resonancia? Compare con ω₀={omega_0:.1f}",
            "Calcule factor Q = mω₀/c. Predice altura del pico de resonancia.",
            "Mida fase entre fuerza y desplazamiento. ¿Cuánto es en resonancia?"
        ],
        expected_observation="Resonancia en ω_res ≈ ω₀·√(1-2ζ²). Amplitud máxima ≈ (F₀/k)·Q. Fase = 90° en resonancia.",
        metadata=ExerciseMetadata(DifficultyLevel.INTERMEDIO, "Vibraciones", ["resonancia", "Q", "fase"], 35)
    )

def _generate_damper_double():
    """Sistema de dos masas acopladas"""
    m1 = round(random.uniform(0.5, 2.0), 1)
    m2 = round(random.uniform(0.5, 2.0), 1)
    k1 = round(random.uniform(10, 30), 0)
    k2 = round(random.uniform(10, 30), 0)
    k_couple = round(random.uniform(5, 15), 0)
    
    return Exercise(
        id=f"damp_double_{random.randint(1000, 9999)}",
        name="Sistema de Dos Masas Acopladas",
        main_topic="Modos Normales de Vibración",
        educational_objective="Encontrar frecuencias naturales y modos normales en sistemas de múltiples grados de libertad.",
        description=f"Dos masas (m₁={m1} kg, m₂={m2} kg) conectadas por resortes (k₁={k1}, k_acople={k_couple}, k₂={k2} N/m).",
        parameters=[
            Parameter(
            name="m1",
            display_name="Masa m₁",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=m1,
            min_value=0.1,
            max_value=5,
            step=0.1,
            unit="kg"
        ),
            Parameter(
            name="m2",
            display_name="Masa m₂",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=m2,
            min_value=0.1,
            max_value=5,
            step=0.1,
            unit="kg"
        ),
            Parameter(
            name="k1",
            display_name="Resorte k₁",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=k1,
            min_value=5,
            max_value=50,
            step=1,
            unit="N/m"
        ),
            Parameter(
            name="k2",
            display_name="Resorte k₂",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=k2,
            min_value=5,
            max_value=50,
            step=1,
            unit="N/m"
        ),
            Parameter(
            name="k_c",
            display_name="Acoplamiento k_c",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=k_couple,
            min_value=1,
            max_value=30,
            step=1,
            unit="N/m"
        )
        ],
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Resuelva el problema de valores propios para encontrar ω₁, ω₂ (frecuencias normales) y vectores propios (formas modales).",
        analysis_questions=[
            "¿Cuáles son las dos frecuencias naturales del sistema?",
            "Describe los modos normales: ¿en fase (simétrico) o fuera de fase (antisimétrico)?",
            "Si k_c→0 (desacoplado), ¿qué ocurre con las frecuencias?"
        ],
        expected_observation="Dos modos independientes: modo simétrico (ω_+) y antisimétrico (ω_-). Cualquier movimiento es combinación lineal de modos.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Sistemas Acoplados", ["modos normales", "valores propios"], 50)
    )

def _generate_newton_heating():
    """Calentamiento (inverso del enfriamiento)"""
    T0 = round(random.uniform(15, 25), 1)
    T_amb = round(random.uniform(60, 95), 1)
    k = round(random.uniform(0.05, 0.3), 3)
    
    return Exercise(
        id=f"newt_heat_{random.randint(1000, 9999)}",
        name="Ley de Newton para Calentamiento",
        main_topic="Transferencia de Calor",
        educational_objective="Aplicar ley de Newton al proceso inverso: calentamiento de un objeto frío en ambiente caliente.",
        description=f"Objeto inicialmente a T₀={T0}°C se calienta en horno a T_amb={T_amb}°C. Mismo modelo exponencial que enfriamiento.",
        parameters=[
            Parameter(
            name="T0",
            display_name="Temperatura inicial",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=T0,
            min_value=0,
            max_value=40,
            step=1,
            unit="°C"
        ),
            Parameter(
            name="T_amb",
            display_name="Temperatura horno",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=T_amb,
            min_value=40,
            max_value=120,
            step=1,
            unit="°C"
        ),
            Parameter(
            name="k",
            display_name="Constante k",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=k,
            min_value=0.01,
            max_value=0.5,
            step=0.01,
            unit="1/min"
        )
        ],
        activity_type=ActivityType.SIMULACION,
        activity_description="Simule calentamiento hasta que T(t) se aproxime a T_amb. Calcule constante de tiempo τ=1/k.",
        analysis_questions=[
            f"¿Cuánto tiempo para alcanzar 50% de (T_amb - T₀)? (τ·ln2 = {np.log(2)/k:.1f} min)",
            "¿La curva es idéntica al enfriamiento (solo invertida)?",
            "Aplicación: ¿cómo afecta k al tiempo de cocción de alimentos?"
        ],
        expected_observation=f"T(t) = T_amb - (T_amb-T₀)·exp(-kt). Crece exponencialmente hacia T_amb={T_amb}°C.",
        metadata=ExerciseMetadata(DifficultyLevel.BASICO, "Termodinámica", ["calentamiento", "exponencial"], 25)
    )

def _generate_newton_multibody():
    """Cadena de objetos con transferencia de calor"""
    n_bodies = 3
    T_exterior = 20
    T_initial_center = 80
    k_transfer = round(random.uniform(0.1, 0.3), 2)
    
    return Exercise(
        id=f"newt_multi_{random.randint(1000, 9999)}",
        name="Transferencia de Calor en Cadena de Cuerpos",
        main_topic="Difusión Térmica Discreta",
        educational_objective="Modelar transferencia de calor entre múltiples objetos acoplados térmicamente.",
        description=f"Cadena de {n_bodies} cuerpos: T₁(0)={T_initial_center}°C, otros a T_amb={T_exterior}°C. Intercambian calor entre sí y con ambiente.",
        parameters=[
            Parameter(name="n_bodies", display_name="Número cuerpos", description="", param_type=ParameterType.INTEGER, default_value=n_bodies, min_value=2, max_value=5),
            Parameter(
            name="k_transfer",
            display_name="k transferencia",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=k_transfer,
            min_value=0.01,
            max_value=0.5,
            step=0.01
        ),
            Parameter(
            name="k_ambient",
            display_name="k ambiente",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=0.05,
            min_value=0.01,
            max_value=0.2,
            step=0.01
        ),
            Parameter(
            name="T_amb",
            display_name="T ambiente",
            description="",
            param_type=ParameterType.FLOAT,
            default_value=T_exterior,
            min_value=0,
            max_value=40,
            step=1,
            unit="°C"
        )
        ],
        activity_type=ActivityType.SIMULACION,
        activity_description="Simule evolución de T₁(t), T₂(t), T₃(t). Observe propagación de calor como onda de difusión.",
        analysis_questions=[
            "¿El calor se propaga instantáneamente o con retardo temporal?",
            "¿Cuál cuerpo alcanza equilibrio último?",
            "Límite continuo (n→∞): ecuación de difusión ∂T/∂t = α·∂²T/∂x²"
        ],
        expected_observation="Calor difunde de cuerpo caliente a vecinos. Todos convergen a T_amb, pero a diferentes tasas.",
        metadata=ExerciseMetadata(DifficultyLevel.AVANZADO, "Física Térmica", ["difusión", "acoplamiento", "cadena"], 45)
    )

