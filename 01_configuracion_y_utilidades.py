def root_scale():
    """Ajusta las fuentes de la interfaz según la resolución."""

    # Resolución de referencia: 1920 x 1080
    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()

    escala = min(ancho / 1920, alto / 1080)

    def aplicar_fuente(widgets, tamaño, **opciones):
        """Configura varios widgets con la misma fuente y opciones."""
        fuente = ("Arial", max(1, int(tamaño * escala)), "bold")

        for widget in widgets:
            widget.config(font=fuente, **opciones)

    def labels(*indices):
        """Obtiene etiquetas existentes por su numeración."""
        return [globals()[f"label_{i}"] for i in indices]

    def entries(*indices):
        return [globals()[f"entry_{i}"] for i in indices]

    def buttons(*indices):
        return [globals()[f"button_{i}"] for i in indices]

    # --------------------------------------------------
    # TÍTULOS Y DEFECTOS
    # --------------------------------------------------

    aplicar_fuente(labels(0), 40)
    aplicar_fuente(labels(1), 16)

    aplicar_fuente(
        labels(*range(2, 32), *range(181, 186))
        + entries(*range(0, 30), *range(31, 36)),
        18
    )

    # --------------------------------------------------
    # INFORMACIÓN DEL PALLET
    # --------------------------------------------------

    aplicar_fuente(labels(32), 10)

    aplicar_fuente(
        labels(33, 34, 35, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48),
        16,
        bd=0.5,
        relief="ridge"
    )

    aplicar_fuente(
        labels(36),
        12,
        bd=0.5,
        relief="ridge"
    )

    aplicar_fuente(labels(49), 14)

    # --------------------------------------------------
    # NÚMEROS DE PARTE
    # --------------------------------------------------

    aplicar_fuente(
        labels(*range(50, 62)),
        14,
        bd=0.5,
        relief="ridge",
        bg="#44B3E1"
    )

    # --------------------------------------------------
    # BLOQUE PRINCIPAL
    # --------------------------------------------------

    aplicar_fuente(labels(62, 88), 13)

    aplicar_fuente(
        labels(
            *range(63, 75),
            *range(76, 88),
            *range(89, 101)
        ),
        20
    )

    # --------------------------------------------------
    # SEGUNDO BLOQUE
    # --------------------------------------------------

    aplicar_fuente(labels(101, 114, 127), 11)

    aplicar_fuente(
        labels(
            *range(102, 114),
            *range(115, 127),
            *range(128, 140)
        ),
        14
    )

    # --------------------------------------------------
    # TOP DEFECTOS
    # --------------------------------------------------

    aplicar_fuente(labels(140, 153, 166), 10)

    aplicar_fuente(labels(*range(141, 153)), 8)
    aplicar_fuente(labels(*range(154, 166)), 10)
    aplicar_fuente(labels(*range(167, 179)), 10)

    # --------------------------------------------------
    # INFORMACIÓN GENERAL
    # --------------------------------------------------

    aplicar_fuente(labels(179), 12)
    aplicar_fuente(labels(180), 8)

    # Número de parte, orden y operador
    aplicar_fuente(
        labels(
            *range(186, 198),
            *range(199, 212),
            *range(213, 225)
        ),
        12
    )

    aplicar_fuente(labels(198, 212), 11)

    # --------------------------------------------------
    # ENTRIES Y SPINBOX
    # --------------------------------------------------

    aplicar_fuente(entries(30), 28)

    aplicar_fuente(
        [globals()[f"spinbox_{i}"] for i in range(6)],
        14
    )

    # --------------------------------------------------
    # BOTONES
    # --------------------------------------------------

    aplicar_fuente(
        buttons(*range(0, 12), *range(18, 30)),
        12
    )

    aplicar_fuente(buttons(*range(12, 17)), 10)
    aplicar_fuente(buttons(17), 10)


def suma_defectos(*args):
    """Calcula el total de defectos registrados."""

    entradas = [
        globals()[f"entry_{i}"]
        for i in list(range(30)) + list(range(31, 36))
    ]

    total = 0

    for entry in entradas:
        valor = entry.get().strip()

        if valor.isdecimal():
            total += int(valor)

    label_34.config(text=str(total))


escribio = False


