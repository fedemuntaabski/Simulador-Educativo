"""
Funciones de simulación para los diferentes sistemas dinámicos.
Utiliza scipy.integrate.solve_ivp para resolver EDOs.
"""

import numpy as np
from scipy.integrate import solve_ivp


class SystemSimulator:
    """
    Clase base para simular sistemas dinámicos usando métodos numéricos.
    """
    
    @staticmethod
    def solve_ode(func, y0, t_span, t_eval=None, **params):
        """
        Resuelve una ecuación diferencial ordinaria.
        
        Args:
            func: Función que define el sistema dy/dt = f(t, y, **params)
            y0: Condiciones iniciales
            t_span: Tupla (t_inicial, t_final)
            t_eval: Puntos de tiempo donde evaluar la solución
            **params: Parámetros adicionales para la función
            
        Returns:
            Objeto solución de solve_ivp
        """
        if t_eval is None:
            t_eval = np.linspace(t_span[0], t_span[1], 1000)
        
        # Wrapper para pasar parámetros adicionales
        def system(t, y):
            return func(t, y, **params)
        
        solution = solve_ivp(
            system,
            t_span,
            y0,
            t_eval=t_eval,
            method='RK45',
            dense_output=True
        )
        
        return solution


class NewtonCoolingSimulator(SystemSimulator):
    """Simulador para la Ley de Enfriamiento de Newton."""
    
    @staticmethod
    def cooling_law(t, T, k, T_env):
        """
        dT/dt = -k(T - T_env)
        
        Args:
            t: Tiempo
            T: Temperatura (array)
            k: Constante de enfriamiento
            T_env: Temperatura ambiente
        """
        return [-k * (T[0] - T_env)]
    
    @classmethod
    def simulate(cls, T0, T_env, k, t_max=50):
        """
        Simula el enfriamiento de Newton.
        
        Args:
            T0: Temperatura inicial
            T_env: Temperatura ambiente
            k: Constante de enfriamiento
            t_max: Tiempo máximo de simulación
            
        Returns:
            (t, T): Arrays de tiempo y temperatura
        """
        t_eval = np.linspace(0, t_max, 500)
        sol = cls.solve_ode(
            cls.cooling_law,
            [T0],
            (0, t_max),
            t_eval=t_eval,
            k=k,
            T_env=T_env
        )
        return sol.t, sol.y[0]


class VanDerPolSimulator(SystemSimulator):
    """Simulador para el oscilador de Van der Pol."""
    
    @staticmethod
    def van_der_pol(t, y, mu):
        """
        Sistema de Van der Pol:
        dx/dt = y
        dy/dt = mu(1 - x²)y - x
        
        Args:
            t: Tiempo
            y: Vector de estado [x, dx/dt]
            mu: Parámetro de no linealidad
        """
        x, v = y
        return [v, mu * (1 - x**2) * v - x]
    
    @classmethod
    def simulate(cls, x0, v0, mu, t_max=50):
        """
        Simula el oscilador de Van der Pol.
        
        Args:
            x0: Posición inicial
            v0: Velocidad inicial
            mu: Parámetro de amortiguamiento no lineal
            t_max: Tiempo máximo
            
        Returns:
            (t, x, v): Arrays de tiempo, posición y velocidad
        """
        t_eval = np.linspace(0, t_max, 1000)
        sol = cls.solve_ode(
            cls.van_der_pol,
            [x0, v0],
            (0, t_max),
            t_eval=t_eval,
            mu=mu
        )
        return sol.t, sol.y[0], sol.y[1]


