defect1 = settings_defects("defect1")
defect2 = settings_defects("defect2")
defect3 = settings_defects("defect3")
defect4 = settings_defects("defect4")
defect5 = settings_defects("defect5")
defect6 = settings_defects("defect6")
defect7 = settings_defects("defect7")
defect8 = settings_defects("defect8")
defect9 = settings_defects("defect9")
defect10 = settings_defects("defect10")
defect11 = settings_defects("defect11")
defect12 = settings_defects("defect12")
defect13 = settings_defects("defect13")
defect14 = settings_defects("defect14")
defect15 = settings_defects("defect15")
defect16 = settings_defects("defect16")
defect17 = settings_defects("defect17")
defect18 = settings_defects("defect18")
defect19 = settings_defects("defect19")
defect20 = settings_defects("defect20")
defect21 = settings_defects("defect21")
defect22 = settings_defects("defect22")
defect23 = settings_defects("defect23")
defect24 = settings_defects("defect24")
defect25 = settings_defects("defect25")
defect26 = settings_defects("defect26")
defect27 = settings_defects("defect27")
defect28 = settings_defects("defect28")
defect29 = settings_defects("defect29")
defect30 = settings_defects("defect30")
# Nuevos defectos disponibles 23/03/2026
defect31 = settings_defects("defect31")
defect32 = settings_defects("defect32")
defect33 = settings_defects("defect33")
defect34 = settings_defects("defect34")
defect35 = settings_defects("defect35")
# Mumero de partes
part_1 = settings_part_numbers("Part#1")
part_2 = settings_part_numbers("Part#2")
part_3 = settings_part_numbers("Part#3")
part_4 = settings_part_numbers("Part#4")
part_5 = settings_part_numbers("Part#5")
part_6 = settings_part_numbers("Part#6")
part_7 = settings_part_numbers("Part#7")
part_8 = settings_part_numbers("Part#8")
part_9 = settings_part_numbers("Part#9")
part_10 = settings_part_numbers("Part#10")
part_11 = settings_part_numbers("Part#11")
part_12 = settings_part_numbers("Part#12")
# Colores:
color_1 = "#F2F2F2"
color_2 = "#A6A6A6"
color_3 = "#D9D9D9"
# ------------------------------------- LogFile -----------------------------------------------------------------------

# Crear csv_file si no existe y actualizar encabezado
encabezados = [
    'Modelo', 'No. Parte', 'No. Orden', 'No. Operador', 'Pallet', 'Defectos', 'Estandar', 'Fecha/Hora', 'FPY',
    'Wave1', 'Wave2', 'Flux', 'Conveyor',
    defect1, defect2, defect3, defect4, defect5, defect6, defect7, defect8,
    defect9, defect10, defect11, defect12, defect13, defect14, defect15,
    defect16, defect17, defect18, defect19, defect20, defect21, defect22,
    defect23, defect24, defect25, defect26, defect27, defect28, defect29, defect30, defect31, defect32,
    defect33, defect34, defect35
]


def asegurar_csv_con_encabezado(csv_file, encabezado_nuevo):
    """Crea el CSV si no existe y actualiza el encabezado si cambió"""

    if not os.path.isfile(csv_file):
        os.makedirs(os.path.dirname(csv_file), exist_ok=True)

        with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezado_nuevo)
        return

    # Leer todo el archivo existente
    with open(csv_file, mode='r', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        filas = list(reader)

    if not filas:
        with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezado_nuevo)
        return

    encabezado_actual = filas[0]

    if encabezado_actual != encabezado_nuevo:
        datos = filas[1:]  # conservar registros existentes

        with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezado_nuevo)
            writer.writerows(datos)


asegurar_csv_con_encabezado(csv_file, encabezados)

# Crear csv_file2 si no existe y actualizar encabezado


