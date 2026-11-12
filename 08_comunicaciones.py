def conectar_puerto_serial_rb():
    """Función para conectar puerto de Raspberry pi pico"""
    if not andon_true:
        return None
    try:
        puerto_serial_rb = serial.Serial(
            com_andon, baudrate=115200, stopbits=1, parity='N', bytesize=8, timeout=1)
        time.sleep(2)
        return puerto_serial_rb
    except serial.SerialException as e:
        messagebox.showerror(
            "Error de conexión con sistema ANDON", f"{e}")
        cerrar_ventana()

        return None


puerto_serial = conectar_puerto_serial_rb()


def enviar_comando_rb(comando):
    """Función para enviar comando a Raspberry pi pico"""
    global puerto_serial

    if not andon_true:
        return

    if puerto_serial and puerto_serial.is_open:
        try:
            puerto_serial.write(comando)
        except serial.SerialException as e:
            messagebox.showerror(
                "Error de comunicación con sistema ANDON", f"{e}")
    else:
        reconectar()


def reconectar():
    """Función para reconectar Raspberry en caso de perdida de conexión"""
    global puerto_serial

    if not andon_true:
        return

    try:
        if puerto_serial and puerto_serial.is_open:
            puerto_serial.close()
    except:
        pass

    puerto_serial = conectar_puerto_serial_rb()


def fpy_andon():
    """Función para encender ANDON de acuerdo al FPY más bajo válido"""
    if not andon_true:
        return

    fpy_model_min = float(settings_limits("FPY_MODEL_min"))
    fpy_model_max = float(settings_limits("FPY_MODEL_max"))

    labels_fpy = [label_89, label_90, label_91, label_92, label_93,
                  label_94, label_95, label_96, label_97, label_98, label_99, label_100]

    valores_validos = []

    for lbl in labels_fpy:
        if lbl is None:
            continue

        texto = lbl.cget("text").strip().replace("%", "")

        if texto == "":
            continue  # 🔹 Vacío = ignorar por ahora

        try:
            numero = float(texto)
            valores_validos.append(numero)
        except ValueError:
            continue

    # 🔴 CASO 1: Todos están vacíos
    if not valores_validos:
        enviar_comando_rb(b"A\r")
        return

    # 🔹 Evaluar solo los que tienen dato
    valor_minimo = min(valores_validos)

    # ---- Decisión ANDON ----
    if valor_minimo >= fpy_model_max:
        enviar_comando_rb(b"A\r")
    elif valor_minimo < fpy_model_min:
        enviar_comando_rb(b"C\r")
    elif valor_minimo >= fpy_model_min and valor_minimo < fpy_model_max:
        enviar_comando_rb(b"B\r")


def soporte_andon(comando, ventana_support=None):
    """Envía comando al sistema ANDON"""
    if not andon_true:
        messagebox.showinfo("ANDON", "Sistema ANDON DESACTIVADO")

        if ventana_support is not None:
            ventana_support.destroy()   # 🔥 Cierra la ventana support

        return

    if comando == "X":
        root.after(200, fpy_andon)
    else:
        mensaje = f"{comando}\r".encode()
        enviar_comando_rb(mensaje)


# ------------------------------------- GUI ---------------------------------------------------------------------------
