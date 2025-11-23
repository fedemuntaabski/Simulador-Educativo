
def get_content_for_topic(topic):
    """
    Returns a dictionary with educational content for a given topic.
    Topics: 'SIR', 'Lorenz', 'Van der Pol', 'Hopf', 'Logística', 'Verhulst', 
            'Órbitas simples', 'RLC', 'Amortiguadores', 'Enfriamiento de Newton'
    """
    
    # Normalización de claves para soportar diferentes variaciones
    topic_map = {
        "sir": "SIR",
        "lorenz": "Lorenz",
        "van_der_pol": "Van der Pol",
        "vdp": "Van der Pol",
        "hopf": "Hopf",
        "logistica": "Logística",
        "logistico": "Logística",
        "verhulst": "Verhulst",
        "orbitas": "Órbitas simples",
        "orbital": "Órbitas simples",
        "orbitas simples": "Órbitas simples",
        "rlc": "RLC",
        "amortiguadores": "Amortiguadores",
        "amortiguador": "Amortiguadores",
        "newton": "Enfriamiento de Newton",
        "enfriamiento de newton": "Enfriamiento de Newton"
    }
    
    normalized_topic = topic_map.get(topic.lower().strip(), topic)

    content = {
        "SIR": {
            "intro": "El modelo SIR es fundamental para entender cómo se propagan las enfermedades infecciosas en una población.",
            "explanation": "Imagina una población dividida en tres grupos: Susceptibles (sanos que pueden enfermar), Infectados (quienes transmiten la enfermedad) y Recuperados (quienes ya sanaron y tienen inmunidad). Esta simulación muestra cómo cambian estos grupos con el tiempo.",
            "questions": [
                "¿Qué sucede con el número de infectados al inicio?",
                "¿Llega un momento en que la epidemia se detiene? ¿Por qué?",
                "¿Cómo afecta la tasa de recuperación a la duración de la epidemia?"
            ],
            "conclusion": "Generalmente, verás que el número de infectados sube hasta un pico y luego baja a medida que la gente se recupera, dejando menos personas susceptibles para contagiar."
        },
        "Lorenz": {
            "intro": "El atractor de Lorenz es un ejemplo clásico de la teoría del caos, usado originalmente para modelar el clima.",
            "explanation": "Representa el movimiento de un fluido (como el aire) calentado desde abajo. Lo interesante es que pequeños cambios en el inicio pueden llevar a resultados totalmente diferentes, conocido como el 'efecto mariposa'.",
            "questions": [
                "¿Las trayectorias se cruzan alguna vez o solo giran cerca?",
                "¿El sistema parece repetirse exactamente o siempre es diferente?",
                "¿Qué forma general ves en el gráfico 3D?"
            ],
            "conclusion": "El sistema nunca pasa dos veces por el mismo punto exacto, mostrando un comportamiento impredecible pero ordenado dentro de una forma de 'mariposa'."
        },
        "Van der Pol": {
            "intro": "El oscilador de Van der Pol describe sistemas que tienen oscilaciones auto-sostenidas.",
            "explanation": "Originalmente usado para circuitos de radio, este modelo muestra cómo un sistema puede mantener un ritmo constante (ciclo límite) incluso si empieza muy rápido o muy lento, gracias a una amortiguación que cambia según la amplitud.",
            "questions": [
                "¿El sistema tiende a estabilizarse en un patrón repetitivo?",
                "¿Importa dónde empieza la simulación para el resultado final?",
                "¿Cómo cambia la forma de la oscilación si aumentas la fuerza del amortiguamiento?"
            ],
            "conclusion": "Independientemente de las condiciones iniciales, el sistema tiende a converger a una órbita cerrada y estable llamada ciclo límite."
        },
        "Hopf": {
            "intro": "La bifurcación de Hopf explica cómo surge una oscilación periódica a partir de un estado estable.",
            "explanation": "Imagina un sistema en equilibrio que, al cambiar un parámetro (como la temperatura o una fuerza), de repente empieza a oscilar. Es clave para entender desde el aleteo de un avión hasta reacciones químicas oscilantes.",
            "questions": [
                "¿En qué punto el sistema deja de estar quieto y empieza a oscilar?",
                "¿La oscilación crece indefinidamente o se mantiene estable?",
                "¿Qué pasa si reviertes el cambio del parámetro?"
            ],
            "conclusion": "Observamos el nacimiento de un ciclo límite: el paso de un punto de equilibrio estable a una oscilación periódica estable."
        },
        "Logística": {
            "intro": "El mapa logístico es un modelo muy simple que puede mostrar comportamiento muy complejo, incluso caos.",
            "explanation": "Se usa para modelar el crecimiento de poblaciones donde los recursos son limitados. Muestra cómo la población del próximo año depende de la actual, pero con un límite máximo que el ambiente puede soportar.",
            "questions": [
                "¿La población se estabiliza en un número fijo?",
                "¿Ves que la población oscila entre dos o más valores?",
                "¿Qué sucede cuando la tasa de crecimiento es muy alta?"
            ],
            "conclusion": "Dependiendo de la tasa de crecimiento, la población puede estabilizarse, oscilar periódicamente o volverse completamente caótica e impredecible."
        },
        "Verhulst": {
            "intro": "La ecuación de Verhulst mejora el modelo de crecimiento exponencial añadiendo un límite de capacidad.",
            "explanation": "A diferencia del crecimiento infinito, aquí la población crece rápido al principio pero se frena a medida que se acerca al límite de recursos (capacidad de carga) del entorno.",
            "questions": [
                "¿Cómo es la velocidad de crecimiento al principio comparada con el final?",
                "¿La población supera alguna vez la capacidad de carga?",
                "¿Qué forma tiene la curva de crecimiento (S, J, lineal)?"
            ],
            "conclusion": "La población sigue una curva en forma de 'S' (sigmoide), estabilizándose suavemente en el máximo que el entorno permite."
        },
        "Órbitas simples": {
            "intro": "Las órbitas simples nos ayudan a entender el movimiento de planetas o satélites bajo la gravedad.",
            "explanation": "Simulamos un cuerpo girando alrededor de otro más grande. Dependiendo de la velocidad inicial, la órbita puede ser un círculo perfecto, una elipse alargada o incluso una ruta de escape.",
            "questions": [
                "¿La órbita se cierra sobre sí misma?",
                "¿Qué pasa si aumentas la velocidad inicial del objeto?",
                "¿El objeto se mueve más rápido cuando está cerca o lejos del centro?"
            ],
            "conclusion": "Vemos cómo la gravedad y la velocidad se equilibran para mantener al objeto en una trayectoria estable y repetitiva."
        },
        "RLC": {
            "intro": "Un circuito RLC es el análogo eléctrico de un oscilador mecánico con resorte y masa.",
            "explanation": "Combina una Resistencia (freno), una Inductancia (inercia) y una Capacitancia (resorte). La energía oscila entre el campo magnético y el eléctrico, perdiéndose poco a poco como calor en la resistencia.",
            "questions": [
                "¿La oscilación de la corriente disminuye con el tiempo?",
                "¿Qué tan rápido desaparece la energía?",
                "¿Podrías hacer que oscile para siempre si quitas la resistencia?"
            ],
            "conclusion": "La corriente oscila como una onda que se hace cada vez más pequeña, mostrando cómo la energía se disipa en el circuito."
        },
        "Amortiguadores": {
            "intro": "El movimiento amortiguado explica por qué las cosas dejan de moverse eventualmente.",
            "explanation": "Es como un columpio que dejas de empujar. La fricción (amortiguamiento) roba energía al sistema, haciendo que cada oscilación sea más corta que la anterior hasta detenerse.",
            "questions": [
                "¿El objeto cruza la posición de equilibrio muchas veces o pocas?",
                "¿Se detiene bruscamente o suavemente?",
                "¿Qué pasa si la fricción es muy, muy grande?"
            ],
            "conclusion": "El sistema pierde energía gradualmente hasta detenerse en el equilibrio. Si la fricción es mucha, puede que ni siquiera llegue a oscilar."
        },
        "Enfriamiento de Newton": {
            "intro": "La Ley de Enfriamiento de Newton describe cómo cambia la temperatura de un objeto en un ambiente.",
            "explanation": "Simplemente dice que cuanto más caliente está algo respecto al ambiente, más rápido se enfría. Una taza de café hirviendo pierde calor muy rápido, pero una tibia lo hace lento.",
            "questions": [
                "¿La temperatura baja a una velocidad constante?",
                "¿Qué pasa con la velocidad de enfriamiento a medida que pasa el tiempo?",
                "¿El objeto llega a estar más frío que el ambiente?"
            ],
            "conclusion": "La temperatura decae exponencialmente: rápido al principio y muy lento al final, acercándose siempre a la temperatura ambiente sin pasarla."
        }
    }
    
    return content.get(normalized_topic, {
        "intro": f"Introducción al tema {topic}.",
        "explanation": "Explicación general del fenómeno simulado.",
        "questions": ["¿Qué observas en la gráfica?", "¿Cómo cambia el sistema con el tiempo?"],
        "conclusion": "Conclusión basada en la observación de la simulación."
    })

def generate_intro(topic):
    """Genera un texto introductorio claro y breve para el tema."""
    content = get_content_for_topic(topic)
    return content["intro"]

def generate_explanation(topic):
    """Genera una explicación conceptual del fenómeno sin tecnicismos."""
    content = get_content_for_topic(topic)
    return content["explanation"]

def generate_guided_questions(topic):
    """Genera una lista de preguntas guía para el estudiante."""
    content = get_content_for_topic(topic)
    # Join questions with newlines or return as list? 
    # Requirement says "devolver strings listos para mostrar". 
    # A formatted string list is usually best for display.
    questions = content["questions"]
    formatted_questions = "\n".join([f"- {q}" for q in questions])
    return formatted_questions

def generate_conclusion(topic):
    """Genera una conclusión esperada sobre el comportamiento del sistema."""
    content = get_content_for_topic(topic)
    return content["conclusion"]
