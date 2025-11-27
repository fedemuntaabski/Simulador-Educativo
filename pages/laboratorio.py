"""
Página de Práctica de Laboratorio - Modo Educativo con Ejercicios Automáticos.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from utils.styles import COLORS, FONTS
from utils.ejercicio_generator import EjercicioGenerator
from utils.evaluador import Evaluador
from utils.ejercicio_state import EjercicioState


class LaboratorioPage(tk.Frame):
    """
    Página de práctica de laboratorio con generación automática de ejercicios,
    instrucciones educacionales y evaluación automática.
    """
    
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        
        self.generator = EjercicioGenerator()
        self.evaluador = Evaluador()
        self.ejercicio_actual = None
        self.respuestas = {}
        self.nav_callback = None  # Para navegación a simuladores
        
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
            ('📚 SISTEMAS DINÁMICOS', 'separator'),
            ('Enfriamiento de Newton', 'newton'),
            ('Oscilador Van der Pol', 'van_der_pol'),
            ('Epidemiología SIR', 'sir'),
            ('Circuito RLC', 'rlc'),
            ('Atractor de Lorenz', 'lorenz'),
            ('Bifurcación de Hopf', 'hopf'),
            ('Crecimiento Logístico', 'logistico'),
            ('Mapa de Verhulst', 'verhulst'),
            ('Mecánica Orbital', 'orbital'),
            ('Atractor de Rössler', 'mariposa'),
            ('Oscilador Amortiguado', 'amortiguador'),
            ('', 'separator2'),
            ('🎓 EJERCICIOS AVANZADOS', 'separator3'),
            ('Equilibrio Poblacional', 'equilibrio_logistico'),
            ('Transiciones al Caos', 'verhulst_transiciones'),
            ('Análisis de Amortiguamiento', 'amortiguamiento_analisis'),
            ('Ciclos Límite', 'ciclo_limite'),
            ('Aparición de Bifurcaciones', 'hopf_aparicion'),
            ('Resonancia Eléctrica', 'rlc_resonancia'),
            ('Propagación de Epidemias', 'sir_propagacion'),
            ('Sensibilidad al Caos', 'lorenz_sensibilidad'),
            ('Leyes de Kepler', 'orbital_kepler'),
            ('Transferencia Orbital', 'orbital_hohmann'),
            ('Transferencia de Calor', 'newton_enfriamiento'),
            ('Carga de Capacitor', 'rc_carga'),
            ('Comparación de Modelos', 'crecimiento_comparacion'),
            ('Estabilidad de Sistemas', 'estabilidad_lineal'),
            ('Vacunación y Epidemias', 'sir_vacunacion'),
            ('Perturbaciones Orbitales', 'orbital_perturbaciones'),
            ('Oscilador Forzado', 'oscilador_forzado')
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
        """Muestra las instrucciones del ejercicio con formato mejorado."""
        if not self.ejercicio_actual:
            return
        
        ej = self.ejercicio_actual
        texto = []
        
        # Las instrucciones ahora vienen pre-formateadas del generador
        if isinstance(ej['instrucciones'], list):
            # Nuevo formato con consigna detallada
            for linea in ej['instrucciones']:
                texto.append(f"{linea}\n")
        else:
            # Formato antiguo (fallback)
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
        
        # Agregar objetivos de aprendizaje si no están en las instrucciones
        if '📋 OBJETIVOS' not in ''.join(texto) and 'OBJETIVOS' not in ''.join(texto):
            texto.append("\n")
            texto.append("📋 OBJETIVOS DE APRENDIZAJE:\n")
            for i, objetivo in enumerate(ej['objetivos'], 1):
                texto.append(f"  {i}. {objetivo}\n")
        
        # Agregar análisis requerido
        if 'analisis_requerido' in ej and ej['analisis_requerido']:
            texto.append("\n")
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
        """Muestra las preguntas del ejercicio con formato mejorado."""
        if not self.ejercicio_actual:
            return
        
        # Limpiar frame
        for widget in self.preguntas_frame.winfo_children():
            widget.destroy()
        
        self.respuestas = {}
        preguntas = self.ejercicio_actual['preguntas']
        
        # Header principal
        header_main = tk.Frame(self.preguntas_frame, bg=COLORS['accent'], height=60)
        header_main.pack(fill=tk.X, pady=(0, 10))
        header_main.pack_propagate(False)
        
        header_content = tk.Frame(header_main, bg=COLORS['accent'])
        header_content.pack(fill=tk.BOTH, expand=True, padx=20)
        
        tk.Label(
            header_content,
            text="❓ PREGUNTAS DEL EJERCICIO",
            font=('Segoe UI', 16, 'bold'),
            bg=COLORS['accent'],
            fg='white'
        ).pack(side=tk.LEFT, pady=15)
        
        # Contador de preguntas
        num_numericas = sum(1 for p in preguntas if p['tipo'] == 'numerica')
        num_multiple = sum(1 for p in preguntas if p['tipo'] == 'opcion_multiple')
        
        tk.Label(
            header_content,
            text=f"📊 {num_numericas} cálculo  |  📝 {num_multiple} selección",
            font=('Segoe UI', 10),
            bg=COLORS['accent'],
            fg='#E0E0E0'
        ).pack(side=tk.RIGHT, pady=15)
        
        # Información del ejercicio
        info_frame = tk.Frame(self.preguntas_frame, bg='#E3F2FD')
        info_frame.pack(fill=tk.X, padx=15, pady=(5, 15))
        
        dificultad_colores = {
            'principiante': '#4CAF50',
            'intermedio': '#FF9800',
            'avanzado': '#F44336'
        }
        dificultad_icons = {
            'principiante': '⭐',
            'intermedio': '⭐⭐',
            'avanzado': '⭐⭐⭐'
        }
        
        dificultad = self.ejercicio_actual.get('dificultad', 'intermedio')
        
        tk.Label(
            info_frame,
            text=f"📚 {self.ejercicio_actual['titulo']}  |  "
                 f"{dificultad_icons.get(dificultad, '⭐')} {dificultad.upper()}  |  "
                 f"Total: {len(preguntas)} preguntas",
            font=('Segoe UI', 10),
            bg='#E3F2FD',
            fg='#1565C0',
            pady=8,
            padx=15
        ).pack(fill=tk.X)
        
        # Instrucciones breves
        instruccion_frame = tk.Frame(self.preguntas_frame, bg='#FFF3E0')
        instruccion_frame.pack(fill=tk.X, padx=15, pady=(0, 10))
        
        tk.Label(
            instruccion_frame,
            text="💡 Responde todas las preguntas y presiona 'Evaluar Respuestas' al finalizar",
            font=('Segoe UI', 9, 'italic'),
            bg='#FFF3E0',
            fg='#E65100',
            pady=6,
            padx=15
        ).pack(fill=tk.X)
        
        # Mostrar cada pregunta
        for pregunta in preguntas:
            self.crear_pregunta_widget(pregunta)
        
        # Footer con botón de enviar
        footer_frame = tk.Frame(self.preguntas_frame, bg=COLORS['card_bg'])
        footer_frame.pack(fill=tk.X, pady=20, padx=15)
        
        tk.Button(
            footer_frame,
            text="✅ Evaluar Mis Respuestas",
            font=('Segoe UI', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            cursor='hand2',
            command=self.evaluar_respuestas,
            pady=12,
            padx=30,
            relief=tk.FLAT
        ).pack(pady=10)
    
    def crear_pregunta_widget(self, pregunta):
        """Crea el widget para una pregunta con diseño mejorado."""
        # Colores según tipo de pregunta
        tipo_colores = {
            'numerica': {'header': '#2E7D32', 'icon': '🔢', 'label': 'CÁLCULO'},
            'opcion_multiple': {'header': '#1565C0', 'icon': '📝', 'label': 'SELECCIÓN'}
        }
        
        tipo_info = tipo_colores.get(pregunta['tipo'], {'header': '#424242', 'icon': '❓', 'label': 'PREGUNTA'})
        
        # Frame contenedor principal con borde redondeado simulado
        container = tk.Frame(self.preguntas_frame, bg=COLORS['content_bg'])
        container.pack(fill=tk.X, padx=15, pady=8)
        
        # Frame para la pregunta con sombra
        q_frame = tk.Frame(container, bg=COLORS['card_bg'], relief=tk.GROOVE, borderwidth=2)
        q_frame.pack(fill=tk.X, padx=2, pady=2)
        
        # Header con color según tipo
        header_frame = tk.Frame(q_frame, bg=tipo_info['header'], height=35)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Número de pregunta e icono
        header_content = tk.Frame(header_frame, bg=tipo_info['header'])
        header_content.pack(fill=tk.BOTH, expand=True, padx=10)
        
        tk.Label(
            header_content,
            text=f"{tipo_info['icon']} Pregunta {pregunta['id']}",
            font=('Segoe UI', 11, 'bold'),
            bg=tipo_info['header'],
            fg='white',
            anchor='w'
        ).pack(side=tk.LEFT, pady=5)
        
        # Etiqueta de tipo
        tk.Label(
            header_content,
            text=f"[ {tipo_info['label']} ]",
            font=('Segoe UI', 9),
            bg=tipo_info['header'],
            fg='#E0E0E0',
            anchor='e'
        ).pack(side=tk.RIGHT, pady=5)
        
        # Cuerpo de la pregunta
        body_frame = tk.Frame(q_frame, bg=COLORS['card_bg'])
        body_frame.pack(fill=tk.X, padx=15, pady=15)
        
        # Texto de la pregunta con mejor formato
        pregunta_label = tk.Label(
            body_frame,
            text=pregunta['texto'],
            font=('Segoe UI', 11),
            bg=COLORS['card_bg'],
            fg=COLORS['text_dark'],
            anchor='w',
            wraplength=650,
            justify=tk.LEFT
        )
        pregunta_label.pack(fill=tk.X, pady=(0, 12))
        
        # Separador visual
        separator = tk.Frame(body_frame, bg='#E0E0E0', height=1)
        separator.pack(fill=tk.X, pady=(0, 12))
        
        # Campo de respuesta según tipo
        if pregunta['tipo'] == 'numerica':
            respuesta_frame = tk.Frame(body_frame, bg=COLORS['card_bg'])
            respuesta_frame.pack(fill=tk.X)
            
            tk.Label(
                respuesta_frame, 
                text="📊 Tu respuesta:",
                font=('Segoe UI', 10, 'bold'),
                bg=COLORS['card_bg'],
                fg=COLORS['text_dark']
            ).pack(side=tk.LEFT)
            
            entry = tk.Entry(
                respuesta_frame, 
                font=('Segoe UI', 11), 
                width=15,
                relief=tk.SOLID,
                borderwidth=1
            )
            entry.pack(side=tk.LEFT, padx=10, ipady=4)
            
            unidad = pregunta.get('unidad', '')
            if unidad:
                tk.Label(
                    respuesta_frame, 
                    text=f"({unidad})",
                    font=('Segoe UI', 10, 'italic'),
                    bg=COLORS['card_bg'], 
                    fg=COLORS['text_muted']
                ).pack(side=tk.LEFT)
            
            # Hint si hay tolerancia
            if pregunta.get('tolerancia'):
                hint_frame = tk.Frame(body_frame, bg='#FFF8E1')
                hint_frame.pack(fill=tk.X, pady=(10, 0))
                tk.Label(
                    hint_frame,
                    text=f"💡 Se acepta tolerancia de ±{pregunta['tolerancia']}",
                    font=('Segoe UI', 9, 'italic'),
                    bg='#FFF8E1',
                    fg='#F57C00',
                    padx=10,
                    pady=4
                ).pack(anchor='w')
            
            self.respuestas[pregunta['id']] = entry
            
        elif pregunta['tipo'] == 'opcion_multiple':
            tk.Label(
                body_frame,
                text="📋 Selecciona una opción:",
                font=('Segoe UI', 10, 'bold'),
                bg=COLORS['card_bg'],
                fg=COLORS['text_dark']
            ).pack(anchor='w', pady=(0, 8))
            
            var = tk.IntVar(value=-1)
            self.respuestas[pregunta['id']] = var
            
            opciones_frame = tk.Frame(body_frame, bg=COLORS['card_bg'])
            opciones_frame.pack(fill=tk.X, padx=10)
            
            letras = ['A', 'B', 'C', 'D', 'E', 'F']
            for i, opcion in enumerate(pregunta['opciones']):
                opcion_container = tk.Frame(opciones_frame, bg='#F5F5F5', relief=tk.FLAT)
                opcion_container.pack(fill=tk.X, pady=3, ipady=3)
                
                rb = tk.Radiobutton(
                    opcion_container,
                    text=f" {letras[i]})  {opcion}",
                    variable=var,
                    value=i,
                    font=('Segoe UI', 10),
                    bg='#F5F5F5',
                    activebackground='#E3F2FD',
                    selectcolor='#BBDEFB',
                    anchor='w',
                    padx=10,
                    pady=2
                )
                rb.pack(fill=tk.X, anchor='w')
    
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
