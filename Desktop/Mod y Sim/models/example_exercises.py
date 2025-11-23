"""
Ejemplos de ejercicios educativos para demostrar el uso de la estructura.
"""

from .exercise import (
    Exercise,
    Parameter,
    ExerciseMetadata,
    ParameterType,
    ActivityType,
    DifficultyLevel
)
from .exercise_factory import ExerciseFactory


def create_pendulum_exercise(factory: ExerciseFactory) -> Exercise:
    """Crea el ejercicio de estabilidad del péndulo simple."""
    
    parameters = [
        Parameter(
            name="theta_0",
            display_name="Ángulo inicial θ₀",
            description="Ángulo inicial del péndulo respecto a la vertical",
            param_type=ParameterType.FLOAT,
            default_value=30.0,
            min_value=-180.0,
            max_value=180.0,
            unit="grados",
            step=1.0
        ),
        Parameter(
            name="omega_0",
            display_name="Velocidad angular inicial ω₀",
            description="Velocidad angular inicial del péndulo",
            param_type=ParameterType.FLOAT,
            default_value=0.0,
            min_value=-10.0,
            max_value=10.0,
            unit="rad/s",
            step=0.1
        ),
        Parameter(
            name="length",
            display_name="Longitud L",
            description="Longitud del péndulo desde el pivote a la masa",
            param_type=ParameterType.FLOAT,
            default_value=1.0,
            min_value=0.5,
            max_value=3.0,
            unit="m",
            step=0.1
        ),
        Parameter(
            name="damping",
            display_name="Amortiguamiento b",
            description="Coeficiente de amortiguamiento viscoso",
            param_type=ParameterType.FLOAT,
            default_value=0.1,
            min_value=0.0,
            max_value=0.5,
            unit="kg·m²/s",
            step=0.01
        )
    ]
    
    metadata = ExerciseMetadata(
        difficulty=DifficultyLevel.BASICO,
        category="Mecánica Clásica",
        tags=["péndulo", "estabilidad", "espacio de fases", "oscilaciones"],
        estimated_time=25,
        author="Sistema generador automático"
    )
    
    return factory.create_exercise(
        exercise_id="pendulum_stability_01",
        name="Estabilidad del Péndulo Simple",
        main_topic="Sistemas dinámicos clásicos",
        educational_objective="Comprender la estabilidad de puntos de equilibrio y cómo las condiciones iniciales afectan la trayectoria del sistema.",
        description="Un péndulo simple oscila bajo la influencia de la gravedad. Dependiendo del ángulo inicial y la velocidad angular, el sistema puede oscilar periódicamente o dar vueltas completas.",
        parameters=parameters,
        activity_type=ActivityType.ANALISIS_FASE,
        activity_description="Simular el movimiento del péndulo en el espacio de fases (θ vs ω) y observar las trayectorias para diferentes condiciones iniciales.",
        analysis_questions=[
            "¿Qué sucede con el péndulo cuando el ángulo inicial es cercano a 0° versus cercano a 180°?",
            "¿Cómo cambia el retrato de fase cuando se incrementa el amortiguamiento?",
            "¿Qué condiciones iniciales llevan al péndulo a dar vueltas completas en lugar de oscilar?"
        ],
        expected_observation="El estudiante debe identificar dos tipos de comportamiento: oscilaciones periódicas alrededor de θ=0 (punto de equilibrio estable) y rotaciones completas. Con amortiguamiento, todas las trayectorias convergen al punto de equilibrio estable.",
        metadata=metadata
    )


def create_lorenz_exercise(factory: ExerciseFactory) -> Exercise:
    """Crea el ejercicio de caos en el atractor de Lorenz."""
    
    parameters = [
        Parameter(
            name="sigma",
            display_name="Parámetro σ (sigma)",
            description="Número de Prandtl, relacionado con la viscosidad",
            param_type=ParameterType.FLOAT,
            default_value=10.0,
            min_value=5.0,
            max_value=15.0,
            unit=None,
            step=0.5
        ),
        Parameter(
            name="rho",
            display_name="Parámetro ρ (rho)",
            description="Número de Rayleigh, relacionado con la diferencia de temperatura",
            param_type=ParameterType.FLOAT,
            default_value=28.0,
            min_value=10.0,
            max_value=40.0,
            unit=None,
            step=1.0
        ),
        Parameter(
            name="beta",
            display_name="Parámetro β (beta)",
            description="Parámetro geométrico del sistema",
            param_type=ParameterType.FLOAT,
            default_value=2.667,
            min_value=1.0,
            max_value=5.0,
            unit=None,
            step=0.1
        ),
        Parameter(
            name="x0",
            display_name="Condición inicial x₀",
            description="Valor inicial de la variable x",
            param_type=ParameterType.FLOAT,
            default_value=1.0,
            min_value=-2.0,
            max_value=2.0,
            unit=None,
            step=0.01
        ),
        Parameter(
            name="y0",
            display_name="Condición inicial y₀",
            description="Valor inicial de la variable y",
            param_type=ParameterType.FLOAT,
            default_value=1.0,
            min_value=-2.0,
            max_value=2.0,
            unit=None,
            step=0.01
        ),
        Parameter(
            name="z0",
            display_name="Condición inicial z₀",
            description="Valor inicial de la variable z",
            param_type=ParameterType.FLOAT,
            default_value=1.0,
            min_value=-2.0,
            max_value=2.0,
            unit=None,
            step=0.01
        )
    ]
    
    metadata = ExerciseMetadata(
        difficulty=DifficultyLevel.AVANZADO,
        category="Sistemas Caóticos",
        tags=["caos", "lorenz", "atractor", "sensibilidad", "condiciones iniciales"],
        estimated_time=35,
        author="Sistema generador automático"
    )
    
    return factory.create_exercise(
        exercise_id="lorenz_chaos_01",
        name="Caos en el Atractor de Lorenz",
        main_topic="Atractor de Lorenz",
        educational_objective="Observar la sensibilidad a condiciones iniciales característica de sistemas caóticos.",
        description="El sistema de Lorenz modela convección atmosférica simplificada y exhibe comportamiento caótico para ciertos valores de parámetros.",
        parameters=parameters,
        activity_type=ActivityType.SIMULACION,
        activity_description="Simular dos trayectorias con condiciones iniciales muy cercanas y observar cómo divergen en el espacio 3D.",
        analysis_questions=[
            "¿Qué sucede con la diferencia entre dos trayectorias que inician muy cerca una de otra?",
            "¿Para qué valores de ρ el sistema exhibe comportamiento caótico versus comportamiento periódico?",
            "¿Qué forma tiene el atractor en el espacio de fases tridimensional?"
        ],
        expected_observation="Para ρ > 24.74 aproximadamente, las trayectorias forman el característico atractor de 'mariposa' y dos condiciones iniciales cercanas divergen exponencialmente.",
        metadata=metadata
    )


