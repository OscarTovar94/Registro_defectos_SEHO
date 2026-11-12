def calcular_defectos():
    """Función para calcular los defectos y FPY"""
    try:
        data_register = pd.read_csv(csv_file2, encoding='latin1')
        data_register['Fecha/Hora'] = pd.to_datetime(
            data_register['Fecha/Hora'], format='%d/%m/%Y %H:%M:%S')

        # ---- Obtener modelos desde settings ----
        models = [settings_part_numbers(f"Part#{i}") for i in range(1, 13)]

        # ---- Listas de labels ----
        labels_def = [label_63, label_64, label_65, label_66, label_67, label_68,
                      label_69, label_70, label_71, label_72, label_73, label_74]

        labels_est = [label_76, label_77, label_78, label_79, label_80, label_81,
                      label_82, label_83, label_84, label_85, label_86, label_87]

        labels_fpy = [label_89, label_90, label_91, label_92, label_93, label_94,
                      label_95, label_96, label_97, label_98, label_99, label_100]

        # Valor mínimo de FPY configurable
        fpy_model_min = int(settings_limits("FPY_MODEL_min"))
        fpy_model_max = int(settings_limits("FPY_MODEL_max"))

        # ---- Fecha seleccionada ----
        date = pd.to_datetime(label_179.cget(
            "text"), format='%d/%m/%Y %H:%M:%S')

        # ---- Horas ----
        hora_inicio_1 = pd.to_datetime(f"{hora_inicial.get()}:{minuto_inicial.get()} {periodo_inicial.get()}",
                                       format='%I:%M %p').time()
        hora_fin_1 = pd.to_datetime(f"{hora_final.get()}:{minuto_final.get()} {periodo_final.get()}",
                                    format='%I:%M %p').time()

        # ==============================================================
        #   CALCULAR PARA CADA MODELO
        # ==============================================================
        for i, modelo in enumerate(models):

            # Filtrar por modelo y fecha
            filtro_modelo_fecha = (data_register["Modelo"] == modelo) & \
                                  (data_register["Fecha/Hora"].dt.date ==
                                   date.date())

            # Filtrar por hora
            filtro_horas = data_register["Fecha/Hora"].dt.time.between(
                hora_inicio_1, hora_fin_1)

            datos = data_register[filtro_modelo_fecha & filtro_horas]

            # ---- DEFECTOS ----
            suma_defectos = datos["Defectos"].sum()

            # ---- ESTÁNDAR ----
            suma_estandar = datos["Estandar"].sum()

            if suma_defectos == 0 and suma_estandar == 0:
                labels_def[i].config(text="")
                labels_est[i].config(text="")
            elif suma_defectos == 0 and suma_estandar != 0:
                labels_def[i].config(text="0")
                labels_est[i].config(text=suma_estandar)
            else:
                labels_def[i].config(text=suma_defectos)
                labels_est[i].config(text=suma_estandar)

            # ---- FPY ----
            if suma_estandar > 0:
                fpy = (1 - (suma_defectos / suma_estandar)) * 100
            else:
                fpy = 0

            lbl = labels_fpy[i]

            valor = float(fpy)

            if valor.is_integer():
                texto = f"{valor:.0f}%"
            else:
                texto = f"{valor:.2f}%"

            # ---- Colores según FPY ----
            if fpy == 0:
                lbl.config(text="", fg="black",
                           bg=color_1, bd=0, relief="flat")
            elif fpy >= fpy_model_max:
                lbl.config(fg="green", bg="#D9F2D0",
                           text=texto, bd=.5, relief="ridge", justify="center")
            elif fpy < fpy_model_min:
                lbl.config(fg="red", bg="#FFCCCC",
                           text=texto, bd=.5, relief="ridge", justify="center")
            elif fpy >= fpy_model_min and fpy < fpy_model_max:
                lbl.config(fg="#E7601D", bg="#FBE7DD",
                           text=texto, bd=.5, relief="ridge", justify="center")
        root.after(300, calcular_defectos_totales)

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")


