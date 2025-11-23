# Simulador de Sistemas Dinámicos 🎯

Aplicación educativa interactiva desarrollada en Python con Tkinter para la simulación, visualización y aprendizaje de sistemas dinámicos. Incluye un modo de **Laboratorio Educativo** con generación automática de ejercicios, evaluación y feedback personalizado.

## 📋 Descripción

Este simulador permite explorar el comportamiento de diferentes sistemas dinámicos a través de una interfaz gráfica intuitiva y educativa. Cada sistema incluye:
- 📚 **Información teórica completa** con ecuaciones y contexto físico
- 🎛️ **Sliders interactivos** con descripciones de cada parámetro
- 📊 **Visualizaciones mejoradas** con análisis cualitativo
- 🧪 **Modo Laboratorio** con ejercicios automáticos y evaluación
- 💾 **Persistencia de ejercicios** para retomar prácticas

## 🔬 Sistemas Dinámicos Disponibles

### Sistemas Clásicos

1. **Ley de Enfriamiento de Newton** 🌡️
   - Modelo de transferencia de calor por convección
   - Ecuación: `dT/dt = -k(T - T_ambiente)`
   - Aplicaciones: Forense, industria alimentaria, meteorología
   - **✨ MEJORADO**: Información educativa completa, análisis cualitativo, carga de parámetros de ejercicios

2. **Oscilador de Van der Pol** 📈
   - Sistema no lineal con oscilaciones autosostenidas
   - Exhibe ciclos límite estables
   - Aplicaciones: Circuitos electrónicos, biología, ingeniería

3. **Modelo Epidemiológico SIR** 🦠
   - Propagación de enfermedades infecciosas
   - Compartimentos: Susceptibles, Infectados, Recuperados
   - Aplicaciones: Salud pública, predicción de epidemias

4. **Circuito RLC** ⚡
   - Circuito eléctrico serie resonante
   - Resistencia, Inductancia y Capacitancia
   - Aplicaciones: Filtros, telecomunicaciones, electrónica

5. **Sistema de Lorenz** 🌀
   - Sistema caótico tridimensional
   - Atractor extraño famoso ("Efecto Mariposa")
   - Aplicaciones: Meteorología, física del caos

### Sistemas Avanzados

6. **Bifurcación de Hopf** 🔄
   - Transición entre punto fijo y ciclo límite
   - Parámetro de bifurcación μ
   - Aplicaciones: Teoría de bifurcaciones, dinámica no lineal

7. **Modelo Logístico** 📊
   - Crecimiento poblacional con capacidad de carga
   - Ecuación: `dN/dt = rN(1 - N/K)`
   - Aplicaciones: Ecología, demografía, economía

8. **Mapa de Verhulst** 🔢
   - Sistema dinámico discreto caótico
   - Ecuación: `x_{n+1} = rx_n(1 - x_n)`
   - Aplicaciones: Teoría del caos, dinámica poblacional

9. **Órbitas Espaciales** 🛰️
   - Mecánica orbital según leyes de Kepler
   - Ecuación: `d²r/dt² = -μr/|r|³`
   - Aplicaciones: Astrodinámica, misiones espaciales

10. **Atractor de Rössler (Mariposa)** 🦋
    - Sistema caótico 3D alternativo a Lorenz
    - Estructura de atractor en forma de mariposa
    - Aplicaciones: Teoría del caos, sistemas dinámicos

11. **Sistema Masa-Resorte-Amortiguador** 🔧
    - Oscilador mecánico con amortiguamiento
    - Ecuación: `m(d²x/dt²) + c(dx/dt) + kx = 0`
    - Aplicaciones: Mecánica, vibraciones, ingeniería civil

## 📁 Estructura del Proyecto

```
Mod y Sim/
│
├── main.py                     # Punto de entrada de la aplicación
│
├── pages/                      # Páginas de cada sistema dinámico
│   ├── __init__.py
│   ├── inicio.py              # Página de bienvenida
│   ├── laboratorio.py         # 🧪 Modo laboratorio educativo
│   ├── newton.py              # ✨ Enfriamiento de Newton (MEJORADO)
│   ├── van_der_pol.py         # Oscilador Van der Pol
│   ├── sir.py                 # Modelo SIR
│   ├── rlc.py                 # Circuito RLC
│   ├── lorenz.py              # Sistema de Lorenz
│   └── hopf.py                # Bifurcación de Hopf
│
├── utils/                      # Utilidades y helpers
│   ├── __init__.py
│   ├── styles.py              # Configuración de estilos y colores
│   ├── navigation.py          # Gestor de navegación entre páginas
│   ├── graph_helper.py        # Integración Matplotlib-Tkinter
│   ├── simulator.py           # Simuladores numéricos (SciPy) - 11 sistemas
│   ├── simulador_base.py      # 🆕 Clase base mejorada para páginas educativas
│   ├── ejercicio_generator.py # 🆕 Generador automático de ejercicios
│   ├── evaluador.py           # 🆕 Sistema de evaluación y feedback
│   └── ejercicio_state.py     # 🆕 Gestión de estado de ejercicios
│
├── assets/                     # Recursos (imágenes, etc.)
│
├── requirements.txt            # Dependencias del proyecto
├── README.md                  # Este archivo
└── GUIA_LABORATORIO.md        # 🆕 Guía completa del modo laboratorio
```

