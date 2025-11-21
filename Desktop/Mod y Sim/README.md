# Simulador de Sistemas Dinámicos 🎯

Aplicación frontend desarrollada en Python con Tkinter para la simulación y visualización de sistemas dinámicos mediante resolución numérica de ecuaciones diferenciales ordinarias (EDOs).

## 📋 Descripción

Este simulador permite explorar el comportamiento de diferentes sistemas dinámicos a través de una interfaz gráfica intuitiva. Cada sistema incluye controles interactivos para ajustar parámetros y visualizar los resultados en tiempo real.

## 🔬 Sistemas Dinámicos Disponibles

1. **Ley de Enfriamiento de Newton** 🌡️
   - Modelo de transferencia de calor
   - Ecuación: `dT/dt = -k(T - T_ambiente)`

2. **Oscilador de Van der Pol** 📈
   - Sistema no lineal con oscilaciones
   - Exhibe ciclos límite

3. **Modelo Epidemiológico SIR** 🦠
   - Propagación de enfermedades infecciosas
   - Compartimentos: Susceptibles, Infectados, Recuperados

4. **Circuito RLC** ⚡
   - Circuito eléctrico serie
   - Resistencia, Inductancia y Capacitancia

5. **Sistema de Lorenz** 🌀
   - Sistema caótico tridimensional
   - Atractor extraño famoso

## 📁 Estructura del Proyecto

```
Mod y Sim/
│
├── main.py                 # Punto de entrada de la aplicación
│
├── pages/                  # Páginas de cada sistema dinámico
│   ├── __init__.py
│   ├── inicio.py          # Página de bienvenida
│   ├── newton.py          # Enfriamiento de Newton
│   ├── van_der_pol.py     # Oscilador Van der Pol
│   ├── sir.py             # Modelo SIR
│   ├── rlc.py             # Circuito RLC
│   └── lorenz.py          # Sistema de Lorenz
│
├── utils/                  # Utilidades y helpers
│   ├── __init__.py
│   ├── styles.py          # Configuración de estilos y colores
│   ├── navigation.py      # Gestor de navegación entre páginas
│   ├── graph_helper.py    # Integración Matplotlib-Tkinter
│   └── simulator.py       # Simuladores numéricos (SciPy)
│
├── assets/                 # Recursos (imágenes, etc.)
│
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias**

```powershell
pip install -r requirements.txt
```

Las dependencias principales son:
- `matplotlib` - Gráficos y visualización
- `numpy` - Computación numérica
- `scipy` - Integración de EDOs
- `tkinter` - Interfaz gráfica (incluido con Python)

3. **Ejecutar la aplicación**

```powershell
python main.py
```

## 🎮 Uso de la Aplicación

1. **Navegación**: Utiliza el menú lateral izquierdo para seleccionar un sistema dinámico

2. **Ajustar Parámetros**: Usa los sliders para modificar:
   - Condiciones iniciales
   - Constantes del sistema
   - Tiempo de simulación

3. **Simular**: Presiona el botón "▶ Ejecutar Simulación"

4. **Visualizar**: Observa los gráficos generados:
   - Gráficos temporales
   - Diagramas de fase
   - Gráficos 3D (Lorenz)

5. **Experimentar**: Modifica los parámetros para explorar diferentes comportamientos

## 🏗️ Arquitectura

### Patrón de Diseño

La aplicación utiliza un patrón de **navegación multipágina** mediante cambio de frames:

- **Ventana Principal**: Contiene la barra lateral y el área de contenido
- **Barra Lateral**: Menú de navegación con botones
- **Área de Contenido**: Frame dinámico que cambia según la selección
- **Páginas**: Cada sistema es un Frame independiente con sus controles y gráfico

### Componentes Principales

#### 1. `main.py` - Aplicación Principal
- Crea la ventana raíz de Tkinter
- Inicializa la interfaz (sidebar + área principal)
- Gestiona el layout general

#### 2. `utils/navigation.py` - Gestor de Navegación
- Implementa el cambio de frames
- Actualiza el encabezado de sección
- Destruye y crea páginas según sea necesario

#### 3. `utils/simulator.py` - Simuladores
- Clases especializadas para cada sistema
- Usa `scipy.integrate.solve_ivp` para resolver EDOs
- Retorna arrays de numpy con los resultados

#### 4. `utils/graph_helper.py` - Helpers de Gráficos
- `GraphCanvas`: Wrapper para gráficos 2D
- `Graph3DCanvas`: Wrapper para gráficos 3D
- Integración de Matplotlib con Tkinter

#### 5. `pages/*.py` - Páginas de Sistemas
Cada página sigue la misma estructura:
- Panel de controles (izquierda)
- Panel de gráfico (derecha)
- Controles con sliders para parámetros
- Botones de acción (simular, limpiar)
- Información del modelo

## 🎨 Personalización

### Colores y Estilos

Los colores y fuentes se definen en `utils/styles.py`:

```python
COLORS = {
    'background': '#f0f0f0',
    'sidebar': '#2c3e50',
    'accent': '#3498db',
    # ... más colores
}

FONTS = {
    'header': ('Segoe UI', 24, 'bold'),
    'button': ('Segoe UI', 10, 'bold'),
    # ... más fuentes
}
```

### Agregar Nuevos Sistemas

1. Crear nueva página en `pages/nuevo_sistema.py`
2. Implementar simulador en `utils/simulator.py`
3. Registrar en `utils/navigation.py`
4. Agregar botón en `main.py`

## 📚 Recursos Matemáticos

### Métodos Numéricos

La aplicación utiliza el método **Runge-Kutta de orden 4-5 (RK45)** de SciPy para resolver las ecuaciones diferenciales con alta precisión.

### Referencias

- Ecuaciones diferenciales ordinarias
- Sistemas dinámicos no lineales
- Teoría del caos (Lorenz)
- Modelado epidemiológico (SIR)
- Circuitos eléctricos

## 🤝 Contribuciones

Proyecto desarrollado para el curso de **Modelado y Simulación**.

## 📄 Licencia

Proyecto educativo - 2025

## ✨ Características Técnicas

- ✅ Interfaz gráfica profesional con Tkinter
- ✅ Integración nativa de Matplotlib
- ✅ Resolución numérica precisa con SciPy
- ✅ Arquitectura modular y extensible
- ✅ Código documentado y organizado
- ✅ Gráficos 2D y 3D interactivos
- ✅ Controles deslizantes (sliders) intuitivos
- ✅ Navegación fluida entre sistemas

---

**Desarrollado con 💙 para el aprendizaje de Sistemas Dinámicos**