def create_sir_exercise(factory: ExerciseFactory) -> Exercise:
    """Crea el ejercicio de dinámica de epidemia SIR."""
    
    parameters = [
        Parameter(
            name="beta",
            display_name="Tasa de transmisión β",
            description="Tasa de contacto efectivo entre susceptibles e infectados",
            param_type=ParameterType.FLOAT,
            default_value=0.5,
            min_value=0.1,
            max_value=2.0,
            unit="1/día",
            step=0.05
        ),
        Parameter(
            name="gamma",
            display_name="Tasa de recuperación γ",
            description="Tasa a la cual los infectados se recuperan",
            param_type=ParameterType.FLOAT,
            default_value=0.1,
            min_value=0.05,
            max_value=0.5,
            unit="1/día",
            step=0.01
        ),
        Parameter(
            name="S0",
            display_name="Susceptibles iniciales S₀",
            description="Población inicial susceptible a la enfermedad",
            param_type=ParameterType.INTEGER,
            default_value=9900,
            min_value=900,
            max_value=9990,
            unit="personas",
            step=100
        ),
        Parameter(
            name="I0",
            display_name="Infectados iniciales I₀",
            description="Población inicial infectada",
            param_type=ParameterType.INTEGER,
            default_value=100,
            min_value=1,
            max_value=100,
            unit="personas",
            step=1
        )
    ]
    
    metadata = ExerciseMetadata(
        difficulty=DifficultyLevel.INTERMEDIO,
        category="Epidemiología",
        tags=["SIR", "epidemia", "salud pública", "número reproductivo"],
        estimated_time=30,
        author="Sistema generador automático"
    )
    
    return factory.create_exercise(
        exercise_id="sir_epidemic_01",
        name="Dinámica de Epidemia SIR Básica",
        main_topic="Modelos epidemiológicos SIR",
        educational_objective="Comprender cómo la tasa de contacto y recuperación afectan la propagación de una enfermedad.",
        description="El modelo SIR divide la población en Susceptibles, Infectados y Recuperados, describiendo la evolución temporal de una epidemia.",
        parameters=parameters,
        activity_type=ActivityType.GRAFICACION,
        activity_description="Graficar las tres poblaciones S(t), I(t), R(t) versus tiempo y determinar si ocurre una epidemia.",
        analysis_questions=[
            "¿Qué condición sobre β/γ determina si habrá un brote epidémico significativo?",
            "¿Cómo afecta el número inicial de infectados al pico de la epidemia?",
            "¿Por qué la curva de susceptibles nunca llega a cero?"
        ],
        expected_observation="Si β/γ > 1 (número reproductivo R₀ > 1), se observa un pico en infectados seguido de decaimiento. La población susceptible final es positiva.",
        metadata=metadata
    )


def load_example_exercises() -> ExerciseFactory:
    """
    Carga ejercicios de ejemplo en una fábrica.
    
    Returns:
        ExerciseFactory con ejercicios precargados
    """
    factory = ExerciseFactory()
    
    # Crear ejercicios de ejemplo
    create_pendulum_exercise(factory)
    create_lorenz_exercise(factory)
    create_sir_exercise(factory)
    
    return factory


if __name__ == "__main__":
    # Demostración de uso
    factory = load_example_exercises()
    
    print("=== Ejercicios cargados ===")
    for exercise in factory.get_all_exercises():
        print(f"\n[{exercise.id}] {exercise.name}")
        print(f"  Tema: {exercise.main_topic}")
        print(f"  Dificultad: {exercise.metadata.difficulty.value if exercise.metadata.difficulty else 'N/A'}")
        print(f"  Parámetros: {len(exercise.parameters)}")
        print(f"  Preguntas: {len(exercise.analysis_questions)}")