## 🎓 Modo Laboratorio Educativo

### Características Principales

#### 🎲 Generación Automática de Ejercicios
- **28 ejercicios educativos** disponibles (11 clásicos + 17 avanzados)
- **3 niveles de dificultad**: Principiante, Intermedio, Avanzado
- Parámetros aleatorios para ejercicios únicos
- Objetivos de aprendizaje claros
- Instrucciones paso a paso

### 📚 Catálogo Completo de Ejercicios

#### Ejercicios Clásicos (Base)
1. **Enfriamiento de Newton** - Procesos térmicos exponenciales
2. **Van der Pol** - Osciladores no lineales
3. **Modelo SIR** - Epidemiología básica
4. **Circuito RLC** - Electrónica y resonancia
5. **Sistema Lorenz** - Teoría del caos
6. **Bifurcación Hopf** - Transiciones de estabilidad
7. **Modelo Logístico** - Crecimiento poblacional
8. **Mapa de Verhulst** - Sistemas discretos
9. **Órbitas Espaciales** - Mecánica celeste
10. **Atractor Mariposa** - Sistemas caóticos
11. **Amortiguadores** - Sistemas mecánicos

#### 🎓 Ejercicios Educativos Avanzados (Nuevos)

##### **Ejercicio 1: Estabilidad de Puntos de Equilibrio en el Sistema Logístico**
- **Objetivo**: Comprender cómo la tasa de crecimiento y capacidad de carga afectan la evolución temporal
- **Conceptos**: Puntos de equilibrio, convergencia, estabilidad
- **Preguntas**: Valor de convergencia, efecto de parámetros, comportamiento oscilatorio

##### **Ejercicio 2: Transiciones de Fase en el Modelo de Verhulst Discreto**
- **Objetivo**: Explorar comportamientos complejos (ciclos, caos) mediante variación paramétrica
- **Conceptos**: Diagrama de bifurcación, duplicación de período, ruta al caos
- **Preguntas**: Primera bifurcación, comportamiento caótico, regiones periódicas

##### **Ejercicio 3: Análisis de Amortiguamiento en Osciladores Mecánicos**
- **Objetivo**: Clasificar regímenes de amortiguamiento
- **Conceptos**: Subamortiguado, crítico, sobreamortiguado, factor ζ
- **Preguntas**: Tipo de amortiguamiento, oscilaciones, retorno al equilibrio

##### **Ejercicio 4: Ciclos Límite en el Oscilador de Van der Pol**
- **Objetivo**: Identificar ciclos límite y su independencia de condiciones iniciales
- **Conceptos**: Atractores, no linealidad, oscilaciones autosostenidas
- **Preguntas**: Dependencia de condiciones iniciales, forma del ciclo, significado físico

##### **Ejercicio 5: Aparición de Oscilaciones por Bifurcación de Hopf**
- **Objetivo**: Observar transición de punto fijo a ciclo límite
- **Conceptos**: Bifurcación supercrítica, valores propios, estabilidad
- **Preguntas**: Comportamiento del sistema, valor crítico μ, crecimiento del ciclo

##### **Ejercicio 6: Circuito RLC - Resonancia y Factor de Calidad**
- **Objetivo**: Analizar respuesta en frecuencia e identificar resonancia
- **Conceptos**: Frecuencia de resonancia, factor Q, ancho de banda
- **Preguntas**: Frecuencia ω₀, selectividad del circuito, efecto de R

##### **Ejercicio 7: Propagación de Epidemias - Modelo SIR Básico**
- **Objetivo**: Comprender dinámica de propagación y número reproductivo R₀
- **Conceptos**: Susceptibles, infectados, recuperados, umbral epidémico
- **Preguntas**: Cálculo de R₀, condición de brote, decaimiento de infectados