def buscar_pallets():
    """Función buscar pallets."""
    pallet_buscado = entry_30.get()
    encontrado = False
    with open(settings_root("Parameters"), newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[0] == pallet_buscado:
                label_36.config(text=fila[1])
                label_38.config(text=fila[2])
                label_42.config(text=fila[3])
                label_44.config(text=fila[4])
                label_46.config(text=fila[5])
                label_48.config(text=fila[6])

                encontrado = True
                break

        if not encontrado:
            label_36.config(text="")
            label_38.config(text="")
            label_42.config(text="")
            label_44.config(text="")
            label_46.config(text="")
            label_48.config(text="")


def fpy_pallets(*args):
    """Función calcular fpy de pallets"""
    defectos_pallet = label_34.cget("text").strip() or "0"
    estandar_pallet = label_38.cget("text").strip() or "0"

    defectos_pallet = int(defectos_pallet)
    estandar_pallet = int(estandar_pallet)

    fpy = ((estandar_pallet - defectos_pallet) / estandar_pallet) * \
        100 if estandar_pallet > 0 else 0

    fpy_por_pallet_min = settings_limits("FPY_PALLET_min")
    fpy_por_pallet_min = int(fpy_por_pallet_min)

    fpy_por_pallet_max = settings_limits("FPY_PALLET_max")
    fpy_por_pallet_max = int(fpy_por_pallet_max)

    if fpy == 0:
        label_40.config(fg="black", bg="#D0D0D0")
        label_40.config(text="")
    elif fpy > fpy_por_pallet_max:
        label_40.config(fg="green", bg="#D9F2D0")
        label_40.config(text=f"{fpy:.2f}%")
    elif fpy < fpy_por_pallet_min:
        label_40.config(fg="red", bg="#FFCCCC")
        label_40.config(text=f"{fpy:.2f}%")
    elif fpy >= fpy_por_pallet_min and fpy <= fpy_por_pallet_max:
        label_40.config(fg="#E7601D", bg="#FBE7DD")
        label_40.config(text=f"{fpy:.2f}%")


def escribir_pallet(event):
    global escribio
    escribio = True
    buscar_pallets()
    fpy_pallets()


def regreso_pallet(event):
    global escribio

    if escribio:
        fpy_pallets()
        escribio = False


def actualizar_fecha_hora():
    """Función para mostrar fecha y hora"""
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # Actualizar el texto del Label
    label_179.config(text=fecha_hora_actual)
    # Llamar a esta función de nuevo después de 1000 ms (1 segundo)
    root.after(1000, actualizar_fecha_hora)


def detectar_codificacion(archivo):
    """Detecta la codificación del archivo"""
    with open(archivo, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def reset(busqueda, reemplazo):
    """
    Modifica el archivo CSV predefinido reemplazando valores en la primera columna
    """
    try:
        # Detectar codificación primero
        try:
            encoding = detectar_codificacion(settings_root("Registro"))
        except Exception as e:
            encoding = 'latin-1'  # Codificación de respaldo

        # Leer el archivo CSV con la codificación detectada
        df = pd.read_csv(settings_root("Registro"), encoding=encoding)

        # Verificar si la primera columna existe
        if len(df.columns) == 0:
            messagebox.showerror(
                "Error", "El archivo CSV no tiene columnas válidas")
            return 0

        primera_col = df.columns[0] if isinstance(df.columns, pd.Index) else 0

        # Contar ocurrencias antes del cambio
        cambios = (df[primera_col] == busqueda).sum()

        if cambios == 0:
            messagebox.showinfo(
                "Información", f"No se encontró '{busqueda}' en el archivo")
            return 0

        # Realizar el reemplazo
        df[primera_col] = df[primera_col].replace(busqueda, reemplazo)

        # Guardar el archivo (sobrescribe el original)
        try:
            df.to_csv(settings_root("Registro"),
                      index=False, encoding=encoding)
        except:
            # Si falla, intentar con UTF-8
            df.to_csv(settings_root("Registro"), index=False, encoding='utf-8')

        root.after(300, calcular_defectos)
        return cambios

    except FileNotFoundError:
        messagebox.showerror(
            "Error", f"No se encontró el archivo: {settings_root('Registro')}")
        return 0
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema: {str(e)}")
        return 0


