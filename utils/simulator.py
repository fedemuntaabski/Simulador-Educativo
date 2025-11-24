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
    
    params = {}
    ranges = {}
    
    @classmethod
    def get_default_params(cls):
        """Devuelve los parámetros por defecto del simulador."""
        return {k: v.get('default') for k, v in cls.params.items()}
    
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
    
    params = {
        'k': {'min': 0.01, 'max': 1.0, 'default': 0.1, 'desc': 'Constante de enfriamiento'},
        'T_env': {'min': -20, 'max': 50, 'default': 20, 'desc': 'Temperatura ambiente'}
    }
    ranges = {
        'k': (0.01, 1.0),
        'T_env': (-20, 50)
    }
    
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
    
    params = {
        'mu': {'min': 0.1, 'max': 10.0, 'default': 1.0, 'desc': 'Parámetro de no linealidad'}
    }
    ranges = {
        'mu': (0.1, 10.0)
    }
    
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
    
    params = {
        'beta': {'min': 0.0, 'max': 2.0, 'default': 0.3, 'desc': 'Tasa de infección'},
        'gamma': {'min': 0.0, 'max': 1.0, 'default': 0.1, 'desc': 'Tasa de recuperación'}
    }
    ranges = {
        'beta': (0.0, 2.0),
        'gamma': (0.0, 1.0)
    }
    
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
    
    params = {
        'R': {'min': 0.1, 'max': 100.0, 'default': 10.0, 'desc': 'Resistencia'},
        'L': {'min': 0.01, 'max': 2.0, 'default': 0.1, 'desc': 'Inductancia'},
        'C': {'min': 0.0001, 'max': 0.01, 'default': 0.001, 'desc': 'Capacitancia'},
        'V0': {'min': 0.0, 'max': 50.0, 'default': 10.0, 'desc': 'Voltaje entrada'}
    }
    ranges = {
        'R': (0.1, 100.0),
        'L': (0.01, 2.0),
        'C': (0.0001, 0.01),
        'V0': (0.0, 50.0)
    }
    
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
    
    params = {
        'sigma': {'min': 1.0, 'max': 50.0, 'default': 10.0, 'desc': 'Número de Prandtl'},
        'rho': {'min': 1.0, 'max': 100.0, 'default': 28.0, 'desc': 'Número de Rayleigh'},
        'beta': {'min': 0.1, 'max': 10.0, 'default': 8/3, 'desc': 'Relación geométrica'}
    }
    ranges = {
        'sigma': (1.0, 50.0),
        'rho': (1.0, 100.0),
        'beta': (0.1, 10.0)
    }
    
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


class HopfSimulator(SystemSimulator):
    """Simulador para la bifurcación de Hopf."""
    
    params = {
        'mu': {'min': -5.0, 'max': 5.0, 'default': 0.5, 'desc': 'Parámetro de bifurcación'},
        'omega': {'min': 0.1, 'max': 10.0, 'default': 1.0, 'desc': 'Frecuencia angular'}
    }
    ranges = {
        'mu': (-5.0, 5.0),
        'omega': (0.1, 10.0)
    }
    
    @staticmethod
    def hopf_system(t, state, mu, omega=1.0):
        """
        Forma normal de Hopf:
        dx/dt = (mu - (x^2 + y^2))x - omega*y
        dy/dt = (mu - (x^2 + y^2))y + omega*x
        """
        x, y = state
        r2 = x**2 + y**2
        dx = (mu - r2) * x - omega * y
        dy = (mu - r2) * y + omega * x
        return [dx, dy]

    @classmethod
    def simulate(cls, x0, y0, mu, omega=1.0, t_max=50):
        t_eval = np.linspace(0, t_max, 1000)
        sol = cls.solve_ode(
            cls.hopf_system, 
            [x0, y0], 
            (0, t_max), 
            t_eval=t_eval, 
            mu=mu, 
            omega=omega
        )
        return sol.t, sol.y[0], sol.y[1]


