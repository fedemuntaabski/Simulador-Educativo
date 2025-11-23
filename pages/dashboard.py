import tkinter as tk
from tkinter import ttk
from utils.styles import COLORS, FONTS, DIMENSIONS, ICONS
from utils.user_metrics import UserMetrics

class DashboardPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['content_bg'])
        self.metrics = UserMetrics()
        self.create_widgets()

    def create_widgets(self):
        canvas = tk.Canvas(self, bg=COLORS['content_bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['content_bg'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=canvas.winfo_reqwidth())
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(
            canvas.find_withtag("all")[0], width=e.width))
        
        main_container = tk.Frame(scrollable_frame, bg=COLORS['content_bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=DIMENSIONS['space_xxl'], pady=DIMENSIONS['space_xl'])
        
        stats = self.metrics.get_dashboard_stats()
        
        # Header
        self.create_header(main_container)
        
        # KPI Cards
        self.create_kpi_cards(main_container, stats)
        
        # History Section
        self.create_history_section(main_container)

    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=COLORS['accent'], height=100)
        header_frame.pack(fill=tk.X, pady=(0, DIMENSIONS['space_xl']))
        header_frame.pack_propagate(False)
        
        content = tk.Frame(header_frame, bg=COLORS['accent'])
        content.place(relx=0.5, rely=0.5, anchor='center')
        
        title_label = tk.Label(
            content,
            text="Mi Progreso",
            font=('Segoe UI', 24, 'bold'),
            bg=COLORS['accent'],
            fg='white'
        )
        title_label.pack()

    def create_kpi_cards(self, parent, stats):
        cards_frame = tk.Frame(parent, bg=COLORS['content_bg'])
        cards_frame.pack(fill=tk.X, pady=(0, DIMENSIONS['space_xl']))
        
        kpis = [
            (ICONS['clipboard'], str(stats['exercises_completed']), "Ejercicios Completados"),
            (ICONS['star'], f"{stats['avg_score']:.1f}%", "Precisión Promedio"),
            (ICONS['time'], f"{stats['total_time_minutes']:.1f} min", "Tiempo Total"),
            (ICONS['graph'], f"{stats['improvement_rate']:+.1f}%", "Tasa de Mejora")
        ]
        
        for i, (icon, value, label) in enumerate(kpis):
            card = tk.Frame(cards_frame, bg='white', relief=tk.RAISED, borderwidth=1)
            card.grid(row=0, column=i, padx=DIMENSIONS['space_md'], sticky="ew")
            cards_frame.grid_columnconfigure(i, weight=1)
            
            tk.Label(card, text=icon, font=FONTS['icon'], bg='white').pack(pady=10)
            tk.Label(card, text=value, font=FONTS['title'], bg='white', fg=COLORS['accent']).pack()
            tk.Label(card, text=label, font=FONTS['tiny'], bg='white', fg=COLORS['text_muted']).pack(pady=(0, 10))


    def create_history_section(self, parent):
        tk.Label(parent, text="Historial Reciente", font=FONTS['section_title'], bg=COLORS['content_bg']).pack(anchor='w', pady=(0, DIMENSIONS['space_lg']))
        
        history_frame = tk.Frame(parent, bg='white', relief=tk.FLAT)
        history_frame.pack(fill=tk.BOTH, expand=True)
        
        history = self.metrics.data['history'][-10:] # Last 10
        history.reverse()
        
        if not history:
            tk.Label(history_frame, text="No hay historial reciente.", bg='white', pady=20).pack()
            return

        # Header
        header = tk.Frame(history_frame, bg=COLORS['header'])
        header.pack(fill=tk.X)
        cols = ["Fecha", "Tema", "Puntaje"]
        for col in cols:
            tk.Label(header, text=col, font=FONTS['small_bold'], bg=COLORS['header'], width=20).pack(side=tk.LEFT, padx=5, pady=5)

        # Rows
        for entry in history:
            row = tk.Frame(history_frame, bg='white', borderwidth=1, relief=tk.SOLID)
            row.pack(fill=tk.X)
            
            date_str = entry['date'].split('T')[0]
            tk.Label(row, text=date_str, width=20, bg='white').pack(side=tk.LEFT, padx=5, pady=5)
            tk.Label(row, text=entry['topic'], width=20, bg='white').pack(side=tk.LEFT, padx=5, pady=5)
            tk.Label(row, text=f"{entry['score']:.1f}", width=20, bg='white').pack(side=tk.LEFT, padx=5, pady=5)
