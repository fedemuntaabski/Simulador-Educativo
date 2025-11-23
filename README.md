# Simulador de Sistemas Dinámicos 🎯

Aplicación educativa interactiva desarrollada en Python con Tkinter para la simulación, visualización y aprendizaje de sistemas dinámicos.

## 📋 Descripción

Este simulador permite explorar el comportamiento de diferentes sistemas dinámicos a través de una interfaz gráfica intuitiva. Incluye un modo de **Laboratorio Educativo** para practicar con ejercicios generados automáticamente.

## 🚀 Instalación

1. **Requisitos**: Python 3.8+ y pip.
2. **Instalar dependencias**:
   ```powershell
   pip install -r requirements.txt
   ```
3. **Ejecutar la aplicación**:
   ```powershell
   python main.py
   ```

## 🎮 Uso

### Modo Simulador
Navega por los diferentes sistemas desde el menú lateral. Ajusta los parámetros con los sliders y visualiza los resultados en tiempo real.

### Modo Laboratorio
1. Ve a la sección **Laboratorio**.
2. Genera un ejercicio aleatorio (Principiante, Intermedio o Avanzado).
3. Resuelve el ejercicio utilizando los simuladores.
4. Evalúa tus respuestas para recibir feedback inmediato.

## 🔬 Sistemas Disponibles

*   **Clásicos**: Ley de Enfriamiento de Newton, Oscilador de Van der Pol, Modelo SIR, Circuito RLC, Sistema de Lorenz.
*   **Avanzados**: Bifurcación de Hopf, Modelo Logístico, Mapa de Verhulst, Órbitas Espaciales, Atractor de Rössler, Sistema Masa-Resorte-Amortiguador.

## 📁 Estructura

*   `main.py`: Punto de entrada.
*   `pages/`: Interfaces de cada sistema y laboratorio.
*   `utils/`: Lógica de simulación, navegación y evaluación.