def asegurar_csv2_con_encabezado(csv_file2, encabezado_nuevo):
    """Crea el CSV si no existe y actualiza el encabezado si cambió"""

    if not os.path.isfile(csv_file2):
        os.makedirs(os.path.dirname(csv_file2), exist_ok=True)

        with open(csv_file2, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezado_nuevo)
        return

    # Leer todo el archivo existente
    with open(csv_file2, mode='r', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        filas = list(reader)

    if not filas:
        with open(csv_file2, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezado_nuevo)
        return

    encabezado_actual = filas[0]

    if encabezado_actual != encabezado_nuevo:

        datos = filas[1:]  # conservar registros existentes

        with open(csv_file2, mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(encabezado_nuevo)
            writer.writerows(datos)


asegurar_csv2_con_encabezado(csv_file2, encabezados)


def obtener_datos_produccion_modelo(modelo):
    """Obtiene los datos confirmados de las etiquetas del modelo seleccionado."""
    modelos = [label_50, label_51, label_52, label_53, label_54, label_55,
               label_56, label_57, label_58, label_59, label_60, label_61]
    partes = [label_186, label_187, label_188, label_189, label_190, label_191,
              label_192, label_193, label_194, label_195, label_196, label_197]
    ordenes = [label_200, label_201, label_202, label_203, label_204, label_205,
               label_206, label_207, label_208, label_209, label_210, label_211]
    operadores = [label_213, label_214, label_215, label_216, label_217, label_218,
                  label_219, label_220, label_221, label_222, label_223, label_224]

    for etiqueta_modelo, parte, orden, operador in zip(modelos, partes, ordenes, operadores):
        if etiqueta_modelo.cget("text").strip() == modelo:
            return (parte.cget("text").strip(), orden.cget("text").strip(),
                    operador.cget("text").strip())
    return "", "", ""


def datos_produccion_validos(parte, orden, operador):
    """Verifica los tres datos antes de permitir un registro."""
    return (len(parte) == 6 and parte.isascii() and parte.isdigit()
            and len(orden) == 9 and orden[:2].isascii()
            and orden[:2].isalpha() and orden[:2].isupper()
            and 1 <= len(operador) <= 4 and operador.isascii()
            and operador.isdigit())


def guardar_datos(event=None):
    """Función para guardar registros en csv de forma segura"""
    global guardando_en_progreso

    # Si ya se está ejecutando un guardado, ignorar nuevas peticiones
    if guardando_en_progreso:
        return

    try:
        guardando_en_progreso = True

        pallet = entry_30.get().strip() or "0"

        # VALIDACIÓN AQUÍ 👇
        if not pallet.isdigit():
            messagebox.showwarning(
                "Dato inválido", "El número de pallet debe ser un número entero.")
            entry_30.delete(0, tk.END)
            guardando_en_progreso = False
            return

        modelo_actual = label_36.cget("text").strip()
        numero_parte, numero_orden, numero_operador = obtener_datos_produccion_modelo(
            modelo_actual)

        if not modelo_actual or not datos_produccion_validos(
                numero_parte, numero_orden, numero_operador):
            messagebox.showwarning(
                "Datos de producción incompletos",
                f"No se puede registrar el pallet del modelo "
                f"{modelo_actual or '(sin modelo)'}\n"
                "Debe confirmar No. Parte, No. Orden y No. Operador "
                "en la columna correspondiente."
            )
            return

        # 1. Recolectar datos de forma limpia
        # Usamos una lista para que sea más fácil de manejar y leer
        datos = [
            modelo_actual,  # Modelo
            numero_parte,  # No. Parte
            numero_orden,  # No. Orden
            numero_operador,  # No. Operador
            entry_30.get().strip() or "0",  # Pallet
            label_34.cget("text").strip() or "0",  # Defectos
            label_38.cget("text").strip() or "0",  # Estandar
            label_179.cget("text").strip() or "0",  # Fecha/Hora
            label_40.cget("text").strip() or "0",  # FPY
            label_42.cget("text").strip() or "0",  # Wave 1
            label_44.cget("text").strip() or "0",  # Wave 2
            label_46.cget("text").strip() or "0",  # Flux
            label_48.cget("text").strip() or "0"  # Conveyor
        ]

        # Agregar los 30 defectos de los entries (entry_0 a entry_35)
        entries_defectos = [
            entry_0, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9,
            entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18, entry_19,
            entry_20, entry_21, entry_22, entry_23, entry_24, entry_25, entry_26, entry_27, entry_28, entry_29, entry_31,
            entry_32, entry_33, entry_34, entry_35
        ]

        for entry in entries_defectos:
            datos.append(entry.get().strip() or "0")

        # 2. Validación: Verificar que el Pallet y Modelo no estén vacíos
        # (dat1 y dat2 en tu código original)
        if not datos[0] or datos[4] == "0" or datos[4] == "":
            messagebox.showwarning(
                "Atención", "El número de Pallet es obligatorio.")
            guardando_en_progreso = False
            return

        # Avisar cada vez que se registra un pallet cuyo mantenimiento está vencido.
        alerta_mantenimiento(pallet)

        # 3. Escritura en archivos (Usando context manager 'with' para cierre automático)
        archivos = [csv_file, csv_file2]
        for ruta in archivos:
            with open(ruta, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(datos)

        # Avisar también cuando el registro actual alcanza exactamente el límite.
        alerta_mantenimiento(pallet, despues_de_guardar=True)

        # 4. Limpieza de la interfaz
        for entry in entries_defectos:
            entry.delete(0, tk.END)

        entry_30.delete(0, tk.END)  # Limpiar Pallet
        label_34.config(text="")  # Limpiar label Defectos

        # 5. Forzar actualización de caché y cálculos
        # Esto asegura que la tabla que acabas de hacer vea el dato nuevo de inmediato
        if 'actualizar_cache' in globals():  # Si tienes una función para refrescar caché
            cargar_datos_cache()

        root.after(300, calcular_defectos)

        # Pequeño mensaje de confirmación (opcional)
        # print(f"Datos guardados correctamente: Pallet {datos[1]}")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar: {e}")
    finally:
        # Importante: liberar el bloqueo siempre, ocurra error o no
        guardando_en_progreso = False


data_logfile = pd.read_csv(csv_file, encoding='latin1')
data_register = pd.read_csv(csv_file2, encoding='latin1')


