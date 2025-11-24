"""
Gestor de estado global para ejercicios de laboratorio.
Permite guardar y recuperar el ejercicio activo cuando el estudiante navega.
"""


from datetime import datetime

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
    _start_time = None
    _selected_system = 'newton'
    _selected_difficulty = 'intermedio'
    
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
        cls._start_time = datetime.now()
    
    @classmethod
    def get_duration_seconds(cls):
        """Retorna la duración en segundos desde que inició el ejercicio."""
        if cls._start_time:
            return (datetime.now() - cls._start_time).total_seconds()
        return 0.0
    
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
    
    @classmethod
    def set_selected_system(cls, system):
        """
        Guarda el sistema dinámico seleccionado.
        
        Args:
            system: ID del sistema seleccionado
        """
        cls._selected_system = system
    
    @classmethod
    def get_selected_system(cls):
        """
        Obtiene el sistema dinámico seleccionado.
        
        Returns:
            String con el ID del sistema
        """
        return cls._selected_system
    
    @classmethod
    def set_selected_difficulty(cls, difficulty):
        """
        Guarda el nivel de dificultad seleccionado.
        
        Args:
            difficulty: Nivel de dificultad seleccionado
        """
        cls._selected_difficulty = difficulty
    
    @classmethod
    def get_selected_difficulty(cls):
        """
        Obtiene el nivel de dificultad seleccionado.
        
        Returns:
            String con el nivel de dificultad
        """
        return cls._selected_difficulty
