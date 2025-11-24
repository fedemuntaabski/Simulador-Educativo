"""
Página de Práctica de Laboratorio - Modo Educativo con Ejercicios Automáticos.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from utils.styles import COLORS, FONTS
from utils.ejercicio_generator import EjercicioGenerator
from utils.exercise_generator import generate_exercise  # Nuevo generador
from models.example_exercises import load_example_exercises  # Ejercicios de ejemplo
from utils.evaluador import Evaluador
from utils.ejercicio_state import EjercicioState
from utils.simulator import (
    NewtonCoolingSimulator, VanDerPolSimulator, SIRSimulator,
    HopfSimulator, LogisticSimulator, VerhulstSimulator,
    OrbitalSimulator, ButterflySimulator, DamperSimulator,
    RLCSimulator, LorenzSimulator
)
from utils.graph_helper import GraphCanvas, Graph3DCanvas
import matplotlib.pyplot as plt


class LaboratorioPage(tk.Frame):
    """
    Página de práctica de laboratorio con generación automática de ejercicios,
    instrucciones educacionales y evaluación automática.
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        self.generator = EjercicioGenerator()
        self.example_factory = None  # Factory de ejemplos desde models
        self.evaluador = Evaluador()
        self.ejercicio_actual = None
        self.respuestas = {}
        self.simulador_actual = None
        self.nav_callback = None  # Para navegación a simuladores
        
        # Cargar ejercicios de ejemplo
        try:
            self.example_factory = load_example_exercises()
            print(f"✓ Ejercicios de ejemplo cargados: {len(self.example_factory.get_all_exercises())} disponibles")
        except Exception as e:
            print(f"⚠ No se pudieron cargar ejercicios de ejemplo: {e}")
        
        self.create_widgets()
        
        # Cargar ejercicio si existe uno guardado
        self.cargar_ejercicio_guardado()
    
    def create_widgets(self):
        """Crea los widgets de la página."""
        # Contenedor principal
        main_container = tk.Frame(self, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título con indicador de ejercicio activo
        title_frame = tk.Frame(main_container, bg=COLORS['accent'], height=80)
        title_frame.pack(fill=tk.X, pady=(0, 15))
        title_frame.pack_propagate(False)
        
        title_container = tk.Frame(title_frame, bg=COLORS['accent'])
        title_container.pack(expand=True, fill=tk.BOTH, padx=20)
        
        tk.Label(
            title_container,
            text="🧪 PRÁCTICA DE LABORATORIO",
            font=('Segoe UI', 20, 'bold'),
            bg=COLORS['accent'],
            fg='white'
        ).pack(side=tk.LEFT, expand=True)
        
        # Indicador de ejercicio activo
        self.ejercicio_indicator = tk.Label(
            title_container,
            text="",
            font=('Segoe UI', 10),
            bg=COLORS['accent'],
            fg='white',
            anchor='e'
        )
        self.ejercicio_indicator.pack(side=tk.RIGHT, padx=10)
        
        # Frame superior: Generador de ejercicios
        self.create_generator_panel(main_container)
        
        # Frame del medio: Notebook con tabs
        self.create_notebook(main_container)
    
    def create_generator_panel(self, parent):
        """Crea el panel generador de ejercicios."""
        gen_frame = tk.Frame(parent, bg=COLORS['header'], relief=tk.RAISED, borderwidth=2)
        gen_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            gen_frame,
            text="📚 Generador de Ejercicios Automáticos",
            font=FONTS['section_title'],
            bg=COLORS['header'],
            fg=COLORS['text_dark']
        ).pack(pady=(15, 10))
        
        # Controles de generación
        controls_frame = tk.Frame(gen_frame, bg=COLORS['header'])
        controls_frame.pack(pady=(0, 15), padx=20, fill=tk.X)
        
        # Sistema
        tk.Label(controls_frame, text="Sistema Dinámico:", font=FONTS['label'],
                bg=COLORS['header']).grid(row=0, column=0, sticky='w', padx=(0, 10))
        
        # Restaurar sistema previamente seleccionado
        saved_system = EjercicioState.get_selected_system()
        self.sistema_var = tk.StringVar(value=saved_system)
        sistemas = [
            ('📚 EJERCICIOS CLÁSICOS', 'separator'),
            ('Enfriamiento Newton', 'newton'),
            ('Van der Pol', 'van_der_pol'),
            ('Modelo SIR', 'sir'),
            ('Circuito RLC', 'rlc'),
            ('Sistema Lorenz', 'lorenz'),
            ('Bifurcación Hopf', 'hopf'),
            ('Modelo Logístico', 'logistico'),
            ('Mapa Verhulst', 'verhulst'),
            ('Órbitas Espaciales', 'orbital'),
            ('Atractor Mariposa', 'mariposa'),
            ('Amortiguador', 'amortiguador'),
            ('', 'separator2'),
            ('🎓 EJERCICIOS EDUCATIVOS AVANZADOS', 'separator3'),
            ('1. Equilibrio Sistema Logístico', 'equilibrio_logistico'),
            ('2. Transiciones Verhulst', 'verhulst_transiciones'),
            ('3. Análisis de Amortiguamiento', 'amortiguamiento_analisis'),
            ('4. Ciclos Límite Van der Pol', 'ciclo_limite'),
            ('5. Aparición Bifurcación Hopf', 'hopf_aparicion'),
            ('6. Resonancia RLC', 'rlc_resonancia'),
            ('7. Propagación Epidemias SIR', 'sir_propagacion'),
            ('8. Sensibilidad Lorenz', 'lorenz_sensibilidad'),
            ('9. Leyes de Kepler', 'orbital_kepler'),
            ('10. Transferencia Hohmann', 'orbital_hohmann'),
            ('11. Enfriamiento Newton', 'newton_enfriamiento'),
            ('12. Carga Capacitor RC', 'rc_carga'),
            ('13. Comparación Crecimiento', 'crecimiento_comparacion'),
            ('14. Estabilidad Lineal', 'estabilidad_lineal'),
            ('15. SIR con Vacunación', 'sir_vacunacion'),
            ('16. Perturbaciones Orbitales', 'orbital_perturbaciones'),
            ('17. Oscilador Forzado', 'oscilador_forzado')
        ]
        
        sistema_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.sistema_var,
            values=[s[0] for s in sistemas if s[1] not in ['separator', 'separator2', 'separator3']],
            state='readonly',
            width=35
        )
        sistema_combo.grid(row=0, column=1, sticky='w')
        sistema_combo.bind('<<ComboboxSelected>>', lambda e: self.on_sistema_changed())
        
        # Mapeo de nombres a IDs
        self.sistema_map = {s[0]: s[1] for s in sistemas if s[1] not in ['separator', 'separator2', 'separator3']}
        
        # Dificultad
        tk.Label(controls_frame, text="Dificultad:", font=FONTS['label'],
                bg=COLORS['header']).grid(row=0, column=2, sticky='w', padx=(20, 10))
        
        # Restaurar dificultad previamente seleccionada
        saved_difficulty = EjercicioState.get_selected_difficulty()
        self.dificultad_var = tk.StringVar(value=saved_difficulty)
        dificultad_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.dificultad_var,
            values=['principiante', 'intermedio', 'avanzado'],
            state='readonly',
            width=15
        )
        dificultad_combo.grid(row=0, column=3, sticky='w')
        dificultad_combo.bind('<<ComboboxSelected>>', lambda e: self.on_dificultad_changed())
        
        # Botón generar
        tk.Button(
            controls_frame,
            text="🎲 Generar Ejercicio Nuevo",
            font=FONTS['button'],
            bg=COLORS['accent'],
            fg='white',
            cursor="hand2",
            command=self.generar_ejercicio,
            pady=8,
            padx=15
        ).grid(row=0, column=4, sticky='w', padx=(20, 0))
    
    def create_notebook(self, parent):
        """Crea el notebook con pestañas."""
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 1: Instrucciones y Objetivos
        self.tab_instrucciones = tk.Frame(self.notebook, bg=COLORS['card_bg'])
        self.notebook.add(self.tab_instrucciones, text='📖 Instrucciones')
        self.create_instrucciones_tab()
        
        # Pestaña 2: Preguntas
        self.tab_preguntas = tk.Frame(self.notebook, bg=COLORS['card_bg'])
        self.notebook.add(self.tab_preguntas, text='❓ Preguntas')
        self.create_preguntas_tab()
        
        # Pestaña 3: Resultados
        self.tab_resultados = tk.Frame(self.notebook, bg=COLORS['card_bg'])
        self.notebook.add(self.tab_resultados, text='📊 Resultados')
        self.create_resultados_tab()
    
    def create_instrucciones_tab(self):
        """Crea la pestaña de instrucciones."""
        # Scrollable text
        self.instrucciones_text = scrolledtext.ScrolledText(
            self.tab_instrucciones,
            font=FONTS['label'],
            wrap=tk.WORD,
            padx=20,
            pady=20,
            bg=COLORS['input_bg']
        )
        self.instrucciones_text.pack(fill=tk.BOTH, expand=True)
        
        # Texto inicial
        self.instrucciones_text.insert('1.0', 
            "🧪 BIENVENIDO AL LABORATORIO DE SISTEMAS DINÁMICOS\n\n"
            "Selecciona un sistema y una dificultad, luego presiona 'Generar Ejercicio Nuevo'.\n\n"
            "Los ejercicios se generan automáticamente con parámetros aleatorios y preguntas específicas.\n\n"
            "Sigue las instrucciones, ejecuta el ejercicio y responde las preguntas para completar el laboratorio."
        )
        self.instrucciones_text.config(state='disabled')
    
    def create_preguntas_tab(self):
        """Crea la pestaña de preguntas."""
        # Scroll frame para preguntas
        canvas = tk.Canvas(self.tab_preguntas, bg=COLORS['card_bg'])
        scrollbar = ttk.Scrollbar(self.tab_preguntas, orient="vertical", command=canvas.yview)
        self.preguntas_frame = tk.Frame(canvas, bg=COLORS['card_bg'])
        
        self.preguntas_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.preguntas_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mensaje inicial
        tk.Label(
            self.preguntas_frame,
            text="Genera un ejercicio para ver las preguntas",
            font=FONTS['label'],
            bg=COLORS['card_bg'],
            fg=COLORS['text_muted']
        ).pack(pady=50)
    
    def create_resultados_tab(self):
        """Crea la pestaña de resultados."""
        self.resultados_text = scrolledtext.ScrolledText(
            self.tab_resultados,
            font=('Courier New', 10),
            wrap=tk.WORD,
            padx=20,
            pady=20,
            bg=COLORS['input_bg']
        )
        self.resultados_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botón evaluar
        btn_frame = tk.Frame(self.tab_resultados, bg=COLORS['card_bg'])
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(
            btn_frame,
            text="✅ Evaluar Respuestas",
            font=FONTS['button'],
            bg=COLORS['accent'],
            fg='white',
            cursor="hand2",
            command=self.evaluar_respuestas,
            pady=12,
            padx=30,
            state='disabled'
        ).pack()
        
        self.btn_evaluar = btn_frame.winfo_children()[-1]
    
    def generar_ejercicio(self):
        """Genera un nuevo ejercicio automático."""
        sistema_nombre = self.sistema_var.get()
        sistema_id = self.sistema_map.get(sistema_nombre, 'newton')
        dificultad = self.dificultad_var.get()
        
        # Guardar selecciones en el estado global
        EjercicioState.set_selected_system(sistema_nombre)
        EjercicioState.set_selected_difficulty(dificultad)
        
        try:
            self.ejercicio_actual = self.generator.generar_ejercicio(sistema_id, dificultad)
            self.respuestas = {}
            
            # Guardar en el estado global
            EjercicioState.set_ejercicio(self.ejercicio_actual)
            
            # Actualizar instrucciones
            self.mostrar_instrucciones()
            
            # Mostrar parámetros
            self.mostrar_parametros()
            
            # Generar preguntas
            self.mostrar_preguntas()
            
            # Habilitar botones
            self.btn_evaluar.config(state='normal')
            
            # Actualizar indicador
            self.actualizar_indicador_ejercicio()
            
            # Limpiar resultados
            self.resultados_text.delete('1.0', tk.END)
            self.resultados_text.insert('1.0', 
                "Completa el ejercicio y responde las preguntas.\n"
                "Luego presiona 'Evaluar Respuestas' para ver tu calificación.")
            
            messagebox.showinfo(
                "Ejercicio Generado",
                f"Nuevo ejercicio de {self.ejercicio_actual['titulo']} generado.\n"
                f"Dificultad: {dificultad.upper()}\n\n"
                "Revisa las instrucciones en la pestaña correspondiente.\n\n"
                "💡 Puedes explorar el simulador individual desde el menú lateral\n"
                "y retomar este ejercicio cuando regreses al Laboratorio."
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el ejercicio:\n{str(e)}")
    
    def mostrar_instrucciones(self):
        """Muestra las instrucciones del ejercicio."""
        if not self.ejercicio_actual:
            return
        
        ej = self.ejercicio_actual
        texto = []
        
        texto.append(f"{'='*60}\n")
        texto.append(f"{ej['titulo']}\n")
        texto.append(f"{'='*60}\n\n")
        texto.append(f"🎯 DIFICULTAD: {ej['dificultad'].upper()}\n\n")
        
        texto.append("📋 OBJETIVOS DE APRENDIZAJE:\n")
        for i, objetivo in enumerate(ej['objetivos'], 1):
            texto.append(f"  {i}. {objetivo}\n")
        texto.append("\n")
        
        texto.append("📝 INSTRUCCIONES:\n")
        for instr in ej['instrucciones']:
            texto.append(f"  {instr}\n")
        texto.append("\n")
        
        if 'analisis_requerido' in ej:
            texto.append("🔬 ANÁLISIS REQUERIDO:\n")
            for analisis in ej['analisis_requerido']:
                texto.append(f"  • {analisis}\n")
        
        self.instrucciones_text.config(state='normal')
        self.instrucciones_text.delete('1.0', tk.END)
        self.instrucciones_text.insert('1.0', ''.join(texto))
        self.instrucciones_text.config(state='disabled')
    
    def mostrar_parametros(self):
        """Muestra los parámetros del ejercicio en las instrucciones."""
        # Esta función ya no es necesaria ya que los parámetros se muestran en las instrucciones
        pass
    
    def mostrar_preguntas(self):
        """Muestra las preguntas del ejercicio."""
        if not self.ejercicio_actual:
            return
        
        # Limpiar frame
        for widget in self.preguntas_frame.winfo_children():
            widget.destroy()
        
        self.respuestas = {}
        
        tk.Label(
            self.preguntas_frame,
            text="❓ PREGUNTAS DEL EJERCICIO",
            font=FONTS['section_title'],
            bg=COLORS['card_bg']
        ).pack(pady=(20, 15))
        
        for pregunta in self.ejercicio_actual['preguntas']:
            self.crear_pregunta_widget(pregunta)
    
    def crear_pregunta_widget(self, pregunta):
        """Crea el widget para una pregunta."""
        # Frame para la pregunta
        q_frame = tk.Frame(self.preguntas_frame, bg=COLORS['card_bg'], relief=tk.RAISED, borderwidth=1)
        q_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Texto de la pregunta
        tk.Label(
            q_frame,
            text=f"Pregunta {pregunta['id']}:",
            font=('Segoe UI', 11, 'bold'),
            bg=COLORS['card_bg'],
            anchor='w'
        ).pack(fill=tk.X, padx=15, pady=(10, 5))
        
        tk.Label(
            q_frame,
            text=pregunta['texto'],
            font=FONTS['label'],
            bg=COLORS['card_bg'],
            anchor='w',
            wraplength=700,
            justify=tk.LEFT
        ).pack(fill=tk.X, padx=15, pady=(0, 10))
        
        # Campo de respuesta según tipo
        if pregunta['tipo'] == 'numerica':
            respuesta_frame = tk.Frame(q_frame, bg=COLORS['card_bg'])
            respuesta_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
            
            tk.Label(respuesta_frame, text="Respuesta:", bg=COLORS['card_bg']).pack(side=tk.LEFT)
            
            entry = tk.Entry(respuesta_frame, font=FONTS['label'], width=15)
            entry.pack(side=tk.LEFT, padx=10)
            
            tk.Label(respuesta_frame, text=pregunta.get('unidad', ''),
                    bg=COLORS['card_bg'], fg=COLORS['text_muted']).pack(side=tk.LEFT)
            
            self.respuestas[pregunta['id']] = entry
            
        elif pregunta['tipo'] == 'opcion_multiple':
            var = tk.IntVar(value=-1)
            self.respuestas[pregunta['id']] = var
            
            for i, opcion in enumerate(pregunta['opciones']):
                tk.Radiobutton(
                    q_frame,
                    text=opcion,
                    variable=var,
                    value=i,
                    font=FONTS['label'],
                    bg=COLORS['card_bg'],
                    anchor='w'
                ).pack(fill=tk.X, padx=30, pady=2)
            
            tk.Label(q_frame, text="", bg=COLORS['card_bg']).pack(pady=5)  # Espaciado
    
    def ejecutar_simulacion(self):
        """Ejecuta el ejercicio con los parámetros especificados."""
        # Esta funcionalidad ya no es necesaria en el laboratorio
        # Los ejercicios se resuelven conceptualmente
        messagebox.showinfo(
            "Información",
            "En el modo laboratorio, los ejercicios se resuelven mediante análisis conceptual.\n\n"
            "Para ver simulaciones interactivas, selecciona el sistema específico del menú lateral."
        )
    
    def evaluar_respuestas(self):
        """Evalúa las respuestas del estudiante."""
        if not self.ejercicio_actual:
            messagebox.showwarning("Aviso", "No hay ejercicio activo")
            return
        
        # Recolectar respuestas
        respuestas_dict = {}
        for pregunta_id, widget in self.respuestas.items():
            if isinstance(widget, tk.Entry):
                valor = widget.get().strip()
                if valor:
                    respuestas_dict[pregunta_id] = valor
            elif isinstance(widget, tk.IntVar):
                valor = widget.get()
                if valor != -1:
                    respuestas_dict[pregunta_id] = valor
        
        # Evaluar
        resultados = self.evaluador.evaluar_ejercicio(
            self.ejercicio_actual, respuestas_dict
        )
        
        # Mostrar resultados
        reporte = self.evaluador.generar_reporte(
            self.ejercicio_actual, resultados
        )
        
        self.resultados_text.delete('1.0', tk.END)
        self.resultados_text.insert('1.0', reporte)
        
        # Sugerencias
        sugerencias = self.evaluador.sugerencias_mejora(
            self.ejercicio_actual, resultados
        )
        
        if sugerencias:
            self.resultados_text.insert(tk.END, "\n\n📚 SUGERENCIAS DE MEJORA:\n")
            for sug in sugerencias:
                self.resultados_text.insert(tk.END, f"  • {sug}\n")
        
        # Cambiar a la pestaña de resultados
        self.notebook.select(self.tab_resultados)
        
        # Mensaje de resultado
        if resultados['aprobado']:
            messagebox.showinfo(
                "¡Felicitaciones! ✓",
                f"Has aprobado el ejercicio\n\n"
                f"Puntuación: {resultados['puntuacion']}/{resultados['puntuacion_maxima']}\n"
                f"Porcentaje: {resultados['porcentaje']:.1f}%"
            )
        else:
            messagebox.showwarning(
                "Necesitas mejorar",
                f"No has alcanzado el mínimo para aprobar\n\n"
                f"Puntuación: {resultados['puntuacion']}/{resultados['puntuacion_maxima']}\n"
                f"Porcentaje: {resultados['porcentaje']:.1f}%\n\n"
                f"Revisa las sugerencias de mejora."
            )
    
    def cargar_ejercicio_guardado(self):
        """Carga el ejercicio guardado si existe."""
        ejercicio_guardado = EjercicioState.get_ejercicio()
        
        if ejercicio_guardado:
            self.ejercicio_actual = ejercicio_guardado
            
            # Restaurar interfaz
            self.mostrar_instrucciones()
            self.mostrar_parametros()
            self.mostrar_preguntas()
            
            # Habilitar botones
            if hasattr(self, 'btn_simular'):
                self.btn_simular.config(state='normal')
            if hasattr(self, 'btn_evaluar'):
                self.btn_evaluar.config(state='normal')
            
            # Actualizar indicador
            if hasattr(self, 'ejercicio_indicator'):
                self.actualizar_indicador_ejercicio()
            
            # Restaurar respuestas guardadas
            respuestas_guardadas = EjercicioState.get_respuestas()
            for pregunta_id, respuesta in respuestas_guardadas.items():
                if pregunta_id in self.respuestas:
                    widget = self.respuestas[pregunta_id]
                    if isinstance(widget, tk.Entry):
                        widget.delete(0, tk.END)
                        widget.insert(0, str(respuesta))
                    elif isinstance(widget, tk.IntVar):
                        widget.set(respuesta)
    
    def actualizar_indicador_ejercicio(self):
        """Actualiza el indicador de ejercicio activo."""
        if self.ejercicio_actual:
            info = EjercicioState.get_info_ejercicio()
            self.ejercicio_indicator.config(
                text=f"📋 Ejercicio activo: {info}",
                fg='#90EE90'  # Verde claro
            )
        else:
            self.ejercicio_indicator.config(text="", fg='white')
    
    def set_navigation_callback(self, callback):
        """
        Establece el callback de navegación.
        
        Args:
            callback: Función para navegar a otras páginas
        """
        self.nav_callback = callback
    
    def on_sistema_changed(self):
        """Callback cuando cambia el sistema seleccionado."""
        sistema_nombre = self.sistema_var.get()
        EjercicioState.set_selected_system(sistema_nombre)
    
    def on_dificultad_changed(self):
        """Callback cuando cambia la dificultad seleccionada."""
        dificultad = self.dificultad_var.get()
        EjercicioState.set_selected_difficulty(dificultad)