class SIRSimulator(SystemSimulator):
    """Simulador para el modelo epidemiológico SIR."""
    
    @staticmethod
    def sir_model(t, y, beta, gamma, N):
        """
        Modelo SIR:
        dS/dt = -beta * S * I / N
        dI/dt = beta * S * I / N - gamma * I
        dR/dt = gamma * I
        
        Args:
            t: Tiempo
            y: Vector [S, I, R]
            beta: Tasa de contacto
            gamma: Tasa de recuperación
            N: Población total
        """
        S, I, R = y
        dS = -beta * S * I / N
        dI = beta * S * I / N - gamma * I
        dR = gamma * I
        return [dS, dI, dR]
    
    @classmethod
    def simulate(cls, S0, I0, R0, beta, gamma, t_max=160):
        """
        Simula el modelo SIR.
        
        Args:
            S0: Población susceptible inicial
            I0: Población infectada inicial
            R0: Población recuperada inicial
            beta: Tasa de contacto
            gamma: Tasa de recuperación
            t_max: Tiempo máximo (días)
            
        Returns:
            (t, S, I, R): Arrays de tiempo y poblaciones
        """
        N = S0 + I0 + R0
        t_eval = np.linspace(0, t_max, 1000)
        sol = cls.solve_ode(
            cls.sir_model,
            [S0, I0, R0],
            (0, t_max),
            t_eval=t_eval,
            beta=beta,
            gamma=gamma,
            N=N
        )
        return sol.t, sol.y[0], sol.y[1], sol.y[2]


class RLCSimulator(SystemSimulator):
    """Simulador para circuito RLC."""
    
    @staticmethod
    def rlc_circuit(t, y, R, L, C, V0):
        """
        Circuito RLC serie:
        dI/dt = (V0 - R*I - Q/C) / L
        dQ/dt = I
        
        Args:
            t: Tiempo
            y: Vector [I, Q]
            R: Resistencia (Ω)
            L: Inductancia (H)
            C: Capacitancia (F)
            V0: Voltaje de entrada
        """
        I, Q = y
        dI = (V0 - R * I - Q / C) / L
        dQ = I
        return [dI, dQ]
    
    @classmethod
    def simulate(cls, I0, Q0, R, L, C, V0, t_max=0.1):
        """
        Simula el circuito RLC.
        
        Args:
            I0: Corriente inicial
            Q0: Carga inicial
            R: Resistencia
            L: Inductancia
            C: Capacitancia
            V0: Voltaje de entrada
            t_max: Tiempo máximo
            
        Returns:
            (t, I, Q, V): Arrays de tiempo, corriente, carga y voltaje
        """
        t_eval = np.linspace(0, t_max, 1000)
        sol = cls.solve_ode(
            cls.rlc_circuit,
            [I0, Q0],
            (0, t_max),
            t_eval=t_eval,
            R=R, L=L, C=C, V0=V0
        )
        V = sol.y[1] / C  # Voltaje en el capacitor
        return sol.t, sol.y[0], sol.y[1], V


class LorenzSimulator(SystemSimulator):
    """Simulador para el sistema de Lorenz."""
    
    @staticmethod
    def lorenz_system(t, y, sigma, rho, beta):
        """
        Sistema de Lorenz:
        dx/dt = sigma(y - x)
        dy/dt = x(rho - z) - y
        dz/dt = xy - beta*z
        
        Args:
            t: Tiempo
            y: Vector [x, y, z]
            sigma: Parámetro sigma
            rho: Parámetro rho
            beta: Parámetro beta
        """
        x, y, z = y
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        return [dx, dy, dz]
    
    @classmethod
    def simulate(cls, x0, y0, z0, sigma=10, rho=28, beta=8/3, t_max=40):
        """
        Simula el sistema de Lorenz.
        
        Args:
            x0, y0, z0: Condiciones iniciales
            sigma, rho, beta: Parámetros del sistema
            t_max: Tiempo máximo
            
        Returns:
            (t, x, y, z): Arrays de tiempo y coordenadas
        """
        t_eval = np.linspace(0, t_max, 5000)
        sol = cls.solve_ode(
            cls.lorenz_system,
            [x0, y0, z0],
            (0, t_max),
            t_eval=t_eval,
            sigma=sigma, rho=rho, beta=beta
        )
        return sol.t, sol.y[0], sol.y[1], sol.y[2]
