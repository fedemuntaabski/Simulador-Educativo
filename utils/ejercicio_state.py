"""
Gestor de estado global para ejercicios de laboratorio.
Permite guardar y recuperar el ejercicio activo cuando el estudiante navega.
"""


class EjercicioState:
    """
    Singleton para gestionar el estado del ejercicio actual.
    Permite que el ejercicio persista entre navegaciones.
    """
    
    _instance = None
    _ejercicio_actual = None
    _respuestas_guardadas = {}
    _simulacion_ejecutada = False
    _datos_simulacion = None
    
    def __new__(cls):
        """Implementa el patrón Singleton."""
        if cls._instance is None:
            cls._instance = super(EjercicioState, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def set_ejercicio(cls, ejercicio):
        """
        Guarda el ejercicio actual.
        
        Args:
            ejercicio: Diccionario con los datos del ejercicio
        """
        cls._ejercicio_actual = ejercicio
        cls._respuestas_guardadas = {}
        cls._simulacion_ejecutada = False
        cls._datos_simulacion = None
    
    @classmethod
    def get_ejercicio(cls):
        """
        Obtiene el ejercicio actual.
        
        Returns:
            Diccionario con el ejercicio o None
        """
        return cls._ejercicio_actual
    
    @classmethod
    def clear_ejercicio(cls):
        """Limpia el ejercicio actual."""
        cls._ejercicio_actual = None
        cls._respuestas_guardadas = {}
        cls._simulacion_ejecutada = False
        cls._datos_simulacion = None
    
    @classmethod
    def tiene_ejercicio(cls):
        """
        Verifica si hay un ejercicio activo.
        
        Returns:
            bool: True si hay ejercicio activo
        """
        return cls._ejercicio_actual is not None
    
    @classmethod
    def set_respuesta(cls, pregunta_id, respuesta):
        """
        Guarda una respuesta.
        
        Args:
            pregunta_id: ID de la pregunta
            respuesta: Respuesta del estudiante
        """
        cls._respuestas_guardadas[pregunta_id] = respuesta
    
    @classmethod
    def get_respuestas(cls):
        """
        Obtiene todas las respuestas guardadas.
        
        Returns:
            Diccionario con las respuestas
        """
        return cls._respuestas_guardadas.copy()
    
    @classmethod
    def set_simulacion_ejecutada(cls, ejecutada=True, datos=None):
        """
        Marca que la simulación fue ejecutada.
        
        Args:
            ejecutada: Si la simulación fue ejecutada
            datos: Datos de la simulación (opcional)
        """
        cls._simulacion_ejecutada = ejecutada
        cls._datos_simulacion = datos
    
    @classmethod
    def simulacion_fue_ejecutada(cls):
        """
        Verifica si la simulación fue ejecutada.
        
        Returns:
            bool: True si fue ejecutada
        """
        return cls._simulacion_ejecutada
    
    @classmethod
    def get_datos_simulacion(cls):
        """
        Obtiene los datos de la simulación.
        
        Returns:
            Datos de la simulación o None
        """
        return cls._datos_simulacion
    
    @classmethod
    def get_parametros_ejercicio(cls):
        """
        Obtiene los parámetros del ejercicio actual.
        
        Returns:
            Diccionario con parámetros o None
        """
        if cls._ejercicio_actual:
            return cls._ejercicio_actual.get('parametros', {})
        return None
    
    @classmethod
    def get_sistema_ejercicio(cls):
        """
        Obtiene el sistema del ejercicio actual.
        
        Returns:
            String con el nombre del sistema o None
        """
        if cls._ejercicio_actual:
            return cls._ejercicio_actual.get('sistema')
        return None
    
    @classmethod
    def get_info_ejercicio(cls):
        """
        Obtiene información resumida del ejercicio.
        
        Returns:
            String con información o None
        """
        if cls._ejercicio_actual:
            titulo = cls._ejercicio_actual.get('titulo', 'Sin título')
            dificultad = cls._ejercicio_actual.get('dificultad', 'intermedio')
            return f"{titulo} ({dificultad.upper()})"
        return None