def calcular_defectos_totales():
    """Función para calcular los defectos y FPY"""
    try:
        data_logfile = pd.read_csv(csv_file, encoding='latin1')
        data_logfile['Fecha/Hora'] = pd.to_datetime(
            data_logfile['Fecha/Hora'], format='%d/%m/%Y %H:%M:%S')

        # ---- Obtener modelos desde settings ----
        models = [settings_part_numbers(f"Part#{i}") for i in range(1, 13)]

        # ---- Listas de labels ----
        labels_def = [label_115, label_116, label_117, label_118, label_119, label_120,
                      label_121, label_122, label_123, label_124, label_125, label_126]

        labels_est = [label_128, label_129, label_130, label_131, label_132, label_133,
                      label_134, label_135, label_136, label_137, label_138, label_139]

        labels_fpy = [label_102, label_103, label_104, label_105, label_106, label_107,
                      label_108, label_109, label_110, label_111, label_112, label_113]

        # Valor mínimo de FPY configurable
        fpy_model_min = int(settings_limits("FPY_MODEL_min"))
        fpy_model_max = int(settings_limits("FPY_MODEL_max"))

        # ---- Fecha seleccionada ----
        date = pd.to_datetime(label_179.cget(
            "text"), format='%d/%m/%Y %H:%M:%S')

        # ---- Horas ----
        hora_inicio_1 = pd.to_datetime(f"{hora_inicial.get()}:{minuto_inicial.get()} {periodo_inicial.get()}",
                                       format='%I:%M %p').time()
        hora_fin_1 = pd.to_datetime(f"{hora_final.get()}:{minuto_final.get()} {periodo_final.get()}",
                                    format='%I:%M %p').time()

        # ==============================================================
        #   CALCULAR PARA CADA MODELO
        # ==============================================================
        for i, modelo in enumerate(models):

            # Filtrar por modelo y fecha
            filtro_modelo_fecha = (data_logfile["Modelo"] == modelo) & \
                                  (data_logfile["Fecha/Hora"].dt.date ==
                                   date.date())

            # Filtrar por hora
            filtro_horas = data_logfile["Fecha/Hora"].dt.time.between(
                hora_inicio_1, hora_fin_1)

            datos = data_logfile[filtro_modelo_fecha & filtro_horas]

            # ---- DEFECTOS ----
            suma_defectos = datos["Defectos"].sum()

            # ---- ESTÁNDAR ----
            suma_estandar = datos["Estandar"].sum()

            if suma_defectos == 0 and suma_estandar == 0:
                labels_def[i].config(text="")
                labels_est[i].config(text="")
            elif suma_defectos == 0 and suma_estandar != 0:
                labels_def[i].config(text="0")
                labels_est[i].config(text=suma_estandar)
            else:
                labels_def[i].config(text=suma_defectos)
                labels_est[i].config(text=suma_estandar)

            # ---- FPY ----
            if suma_estandar > 0:
                fpy = (1 - (suma_defectos / suma_estandar)) * 100
            else:
                fpy = 0

            lbl = labels_fpy[i]

            valor = float(fpy)

            if valor.is_integer():
                texto = f"{valor:.0f}%"
            else:
                texto = f"{valor:.2f}%"

            # ---- Colores según FPY ----
            if fpy == 0:
                lbl.config(text="", fg="black",
                           bg=color_1, bd=0, relief="flat")
            elif fpy >= fpy_model_max:
                lbl.config(fg="green", bg="#D9F2D0",
                           text=texto, bd=.5, relief="ridge", justify="center")
            elif fpy < fpy_model_min:
                lbl.config(fg="red", bg="#FFCCCC",
                           text=texto, bd=.5, relief="ridge", justify="center")
            elif fpy >= fpy_model_min and fpy < fpy_model_max:
                lbl.config(fg="#E7601D", bg="#FBE7DD",
                           text=texto, bd=.5, relief="ridge", justify="center")

        root.after(100,  calcular_top_defecto_por_modelo)

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")


andon_true = settings_root("ANDON")
# Convertir a booleano
andon_true = True if str(andon_true).lower() == "true" else False


def calcular_top_defecto_por_modelo():
    """Función para calcular top defectos"""
    try:
        # --- Leer CSV ---
        df, defect_names = cargar_datos_cache()
        df.columns = df.columns.str.strip()

        df["Fecha/Hora"] = pd.to_datetime(
            df["Fecha/Hora"], format="%d/%m/%Y %H:%M:%S"
        )

        # --- Leer defects.ini ---
        defect_names = []
        with open("C:/Registro_defectos_SEHO/defects.ini", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "=" not in line:
                    continue
                _, value = line.split("=", 1)
                defect_names.append(value.strip())

        # --- Modelos ---
        models = [settings_part_numbers(f"Part#{i}") for i in range(1, 13)]

        # --- Labels ---
        labels_top = [
            label_141, label_142, label_143, label_144, label_145, label_146,
            label_147, label_148, label_149, label_150, label_151, label_152
        ]

        labels_pct = [
            label_167, label_168, label_169, label_170, label_171, label_172,
            label_173, label_174, label_175, label_176, label_177, label_178
        ]

        labels_cantidad = [
            label_154, label_155, label_156, label_157, label_158, label_159,
            label_160, label_161, label_162, label_163, label_164, label_165
        ]

        # --- Fecha ---
        date = pd.to_datetime(
            label_179.cget("text"),
            format="%d/%m/%Y %H:%M:%S"
        )

        # --- Horas ---
        hora_inicio = pd.to_datetime(
            f"{hora_inicial.get()}:{minuto_inicial.get()} {periodo_inicial.get()}",
            format="%I:%M %p"
        ).time()

        hora_fin = pd.to_datetime(
            f"{hora_final.get()}:{minuto_final.get()} {periodo_final.get()}",
            format="%I:%M %p"
        ).time()

        # ==================================================
        #   TOP DEFECTO + PORCENTAJE
        # ==================================================
        for i, modelo in enumerate(models):

            filtro = (
                (df["Modelo"] == modelo) &
                (df["Fecha/Hora"].dt.date == date.date()) &
                (df["Fecha/Hora"].dt.time.between(hora_inicio, hora_fin))
            )

            datos = df.loc[filtro, defect_names]

            if datos.empty or datos.sum().sum() == 0:
                labels_top[i].config(text="")
                labels_pct[i].config(text="")
                labels_cantidad[i].config(text="")
                continue

            suma_defectos = datos.sum()

            top_defecto = suma_defectos.idxmax()
            top_valor = int(suma_defectos.max())

            total_defectos = suma_defectos.sum()

            porcentaje = (top_valor / total_defectos) * 100

            # Formato del porcentaje
            if porcentaje.is_integer():
                texto_pct = f"{porcentaje:.0f}%"
            else:
                texto_pct = f"{porcentaje:.2f}%"

            # --- Labels ---
            labels_top[i].config(text=f"{top_defecto}")

            labels_cantidad[i].config(text=f"{top_valor}")

            labels_pct[i].config(text=texto_pct)

        root.after(100, fpy_andon)
        entry_30.focus()

    except Exception as e:
        messagebox.showerror("Error", f"Error TOP defecto: {e}")

# ------------------------------------- ANDON -------------------------------------------------------------------------


com_andon = settings_root("COM_ANDON")


