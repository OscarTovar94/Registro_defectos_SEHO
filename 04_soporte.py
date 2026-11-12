def support_root(funcion_andon):
    """Función para abrir ventana de solicitud de soporte (Ingeniería, Calidad, Producción)"""
    # ----- Variables root support
    global root
    # ----- Logit root support ----------------------------------------------------------------------------------------

    def root_support_scale():
        """Funcíon para escalar root soport"""
        # Obtener el tamaño de la pantalla
        pantalla_ancho = root_support.winfo_screenwidth()
        pantalla_alto = root_support.winfo_screenheight()

        # Calcular el factor de escala basado en una resolución de referencia (1920x1080)
        escala_x = pantalla_ancho / 1920
        escala_y = pantalla_alto / 1080
        escala = min(escala_x, escala_y)
        frame0_rs.config(padx=0 * escala, pady=0 * escala)
        frame1_rs.config(padx=0 * escala, pady=0 * escala)
        frame2_rs.config(padx=0 * escala, pady=0 * escala)
        frame3_rs.config(padx=0 * escala, pady=0 * escala)

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
        fuente_70 = int(70 * escala)
        button_support = int(40 * escala)

        # ----- Label's
        label_rs_0.config(font=("Arial", fuente_70, "bold"))  # Título
        label_rs_1.config(font=("Arial", fuente_40, "bold")
                          )  # Código de colores ANDON
        label_rs_2.config(font=("Arial", fuente_20, "bold"))  # Ingeniería
        label_rs_3.config(font=("Arial", fuente_16, "bold"))  # Ingeniería Rojo
        label_rs_4.config(font=("Arial", fuente_20, "bold"))  # Calidad
        label_rs_5.config(font=("Arial", fuente_16, "bold"))  # Calidad Rojo
        label_rs_6.config(font=("Arial", fuente_20, "bold"))  # Calidad +
        label_rs_7.config(font=("Arial", fuente_16, "bold"))  # Calidad Naranja
        label_rs_8.config(font=("Arial", fuente_20, "bold"))  # Producción
        label_rs_9.config(font=("Arial", fuente_16, "bold"))  # Producción Rojo
        label_rs_10.config(font=("Arial", fuente_20, "bold"))  # Producción +
        label_rs_11.config(font=("Arial", fuente_16, "bold")
                           )  # Producción Verde
        label_rs_12.config(font=("Arial", fuente_20, "bold"))  # Todos
        label_rs_13.config(font=("Arial", fuente_16, "bold"))  # Todos Rojo
        label_rs_14.config(font=("Arial", fuente_20, "bold"))  # Todos +
        label_rs_15.config(font=("Arial", fuente_16, "bold"))  # Todos Naranja
        label_rs_16.config(font=("Arial", fuente_20, "bold"))  # Todos +
        label_rs_17.config(font=("Arial", fuente_16, "bold"))  # Todos Verde

        # ----- Botton's
        # Solicitar soporte ingeniería
        button_rs_0.config(font=("Arial", button_support, "bold"))
        # Solicitar soporte calidad
        button_rs_1.config(font=("Arial", button_support, "bold"))
        # Solicitar soporte producción
        button_rs_2.config(font=("Arial", button_support, "bold"))
        # Solicitar soporte todos
        button_rs_3.config(font=("Arial", button_support, "bold"))
        button_rs_4.config(font=("Arial", fuente_20, "bold"))  # Cerrar ventana

    def closed_rs():
        """Función para cerrar root soporte"""
        root_support.destroy()
        funcion_andon("X", root_support)

    def ingenieria():
        """Función para solicitar soporte de ingeniería"""
        if button_rs_0["bg"] == "red":
            # Cambiar a amarillo
            button_rs_0.configure(bg="yellow")
            button_rs_1.configure(bg="#FFC000")
            button_rs_2.configure(bg="green")
            button_rs_3.configure(bg="#00B0F0")
            # funcion_andon("H", root_support)
            # time.sleep(0.3)
            funcion_andon("D", root_support)
        else:
            # Cambiar a rojo
            button_rs_0.configure(bg="red")
            funcion_andon("H", root_support)

    def calidad():
        """Función para solicitar soporte de calidad"""
        if button_rs_1["bg"] == "#FFC000":
            # Cambiar a amarillo
            button_rs_1.configure(bg="yellow")
            button_rs_0.configure(bg="red")
            button_rs_2.configure(bg="green")
            button_rs_3.configure(bg="#00B0F0")
            # funcion_andon("H", root_support)
            # time.sleep(0.3)
            funcion_andon("E", root_support)

        else:
            # Cambiar a rojo
            button_rs_1.configure(bg="#FFC000")
            funcion_andon("H", root_support)

    def produccion():
        """Función para solicitar soporte de producción"""
        if button_rs_2["bg"] == "green":
            # Cambiar a amarillo
            button_rs_2.configure(bg="yellow")
            button_rs_0.configure(bg="red")
            button_rs_1.configure(bg="#FFC000")
            button_rs_3.configure(bg="#00B0F0")
            # funcion_andon("H", root_support)
            # time.sleep(0.3)
            funcion_andon("F", root_support)

        else:
            # Cambiar a rojo
            button_rs_2.configure(bg="green")
            funcion_andon("H", root_support)

    def todos():
        """Función para solicitar soporte de todos"""
        if button_rs_3["bg"] == "#00B0F0":
            # Cambiar a amarillo
            button_rs_3.configure(bg="yellow")
            button_rs_0.configure(bg="red")
            button_rs_1.configure(bg="#FFC000")
            button_rs_2.configure(bg="green")
            # funcion_andon("H", root_support)
            # time.sleep(0.3)
            funcion_andon("G", root_support)
        else:
            # Cambiar a rojo
            button_rs_3.configure(bg="#00B0F0")
            funcion_andon("H", root_support)

    # ----- GUI root support ------------------------------------------------------------------------------------------
    root_support = tk.Toplevel(root)
    root_support.attributes("-topmost", True)
    root_support.attributes("-fullscreen", True)
    root_support.overrideredirect(False)
    root_support.resizable(False, False)
    root_support.configure(bg=color_1)

    # ----- Acomodo de Frame's
    root_support.grid_rowconfigure(0, weight=0)
    root_support.grid_rowconfigure(1, weight=1)
    root_support.grid_rowconfigure(2, weight=0)
    root_support.grid_rowconfigure(3, weight=0)
    root_support.grid_columnconfigure(0, weight=1)

    # ----- Frame's root_defect
    frame0_rs = tk.Frame(root_support, bg=color_1, padx=0, pady=30)
    frame1_rs = tk.Frame(root_support, bg=color_1, padx=0, pady=0)
    frame2_rs = tk.Frame(root_support, bg=color_1,
                         padx=0, pady=0, bd=2, relief="solid")
    frame3_rs = tk.Frame(root_support, bg=color_1, padx=0, pady=0)

    # ----- Frame0
    frame0_rs.grid_columnconfigure(0, weight=1)
    frame0_rs.grid_rowconfigure(0, weight=1)

    # ----- Frame1
    frame1_rs.grid_columnconfigure(0, weight=1)
    frame1_rs.grid_columnconfigure(1, weight=1)
    frame1_rs.grid_columnconfigure(2, weight=1)
    frame1_rs.grid_columnconfigure(3, weight=1)
    frame1_rs.grid_rowconfigure(0, weight=1)
    for col in range(0, 4):
        frame1_rs.grid_columnconfigure(col, weight=1, uniform="cols")

    # ----- Frame2
    frame2_rs.grid_columnconfigure(0, weight=1)
    frame2_rs.grid_columnconfigure(1, weight=1)
    frame2_rs.grid_columnconfigure(2, weight=1)
    frame2_rs.grid_columnconfigure(3, weight=1)
    frame2_rs.grid_columnconfigure(4, weight=1)
    frame2_rs.grid_columnconfigure(5, weight=1)
    frame2_rs.grid_columnconfigure(6, weight=1)
    frame2_rs.grid_columnconfigure(7, weight=1)
    frame2_rs.grid_rowconfigure(0, weight=1)
    frame2_rs.grid_rowconfigure(1, weight=1)
    frame2_rs.grid_rowconfigure(2, weight=1)
    frame2_rs.grid_rowconfigure(3, weight=1)
    frame2_rs.grid_rowconfigure(4, weight=1)
    for col in range(0, 8):
        frame2_rs.grid_columnconfigure(col, weight=1, uniform="cols")

    # ----- Frame3
    frame3_rs.grid_columnconfigure(0, weight=1)
    frame3_rs.grid_rowconfigure(0, weight=1)

    # ----- Frame0_Row0
    # label_rs_0: Título
    label_rs_0 = tk.Label(frame0_rs, text="Solicitud de soporte",
                          fg="black", bg=color_1)
    label_rs_0.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

    # ----- Frame1_Row0
    # button_rs_0: Ingeniería
    button_rs_0 = tk.Button(frame1_rs, text="Ingeniería", height=0, width=0,
                            border=5, background="red", command=ingenieria)
    button_rs_0.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # button_rs_1: Calidad
    button_rs_1 = tk.Button(frame1_rs, text="Calidad", height=0, width=0,
                            border=5, background="#FFC000", command=calidad)
    button_rs_1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # button_rs_2: Producción
    button_rs_2 = tk.Button(frame1_rs, text="Producción", height=0, width=0,
                            border=5, background="green", command=produccion)
    button_rs_2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    # button_rs_3: Todos
    button_rs_3 = tk.Button(frame1_rs, text="Todos", height=0, width=0,
                            border=5, background="#00B0F0", command=todos)
    button_rs_3.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

    # ----- Frame2_Row0
    # label_rs_1: Código de colores ANDON
    label_rs_1 = tk.Label(frame2_rs, text="Código de colores ANDON",
                          fg="black", bg=color_1)
    label_rs_1.grid(row=0, column=1, columnspan=6,
                    padx=0, pady=0, sticky="nsew")

    # ----- Frame2_Row1
    # label_rs_2: Ingeniería
    label_rs_2 = tk.Label(frame2_rs, text="Ingeniería:",
                          fg="black", bg=color_1, anchor="e")
    label_rs_2.grid(row=1, column=1,
                    padx=0, pady=0, sticky="nsew")

    # label_rs_3: Rojo Ingeniería
    label_rs_3 = tk.Label(frame2_rs, text="Alarma",
                          fg="black", bg="red")
    label_rs_3.grid(row=1, column=2,
                    padx=0, pady=0, sticky="nsew")

    # ----- Frame2_Row2
    # label_rs_4: Calidad
    label_rs_4 = tk.Label(frame2_rs, text="Calidad:",
                          fg="black", bg=color_1, anchor="e")
    label_rs_4.grid(row=2, column=1,
                    padx=0, pady=5, sticky="nsew")

    # label_rs_5: Rojo Calidad
    label_rs_5 = tk.Label(frame2_rs, text="Alarma",
                          fg="black", bg="red")
    label_rs_5.grid(row=2, column=2,
                    padx=0, pady=5, sticky="nsew")

    # label_rs_6: + Calidad
    label_rs_6 = tk.Label(frame2_rs, text="+",
                          fg="black", bg=color_1)
    label_rs_6.grid(row=2, column=3,
                    padx=0, pady=5, sticky="nsew")

    # label_rs_7: Naranja Calidad
    label_rs_7 = tk.Label(frame2_rs,
                          fg="black", bg="#FFC000")
    label_rs_7.grid(row=2, column=4,
                    padx=0, pady=5, sticky="nsew")

    # ----- Frame2_Row3
    # label_rs_8: Producción
    label_rs_8 = tk.Label(frame2_rs, text="Producción:",
                          fg="black", bg=color_1, anchor="e")
    label_rs_8.grid(row=3, column=1,
                    padx=0, pady=5, sticky="nsew")

    # label_rs_9: Rojo Producción
    label_rs_9 = tk.Label(frame2_rs, text="Alarma",
                          fg="black", bg="red")
    label_rs_9.grid(row=3, column=2,
                    padx=0, pady=5, sticky="nsew")

    # label_rs_10: + Producción
    label_rs_10 = tk.Label(frame2_rs, text="+",
                           fg="black", bg=color_1)
    label_rs_10.grid(row=3, column=3,
                     padx=0, pady=5, sticky="nsew")

    # label_rs_11: Verde Producción
    label_rs_11 = tk.Label(frame2_rs,
                           fg="black", bg="#4EA72E")
    label_rs_11.grid(row=3, column=4,
                     padx=0, pady=5, sticky="nsew")

    # ----- Frame2_Row4
    # label_rs_12: Todos
    label_rs_12 = tk.Label(frame2_rs, text="Todos:",
                           fg="black", bg=color_1, anchor="e")
    label_rs_12.grid(row=4, column=1,
                     padx=0, pady=5, sticky="nsew")

    # label_rs_13: Rojo Todos
    label_rs_13 = tk.Label(frame2_rs, text="Alarma",
                           fg="black", bg="red")
    label_rs_13.grid(row=4, column=2,
                     padx=0, pady=5, sticky="nsew")

    # label_rs_14: + Todos
    label_rs_14 = tk.Label(frame2_rs, text="+",
                           fg="black", bg=color_1)
    label_rs_14.grid(row=4, column=3,
                     padx=0, pady=5, sticky="nsew")

    # label_rs_15: Naranja Todos
    label_rs_15 = tk.Label(frame2_rs,
                           fg="black", bg="#FFC000")
    label_rs_15.grid(row=4, column=4,
                     padx=0, pady=5, sticky="nsew")

    # label_rs_16: + Todos
    label_rs_16 = tk.Label(frame2_rs, text="+",
                           fg="black", bg=color_1)
    label_rs_16.grid(row=4, column=5,
                     padx=0, pady=5, sticky="nsew")

    # label_rs_17: Verde Todos
    label_rs_17 = tk.Label(frame2_rs,
                           fg="black", bg="#4EA72E")
    label_rs_17.grid(row=4, column=6,
                     padx=0, pady=5, sticky="nsew")

    # ----- Frame3_Row0
    # button_rs_4: Cerrar_root
    button_rs_4 = tk.Button(frame3_rs, text="Cerrar", height=0, width=20,
                            border=5, background="red", fg="white", command=closed_rs)
    button_rs_4.grid(row=0, column=0, padx=0, pady=10)

    # ---------------------------------------------------------------------------------------------
    frame0_rs.grid(row=0, column=0, sticky="nsew")
    frame1_rs.grid(row=1, column=0, sticky="nsew")
    frame2_rs.grid(row=2, column=0, sticky="nsew")
    frame3_rs.grid(row=3, column=0, sticky="nsew")
    root_support_scale()