class LogisticSimulator(SystemSimulator):
    """Simulador para crecimiento logístico (continuo)."""
    
    params = {
        'r': {'min': 0.0, 'max': 2.0, 'default': 0.1, 'desc': 'Tasa de crecimiento'},
        'K': {'min': 100, 'max': 2000, 'default': 1000, 'desc': 'Capacidad de carga'}
    }
    ranges = {
        'r': (0.0, 2.0),
        'K': (100, 2000)
    }
    
    @staticmethod
    def logistic_equation(t, N, r, K):
        """dN/dt = r * N * (1 - N/K)"""
        return [r * N[0] * (1 - N[0] / K)]

    @classmethod
    def simulate(cls, N0, r, K, t_max=50):
        t_eval = np.linspace(0, t_max, 500)
        sol = cls.solve_ode(
            cls.logistic_equation, 
            [N0], 
            (0, t_max), 
            t_eval=t_eval, 
            r=r, 
            K=K
        )
        return sol.t, sol.y[0]


class VerhulstSimulator:
    """Simulador para el mapa logístico (discreto)."""
    
    params = {
        'r': {'min': 0.0, 'max': 4.0, 'default': 3.0, 'desc': 'Tasa de crecimiento'}
    }
    ranges = {
        'r': (0.0, 4.0)
    }
    
    @classmethod
    def get_default_params(cls):
        return {k: v.get('default') for k, v in cls.params.items()}
    
    @staticmethod
    def simulate(x0, r, steps=100):
        """
        x_{n+1} = r * x_n * (1 - x_n)
        """
        n = np.arange(steps + 1)
        x = np.zeros(steps + 1)
        x[0] = x0
        for i in range(steps):
            x[i+1] = r * x[i] * (1 - x[i])
        return n, x


class OrbitalSimulator(SystemSimulator):
    """Simulador de órbita simple (2 cuerpos)."""
    
    params = {
        'GM': {'min': 100, 'max': 5000, 'default': 1000, 'desc': 'Parámetro gravitacional'}
    }
    ranges = {
        'GM': (100, 5000)
    }
    
    @staticmethod
    def orbital_system(t, state, GM):
        x, y, vx, vy = state
        r2 = x**2 + y**2
        r = np.sqrt(r2)
        r3 = r**3
        
        ax = -GM * x / r3
        ay = -GM * y / r3
        return [vx, vy, ax, ay]

    @classmethod
    def simulate(cls, x0, y0, vx0, vy0, GM=1000, t_max=200):
        t_eval = np.linspace(0, t_max, 2000)
        sol = cls.solve_ode(
            cls.orbital_system, 
            [x0, y0, vx0, vy0], 
            (0, t_max), 
            t_eval=t_eval, 
            GM=GM
        )
        return sol.t, sol.y[0], sol.y[1], sol.y[2], sol.y[3]


class DamperSimulator(SystemSimulator):
    """Simulador de oscilador amortiguado y forzado."""
    
    params = {
        'm': {'min': 0.1, 'max': 10.0, 'default': 1.0, 'desc': 'Masa'},
        'c': {'min': 0.0, 'max': 10.0, 'default': 0.5, 'desc': 'Amortiguamiento'},
        'k': {'min': 0.1, 'max': 50.0, 'default': 2.0, 'desc': 'Constante elástica'},
        'F0': {'min': 0.0, 'max': 20.0, 'default': 0.0, 'desc': 'Amplitud fuerza'},
        'omega_f': {'min': 0.0, 'max': 10.0, 'default': 0.0, 'desc': 'Frecuencia fuerza'}
    }
    ranges = {
        'm': (0.1, 10.0),
        'c': (0.0, 10.0),
        'k': (0.1, 50.0),
        'F0': (0.0, 20.0),
        'omega_f': (0.0, 10.0)
    }
    
    @staticmethod
    def damped_oscillator(t, state, m, c, k, F0=0, omega_f=0):
        """m*x'' + c*x' + k*x = F0 * cos(omega_f * t)"""
        x, v = state
        dx = v
        forcing = F0 * np.cos(omega_f * t)
        dv = (forcing - c * v - k * x) / m
        return [dx, dv]

    @classmethod
    def simulate(cls, x0, v0, m, c, k, F0=0, omega_f=0, t_max=50):
        t_eval = np.linspace(0, t_max, 1000)
        sol = cls.solve_ode(
            cls.damped_oscillator, 
            [x0, v0], 
            (0, t_max), 
            t_eval=t_eval, 
            m=m, 
            c=c, 
            k=k,
            F0=F0,
            omega_f=omega_f
        )
        return sol.t, sol.y[0], sol.y[1]


class ButterflySimulator(LorenzSimulator):
    """Alias para el simulador de Lorenz (Efecto Mariposa)."""
    pass