##### **Ejercicio 8: Atractor de Lorenz - Sensibilidad a Condiciones Iniciales**
- **Objetivo**: Demostrar sensibilidad a condiciones iniciales (efecto mariposa)
- **Conceptos**: Caos determinista, atractores extraños, divergencia exponencial
- **Preguntas**: Divergencia de trayectorias, lóbulos del atractor, transición a caos

##### **Ejercicio 9: Órbitas Planetarias - Leyes de Kepler**
- **Objetivo**: Verificar leyes de Kepler mediante simulación
- **Conceptos**: Órbitas elípticas, conservación de energía/momento, período orbital
- **Preguntas**: Tipo de órbita, conservación de momento angular, tercera ley de Kepler

##### **Ejercicio 10: Transferencia Orbital de Hohmann**
- **Objetivo**: Diseñar maniobras orbitales eficientes
- **Conceptos**: Órbita de transferencia, Δv, eficiencia energética
- **Preguntas**: Semieje mayor, impulsos de velocidad, tiempo de transferencia

##### **Ejercicio 11: Enfriamiento de un Cuerpo - Ley de Newton**
- **Objetivo**: Aplicar ley de enfriamiento y determinar constantes térmicas
- **Conceptos**: Constante de tiempo τ, decaimiento exponencial, aproximación asintótica
- **Preguntas**: Fracción después de τ, tiempo de medio enfriamiento, convergencia

##### **Ejercicio 12: Dinámica de Carga de un Capacitor (RC)**
- **Objetivo**: Analizar carga/descarga de capacitores
- **Conceptos**: Constante RC, respuesta exponencial, transientes
- **Preguntas**: Tiempo para 95% de carga, efecto de duplicar R, corriente inicial

##### **Ejercicio 13: Comparación de Modelos de Crecimiento Poblacional**
- **Objetivo**: Contrastar crecimiento exponencial vs logístico
- **Conceptos**: Recursos limitados, punto de inflexión, divergencia de modelos
- **Preguntas**: Rango de similitud, tasa máxima, limitaciones del exponencial

##### **Ejercicio 14: Estabilidad en Sistemas Lineales de Segundo Orden**
- **Objetivo**: Clasificar estabilidad mediante valores propios
- **Conceptos**: Nodos, espirales, sillas, traza y determinante
- **Preguntas**: Estabilidad según tr y det, oscilaciones, tipo de punto fijo

##### **Ejercicio 15: Modelo SIR con Vacunación**
- **Objetivo**: Evaluar efecto de vacunación y calcular inmunidad de rebaño
- **Conceptos**: R₀ efectivo, umbral de vacunación, prevención de brotes
- **Preguntas**: Umbral p_c, prevención de brote, necesidad de 100% vacunación

##### **Ejercicio 16: Análisis de Perturbaciones en Órbitas Circulares**
- **Objetivo**: Estudiar efecto de perturbaciones en órbitas
- **Conceptos**: Perturbaciones radiales/tangenciales, excentricidad, cambios de energía
- **Preguntas**: Mantenimiento de circularidad, tipo de perturbación más efectiva, cambio energético

##### **Ejercicio 17: Oscilaciones Forzadas y Resonancia**
- **Objetivo**: Analizar respuesta a fuerzas periódicas externas
- **Conceptos**: Resonancia, curva de respuesta, desfase, peligro de resonancia
- **Preguntas**: Frecuencia de resonancia, efecto del amortiguamiento, susceptibilidad a daños

#### 📝 Tipos de Preguntas
- **Preguntas Numéricas**: Requieren cálculos basados en la simulación
- **Opción Múltiple**: Conceptos teóricos y análisis cualitativo
- Tolerancia de error configurable
- Unidades específicas por sistema

#### ✅ Evaluación Automática
- Calificación instantánea (10 puntos por pregunta)
- Aprobación con 70% o más
- Feedback detallado por cada pregunta
- Sugerencias personalizadas de mejora
- Reportes completos de laboratorio

#### 💾 Persistencia de Ejercicios
- Los ejercicios se guardan automáticamente
- Navega entre simuladores sin perder el ejercicio
- **Banner de ejercicio activo** en simuladores
- **Carga de parámetros** con un click
- Retoma donde dejaste

### Workflow Educativo

1. **Generar Ejercicio**
   - Selecciona sistema y dificultad
   - Genera ejercicio con parámetros aleatorios

2. **Leer Instrucciones**
   - Objetivos de aprendizaje
   - Instrucciones paso a paso
   - Análisis requerido

3. **Ejecutar Simulación**
   - Parámetros del ejercicio mostrados
   - Simulación con gráficos
   - Análisis cualitativo automático

