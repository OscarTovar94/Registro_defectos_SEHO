def defect_root():
    """ Función que abre la ventana defectos """
    # ---------- Logic root_defect

    def settings_root_rd(clave):
        """Function to load settings."""
        try:
            with open("C:/Registro_defectos_SEHO/root_settings_rd.ini", "r",  encoding="utf-8") as config:
                for linea in config:
                    if linea.startswith(clave):
                        return linea.split("=")[1].strip()
        except FileNotFoundError:
            messagebox.showerror(
                "Error", "El archivo de configuración 'setting.txt' no fue encontrado.")
        except ImportError as e:
            messagebox.showerror(
                "Error", f"Ocurrió un error al leer la configuración: {e}")
        return None

    def root_defect_scale():
        """Funcíon para escalar root defectos"""
        # Obtener el tamaño de la pantalla
        pantalla_ancho = root_defect.winfo_screenwidth()
        pantalla_alto = root_defect.winfo_screenheight()

        # Calcular el factor de escala basado en una resolución de referencia (1920x1080)
        escala_x = pantalla_ancho / 1920
        escala_y = pantalla_alto / 1080
        escala = min(escala_x, escala_y)
        frame0_rd.config(padx=0 * escala, pady=0 * escala)
        frame1_rd.config(padx=0 * escala, pady=0 * escala)
        frame2_rd.config(padx=0 * escala, pady=0 * escala)
        frame3_rd.config(padx=0 * escala, pady=0 * escala)
        frame4_rd.config(padx=0 * escala, pady=0 * escala)

        # Ajustar el tamaño de la fuente
        fuente_8 = int(8 * escala)
        fuente_10 = int(10 * escala)
        fuente_12 = int(12 * escala)
        fuente_14 = int(14 * escala)
        fuente_16 = int(16 * escala)
        fuente_20 = int(20 * escala)
        fuente_22 = int(22 * escala)
        fuente_30 = int(30 * escala)
        fuente_40 = int(40 * escala)
        fuente_50 = int(50 * escala)
        fuente_70 = int(90 * escala)
        menu = int(12 * escala)
        defectos_menu = int(14 * escala)
        defectos = int(10 * escala)

        # label's
        label_rd_0.config(font=("Arial", fuente_40, "bold"))  # Título
        label_rd_1.config(font=("Arial", menu, "bold"))  # Modelo
        label_rd_2.config(font=("Arial", menu, "bold"))  # Fecha
        label_rd_3.config(font=("Arial", menu, "bold"))  # Horario
        label_rd_4.config(font=("Arial", defectos_menu, "bold"), bd=1,  relief="ridge",
                          highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defectos
        label_rd_5.config(font=("Arial", defectos_menu, "bold"), bd=1,  relief="ridge",
                          highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad
        label_rd_6.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                          highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto1
        label_rd_7.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                          highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto2
        label_rd_8.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                          highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto3
        label_rd_9.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                          highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto4
        label_rd_10.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto5
        label_rd_11.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto6
        label_rd_12.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto7
        label_rd_13.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto8
        label_rd_14.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto9
        label_rd_15.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto10
        label_rd_16.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto11
        label_rd_17.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto12
        label_rd_18.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto13
        label_rd_19.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto14
        label_rd_20.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto15
        label_rd_21.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto16
        label_rd_22.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto17
        label_rd_23.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto18
        label_rd_24.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto19
        label_rd_25.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto20
        label_rd_26.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto21
        label_rd_27.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto22
        label_rd_28.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto23
        label_rd_29.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto24
        label_rd_30.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto25
        label_rd_31.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto26
        label_rd_32.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto27
        label_rd_33.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto28
        label_rd_34.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto29
        label_rd_35.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto30
        label_rd_88.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto31
        label_rd_89.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto32
        label_rd_90.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto33
        label_rd_91.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto34
        label_rd_92.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Defecto35
        label_rd_36.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto1
        label_rd_37.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto2
        label_rd_38.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto3
        label_rd_39.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto4
        label_rd_40.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto5
        label_rd_41.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto6
        label_rd_42.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto7
        label_rd_43.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto8
        label_rd_44.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto9
        label_rd_45.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto10
        label_rd_46.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto11
        label_rd_47.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto12
        label_rd_48.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto13
        label_rd_49.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto14
        label_rd_50.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto15
        label_rd_51.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto16
        label_rd_52.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto17
        label_rd_53.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto18
        label_rd_54.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto19
        label_rd_55.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto20
        label_rd_56.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto21
        label_rd_57.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto22
        label_rd_58.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto23
        label_rd_59.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto24
        label_rd_60.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto25
        label_rd_61.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto26
        label_rd_62.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto27
        label_rd_63.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto28
        label_rd_64.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto29
        label_rd_65.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto30
        label_rd_93.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto31
        label_rd_94.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto32
        label_rd_95.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto33
        label_rd_96.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto34
        label_rd_97.config(font=("Arial", defectos, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)  # Cantidad_defecto35
        label_rd_66.config(font=("Arial", fuente_30, "bold"))
        label_rd_67.config(font=("Arial", fuente_22, "bold"))
        label_rd_68.config(font=("Arial", fuente_22, "bold"))
        label_rd_69.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_70.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_71.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_72.config(font=("Arial", fuente_22, "bold"))
        label_rd_73.config(font=("Arial", fuente_22, "bold"))
        label_rd_74.config(font=("Arial", fuente_22, "bold"))
        label_rd_75.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_76.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_77.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_78.config(font=("Arial", fuente_30, "bold"))
        label_rd_79.config(font=("Arial", fuente_30, "bold"))
        label_rd_80.config(font=("Arial", fuente_22, "bold"))
        label_rd_81.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_82.config(font=("Arial", fuente_22, "bold"), bd=1,  relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_83.config(font=("Arial", fuente_22, "bold"), bd=1, relief="ridge",
                           highlightbackground="black", highlightcolor="black", highlightthickness=1)
        label_rd_84.config(font=("Arial", fuente_22, "bold"))
        label_rd_85.config(font=("Arial", fuente_22, "bold"), bd=1, relief="ridge", highlightbackground="black",
                           highlightcolor="black", highlightthickness=1)
        label_rd_86.config(font=("Arial", fuente_22, "bold"), bd=1, relief="ridge", highlightbackground="black",
                           highlightcolor="black", highlightthickness=1)
        label_rd_87.config(font=("Arial", fuente_22, "bold"), bd=1, relief="ridge", highlightbackground="black",
                           highlightcolor="black", highlightthickness=1)

        # menu's
        menu_rd_1.config(font=("Arial", fuente_12, "bold"), activebackground="deep sky blue",
                         bg="#AEAEAE", fg="black", width=15)  # Modelos
        date_rd_1.config(font=("Arial", menu, "bold"))  # Selección Fecha
        spinbox_rd_1.config(font=("Arial", menu, "bold"))  # Hora de inicio
        spinbox_rd_2.config(font=("Arial", menu, "bold"))  # Minuto de inicio
        spinbox_rd_3.config(font=("Arial", menu, "bold"))  # Periodo de inicio
        spinbox_rd_4.config(font=("Arial", menu, "bold"))  # Hora final
        spinbox_rd_5.config(font=("Arial", menu, "bold"))  # Minuto final
        spinbox_rd_6.config(font=("Arial", menu, "bold"))  # Periodo final
        button_rd_1.config(font=("Arial", menu, "bold"))  # Buscar
        button_rd_2.config(font=("Arial", menu, "bold"))

    def settings_part_numbers_rd(clave):
        """Función para cargar defectos."""
        try:
            with open("C:/Registro_defectos_SEHO/models.ini", "r",  encoding="utf-8") as config:
                for linea in config:
                    if linea.startswith(clave):
                        return linea.split("=")[1].strip()
        except FileNotFoundError:
            messagebox.showerror(
                "Error", "El archivo de configuración 'setting.txt' no fue encontrado.")
        except ImportError as e:
            messagebox.showerror(
                "Error", f"Ocurrió un error al leer la configuración: {e}")
        return None

    def closed_rd():
        """Función para cerrar root defectos"""
        root_defect.destroy()

    def dashboard_seho():
        """Dashboard interactivo con KPIs de calidad y emojis de estado"""
        try:
            def cerrar_dash():
                win.destroy()

            # ==========================================
            # 1. CONFIGURACIÓN DE VENTANA (MODO DASHBOARD)
            # ==========================================
            win = tk.Toplevel()
            win.title("Dashboard de Control SEHO")
            win.attributes("-fullscreen", True)
            win.configure(bg="#0F111A")  # Fondo oscuro elegante
            win.attributes("-topmost", True)

            # Header con Título y Botón
            header = tk.Frame(win, bg="#1A1C26", height=60)
            header.pack(side="top", fill="x")

            fecha_str = date_rd_1.get()
            tk.Label(header, text=f"DASHBOARD OPERATIVO — {fecha_str}",
                     font=("Segoe UI", 22, "bold"), bg="#1A1C26", fg="#00D4FF").pack(side="left", padx=20)

            tk.Button(header, text="SALIR (X)", font=("Arial", 12, "bold"), bg="#E74C3C",
                      fg="white", command=cerrar_dash, relief="flat", padx=25).pack(side="right", padx=20, pady=10)

            # ==========================================
            # 2. PROCESAMIENTO DE DATOS (EVITAR DUPLICADOS)
            # ==========================================
            df_raw, _ = cargar_datos_cache()
            df = df_raw.drop_duplicates().copy()  # Limpieza de duplicados
            df.columns = df.columns.str.strip()
            df["Fecha/Hora"] = pd.to_datetime(df["Fecha/Hora"],
                                              format="%d/%m/%Y %H:%M:%S")

            # Filtro de fecha actual de la UI
            fecha_dt = pd.to_datetime(fecha_str, format="%d/%m/%Y").date()
            df = df[df["Fecha/Hora"].dt.date == fecha_dt]

            if df.empty:
                tk.Label(win, text="⚠️ NO HAY DATOS PARA LA FECHA SELECCIONADA",
                         font=("Segoe UI", 24), bg="#0F111A", fg="#555").pack(expand=True)
                return

            # ==========================================
            # 3. CÁLCULOS DE KPIs Y LÍMITES
            # ==========================================
            # Cargar nombres de defectos
            defect_names = []
            with open("C:/Registro_defectos_SEHO/defects.ini", encoding="utf-8") as f:
                defect_names = [line.split("=")[1].strip()
                                for line in f if "=" in line]

            defectos_validos = [d for d in defect_names if d in df.columns]

            # Totales principales
            total_producido = int(df["Estandar"].sum())
            suma_defectos = df[defectos_validos].sum()
            total_defectos = int(suma_defectos.sum())
            buenos = total_producido - total_defectos
            fpy = (buenos / total_producido *
                   100) if total_producido > 0 else 0

            # Obtener Meta desde el .ini
            try:
                fpy_meta_min = int(settings_limits("FPY_MODEL_min"))
                fpy_meta_max = int(settings_limits("FPY_MODEL_max"))
            except:
                fpy_meta_min = 95
                fpy_meta_max = 99

            # Lógica de Emojis y Colores
            if fpy >= fpy_meta_max:
                estado, emoji, color_kpi = "BUENO", "😊", "#2ECC71"  # Verde
            elif fpy >= fpy_meta_min and fpy < fpy_meta_max:
                estado, emoji, color_kpi = "REGULAR", "😐", "#F1C40F"  # Amarillo
            else:
                estado, emoji, color_kpi = "CRÍTICO", "😟", "#E74C3C"  # Rojo

            # ==========================================
            # 4. CONTENEDOR PRINCIPAL DE GRÁFICAS
            # ==========================================
            plt.style.use("dark_background")
            main_container = tk.Frame(win, bg="#0F111A")
            main_container.pack(fill="both", expand=True, padx=10, pady=5)

            main_container.columnconfigure(0, weight=1)
            main_container.columnconfigure(1, weight=1)
            for i in range(3):
                main_container.rowconfigure(i, weight=1)

            # --- GRÁFICA 1: DONA FPY (CON EMOJI) ---
            fig1 = plt.Figure(figsize=(5, 5), facecolor="#0F111A")
            ax1 = fig1.add_subplot(111)
            ax1.pie([fpy, max(0, 100 - fpy)], colors=[color_kpi, "#2A2D3E"],
                    startangle=90, wedgeprops={'width': 0.35, 'edgecolor': '#0F111A'})

            # Textos centrales (Emoji y FPY)
            ax1.text(0, 0.2, emoji, ha='center', va='center', fontsize=50)
            ax1.text(0, -0.2, f"{fpy:.1f}%", ha='center',
                     va='center', fontsize=18, fontweight='bold')
            ax1.text(0, -0.45, f"STATUS: {estado}", ha='center', va='center', fontsize=6, color=color_kpi,
                     fontweight='bold')
            ax1.set_title(f"Calidad vs Meta ({fpy_meta_max}%)", pad=5)

            FigureCanvasTkAgg(fig1, main_container).get_tk_widget().grid(
                row=0, column=0, sticky="nsew", padx=5)

            # --- GRÁFICA 2: PRODUCCIÓN TOTAL (PRO STACKED BAR) ---
            fig2 = plt.Figure(figsize=(5, 3), facecolor="#0F111A")
            ax2 = fig2.add_subplot(111)

            # Colores más "Pro" (Verde Esmeralda y Rojo Coral)
            color_ok = "#00FF87"  # Verde Neón
            color_ng = "#FF4646"  # Rojo Vibrante

            # Calcular porcentajes
            porc_ok = (buenos / total_producido *
                       100) if total_producido > 0 else 0
            porc_ng = (total_defectos / total_producido *
                       100) if total_producido > 0 else 0

            # Crear las barras
            ax2.bar(["Estado"], [buenos], color=color_ok,
                    label="OK", width=0.6)
            ax2.bar(["Estado"], [total_defectos], bottom=[buenos],
                    color=color_ng, label="Defectos", width=0.6)

            # Título con el gran total
            ax2.set_title(f"PRODUCCIÓN TOTAL: {total_producido}",
                          fontsize=12, color='white', fontweight='bold', pad=5)

            # Etiquetas internas con Cantidad y Porcentaje
            # Texto para BUENOS
            if buenos > 0:
                ax2.text(0, buenos / 2, f"{int(buenos)}\n({porc_ok:.1f}%)",
                         ha='center', va='center', color='#0F111A', fontweight='bold', fontsize=8)

            # Texto para DEFECTOS
            if total_defectos > 0:
                ax2.text(0, buenos + (total_defectos / 2), f"{int(total_defectos)}\n({porc_ng:.1f}%)",
                         ha='center', va='center', color='white', fontweight='bold', fontsize=8)

            # Estética Pro: Quitar bordes y ajustar leyenda
            # ax2.legend(frameon=False, loc='upper right', labelcolor='white')
            ax2.spines['top'].set_visible(False)
            ax2.spines['right'].set_visible(False)
            ax2.spines['left'].set_color('#2A2D3E')
            ax2.spines['bottom'].set_color('#2A2D3E')
            ax2.tick_params(colors='white')

            FigureCanvasTkAgg(fig2, main_container).get_tk_widget().grid(
                row=0, column=1, sticky="nsew", padx=5)

            # --- GRÁFICA 3: PARETO TOP 5 DEFECTOS ---
            top5 = suma_defectos.sort_values(ascending=True).tail(5)

            fig3 = plt.Figure(figsize=(6, 4), facecolor="#0F111A")
            ax3 = fig3.add_subplot(111)

            # Dibujar la gráfica
            top5.plot(kind="barh", ax=ax3, color="#F1C40F", width=0.7)

            # AJUSTE 1: Reducir tamaño de letra de las etiquetas del eje Y (los nombres)
            ax3.tick_params(axis='y', labelsize=9, colors='white')

            # AJUSTE 2: Título y etiquetas
            ax3.set_title("Top 5 Defectos", fontsize=12, color='white', pad=10)

            # AJUSTE 3: Espacio extra a la derecha para que el número no se corte
            max_val = top5.max() if not top5.empty else 10
            ax3.set_xlim(0, max_val * 1.2)

            for i, v in enumerate(top5):
                ax3.text(v + (max_val * 0.02), i, str(int(v)),
                         va='center', color='white', fontweight='bold', fontsize=9)

            # LA CLAVE: Ajustar el diseño para que no se corten los nombres largos
            fig3.tight_layout()

            FigureCanvasTkAgg(fig3, main_container).get_tk_widget().grid(
                row=1, column=0, sticky="nsew", padx=5)

            # --- GRÁFICA 4: RENDIMIENTO POR HORA (ÁREA CON ETIQUETAS) ---
            df["Hora"] = df["Fecha/Hora"].dt.hour
            prod_hora = df.groupby("Hora")["Estandar"].sum()

            fig4 = plt.Figure(figsize=(6, 4), facecolor="#0F111A")
            ax4 = fig4.add_subplot(111)

            # Dibujamos la línea y el área
            ax4.plot(prod_hora.index, prod_hora.values, color="#00D4FF",
                     marker="o", markersize=8, linewidth=2, zorder=2)
            ax4.fill_between(prod_hora.index, prod_hora.values,
                             color="#00D4FF", alpha=0.1)

            # AJUSTE DE RANGO: Damos un 15% más de espacio arriba para que el número más alto no se corte
            if not prod_hora.empty:
                ax4.set_ylim(0, prod_hora.max() * 1.15)

            # AÑADIR NÚMEROS EN CADA BOLITA
            for x, y in zip(prod_hora.index, prod_hora.values):
                ax4.text(x, y + (prod_hora.max() * 0.03),  # Desplazamos el número un 3% arriba del valor
                         f'{int(y)}',
                         ha='center',
                         va='bottom',
                         color='white',
                         fontsize=10,
                         fontweight='bold',
                         # Añadimos un pequeño borde/fondo oscuro para que resalte sobre cualquier línea
                         bbox=dict(facecolor='#0F111A', alpha=0.6, edgecolor='none', pad=1))

            ax4.set_title("Producción por Hora", fontsize=12, color='white')
            ax4.set_xticks(prod_hora.index)
            ax4.tick_params(axis='both', colors='white')

            # Quitar bordes innecesarios
            ax4.spines['top'].set_visible(False)
            ax4.spines['right'].set_visible(False)

            FigureCanvasTkAgg(fig4, main_container).get_tk_widget().grid(
                row=1, column=1, sticky="nsew", padx=5)

            # --- GRÁFICA 5: PRODUCCIÓN POR MODELO (OPTIMIZADA PARA BARRAS PEQUEÑAS) ---
            resumen_modelos = df.groupby("Modelo").agg(
                {"Estandar": "sum"}).copy()
            resumen_modelos["Defectos"] = df.groupby(
                "Modelo")[defectos_validos].sum().sum(axis=1)
            resumen_modelos["Buenos"] = resumen_modelos["Estandar"] - \
                resumen_modelos["Defectos"]

            fig5 = plt.Figure(figsize=(10, 4), facecolor="#0F111A")
            ax5 = fig5.add_subplot(111)

            modelos = resumen_modelos.index
            buenos_val = resumen_modelos["Buenos"]
            defectos_val = resumen_modelos["Defectos"]
            totales = resumen_modelos["Estandar"]

            # Colores Neón para combinar con el resto del dashboard
            color_ok = "#00FF87"
            color_ng = "#FF4646"

            ax5.bar(modelos, buenos_val, color=color_ok, label="Buenos")
            ax5.bar(modelos, defectos_val, bottom=buenos_val,
                    color=color_ng, label="Malos")

            # Ajustar el límite superior para que los totales no se corten
            if not totales.empty:
                ax5.set_ylim(0, totales.max() * 1.2)

            for i in range(len(modelos)):
                total = totales.iloc[i]
                b = buenos_val.iloc[i]
                d = defectos_val.iloc[i]

                if total > 0:
                    porc_b = (b / total) * 100
                    porc_d = (d / total) * 100

                    # --- Lógica para BUENOS ---
                    # Si la barra es muy pequeña (menor al 15% del total max), no ponemos porcentaje, solo el número
                    if b > 0:
                        txt_b = f"{int(b)}\n({porc_b:.1f}%)" if b > (
                            totales.max() * 0.1) else f"{int(b)}"
                        ax5.text(i, b / 2, txt_b, ha='center', va='center',
                                 color='#0F111A', fontsize=8, fontweight='bold')

                    # --- Lógica para MALOS (Defectos) ---
                    if d > 0:
                        # Si el área roja es muy delgada, ponemos el texto arriba del total con una flecha o color distinto
                        if d < (totales.max() * 0.08):
                            # Barra muy pequeña: Texto pequeño justo arriba de la barra roja
                            ax5.text(i, b + d + (totales.max() * 0.01), f"NG:{int(d)}",
                                     ha='center', va='bottom', color=color_ng, fontsize=7, fontweight='bold')
                        else:
                            # Barra normal: Texto dentro
                            ax5.text(i, b + (d / 2), f"{int(d)}\n({porc_d:.1f}%)",
                                     ha='center', va='center', color='white', fontsize=8, fontweight='bold')

                    # --- TOTAL (Siempre arriba) ---
                    ax5.text(i, total + (totales.max() * 0.05), f"TOT: {int(total)}",
                             ha='center', va='bottom', color='#00D4FF', fontsize=9, fontweight='bold')

            ax5.set_title("PRODUCCIÓN POR MODELO",
                          fontsize=12, color="white", pad=5)
            ax5.tick_params(axis='x', colors='white', labelsize=8)
            ax5.tick_params(axis='y', colors='white')
            ax5.spines['top'].set_visible(False)
            ax5.spines['right'].set_visible(False)

            # Ajustar leyenda para que no estorbe
            # ax5.legend(frameon=False, labelcolor='white', loc='upper right', fontsize=8)

            fig5.tight_layout()
            FigureCanvasTkAgg(fig5, main_container).get_tk_widget().grid(row=2, column=0, columnspan=2, sticky="nsew",
                                                                         pady=10)

        except Exception as e:
            messagebox.showerror(
                "Error Dashboard", f"No se pudo cargar la dashboard: {e}")

    def contar_defectos_por_modelo():
        """Cuenta defectos por modelo, fecha y rango de horas - CORREGIDA (Evita conteo doble)"""
        try:
            # ==============================
            # LEER CSV Y LIMPIAR DUPLICADOS
            # ==============================
            df_original, _ = cargar_datos_cache()
            # Creamos una copia y eliminamos duplicados exactos para evitar contar doble
            df = df_original.drop_duplicates().copy()

            df.columns = df.columns.str.strip()

            df["Fecha/Hora"] = pd.to_datetime(
                df["Fecha/Hora"], format="%d/%m/%Y %H:%M:%S"
            )

            # ==============================
            # LEER defects.ini
            # ==============================
            defect_names = []
            with open("C:/Registro_defectos_SEHO/defects.ini", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or "=" not in line:
                        continue
                    _, value = line.split("=", 1)
                    defect_names.append(value.strip())

            # ==============================
            # LABELS (Referencia a tus etiquetas de la UI)
            # ==============================
            labels_defectos = [
                label_rd_36, label_rd_37, label_rd_38, label_rd_39, label_rd_40, label_rd_41,
                label_rd_42, label_rd_43, label_rd_44, label_rd_45, label_rd_46, label_rd_47,
                label_rd_48, label_rd_49, label_rd_50, label_rd_51, label_rd_52, label_rd_53,
                label_rd_54, label_rd_55, label_rd_56, label_rd_57, label_rd_58, label_rd_59,
                label_rd_60, label_rd_61, label_rd_62, label_rd_63, label_rd_64, label_rd_65,
                label_rd_93, label_rd_94, label_rd_95, label_rd_96, label_rd_97
            ]

            # ==============================
            # OBTENER FILTROS DE LA UI
            # ==============================
            modelo = opcion_seleccionada_model.get()
            fecha = pd.to_datetime(date_rd_1.get(), format="%d/%m/%Y").date()

            hora_inicio = pd.to_datetime(
                f"{hora_inicio_rd.get()}:{minuto_inicio_rd.get()} {periodo_inicio_rd.get()}",
                format="%I:%M %p"
            ).time()

            hora_fin = pd.to_datetime(
                f"{hora_final_rd.get()}:{minuto_final_rd.get()} {periodo_final_rd.get()}",
                format="%I:%M %p"
            ).time()

            # ==============================
            # APLICAR FILTRO
            # ==============================
            filtro = (
                (df["Modelo"] == modelo) &
                (df["Fecha/Hora"].dt.date == fecha) &
                (df["Fecha/Hora"].dt.time >= hora_inicio) &
                (df["Fecha/Hora"].dt.time <= hora_fin)
            )

            datos_filtrados = df.loc[filtro]

            # ==============================
            # SUMAR DEFECTOS Y PRODUCIDO
            # ==============================
            # Sumamos sobre los datos ya filtrados y sin duplicados
            suma_defectos = datos_filtrados[defect_names].sum()
            total_producido = int(datos_filtrados["Estandar"].sum())
            total_defectos = int(suma_defectos.sum())

            # Actualizar labels principales
            label_rd_73.config(text=str(total_producido))
            label_rd_68.config(text=str(total_defectos))

            # ==============================
            # FPY
            # ==============================
            fpy = ((total_producido - total_defectos) /
                   total_producido) * 100 if total_producido > 0 else 0
            fpy_por_pallet_min = int(settings_limits("FPY_MODEL_min"))
            fpy_por_pallet_max = int(settings_limits("FPY_MODEL_max"))

            if total_producido == 0:
                label_rd_79.config(text="N/A", fg="black", bg=color_3)
            else:
                if fpy >= fpy_por_pallet_max:
                    label_rd_79.config(
                        text=f"{fpy:.2f}%", fg="green", bg="#D9F2D0")
                elif fpy < fpy_por_pallet_min:
                    label_rd_79.config(
                        text=f"{fpy:.2f}%", fg="red", bg="#FFCCCC")
                elif fpy >= fpy_por_pallet_min and fpy < fpy_por_pallet_max:
                    label_rd_79.config(
                        text=f"{fpy:.2f}%", fg="#E7601D", bg="#FBE7DD")

            # ==============================
            # TOP DEFECTOS (1, 2 y 3)
            # ==============================
            top_defectos = suma_defectos[suma_defectos > 0].sort_values(
                ascending=False)

            # Lógica para llenar los Top Labels (simplificada para evitar repetición)
            def actualizar_top(label_nom, label_cant, label_porc, index, color):
                if len(top_defectos) > index:
                    nombre = top_defectos.index[index]
                    cant = int(top_defectos.iloc[index])
                    porc = (cant / total_defectos *
                            100) if total_defectos > 0 else 0
                    label_nom.config(text=nombre, bg=color)
                    label_cant.config(text=str(cant), bg=color)
                    label_porc.config(text=f"{porc:.1f}%", bg=color)
                else:
                    label_nom.config(text="N/A", bg=color_3)
                    label_cant.config(text="N/A", bg=color_3)
                    label_porc.config(text="N/A", bg=color_3)

            actualizar_top(label_rd_75, label_rd_76,
                           label_rd_77, 0, "#FFD700")  # Top 1
            actualizar_top(label_rd_81, label_rd_82,
                           label_rd_83, 1, "#C0C0C0")  # Top 2
            actualizar_top(label_rd_85, label_rd_86,
                           label_rd_87, 2, "#CD7F32")  # Top 3

            # ==============================
            # HEATMAP DE DEFECTOS
            # ==============================
            valores = suma_defectos.values
            valores_validos = [v for v in valores if v > 0]
            minimo = min(valores_validos) if valores_validos else 0
            maximo = max(valores_validos) if valores_validos else 0

            for i in range(len(labels_defectos)):
                valor = int(valores[i])
                if valor == 0:
                    color_bg = "#C0E6F5" if i % 2 == 0 else "white"
                    labels_defectos[i].config(
                        text="0", bg=color_bg, fg="black")
                else:
                    ratio = (valor - minimo) / (maximo -
                                                minimo) if maximo != minimo else 1
                    # De Amarillo (255, 255, 0) a Rojo (255, 0, 0)
                    verde = int(255 * (1 - ratio))
                    color_hex = f'#ff{verde:02x}00'
                    labels_defectos[i].config(
                        text=str(valor), bg=color_hex, fg="black")

            # LLAMAR A LA TABLA DE PALLETS
            crear_tabla_pallets()

        except Exception as e:
            messagebox.showerror("Error", f"Error calculo de defectos: {e}")

    def crear_tabla_pallets():
        try:
            # 1. Limpiar el frame completamente antes de empezar
            for widget in frame4_rd.winfo_children():
                widget.destroy()

            frame_tabla = tk.Frame(frame4_rd, bg=frame4_rd.cget("bg"))
            frame_tabla.grid(row=0, column=0, padx=50, pady=30, sticky="nsew")
            frame_tabla.grid_columnconfigure(0, weight=1)
            frame_tabla.grid_rowconfigure(0, weight=1)

            # 2. Leer archivos (con el fix de cierre de archivo para evitar bloqueos)
            with open("C:/Registro_defectos_SEHO/Parameters.csv", "r", encoding="utf-8") as f:
                df_params = pd.read_csv(io.StringIO(f.read()))

            # IMPORTANTE: Asegúrate de que cargar_datos_cache no esté duplicando filas
            df_log, _ = cargar_datos_cache()

            # ELIMINAR DUPLICADOS SI EXISTEN (Esto evita el conteo doble)
            df_log = df_log.drop_duplicates()

            # 3. Preparar Filtros
            modelo_sel = opcion_seleccionada_model.get()
            fecha_sel = pd.to_datetime(
                date_rd_1.get(), format="%d/%m/%Y").date()
            h_ini = pd.to_datetime(f"{hora_inicio_rd.get()}:{minuto_inicio_rd.get()} {periodo_inicio_rd.get()}",
                                   format="%I:%M %p").time()
            h_fin = pd.to_datetime(f"{hora_final_rd.get()}:{minuto_final_rd.get()} {periodo_final_rd.get()}",
                                   format="%I:%M %p").time()

            # 4. Aplicar Filtro Estricto
            df_log.loc[:, "Fecha/Hora"] = pd.to_datetime(
                df_log["Fecha/Hora"], format="%d/%m/%Y %H:%M:%S")

            mask = (
                (df_log["Modelo"] == modelo_sel) &
                (df_log["Fecha/Hora"].dt.date == fecha_sel) &
                (df_log["Fecha/Hora"].dt.time >= h_ini) &
                (df_log["Fecha/Hora"].dt.time <= h_fin)
            )
            df_filtrado = df_log.loc[mask].copy()

            # 5. Configurar Tabla y Estilos
            style = ttk.Style()
            style.theme_use("alt")

            # Definimos las fuentes para poder medir el ancho del texto
            fuente_cabecera = tkfont.Font(
                family='Segoe UI', size=18, weight='bold')
            fuente_cuerpo = tkfont.Font(
                family='Segoe UI', size=14,  weight='bold')

            style.configure("Treeview.Heading", font=(
                'Segoe UI', 18, 'bold'), background="#2C3E50", foreground="white")
            style.configure("Treeview", font=(
                'Segoe UI', 14), rowheight=35)

            columnas = ("Pallet", "V/SEHO", "Defectos", "Producido",
                        "FPY", "TopDefecto", "C/TopDefecto", "%TopDefecto")

            tabla = ttk.Treeview(
                frame_tabla, columns=columnas, show="headings")

            # Configuración dinámica de columnas
            for col in columnas:
                # Calculamos el ancho del texto del encabezado + un margen de 30px
                ancho_texto = fuente_cabecera.measure(col) + 10

                tabla.heading(col, text=col)
                # minwidth asegura que no se encoja demasiado, width establece el inicial
                tabla.column(col, width=ancho_texto,
                             minwidth=ancho_texto, anchor="center")

            # Scrollbar y Layout
            scrollbar = ttk.Scrollbar(
                frame_tabla, orient="vertical", command=tabla.yview)
            tabla.configure(yscrollcommand=scrollbar.set)

            tabla.grid(row=0, column=0, sticky="nsew")
            scrollbar.grid(row=0, column=1, sticky="ns")

            # 6. Procesar y Colorear
            todos_los_pallets = sorted(
                df_params[df_params.iloc[:, 1] == modelo_sel].iloc[:, 0].unique())

            defect_names = []
            with open("C:/Registro_defectos_SEHO/defects.ini", "r", encoding="utf-8") as f:
                for line in f:
                    if "=" in line:
                        defect_names.append(line.split("=")[1].strip())

            fpy_valores = []
            resultados_finales = []

            for p_id in todos_los_pallets:
                # Filtramos por Pallet sobre el DF ya filtrado por tiempo
                df_p = df_filtrado[df_filtrado["Pallet"] == p_id]

                if not df_p.empty:
                    # Usamos sum() pero asegurándonos de que no haya filas repetidas
                    v_seho = len(df_p)
                    producido = int(df_p["Estandar"].sum())
                    suma_def = df_p[defect_names].sum()
                    total_def = int(suma_def.sum())
                    fpy_v = ((producido - total_def) / producido *
                             100) if producido > 0 else 0

                    # Top Defecto
                    top = suma_def[suma_def > 0].sort_values(ascending=False)
                    t_nom, t_can, t_por = (
                        top.index[0], int(top.iloc[0]), f"{(top.iloc[0] / total_def * 100):.1f}%") if not top.empty else (
                        "N/A", 0, "0%")

                    fpy_valores.append(fpy_v)
                    resultados_finales.append({
                        "data": (p_id, v_seho, total_def, producido, f"{fpy_v:.2f}%", t_nom, t_can, t_por),
                        "fpy": fpy_v, "activo": True
                    })
                else:
                    resultados_finales.append(
                        {"data": (p_id, "-", "-", "-", "-", "-", "-", "-"), "activo": False})

            # 7. Insertar con el degradado corregido
            f_min, f_max = (min(fpy_valores), max(
                fpy_valores)) if fpy_valores else (0, 0)

            for i, res in enumerate(resultados_finales):
                if res["activo"]:
                    ratio = (res["fpy"] - f_min) / \
                        (f_max - f_min) if f_max != f_min else 1
                    # Color pastel dinámico
                    r, g, b = (1.0, 0.8 + (ratio * 0.2), 0.8) if ratio < 0.5 else (
                        1.0 - ((ratio - 0.5) * 0.2), 1.0, 0.8 + ((ratio - 0.5) * 0.2))
                    color_hex = mcolors.to_hex((r, g, b))

                    tag_id = f"tag_{i}"
                    tabla.tag_configure(tag_id, background=color_hex)
                    tabla.insert("", "end", values=res["data"], tags=(tag_id,))
                else:
                    tabla.tag_configure(
                        'inactivo', background="#F5F5F5", foreground="#95A5A6")
                    tabla.insert(
                        "", "end", values=res["data"], tags=('inactivo',))

        except Exception as e:
            messagebox.showerror("Error", f"Error en conteo: {e}")

    # ---------- Variables root_defect
    global root
    model1 = settings_part_numbers_rd("Part#1")
    model2 = settings_part_numbers_rd("Part#2")
    model3 = settings_part_numbers_rd("Part#3")
    model4 = settings_part_numbers_rd("Part#4")
    model5 = settings_part_numbers_rd("Part#5")
    model6 = settings_part_numbers_rd("Part#6")
    model7 = settings_part_numbers_rd("Part#7")
    model8 = settings_part_numbers_rd("Part#8")
    model9 = settings_part_numbers_rd("Part#9")
    model10 = settings_part_numbers_rd("Part#10")
    model11 = settings_part_numbers_rd("Part#11")
    model12 = settings_part_numbers_rd("Part#12")

   # ----- GUI root defect ------------------------------------------------------------------------------------------
    root_defect = tk.Toplevel(root)
    root_defect.attributes("-topmost", True)
    root_defect.attributes("-fullscreen", True)
    root_defect.overrideredirect(False)
    root_defect.resizable(False, False)
    root_defect.configure(bg=color_1)

    # ----- Acomodo de Frame's
    root_defect.grid_rowconfigure(0, weight=0)
    root_defect.grid_rowconfigure(1, weight=0)
    root_defect.grid_rowconfigure(2, weight=0)
    root_defect.grid_rowconfigure(3, weight=1)
    # root_defect.grid_rowconfigure(3, weight=1)
    root_defect.grid_columnconfigure(0, weight=0)
    root_defect.grid_columnconfigure(1, weight=1)

    # ----- Frame's root_defect
    frame0_rd = tk.Frame(root_defect, bg=color_1, padx=0, pady=0)
    frame1_rd = tk.Frame(root_defect, bg=color_1, padx=0, pady=0)
    frame2_rd = tk.Frame(root_defect, bg=color_1, padx=0, pady=0)
    frame3_rd = tk.Frame(root_defect, bg=color_1, padx=0, pady=0)
    frame4_rd = tk.Frame(root_defect, bg=color_1, padx=0, pady=0)

    # ----- Frame0
    frame0_rd.grid_columnconfigure(0, weight=1)
    frame0_rd.grid_columnconfigure(1, weight=1)
    frame0_rd.grid_columnconfigure(2, weight=1)
    frame0_rd.grid_rowconfigure(0, weight=1)

    # ----- Frame1
    frame1_rd.grid_columnconfigure(0, weight=0)
    frame1_rd.grid_columnconfigure(1, weight=0)
    frame1_rd.grid_columnconfigure(2, weight=0)
    frame1_rd.grid_columnconfigure(3, weight=0)
    frame1_rd.grid_columnconfigure(4, weight=0)
    frame1_rd.grid_columnconfigure(5, weight=0)
    frame1_rd.grid_columnconfigure(6, weight=0)
    frame1_rd.grid_columnconfigure(7, weight=0)
    frame1_rd.grid_columnconfigure(8, weight=0)
    frame1_rd.grid_columnconfigure(9, weight=0)
    frame1_rd.grid_columnconfigure(10, weight=0)
    frame1_rd.grid_columnconfigure(11, weight=0)
    frame1_rd.grid_columnconfigure(12, weight=0)
    frame1_rd.grid_rowconfigure(0, weight=1)
    # for col in range(0, 11):
    # frame1_rd.grid_columnconfigure(col, weight=1, uniform="cols")

    # ----- Frame2
    frame2_rd.grid_columnconfigure(0, weight=1)
    frame2_rd.grid_columnconfigure(1, weight=1)
    frame2_rd.grid_rowconfigure(0, weight=1)
    frame2_rd.grid_rowconfigure(1, weight=1)
    frame2_rd.grid_rowconfigure(2, weight=1)
    frame2_rd.grid_rowconfigure(3, weight=1)
    frame2_rd.grid_rowconfigure(4, weight=1)
    frame2_rd.grid_rowconfigure(5, weight=1)
    frame2_rd.grid_rowconfigure(6, weight=1)
    frame2_rd.grid_rowconfigure(7, weight=1)
    frame2_rd.grid_rowconfigure(8, weight=1)
    frame2_rd.grid_rowconfigure(9, weight=1)
    frame2_rd.grid_rowconfigure(10, weight=1)
    frame2_rd.grid_rowconfigure(11, weight=1)
    frame2_rd.grid_rowconfigure(12, weight=1)
    frame2_rd.grid_rowconfigure(13, weight=1)
    frame2_rd.grid_rowconfigure(14, weight=1)
    frame2_rd.grid_rowconfigure(15, weight=1)
    frame2_rd.grid_rowconfigure(16, weight=1)
    frame2_rd.grid_rowconfigure(17, weight=1)
    frame2_rd.grid_rowconfigure(18, weight=1)
    frame2_rd.grid_rowconfigure(19, weight=1)
    frame2_rd.grid_rowconfigure(20, weight=1)
    frame2_rd.grid_rowconfigure(21, weight=1)
    frame2_rd.grid_rowconfigure(22, weight=1)
    frame2_rd.grid_rowconfigure(23, weight=1)
    frame2_rd.grid_rowconfigure(24, weight=1)
    frame2_rd.grid_rowconfigure(25, weight=1)
    frame2_rd.grid_rowconfigure(26, weight=1)
    frame2_rd.grid_rowconfigure(27, weight=1)
    frame2_rd.grid_rowconfigure(28, weight=1)
    frame2_rd.grid_rowconfigure(29, weight=1)
    frame2_rd.grid_rowconfigure(30, weight=1)
    frame2_rd.grid_rowconfigure(31, weight=1)
    frame2_rd.grid_rowconfigure(32, weight=1)
    frame2_rd.grid_rowconfigure(33, weight=1)
    frame2_rd.grid_rowconfigure(34, weight=1)
    frame2_rd.grid_rowconfigure(35, weight=1)

    # ----- Frame3
    frame3_rd.grid_columnconfigure(0, weight=1)
    frame3_rd.grid_columnconfigure(1, weight=1)
    frame3_rd.grid_columnconfigure(2, weight=1)
    frame3_rd.grid_columnconfigure(3, weight=1)
    frame3_rd.grid_columnconfigure(4, weight=1)
    frame3_rd.grid_columnconfigure(5, weight=1)
    frame3_rd.grid_rowconfigure(0, weight=1)
    frame3_rd.grid_rowconfigure(1, weight=1)
    frame3_rd.grid_rowconfigure(2, weight=1)
    frame3_rd.grid_rowconfigure(3, weight=1)
    frame3_rd.grid_rowconfigure(4, weight=1)

    # ----- Frame4
    frame4_rd.grid_columnconfigure(0, weight=1)
    frame4_rd.grid_rowconfigure(0, weight=1)

    # ----- Frame0_Row0
    # Cargar logo ELRAD
    logo_elrad_rd = Image.open(settings_root_rd("LogoELRAD"))
    logo_elrad_rd = logo_elrad_rd.resize((100, 50), Image.Resampling.LANCZOS)
    logo_elrad_tk_rd = ImageTk.PhotoImage(logo_elrad_rd)

    # Imagen ELRAD
    label_logo_elrad_rd = tk.Label(
        frame0_rd, image=logo_elrad_tk_rd, borderwidth=0, bg=color_1)
    label_logo_elrad_rd.image = logo_elrad_tk_rd
    label_logo_elrad_rd.grid(row=0, column=0, padx=0, pady=0, sticky="nw")

    # label_rd_0: Titulo
    label_rd_0 = tk.Label(frame0_rd, text="Defectos SEHO",
                          fg="black", bg=color_1)
    label_rd_0.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

    # Cargar logo SEHO
    logo_seho_rd = Image.open(settings_root_rd("LogoSEHO"))
    logo_seho_rd = logo_seho_rd.resize((100, 50), Image.Resampling.LANCZOS)
    logo_seho_tk_rd = ImageTk.PhotoImage(logo_seho_rd)

    # Imagen SEHO como boton de cerrado
    boton_cerrar_rd = tk.Button(frame0_rd, image=logo_seho_tk_rd,
                                command=closed_rd, borderwidth=0, bg=color_1)
    boton_cerrar_rd.image = logo_seho_tk_rd
    boton_cerrar_rd.grid(row=0, column=2, padx=0, pady=0, sticky="ne")

    # ----- Frame1_Row0
    # label_rd_1: Modelo
    label_rd_1 = tk.Label(frame1_rd, text="Modelo:",
                          fg="black", bg=color_1, anchor="e")
    label_rd_1.grid(row=0, column=0, padx=(10, 0), pady=0, sticky="nsew")

    # menu_rd_1: Modelos
    opcion_seleccionada_model = tk.StringVar(frame1_rd)
    opciones_model = [model1, model2, model3, model4, model5,
                      model6, model7, model8, model9, model10, model11, model12]
    opcion_seleccionada_model.set(opciones_model[0])
    menu_rd_1 = tk.OptionMenu(
        frame1_rd, opcion_seleccionada_model, *opciones_model)
    menu_rd_1.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_2: Fecha
    label_rd_2 = tk.Label(frame1_rd, text="Fecha:",
                          fg="black", bg=color_1, anchor="e")
    label_rd_2.grid(row=0, column=2, padx=(10, 0), pady=0, sticky="nsew")

    # date_rd_1: Selección de fecha
    date_rd_1 = DateEntry(frame1_rd, background='darkblue',
                          foreground='#AEAEAE', borderwidth=2, date_pattern='dd/mm/yyyy', showweeknumbers=False, state='readonly', justify="center")
    date_rd_1.grid(row=0, column=3, padx=0, pady=0,
                   sticky="nsew")

    # Configuración de estilo para que no se vea "viejo"
    style = ttk.Style()
    # Usar 'default' permite personalizar más colores
    style.theme_use('default')
    style.configure("Custom.TCombobox", fieldbackground="white",
                    foreground="black", padding=2)

    # Horas con formato 1, 2, 12...
    horas_vals_rd = [str(i) for i in range(1, 13)]
    # Minutos con formato 00, 01, 02...
    minutos_vals_rd = ["00", "10", "20", "30", "40", "50", "59"]
    # Opciones de periodo
    lista_periodos_rd = ["AM", "PM"]

    # spinbox_rs_1: Hora de inicio
    hora_inicio_rd = tk.StringVar(value="6")
    spinbox_rd_1 = ttk.Combobox(frame1_rd, values=horas_vals_rd, style="Custom.TCombobox", textvariable=hora_inicio_rd,
                                width=4, state="readonly", justify="center")
    spinbox_rd_1.grid(row=0, column=4, padx=(10, 0), pady=0, sticky="nsew")

    # spinbox_rs_2: Minuto de inicio
    minuto_inicio_rd = tk.StringVar(value="00")
    spinbox_rd_2 = ttk.Combobox(frame1_rd, values=minutos_vals_rd, style="Custom.TCombobox", textvariable=minuto_inicio_rd,
                                width=4, state="readonly", justify="center")
    spinbox_rd_2.grid(row=0, column=5, padx=0, pady=0,
                      sticky="nsew")

    # spinbox_rs_3: Periodo de inicio
    periodo_inicio_rd = tk.StringVar(value="AM")
    spinbox_rd_3 = ttk.Combobox(frame1_rd, values=lista_periodos_rd, style="Custom.TCombobox", textvariable=periodo_inicio_rd,
                                width=4, state="readonly", justify="center")
    spinbox_rd_3.grid(row=0, column=6, padx=0, pady=0,
                      sticky="nsew")

    # label_rd_3: Horario
    label_rd_3 = tk.Label(frame1_rd, text="<-Horario->",
                          fg="black", bg=color_1)
    label_rd_3.grid(row=0, column=7, padx=3, pady=0, sticky="nsew")

    # spinbox_rs_4: Hora final
    hora_final_rd = tk.StringVar(value="11")
    spinbox_rd_4 = ttk.Combobox(frame1_rd, values=horas_vals_rd, style="Custom.TCombobox", textvariable=hora_final_rd,
                                width=4, state="readonly", justify="center")
    spinbox_rd_4.grid(row=0, column=8, padx=0, pady=0, sticky="nsew")

    # spinbox_rs_5: Minuto final
    minuto_final_rd = tk.StringVar(value="30")
    spinbox_rd_5 = ttk.Combobox(frame1_rd, values=minutos_vals_rd, style="Custom.TCombobox", textvariable=minuto_final_rd,
                                width=4, state="readonly", justify="center")
    spinbox_rd_5.grid(row=0, column=9, padx=0, pady=0, sticky="nsew")

    # spinbox_rs_6: Periodo final
    periodo_final_rd = tk.StringVar(value="PM")
    spinbox_rd_6 = ttk.Combobox(frame1_rd, values=lista_periodos_rd, style="Custom.TCombobox", textvariable=periodo_final_rd,
                                width=4, state="readonly", justify="center")
    spinbox_rd_6.grid(row=0, column=10, padx=(0, 10), pady=0,
                      sticky="nsew")

    # button_rd_1:
    button_rd_1 = tk.Button(frame1_rd, text="Buscar", height=0, width=20,
                            border=3, background="deepskyblue", command=contar_defectos_por_modelo)
    button_rd_1.grid(row=0, column=11, padx=5, pady=0, sticky="nsew")

    # button_rd_2:
    button_rd_2 = tk.Button(frame1_rd, text="DASHBOARD", height=0, width=20,
                            border=3, background="deepskyblue", command=dashboard_seho)
    button_rd_2.grid(row=0, column=12, padx=5, pady=0, sticky="nsew")

    # ----- Frame2_Row0
    # label_rd_4: Defectos
    label_rd_4 = tk.Label(frame2_rd, text="Defectos",
                          fg="white", bg="#156082")
    label_rd_4.grid(row=0, column=0, padx=0, pady=(20, 0), sticky="nsew")
    # label_rd_5: Cantidad
    label_rd_5 = tk.Label(frame2_rd, text="Cantidad",
                          fg="white", bg="#156082")
    label_rd_5.grid(row=0, column=1, padx=0, pady=(20, 0), sticky="nsew")

    # ----- Frame2_Defectos
    # label_rd_6: defect1
    label_rd_6 = tk.Label(frame2_rd, text=defect1,
                          fg="black", bg="#C0E6F5")
    label_rd_6.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_7: defect2
    label_rd_7 = tk.Label(frame2_rd, text=defect2,
                          fg="black", bg="white")
    label_rd_7.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_8: defect3
    label_rd_8 = tk.Label(frame2_rd, text=defect3,
                          fg="black", bg="#C0E6F5")
    label_rd_8.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_9: defect4
    label_rd_9 = tk.Label(frame2_rd, text=defect4,
                          fg="black", bg="white")
    label_rd_9.grid(row=4, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_10: defect5
    label_rd_10 = tk.Label(frame2_rd, text=defect5,
                           fg="black", bg="#C0E6F5")
    label_rd_10.grid(row=5, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_11: defect6
    label_rd_11 = tk.Label(frame2_rd, text=defect6,
                           fg="black", bg="white")
    label_rd_11.grid(row=6, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_12: defect7
    label_rd_12 = tk.Label(frame2_rd, text=defect7,
                           fg="black", bg="#C0E6F5")
    label_rd_12.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_13: defect8
    label_rd_13 = tk.Label(frame2_rd, text=defect8,
                           fg="black", bg="white")
    label_rd_13.grid(row=8, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_14: defect9
    label_rd_14 = tk.Label(frame2_rd, text=defect9,
                           fg="black", bg="#C0E6F5")
    label_rd_14.grid(row=9, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_15: defect10
    label_rd_15 = tk.Label(frame2_rd, text=defect10,
                           fg="black", bg="white")
    label_rd_15.grid(row=10, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_16: defect11
    label_rd_16 = tk.Label(frame2_rd, text=defect11,
                           fg="black", bg="#C0E6F5")
    label_rd_16.grid(row=11, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_17: defect12
    label_rd_17 = tk.Label(frame2_rd, text=defect12,
                           fg="black", bg="white")
    label_rd_17.grid(row=12, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_18: defect13
    label_rd_18 = tk.Label(frame2_rd, text=defect13,
                           fg="black", bg="#C0E6F5")
    label_rd_18.grid(row=13, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_19: defect14
    label_rd_19 = tk.Label(frame2_rd, text=defect14,
                           fg="black", bg="white")
    label_rd_19.grid(row=14, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_20: defect15
    label_rd_20 = tk.Label(frame2_rd, text=defect15,
                           fg="black", bg="#C0E6F5")
    label_rd_20.grid(row=15, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_21: defect16
    label_rd_21 = tk.Label(frame2_rd, text=defect16,
                           fg="black", bg="white")
    label_rd_21.grid(row=16, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_22: defect17
    label_rd_22 = tk.Label(frame2_rd, text=defect17,
                           fg="black", bg="#C0E6F5")
    label_rd_22.grid(row=17, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_23: defect18
    label_rd_23 = tk.Label(frame2_rd, text=defect18,
                           fg="black", bg="white")
    label_rd_23.grid(row=18, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_24: defect19
    label_rd_24 = tk.Label(frame2_rd, text=defect19,
                           fg="black", bg="#C0E6F5")
    label_rd_24.grid(row=19, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_25: defect20
    label_rd_25 = tk.Label(frame2_rd, text=defect20,
                           fg="black", bg="white")
    label_rd_25.grid(row=20, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_26: defect21
    label_rd_26 = tk.Label(frame2_rd, text=defect21,
                           fg="black", bg="#C0E6F5")
    label_rd_26.grid(row=21, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_27: defect22
    label_rd_27 = tk.Label(frame2_rd, text=defect22,
                           fg="black", bg="white")
    label_rd_27.grid(row=22, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_28: defect23
    label_rd_28 = tk.Label(frame2_rd, text=defect23,
                           fg="black", bg="#C0E6F5")
    label_rd_28.grid(row=23, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_29: defect24
    label_rd_29 = tk.Label(frame2_rd, text=defect24,
                           fg="black", bg="white")
    label_rd_29.grid(row=24, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_30: defect25
    label_rd_30 = tk.Label(frame2_rd, text=defect25,
                           fg="black", bg="#C0E6F5")
    label_rd_30.grid(row=25, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_31: defect26
    label_rd_31 = tk.Label(frame2_rd, text=defect26,
                           fg="black", bg="white")
    label_rd_31.grid(row=26, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_32: defect27
    label_rd_32 = tk.Label(frame2_rd, text=defect27,
                           fg="black", bg="#C0E6F5")
    label_rd_32.grid(row=27, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_33: defect28
    label_rd_33 = tk.Label(frame2_rd, text=defect28,
                           fg="black", bg="white")
    label_rd_33.grid(row=28, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_34: defect29
    label_rd_34 = tk.Label(frame2_rd, text=defect29,
                           fg="black", bg="#C0E6F5")
    label_rd_34.grid(row=29, column=0, padx=0, pady=0, sticky="nsew")
    # label_rd_35: defect30
    label_rd_35 = tk.Label(frame2_rd, text=defect30,
                           fg="black", bg="white")
    label_rd_35.grid(row=30, column=0, padx=0, pady=0, sticky="nsew")

    # ----- Frame2_Cantidad
    # label_rd_36: Cantidad_defect1
    label_rd_36 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_36.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_37: Cantidad_defect2
    label_rd_37 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_37.grid(row=2, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_38: Cantidad_defect3
    label_rd_38 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_38.grid(row=3, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_39: Cantidad_defect4
    label_rd_39 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_39.grid(row=4, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_40: Cantidad_defect5
    label_rd_40 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_40.grid(row=5, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_41: Cantidad_defect6
    label_rd_41 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_41.grid(row=6, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_42: Cantidad_defect7
    label_rd_42 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_42.grid(row=7, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_43: Cantidad_defect8
    label_rd_43 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_43.grid(row=8, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_44: Cantidad_defect9
    label_rd_44 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_44.grid(row=9, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_45: Cantidad_defect10
    label_rd_45 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_45.grid(row=10, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_46: Cantidad_defect11
    label_rd_46 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_46.grid(row=11, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_47: Cantidad_defect12
    label_rd_47 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_47.grid(row=12, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_48: Cantidad_defect13
    label_rd_48 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_48.grid(row=13, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_49: Cantidad_defect14
    label_rd_49 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_49.grid(row=14, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_50: Cantidad_defect15
    label_rd_50 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_50.grid(row=15, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_51: Cantidad_defect16
    label_rd_51 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_51.grid(row=16, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_52: Cantidad_defect17
    label_rd_52 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_52.grid(row=17, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_53: Cantidad_defect18
    label_rd_53 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_53.grid(row=18, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_54: Cantidad_defect19
    label_rd_54 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_54.grid(row=19, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_55: Cantidad_defect20
    label_rd_55 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_55.grid(row=20, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_56: Cantidad_defect21
    label_rd_56 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_56.grid(row=21, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_57: Cantidad_defect22
    label_rd_57 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_57.grid(row=22, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_58: Cantidad_defect23
    label_rd_58 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_58.grid(row=23, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_59: Cantidad_defect24
    label_rd_59 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_59.grid(row=24, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_60: Cantidad_defect25
    label_rd_60 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_60.grid(row=25, column=1, padx=0, pady=0, sticky="nsew")
    # label_rd_61: Cantidad_defect26
    label_rd_61 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_61.grid(row=26, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_62: Cantidad_defect27
    label_rd_62 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_62.grid(row=27, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_63: Cantidad_defect28
    label_rd_63 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_63.grid(row=28, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_64: Cantidad_defect29
    label_rd_64 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_64.grid(row=29, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_65: Cantidad_defect30
    label_rd_65 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_65.grid(row=30, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_88: defect31
    label_rd_88 = tk.Label(frame2_rd, text=defect31,
                           fg="black", bg="#C0E6F5")
    label_rd_88.grid(row=31, column=0, padx=0, pady=0, sticky="nsew")

    # label_rd_89: defect32
    label_rd_89 = tk.Label(frame2_rd, text=defect32,
                           fg="black", bg="white")
    label_rd_89.grid(row=32, column=0, padx=0, pady=0, sticky="nsew")

    # label_rd_90: defect33
    label_rd_90 = tk.Label(frame2_rd, text=defect33,
                           fg="black", bg="#C0E6F5")
    label_rd_90.grid(row=33, column=0, padx=0, pady=0, sticky="nsew")

    # label_rd_91: defect34
    label_rd_91 = tk.Label(frame2_rd, text=defect34,
                           fg="black", bg="white")
    label_rd_91.grid(row=34, column=0, padx=0, pady=0, sticky="nsew")

    # label_rd_92: defect35
    label_rd_92 = tk.Label(frame2_rd, text=defect35,
                           fg="black", bg="#C0E6F5")
    label_rd_92.grid(row=35, column=0, padx=0, pady=0, sticky="nsew")

    # label_rd_93: Cantidad_defect31
    label_rd_93 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_93.grid(row=31, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_94: Cantidad_defect32
    label_rd_94 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_94.grid(row=32, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_95: Cantidad_defect33
    label_rd_95 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_95.grid(row=33, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_96: Cantidad_defect34
    label_rd_96 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="white")
    label_rd_96.grid(row=34, column=1, padx=0, pady=0, sticky="nsew")

    # label_rd_97: Cantidad_defect35
    label_rd_97 = tk.Label(frame2_rd, text="0",
                           fg="black", bg="#C0E6F5")
    label_rd_97.grid(row=35, column=1, padx=0, pady=0, sticky="nsew")

    # ----- Frame3

    label_rd_66 = tk.Label(frame3_rd, textvariable=opcion_seleccionada_model,
                           fg="black", bg="#F2CEEF")
    label_rd_66.grid(row=0, column=0, columnspan=6,
                     padx=50, pady=(20, 0), sticky="nsew")

    label_rd_67 = tk.Label(frame3_rd, text="Defectos:",
                           fg="black", bg="#FFFFC9", anchor="e")
    label_rd_67.grid(row=1, column=0,
                     padx=(50, 0), pady=(5, 0), sticky="nsew")
    label_rd_68 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_68.grid(row=1, column=1, padx=0, pady=(5, 0), sticky="nsew")

    label_rd_69 = tk.Label(
        frame3_rd, text="Top3 Defectos", fg="black", bg="#CAEDFB")
    label_rd_69.grid(row=1, column=3, padx=0, pady=(5, 0), sticky="nsew")

    label_rd_70 = tk.Label(
        frame3_rd, text="Cantidad", fg="black", bg="#CAEDFB")
    label_rd_70.grid(row=1, column=4, padx=0, pady=(5, 0), sticky="nsew")

    label_rd_71 = tk.Label(
        frame3_rd, text="%", fg="black", bg="#CAEDFB")
    label_rd_71.grid(row=1, column=5, padx=(0, 50), pady=(5, 0), sticky="nsew")

    label_rd_72 = tk.Label(frame3_rd, text="Producido:",
                           fg="black", bg="#FFFFC9", anchor="e")
    label_rd_72.grid(row=2, column=0,
                     padx=(50, 0), pady=0, sticky="nsew")

    label_rd_73 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_73.grid(row=2, column=1, padx=0, pady=0, sticky="nsew")

    label_rd_74 = tk.Label(frame3_rd, text="1",
                           fg="black", bg=color_1, anchor="e")
    label_rd_74.grid(row=2, column=2, padx=0, pady=0, sticky="nsew")

    label_rd_75 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_75.grid(row=2, column=3, padx=0, pady=0, sticky="nsew")

    label_rd_76 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_76.grid(row=2, column=4, padx=0, pady=0, sticky="nsew")

    label_rd_77 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_77.grid(row=2, column=5, padx=(0, 50), pady=0, sticky="nsew")

    label_rd_78 = tk.Label(frame3_rd, text="FPY:",
                           fg="black", bg="#FFFFC9", anchor="e")
    label_rd_78.grid(row=3, column=0,
                     padx=(50, 0), pady=0, rowspan=2, sticky="nsew")

    label_rd_79 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_1)
    label_rd_79.grid(row=3, column=1, padx=0, pady=0, rowspan=2, sticky="nsew")

    label_rd_80 = tk.Label(frame3_rd, text="2",
                           fg="black", bg=color_1, anchor="e")
    label_rd_80.grid(row=3, column=2, padx=0, pady=0, sticky="nsew")

    label_rd_81 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_1)
    label_rd_81.grid(row=3, column=3, padx=0, pady=0, sticky="nsew")

    label_rd_82 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_1)
    label_rd_82.grid(row=3, column=4, padx=0, pady=0, sticky="nsew")

    label_rd_83 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_1)
    label_rd_83.grid(row=3, column=5, padx=(0, 50), pady=0, sticky="nsew")

    label_rd_84 = tk.Label(frame3_rd, text="3",
                           fg="black", bg=color_1, anchor="e")
    label_rd_84.grid(row=4, column=2, padx=0, pady=0, sticky="nsew")

    label_rd_85 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_85.grid(row=4, column=3, padx=0, pady=0, sticky="nsew")

    label_rd_86 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_86.grid(row=4, column=4, padx=0, pady=0, sticky="nsew")

    label_rd_87 = tk.Label(frame3_rd, text="N/A", fg="black", bg=color_3)
    label_rd_87.grid(row=4, column=5, padx=(0, 50), pady=0, sticky="nsew")

    # ---------------------------------------------------------------------------------------------
    frame0_rd.grid(row=0, column=0, sticky="nsew", columnspan=2)
    frame1_rd.grid(row=1, column=0, sticky="nsew", columnspan=2)
    frame2_rd.grid(row=2, column=0, sticky="nsew", rowspan=2)
    frame3_rd.grid(row=2, column=1, sticky="nsew")
    frame4_rd.grid(row=3, column=1, sticky="nsew")
    root_defect_scale()


# ------------------------------------- Variables ---------------------------------------------------------------------
# Defectos
