import math

def simulate_sir(params):
    """
    Simulates the SIR model (Susceptible-Infected-Recovered).
    
    Params:
        beta (float): Infection rate.
        gamma (float): Recovery rate.
        S0 (float): Initial susceptible population.
        I0 (float): Initial infected population.
        R0 (float): Initial recovered population.
        steps (int): Number of simulation steps.
        dt (float): Time step size.
        
    Returns:
        dict: {'t': [], 'S': [], 'I': [], 'R': []}
    """
    beta = params.get('beta', 0.3)
    gamma = params.get('gamma', 0.1)
    S = params.get('S0', 990)
    I = params.get('I0', 10)
    R = params.get('R0', 0)
    steps = params.get('steps', 100)
    dt = params.get('dt', 0.1)
    
    t_values = [0]
    S_values = [S]
    I_values = [I]
    R_values = [R]
    
    current_t = 0
    total_pop = S + I + R
    
    for _ in range(steps):
        # Simple Euler method
        # dS/dt = -beta * S * I / N
        # dI/dt = beta * S * I / N - gamma * I
        # dR/dt = gamma * I
        
        new_S = S - (beta * S * I / total_pop) * dt
        new_I = I + ((beta * S * I / total_pop) - gamma * I) * dt
        new_R = R + (gamma * I) * dt
        
        S, I, R = new_S, new_I, new_R
        current_t += dt
        
        t_values.append(round(current_t, 2))
        S_values.append(S)
        I_values.append(I)
        R_values.append(R)
        
    return {
        't': t_values,
        'S': S_values,
        'I': I_values,
        'R': R_values
    }

def simulate_logistic(params):
    """
    Simulates the Logistic Map (discrete chaos).
    x_{n+1} = r * x_n * (1 - x_n)
    
    Params:
        r (float): Growth rate parameter (typically 0-4).
        x0 (float): Initial population ratio (0-1).
        steps (int): Number of steps.
        
    Returns:
        dict: {'t': [], 'x': []}
    """
    r = params.get('r', 3.0)
    x = params.get('x0', 0.5)
    steps = params.get('steps', 50)
    
    t_values = [0]
    x_values = [x]
    
    for i in range(1, steps + 1):
        x = r * x * (1 - x)
        t_values.append(i)
        x_values.append(x)
        
    return {
        't': t_values,
        'x': x_values
    }

def simulate_verhulst(params):
    """
    Simulates the Verhulst equation (Logistic growth continuous approximation).
    dP/dt = r * P * (1 - P / K)
    
    Params:
        r (float): Growth rate.
        K (float): Carrying capacity.
        P0 (float): Initial population.
        steps (int): Number of steps.
        dt (float): Time step.
        
    Returns:
        dict: {'t': [], 'P': []}
    """
    r = params.get('r', 0.1)
    K = params.get('K', 1000)
    P = params.get('P0', 10)
    steps = params.get('steps', 100)
    dt = params.get('dt', 0.1)
    
    t_values = [0]
    P_values = [P]
    current_t = 0
    
    for _ in range(steps):
        # dP = r * P * (1 - P/K) * dt
        dP = r * P * (1 - P / K) * dt
        P += dP
        current_t += dt
        
        t_values.append(round(current_t, 2))
        P_values.append(P)
        
    return {
        't': t_values,
        'P': P_values
    }

def simulate_newton_cooling(params):
    """
    Simulates Newton's Law of Cooling.
    dT/dt = -k * (T - T_env)
    
    Params:
        k (float): Cooling constant.
        T0 (float): Initial temperature.
        T_env (float): Environment temperature.
        steps (int): Number of steps.
        dt (float): Time step.
        
    Returns:
        dict: {'t': [], 'T': []}
    """
    k = params.get('k', 0.1)
    T = params.get('T0', 100)
    T_env = params.get('T_env', 20)
    steps = params.get('steps', 100)
    dt = params.get('dt', 0.1)
    
    t_values = [0]
    T_values = [T]
    current_t = 0
    
    for _ in range(steps):
        dT = -k * (T - T_env) * dt
        T += dT
        current_t += dt
        
        t_values.append(round(current_t, 2))
        T_values.append(T)
        
    return {
        't': t_values,
        'T': T_values
    }

def simulate_damped_oscillator(params):
    """
    Simulates a Damped Harmonic Oscillator.
    m*x'' + c*x' + k*x = 0
    
    Params:
        m (float): Mass.
        c (float): Damping coefficient.
        k (float): Spring constant.
        x0 (float): Initial position.
        v0 (float): Initial velocity.
        steps (int): Number of steps.
        dt (float): Time step.
        
    Returns:
        dict: {'t': [], 'x': [], 'v': []}
    """
    m = params.get('m', 1.0)
    c = params.get('c', 0.5)
    k = params.get('k', 2.0)
    x = params.get('x0', 1.0)
    v = params.get('v0', 0.0)
    steps = params.get('steps', 100)
    dt = params.get('dt', 0.1)
    
    t_values = [0]
    x_values = [x]
    v_values = [v]
    current_t = 0
    
    for _ in range(steps):
        # Acceleration a = (-c*v - k*x) / m
        a = (-c * v - k * x) / m
        
        # Update velocity and position (Euler-Cromer for better stability)
        v += a * dt
        x += v * dt
        current_t += dt
        
        t_values.append(round(current_t, 2))
        x_values.append(x)
        v_values.append(v)
        
    return {
        't': t_values,
        'x': x_values,
        'v': v_values
    }

def simulate_simple_orbit(params):
    """
    Simulates a simple 2D orbit (e.g., planet around a star) using Newton's gravity.
    F = G * M * m / r^2
    
    Params:
        GM (float): Gravitational parameter (G * Mass of central body).
        x0 (float): Initial x position.
        y0 (float): Initial y position.
        vx0 (float): Initial x velocity.
        vy0 (float): Initial y velocity.
        steps (int): Number of steps.
        dt (float): Time step.
        
    Returns:
        dict: {'t': [], 'x': [], 'y': [], 'vx': [], 'vy': []}
    """
    GM = params.get('GM', 1000.0)
    x = params.get('x0', 10.0)
    y = params.get('y0', 0.0)
    vx = params.get('vx0', 0.0)
    vy = params.get('vy0', 8.0) # Approximate circular velocity sqrt(GM/r) ~ sqrt(1000/10) = 10
    steps = params.get('steps', 200)
    dt = params.get('dt', 0.05)
    
    t_values = [0]
    x_values = [x]
    y_values = [y]
    vx_values = [vx]
    vy_values = [vy]
    current_t = 0
    
    for _ in range(steps):
        r2 = x*x + y*y
        r = math.sqrt(r2)
        
        # Acceleration components
        # a = -GM / r^2 * (unit vector)
        # ax = -GM / r^2 * (x/r) = -GM * x / r^3
        # ay = -GM / r^2 * (y/r) = -GM * y / r^3
        
        factor = -GM / (r * r * r)
        ax = factor * x
        ay = factor * y
        
        # Semi-implicit Euler (Symplectic Euler) for energy conservation
        vx += ax * dt
        vy += ay * dt
        
        x += vx * dt
        y += vy * dt
        
        current_t += dt
        
        t_values.append(round(current_t, 2))
        x_values.append(x)
        y_values.append(y)
        vx_values.append(vx)
        vy_values.append(vy)
        
    return {
        't': t_values,
        'x': x_values,
        'y': y_values,
        'vx': vx_values,
        'vy': vy_values
    }
