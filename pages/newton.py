"""
Página de simulación de la Ley de Enfriamiento de Newton - Versión Educativa Mejorada.
"""

import tkinter as tk
import numpy as np
from utils.simulador_base import SimuladorBasePage
from utils.simulator import NewtonCoolingSimulator
from utils.styles import COLORS


class NewtonPage(SimuladorBasePage):
    """
    Página para simular la Ley de Enfriamiento de Newton con componentes educativos.
    Ecuación: dT/dt = -k(T - T_ambiente)
    """
    
    def __init__(self, parent):
        """
        Inicializa la página de enfriamiento de Newton.
        
        Args:
            parent: Widget padre
        """
        # Inicializar clase base
        super().__init__(parent, "Ley de Enfriamiento de Newton", "newton")
        
        # Información teórica
        info_teorica = {
            'descripcion': (
                "La Ley de Enfriamiento de Newton establece que la tasa de pérdida de calor de un cuerpo "
                "es proporcional a la diferencia entre su temperatura y la temperatura del ambiente. "
                "Este modelo describe procesos de enfriamiento y calentamiento en sistemas donde la "
                "transferencia de calor es por convección y radiación. La solución es una función exponencial "
                "decreciente que tiende asintóticamente a la temperatura ambiente."
            ),
            'aplicaciones': [
                "Forense: Estimación del tiempo de muerte mediante temperatura corporal",
                "Industria alimentaria: Control de enfriamiento de productos",
                "Meteorología: Predicción de enfriamiento nocturno",
                "Ingeniería térmica: Diseño de sistemas de enfriamiento",
                "Medicina: Hipotermia terapéutica controlada"
            ]
        }
        
        ecuaciones = [
            "dT/dt = -k(T - T_amb)",
            "",
            "Solución analítica:",
            "T(t) = T_amb + (T₀ - T_amb) × e^(-kt)",
            "",
            "Donde:",
            "  T(t)  = Temperatura en el tiempo t",
            "  T₀    = Temperatura inicial",
            "  T_amb = Temperatura ambiente",
            "  k     = Constante de enfriamiento (depende del material y condiciones)",
            "  t     = Tiempo"
        ]
        
        # Configuración de parámetros con sliders
        parametros_config = {
            'T0': {
                'label': 'Temperatura Inicial (T₀)',
                'min': 0,
                'max': 200,
                'default': 100,
                'resolution': 1,
                'descripcion': 'Temperatura inicial del objeto en °C'
            },
            'T_env': {
                'label': 'Temperatura Ambiente (T_amb)',
                'min': -20,
                'max': 50,
                'default': 25,
                'resolution': 0.5,
                'descripcion': 'Temperatura del entorno en °C'
            },
            'k': {
                'label': 'Constante de Enfriamiento (k)',
                'min': 0.01,
                'max': 1.0,
                'default': 0.1,
                'resolution': 0.01,
                'descripcion': 'Mayor k = enfriamiento más rápido'
            },
            't_max': {
                'label': 'Tiempo de Simulación',
                'min': 10,
                'max': 200,
                'default': 50,
                'resolution': 5,
                'descripcion': 'Duración de la simulación en minutos'
            }
        }
        
        # Crear layout
        self.create_layout(info_teorica, ecuaciones, parametros_config)
    
    def ejecutar_simulacion(self):
        """Ejecuta la simulación del enfriamiento de Newton."""
        # Obtener parámetros
        T0 = self.parametros['T0']
        T_env = self.parametros['T_env']
        k = self.parametros['k']
        t_max = self.parametros['t_max']
        
        # Validaciones
        if T0 == T_env:
            self.update_analysis(
                "⚠️ ADVERTENCIA: La temperatura inicial es igual a la ambiente.\n"
                "No habrá cambio de temperatura. El sistema ya está en equilibrio térmico."
            )
            return
        
        # Simular
        t, T = NewtonCoolingSimulator.simulate(T0, T_env, k, t_max)
        
        # Graficar
        self.graph.clear()
        
        # Curva de temperatura
        color = 'b' if T0 > T_env else 'r'
        self.graph.plot(t, T, color=color, linewidth=2.5, 
                       label=f'T(t) con k={k}')
        
        # Línea de temperatura ambiente
        self.graph.ax.axhline(y=T_env, color='green', linestyle='--', 
                             linewidth=2, alpha=0.7, label=f'T_ambiente = {T_env}°C')
        
        # Línea de temperatura inicial
        self.graph.ax.axhline(y=T0, color='orange', linestyle=':', 
                             linewidth=1.5, alpha=0.5, label=f'T₀ = {T0}°C')
        
        # Marcar constante de tiempo (1/k)
        tau = 1/k  # Constante de tiempo
        if tau < t_max:
            T_tau = T_env + (T0 - T_env) * np.exp(-1)
            self.graph.ax.plot(tau, T_tau, 'ro', markersize=10, 
                              label=f'τ = {tau:.1f} min (63% del cambio)')
        
        self.graph.set_labels(
            xlabel='Tiempo (minutos)',
            ylabel='Temperatura (°C)',
            title=f'Enfriamiento de Newton: {"Enfriamiento" if T0 > T_env else "Calentamiento"}'
        )
        self.graph.grid(True, alpha=0.3)
        self.graph.legend()
        self.graph.tight_layout()
        
        # Análisis cualitativo
        self.generar_analisis(T0, T_env, k, t, T)
    
    def generar_analisis(self, T0, T_env, k, t, T):
        """Genera el análisis cualitativo del comportamiento."""
        proceso = "enfriamiento" if T0 > T_env else "calentamiento"
        tau = 1/k
        
        # Calcular tiempo para alcanzar cierta cercanía a T_env
        diferencia_inicial = abs(T0 - T_env)
        T_95 = T_env + 0.05 * (T0 - T_env)  # 95% del cambio
        t_95 = -np.log(0.05) / k  # Aproximadamente 3*tau
        
        # Temperatura final simulada
        T_final = T[-1]
        diferencia_final = abs(T_final - T_env)
        porcentaje_completado = (1 - diferencia_final/diferencia_inicial) * 100
        
        analisis = f"""
🔍 ANÁLISIS DEL COMPORTAMIENTO:

📊 Tipo de proceso: {proceso.upper()}
   - Temperatura inicial: {T0}°C
   - Temperatura ambiente: {T_env}°C
   - Cambio total esperado: {diferencia_inicial}°C

⏱️ DINÁMICA TEMPORAL:
   - Constante de tiempo (τ = 1/k): {tau:.2f} minutos
   - Después de τ: Se completa el 63.2% del cambio
   - Después de 3τ: Se completa el 95% del cambio (~{t_95:.1f} min)
   - Después de 5τ: Se completa el 99.3% del cambio (~{5*tau:.1f} min)

📈 ESTADO ACTUAL:
   - Temperatura al final de la simulación: {T_final:.2f}°C
   - Porcentaje de cambio completado: {porcentaje_completado:.1f}%
   - Diferencia con el equilibrio: {diferencia_final:.2f}°C

💡 INTERPRETACIÓN:
   - Velocidad de {proceso}: {"Rápida" if k > 0.2 else "Moderada" if k > 0.05 else "Lenta"} (k = {k})
   - Comportamiento: Exponencial decreciente
   - Tendencia asintótica: T(t) → {T_env}°C cuando t → ∞
   
⚙️ EFECTO DE LOS PARÁMETROS:
   - Aumentar k → {proceso} más rápido
   - Mayor diferencia (T₀ - T_amb) → Mayor tasa inicial de cambio
   - La temperatura NUNCA alcanza exactamente T_amb (solo asintóticamente)
        """
        
        self.update_analysis(analisis.strip())