4. **Explorar Libremente** ⭐ NUEVO
   - Navega a simuladores individuales
   - Ejercicio permanece guardado
   - Carga parámetros del ejercicio
   - Experimenta con variaciones

5. **Responder Preguntas**
   - Preguntas basadas en la simulación
   - Campos de entrada validados

6. **Evaluar y Mejorar**
   - Feedback detallado
   - Sugerencias de estudio
   - Genera nuevo ejercicio para practicar

## ✨ Mejoras Educativas Implementadas

### Páginas de Simuladores Mejoradas

Cada simulador ahora incluye:

#### 📚 Panel de Información Teórica (Colapsable)
- **Descripción completa** del fenómeno físico
- **Ecuaciones fundamentales** con notación matemática
- **Aplicaciones prácticas** en diferentes campos
- Contexto histórico y relevancia

#### 🎛️ Controles Interactivos Mejorados
- **Sliders con valores en tiempo real**
- **Descripción de cada parámetro** (qué representa)
- **Rangos educativos** (valores físicamente razonables)
- **Entry numérico** para valores exactos
- Sincronización bidireccional slider ↔ entry

#### 🔍 Análisis Cualitativo Automático
- Interpretación del comportamiento observado
- Identificación de regímenes dinámicos
- Análisis de estabilidad (sin cálculo pesado)
- Constantes de tiempo y escalas características
- Efecto de parámetros en el comportamiento

#### 📋 Integración con Ejercicios
- **Banner verde** cuando hay ejercicio activo
- Botón **"Cargar Parámetros del Ejercicio"**
- Información del ejercicio visible
- Navegación fluida laboratorio ↔ simuladores

### Ejemplo: Newton Mejorado

La página de Enfriamiento de Newton ahora incluye:

```python
📚 Información Teórica:
- Descripción del proceso físico
- Ecuaciones: dT/dt = -k(T - T_amb) y solución analítica
- 5 aplicaciones prácticas (forense, industria, medicina, etc.)

🎛️ Parámetros con Sliders:
- Temperatura Inicial (T₀): 0-200°C con descripción
- Temperatura Ambiente: -20-50°C con descripción
- Constante k: 0.01-1.0 (velocidad de enfriamiento)
- Tiempo de simulación: 10-200 min

📊 Visualización Mejorada:
- Curva de temperatura (azul/rojo según proceso)
- Línea de T_ambiente (verde)
- Constante de tiempo τ marcada
- Grid y leyendas claras

🔍 Análisis Automático:
- Tipo de proceso (enfriamiento/calentamiento)
- Constante de tiempo τ = 1/k
- Porcentaje de cambio completado
- Velocidad del proceso según k
- Interpretación física completa
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

### Modo Estándar (Simuladores Individuales)

1. **Navegación**: Utiliza el menú lateral izquierdo para seleccionar un sistema dinámico
2. **Ajustar Parámetros**: Usa los sliders para modificar condiciones y constantes
3. **Simular**: Presiona "▶ Ejecutar Simulación"
4. **Analizar**: Observa gráficos temporales, diagramas de fase o visualizaciones 3D

### Modo Laboratorio (Ejercicios Educativos)

1. **Generar Ejercicio**:
   - Selecciona un sistema del menú desplegable (28 opciones)
   - Elige dificultad: Principiante, Intermedio o Avanzado
   - Presiona "🎲 Generar Ejercicio Nuevo"

2. **Leer Instrucciones**:
   - Revisa objetivos de aprendizaje
   - Lee las instrucciones paso a paso
   - Comprende los parámetros del ejercicio

3. **Trabajar en Simuladores**:
   - El ejercicio queda **guardado automáticamente**
   - Navega al simulador individual correspondiente
   - Verás un **banner verde** indicando el ejercicio activo
   - Presiona "⚙ Cargar Parámetros" para usar los valores del ejercicio
   - Experimenta modificando parámetros
   - El ejercicio persiste al volver al laboratorio

4. **Responder Preguntas**:
   - Completa las preguntas numéricas o de opción múltiple
   - Basadas en el análisis de la simulación

5. **Evaluar Resultados**:
   - Presiona "✅ Evaluar Respuestas"
   - Recibe calificación automática (70% para aprobar)
   - Obtén feedback personalizado
   - Lee sugerencias de mejora específicas

### Ventajas del Sistema de Persistencia

✅ **Flexibilidad**: Navega libremente sin perder el ejercicio  
✅ **Exploración**: Experimenta con diferentes valores  
✅ **Aprendizaje Activo**: Combina teoría con práctica  
✅ **Trazabilidad**: Siempre sabes qué ejercicio está activo

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
