

import tkinter as tk
from PIL import Image, ImageTk
import csv
from datetime import datetime
import pandas as pd
import pyautogui
from tkinter import ttk, messagebox
import chardet
import os
import time
# -------------------------------------Funciones o definiciones--------------------------------------------------------


def inicio():
    entry_pallet.insert(0, 1000)
    delay_ms = 300
    time.sleep(delay_ms / 1000)
    pyautogui.press("enter")
    pyautogui.press("enter")
    eliminar_filas_setup()
    eliminar_filas_setup_2()


def fun_buscar_fpy_pallets(event):
    buscar_pallet(event)
    fpy_pallets(event)


def fpy_pallets(*args):
    defectos_pallets = int(entry_defectos_con.get()
                           ) if entry_defectos_con.get() else 0
    estandar = int(entry_estandar_con.get()) if entry_estandar_con.get() else 0

    fpy = ((estandar - defectos_pallets) / estandar) * \
        100 if estandar > 0 else 0

    entry_fpy_pallet_con.delete(0, tk.END)
    entry_fpy_pallet_con.insert(0, f"{fpy:.2f}%")

    fpy_por_pallet = obtener_configuracion("")
    fpy_por_pallet = int(fpy_por_pallet)

    if fpy == 0:
        entry_fpy_pallet_con.config(fg="black", bg="#AEAEAE")
    elif fpy > fpy_por_pallet:
        entry_fpy_pallet_con.config(fg="green")  # Verde
        entry_fpy_pallet_con.config(bg="#D9F2D0")
    elif fpy < fpy_por_pallet:
        entry_fpy_pallet_con.config(fg="red")  # Rojo
        entry_fpy_pallet_con.config(bg="#FFCCCC")
    else:
        entry_fpy_pallet_con.config(fg="#E7601D")  # Naranja
        entry_fpy_pallet_con.config(bg="#FBE7DD")


def cerrar_ventana():  # Función para cerrar ventana
    ventana.destroy()


def toggle_minimize(event=None):  # Funcion para minizar la ventana al presionar Escape
    ventana.iconify()


def on_restore(event=None):  # Función para maximizar la ventana a pantalla completa al restaurarla
    ventana.attributes("-fullscreen", True)


def obtener_configuracion(clave):
    try:
        with open("C:/Registro_defectos_SEHO/Program/SupportFiles/settings.ini", "r") as config:
            for linea in config:
                if linea.startswith(clave):
                    return linea.split("=")[1].strip()
    except FileNotFoundError:
        messagebox.showerror(
            "Error", "El archivo de configuración 'setting.txt' no fue encontrado.")
    except Exception as e:
        messagebox.showerror(
            "Error", f"Ocurrió un error al leer la configuración: {e}")
    return None


def buscar_pallet(event):
    pallet_buscado = entry_pallet.get()
    encontrado = False
    with open(obtener_configuracion("LogParameters"), newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if fila[0] == pallet_buscado:
                # Limpiar y actualizar las entradas con los valores de la fila
                entry_modelo_con.delete(0, tk.END)
                entry_modelo_con.insert(0, fila[1])

                entry_estandar_con.delete(0, tk.END)
                entry_estandar_con.insert(0, fila[2])

                entry_wave_1_con.delete(0, tk.END)
                entry_wave_1_con.insert(0, fila[3])

                entry_wave_2_con.delete(0, tk.END)
                entry_wave_2_con.insert(0, fila[4])

                entry_flux_con.delete(0, tk.END)
                entry_flux_con.insert(0, fila[5])

                entry_conveyor_con.delete(0, tk.END)
                entry_conveyor_con.insert(0, fila[6])

                encontrado = True
                break

        if not encontrado:
            # Si no se encuentra, mostrar "N/A" en las entradas
            entry_modelo_con.delete(0, tk.END)
            entry_modelo_con.insert(0, "")

            entry_estandar_con.delete(0, tk.END)
            entry_estandar_con.insert(0, "")

            entry_wave_1_con.delete(0, tk.END)
            entry_wave_1_con.insert(0, "")

            entry_wave_2_con.delete(0, tk.END)
            entry_wave_2_con.insert(0, "")

            entry_flux_con.delete(0, tk.END)
            entry_flux_con.insert(0, "")

            entry_conveyor_con.delete(0, tk.END)
            entry_conveyor_con.insert(0, "")


def actualizar_fecha_hora():
    # Obtener la fecha y la hora actuales
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    hora_actual = datetime.now().strftime("%H:%M:%S")

    # Mostrar la fecha y la hora en las entradas
    entry_fecha_con.delete(0, tk.END)
    entry_fecha_con.insert(0, fecha_actual)

    entry_hora_con.delete(0, tk.END)
    entry_hora_con.insert(0, hora_actual)

    # Llamar a la función cada segundo para mantener la hora actualizada
    ventana.after(1000, actualizar_fecha_hora)


def ajustar_escala():  # Funcion para ajustar escala de ventana
    # Obtener el tamaño de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular el factor de escala basado en una resolución de referencia (1920x1080)
    escala_x = pantalla_ancho / 1920
    escala_y = pantalla_alto / 1080
    escala = min(escala_x, escala_y)
    frame.config(padx=1 * escala, pady=1 * escala)
    frame2.config(padx=1 * escala, pady=1 * escala)

    # Ajustar el tamaño de la fuente
    fuente_8 = int(8 * escala)
    # fuente_10 = int(10 * escala)
    fuente_12 = int(12 * escala)
    fuente_14 = int(14 * escala)
    fuente_16 = int(16 * escala)
    fuente_20 = int(20 * escala)
    fuente_22 = int(22 * escala)
    fuente_30 = int(30 * escala)
    fuente_50 = int(50 * escala)
    # ------------
    label_numero_pallet.config(font=("Arial", fuente_20, "bold"))
    entry_pallet.config(font=("Arial", fuente_30, "bold"))

    # ------------
    label_titulo.config(font=("Arial", fuente_50, "bold"))
    label_titulo_defectos.config(font=("Arial", fuente_14, "bold"))
    # ----------- Defectos
    label_falta_de_soldadura.config(font=("Arial", fuente_16, "bold"))
    entry_falta_de_soldadura.config(font=("Arial", fuente_16, "bold"))
    label_exceso_de_soldadura.config(font=("Arial", fuente_16, "bold"))
    entry_exceso_de_soldadura.config(font=("Arial", fuente_16, "bold"))
    label_cortos.config(font=("Arial", fuente_16, "bold"))
    entry_cortos.config(font=("Arial", fuente_16, "bold"))
    label_falta_de_housing.config(font=("Arial", fuente_16, "bold"))
    entry_falta_de_housing.config(font=("Arial", fuente_16, "bold"))
    label_com_smt_dañado.config(font=("Arial", fuente_16, "bold"))
    entry_com_smt_dañado.config(font=("Arial", fuente_16, "bold"))
    label_falta_comp_smt.config(font=("Arial", fuente_16, "bold"))
    entry_falta_comp_smt.config(font=("Arial", fuente_16, "bold"))
    label_falta_conector.config(font=("Arial", fuente_16, "bold"))
    entry_falta_conector.config(font=("Arial", fuente_16, "bold"))
    label_housing_dañado.config(font=("Arial", fuente_16, "bold"))
    entry_housing_dañado.config(font=("Arial", fuente_16, "bold"))
    label_com_tht_dañado.config(font=("Arial", fuente_16, "bold"))
    entry_com_tht_dañado.config(font=("Arial", fuente_16, "bold"))
    label_falta_comp_tht.config(font=("Arial", fuente_16, "bold"))
    entry_falta_comp_tht.config(font=("Arial", fuente_16, "bold"))
    label_conector_levantado.config(font=("Arial", fuente_16, "bold"))
    entry_conector_levantado.config(font=("Arial", fuente_16, "bold"))
    label_housing_quemado.config(font=("Arial", fuente_16, "bold"))
    entry_housing_quemado.config(font=("Arial", fuente_16, "bold"))
    label_comp_smt_levantado.config(font=("Arial", fuente_16, "bold"))
    entry_comp_smt_levantado.config(font=("Arial", fuente_16, "bold"))
    label_comp_tht_levantado.config(font=("Arial", fuente_16, "bold"))
    entry_comp_tht_levantado.config(font=("Arial", fuente_16, "bold"))
    label_bola_soldadura.config(font=("Arial", fuente_16, "bold"))
    entry_bola_soldadura.config(font=("Arial", fuente_16, "bold"))
    label_cable_dañado.config(font=("Arial", fuente_16, "bold"))
    entry_cable_dañado.config(font=("Arial", fuente_16, "bold"))
    label_falta_cable.config(font=("Arial", fuente_16, "bold"))
    entry_falta_cable.config(font=("Arial", fuente_16, "bold"))
    label_cable_suelto.config(font=("Arial", fuente_16, "bold"))
    entry_cable_suelto.config(font=("Arial", fuente_16, "bold"))
    label_cable_quemado.config(font=("Arial", fuente_16, "bold"))
    entry_cable_quemado.config(font=("Arial", fuente_16, "bold"))
    label_terminales_iguales.config(font=("Arial", fuente_16, "bold"))
    entry_terminales_iguales.config(font=("Arial", fuente_16, "bold"))
    label_l1_dañado.config(font=("Arial", fuente_16, "bold"))
    entry_l1_dañado.config(font=("Arial", fuente_16, "bold"))
    label_pin_largo.config(font=("Arial", fuente_16, "bold"))
    entry_pin_largo.config(font=("Arial", fuente_16, "bold"))
    label_falta_evidencia_pin.config(font=("Arial", fuente_16, "bold"))
    entry_falta_evidencia_pin.config(font=("Arial", fuente_16, "bold"))
    label_cable_invertido.config(font=("Arial", fuente_16, "bold"))
    entry_cable_invertido.config(font=("Arial", fuente_16, "bold"))
    label_terminales_chuecas.config(font=("Arial", fuente_16, "bold"))
    entry_terminales_chuecas.config(font=("Arial", fuente_16, "bold"))

    # -----------
    label_defectos_ti.config(font=("Arial", fuente_14, "bold"))
    entry_defectos_con.config(font=("Arial", fuente_14, "bold"))
    label_modelo_ti.config(font=("Arial", fuente_14, "bold"))
    entry_modelo_con.config(font=("Arial", fuente_14, "bold"))
    label_estandar_ti.config(font=("Arial", fuente_14, "bold"))
    entry_estandar_con.config(font=("Arial", fuente_14, "bold"))
    label_fpy_pallet_ti.config(font=("Arial", fuente_14, "bold"))
    entry_fpy_pallet_con.config(font=("Arial", fuente_14, "bold"))
    entry_fecha_con.config(font=("Arial", fuente_12, "bold"))
    entry_hora_con.config(font=("Arial", fuente_12, "bold"))
    label_wave_1_ti.config(font=("Arial", fuente_14, "bold"))
    entry_wave_1_con.config(font=("Arial", fuente_14, "bold"))
    label_wave_2_ti.config(font=("Arial", fuente_14, "bold"))
    entry_wave_2_con.config(font=("Arial", fuente_14, "bold"))
    label_flux_ti.config(font=("Arial", fuente_14, "bold"))
    entry_flux_con.config(font=("Arial", fuente_14, "bold"))
    label_conveyor_ti.config(font=("Arial", fuente_14, "bold"))
    entry_conveyor_con.config(font=("Arial", fuente_14, "bold"))
    # -----------
    label_lm.config(font=("Arial", fuente_16, "bold"))
    label_rz.config(font=("Arial", fuente_16, "bold"))
    label_ROUTER.config(font=("Arial", fuente_16, "bold"))
    label_pr20.config(font=("Arial", fuente_16, "bold"))
    label_fa08.config(font=("Arial", fuente_16, "bold"))
    label_HLA.config(font=("Arial", fuente_16, "bold"))
    label_BGA200.config(font=("Arial", fuente_16, "bold"))
    label_FSA135.config(font=("Arial", fuente_16, "bold"))
    # label_DC.config(font=("Arial", fuente_16, "bold"))
    label_dc_i.config(font=("Arial", fuente_16, "bold"))
    label_locus.config(font=("Arial", fuente_16, "bold"))
    # -----------------Frame 2 row1
    label_horario.config(font=("Arial", fuente_14, "bold"))
    Hora_inicio.config(font=("Arial", fuente_12, "bold"))
    Minuto_inicio.config(font=("Arial", fuente_12, "bold"))
    Periodo_inicio.config(font=("Arial", fuente_12, "bold"))
    Hora_final.config(font=("Arial", fuente_12, "bold"))
    Minuto_final.config(font=("Arial", fuente_12, "bold"))
    Periodo_Final.config(font=("Arial", fuente_12, "bold"))
    # -----------------Frame 2 row3
    label_defectos_2.config(font=("Arial", fuente_14, "bold"))
    entry_con_def_lm.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_rz.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_router.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_pr20.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_fa08.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_hla.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_bga200.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_fsa135.config(font=("Arial", fuente_20, "bold"))
    # entry_con_def_dc.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_dc_i.config(font=("Arial", fuente_20, "bold"))
    entry_con_def_locus.config(font=("Arial", fuente_20, "bold"))
    # -----------------Frame 2 row4
    label_producido.config(font=("Arial", fuente_14, "bold"))
    entry_con_estan_lm.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_rz.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_router.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_pr20.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_fa08.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_hla.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_bga200.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_fsa135.config(font=("Arial", fuente_20, "bold"))
    # entry_con_estan_dc.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_dc_i.config(font=("Arial", fuente_20, "bold"))
    entry_con_estan_locus.config(font=("Arial", fuente_20, "bold"))
    # -----------------Frame 2 row5
    label_Fpy.config(font=("Arial", fuente_20, "bold"))
    entry_fpy_lion.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_rz.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_router.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_pr20.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_fa08.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_hla.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_bga200.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_fsa135.config(font=("Arial", fuente_22, "bold"))
    # entry_fpy_dc.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_dc_i.config(font=("Arial", fuente_22, "bold"))
    entry_fpy_locus.config(font=("Arial", fuente_22, "bold"))
    # -----------------Frame 2 row6
    reset_lm.config(font=("Arial", fuente_12, "bold"))
    reset_rotozip.config(font=("Arial", fuente_12, "bold"))
    reset_router.config(font=("Arial", fuente_12, "bold"))
    reset_pr20.config(font=("Arial", fuente_12, "bold"))
    reset_fa08.config(font=("Arial", fuente_12, "bold"))
    reset_hla.config(font=("Arial", fuente_12, "bold"))
    reset_bga200.config(font=("Arial", fuente_12, "bold"))
    reset_fsa135.config(font=("Arial", fuente_12, "bold"))
    # reset_dc.config(font=("Arial", fuente_12, "bold"))
    reset_dci.config(font=("Arial", fuente_12, "bold"))
    reset_locus.config(font=("Arial", fuente_12, "bold"))
    # -----------------Frame 2 row7
    label_fpyTotal.config(font=("Arial", fuente_16, "bold"))
    # -----------------Frame 2 row8
    label_TopDefectos.config(font=("Arial", fuente_14, "bold"))
    # -----------------Frame 2 row9
    label_TotalDefectos.config(font=("Arial", fuente_14, "bold"))
    # -----------------Frame 2 row10
    label_PorDefectos.config(font=("Arial", fuente_14, "bold"))
    # -----------------Frame 2 row11
    label_By.config(font=("Arial", fuente_8, "bold"))
    boton_logfiletotal.config(font=("Arial", fuente_8, "bold"))
    boton_logfileregistro.config(font=("Arial", fuente_8, "bold"))
    boton_defectos.config(font=("Arial", fuente_8, "bold"))
    boton_parametros.config(font=("Arial", fuente_8, "bold"))


def actualizar_suma_defectos(*args):
    try:
        defecto_1 = int(entry_falta_de_soldadura.get()
                        ) if entry_falta_de_soldadura.get() else 0

        defecto_2 = int(entry_exceso_de_soldadura.get()
                        ) if entry_exceso_de_soldadura.get() else 0
        defecto_3 = int(entry_cortos.get()
                        ) if entry_cortos.get() else 0
        defecto_4 = int(entry_falta_de_housing.get()
                        ) if entry_falta_de_housing.get() else 0
        defecto_5 = int(entry_com_smt_dañado.get()
                        ) if entry_com_smt_dañado.get() else 0
        defecto_6 = int(entry_falta_comp_smt.get()
                        ) if entry_falta_comp_smt.get() else 0
        defecto_7 = int(entry_falta_conector.get()
                        ) if entry_falta_conector.get() else 0
        defecto_8 = int(entry_housing_dañado.get()
                        ) if entry_housing_dañado.get() else 0
        defecto_9 = int(entry_com_tht_dañado.get()
                        ) if entry_com_tht_dañado.get() else 0
        defecto_10 = int(entry_falta_comp_tht.get()
                         ) if entry_falta_comp_tht.get() else 0
        defecto_11 = int(entry_conector_levantado.get()
                         ) if entry_conector_levantado.get() else 0
        defecto_12 = int(entry_housing_quemado.get()
                         ) if entry_housing_quemado.get() else 0
        defecto_13 = int(entry_comp_smt_levantado.get()
                         ) if entry_comp_smt_levantado.get() else 0
        defecto_14 = int(entry_comp_tht_levantado.get()
                         ) if entry_comp_tht_levantado.get() else 0
        defecto_15 = int(entry_bola_soldadura.get()
                         ) if entry_bola_soldadura.get() else 0
        defecto_16 = int(entry_cable_dañado.get()
                         ) if entry_cable_dañado.get() else 0
        defecto_17 = int(entry_falta_cable.get()
                         ) if entry_falta_cable.get() else 0
        defecto_18 = int(entry_cable_suelto.get()
                         ) if entry_cable_suelto.get() else 0
        defecto_19 = int(entry_cable_quemado.get()
                         ) if entry_cable_quemado.get() else 0
        defecto_20 = int(entry_terminales_iguales.get()
                         ) if entry_terminales_iguales.get() else 0
        defecto_21 = int(entry_l1_dañado.get()) if entry_l1_dañado.get() else 0
        defecto_22 = int(entry_pin_largo.get()
                         ) if entry_pin_largo.get() else 0
        defecto_23 = int(entry_falta_evidencia_pin.get()
                         ) if entry_falta_evidencia_pin.get() else 0
        defecto_24 = int(entry_cable_invertido.get()
                         ) if entry_cable_invertido.get() else 0
        defecto_25 = int(entry_terminales_chuecas.get()
                         ) if entry_terminales_chuecas.get() else 0

        suma_defectos = defecto_1 + defecto_2 + defecto_3 + \
            defecto_4 + defecto_5 + defecto_6 + defecto_7 + defecto_8 + defecto_9 + \
            defecto_10 + defecto_11 + defecto_12 + defecto_13 + defecto_14 + defecto_15 + defecto_16 + \
            defecto_17 + defecto_18 + defecto_19 + \
            defecto_20 + defecto_21 + defecto_22 + defecto_23 + defecto_24 + defecto_25
        entry_defectos_con.delete(0, tk.END)
        entry_defectos_con.insert(0, suma_defectos)

    except ValueError:
        entry_defectos_con.delete(0, tk.END)
        entry_defectos_con.insert(0, "Error")


RUTA_CSV = obtener_configuracion("LogFileRegistro_csv")
RUTA_CSV_2 = obtener_configuracion("LogFileTotal_csv")


def detectar_codificacion(archivo):
    """Detecta la codificación del archivo"""
    with open(archivo, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def modificar_csv(busqueda, reemplazo):
    """
    Modifica el archivo CSV predefinido reemplazando valores en la primera columna
    """
    try:
        # Detectar codificación primero
        try:
            encoding = detectar_codificacion(RUTA_CSV)
        except Exception as e:
            encoding = 'latin-1'  # Codificación de respaldo

        # Leer el archivo CSV con la codificación detectada
        df = pd.read_csv(RUTA_CSV, encoding=encoding)

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
            df.to_csv(RUTA_CSV, index=False, encoding=encoding)
        except:
            # Si falla, intentar con UTF-8
            df.to_csv(RUTA_CSV, index=False, encoding='utf-8')
        inicio()
        return cambios

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo: {RUTA_CSV}")
        return 0
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema: {str(e)}")
        return 0


def eliminar_filas_setup():
    """
    Elimina todas las filas donde la primera columna contenga 'SetUp'
    """
    try:
        # Leer el archivo CSV (con manejo de codificación)
        try:
            df = pd.read_csv(RUTA_CSV, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(RUTA_CSV, encoding='latin-1')

        # Filas originales para comparación
        filas_originales = len(df)

        # Eliminar filas donde la primera columna sea 'SetUp'
        primera_col = df.columns[0] if isinstance(df.columns, pd.Index) else 0
        df = df[df[primera_col] != 'SetUp']

        # Filas después del filtro
        filas_eliminadas = filas_originales - len(df)

        if filas_eliminadas == 0:
            return 0

        # Guardar el archivo (manteniendo la codificación original)
        try:
            df.to_csv(RUTA_CSV, index=False, encoding='utf-8')
        except:
            df.to_csv(RUTA_CSV, index=False, encoding='latin-1')
        return filas_eliminadas

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo: {RUTA_CSV}")
        return 0
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema: {str(e)}")
        return 0


def eliminar_filas_setup_2():
    """
    Elimina todas las filas donde la primera columna contenga 'SetUp'
    """
    try:
        # Leer el archivo CSV (con manejo de codificación)
        try:
            df = pd.read_csv(RUTA_CSV_2, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(RUTA_CSV_2, encoding='latin-1')

        # Filas originales para comparación
        filas_originales = len(df)

        # Eliminar filas donde la primera columna sea 'SetUp'
        primera_col = df.columns[0] if isinstance(df.columns, pd.Index) else 0
        df = df[df[primera_col] != 'SetUp']

        # Filas después del filtro
        filas_eliminadas = filas_originales - len(df)

        if filas_eliminadas == 0:
            return 0

        # Guardar el archivo (manteniendo la codificación original)
        try:
            df.to_csv(RUTA_CSV_2, index=False, encoding='utf-8')
        except:
            df.to_csv(RUTA_CSV_2, index=False, encoding='latin-1')
        return filas_eliminadas

    except FileNotFoundError:
        messagebox.showerror(
            "Error", f"No se encontró el archivo: {RUTA_CSV_2}")
        return 0
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema: {str(e)}")
        return 0


# ----------Ventana LogFileTotal----------------------------------------------------------------
# Ruta del archivo CSV predeterminado
# Cambia esta ruta si es necesario
CSV_PATH = obtener_configuracion("LogFileTotal_csv")


def abrir_ventana_csv():
    """ Función que abre la ventana secundaria para editar el CSV """
    class CSVEditor:
        def __init__(self, root):
            self.root = root
            self.root.title("LogFile")

            def cerrar_root():
                root.destroy()
                inicio()
            root.protocol("WM_DELETE_WINDOW", cerrar_root)

            # Configura la ventana para que se abra en pantalla completa pero manteniendo los botones de cerrar y minimizar
            self.root.state('zoomed')  # Maximiza la ventana al abrir
            # También puedes definir un tamaño inicial si no se quiere pantalla completa
            self.root.geometry("900x500")
            self.root.attributes("-topmost", True)

            self.archivo_csv = CSV_PATH  # Cargar automáticamente desde la ruta
            self.df = None

            # Botones de carga y guardado
            btn_frame = tk.Frame(root)
            btn_frame.pack(fill="x", padx=10, pady=5)

            self.btn_guardar = tk.Button(
                btn_frame, text="Guardar Cambios", command=self.guardar_csv, state=tk.DISABLED)
            self.btn_guardar.pack(side="right", padx=5)

            # Frame para la tabla con scroll
            table_frame = tk.Frame(root)
            table_frame.pack(expand=True, fill="both")

            # Scrollbars
            self.scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
            self.scroll_y = tk.Scrollbar(table_frame, orient="vertical")

            self.tree = ttk.Treeview(
                table_frame, yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
            self.tree.grid(row=0, column=0, sticky="nsew")

            self.scroll_x.config(command=self.tree.xview)
            self.scroll_y.config(command=self.tree.yview)

            self.scroll_x.grid(row=1, column=0, sticky="ew")
            self.scroll_y.grid(row=0, column=1, sticky="ns")

            # Configurar el diseño para expandirse
            table_frame.grid_rowconfigure(0, weight=1)
            table_frame.grid_columnconfigure(0, weight=1)

            # Eventos
            # Editar con doble clic
            self.tree.bind("<Double-1>", self.editar_celda)
            # Clic derecho para menú
            self.tree.bind("<Button-3>", self.mostrar_menu)

            # Crear menú contextual
            self.menu_contextual = tk.Menu(self.root, tearoff=0)
            self.menu_contextual.add_command(
                label="Eliminar fila", command=self.eliminar_fila)

            # Aplicar estilo al encabezado
            style = ttk.Style()
            style.configure("Treeview.Heading", font=(
                "Arial", 10, "bold"), background="lightblue", foreground="black")
            # Color de fondo del encabezado
            self.tree.tag_configure("header", background="lightblue")

            # Cargar el CSV al abrir el programa
            if os.path.exists(self.archivo_csv):
                self.cargar_csv()
            else:
                messagebox.showerror(
                    "Error", f"No se encontró el archivo: {self.archivo_csv}", parent=self.root)

        def detectar_codificacion(self, archivo):
            """ Detecta la codificación del archivo CSV """
            with open(archivo, "rb") as f:
                result = chardet.detect(f.read())
            return result["encoding"]

        def cargar_csv(self):
            """ Carga el archivo CSV y lo muestra en la tabla en orden inverso """
            try:
                encoding_detectado = self.detectar_codificacion(
                    self.archivo_csv)
                self.df = pd.read_csv(
                    self.archivo_csv, encoding=encoding_detectado)

                self.df = pd.concat(
                    [self.df.iloc[:0], self.df.iloc[0:].iloc[::-1]], ignore_index=True)

                self.mostrar_datos()
                # Habilita el botón de guardar
                self.btn_guardar.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo cargar el archivo CSV.\n{str(e)}", parent=self.root)

        def mostrar_datos(self):
            """ Muestra los datos del DataFrame en el Treeview con encabezados de color """
            # Limpiar tabla
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = list(self.df.columns)
            self.tree["show"] = "headings"

            # Configurar encabezados y ancho fijo
            for col in self.df.columns:
                self.tree.heading(col, text=col, anchor="center")
                # Ancho fijo de 160 píxeles
                self.tree.column(col, width=160, anchor="center")

            # Insertar filas
            for i, row in self.df.iterrows():
                # Aplica estilo solo a la primera fila (encabezado)
                tag = "header" if i == 0 else ""
                self.tree.insert("", "end", values=list(row), tags=(tag,))

        def editar_celda(self, event):
            """ Permite editar una celda con doble clic """
            item = self.tree.identify_row(event.y)  # Obtener fila seleccionada
            column = self.tree.identify_column(
                event.x)  # Obtener columna seleccionada

            if item and column:
                col_index = int(column[1:]) - 1  # Convertir columna a índice
                # Obtener índice de fila en la tabla
                row_id = self.tree.index(item)

                # Obtener coordenadas para posicionar el Entry
                x, y, width, height = self.tree.bbox(item, column)

                # Crear un Entry en la celda
                entry = tk.Entry(self.tree)
                entry.place(x=x, y=y, width=width, height=height)
                entry.insert(0, self.tree.item(item, "values")[col_index])
                entry.focus()

                def guardar_valor(event):
                    nuevo_valor = entry.get()
                    self.tree.set(item, column, nuevo_valor)
                    # Actualiza DataFrame
                    self.df.iloc[row_id, col_index] = nuevo_valor
                    entry.destroy()

                entry.bind("<Return>", guardar_valor)
                entry.bind("<FocusOut>", lambda e: entry.destroy())

        def mostrar_menu(self, event):
            """ Muestra el menú contextual al hacer clic derecho """
            item = self.tree.identify_row(event.y)
            if item:
                # Selecciona la fila sobre la que se hizo clic
                self.tree.selection_set(item)
                self.menu_contextual.post(event.x_root, event.y_root)

        def eliminar_fila(self):
            """ Elimina la fila seleccionada """
            seleccion = self.tree.selection()
            if seleccion:
                # Obtener índice de la fila seleccionada
                row_id = self.tree.index(seleccion[0])
                # Eliminar fila del DataFrame
                self.df.drop(self.df.index[row_id], inplace=True)
                # Resetear índices
                self.df.reset_index(drop=True, inplace=True)
                self.mostrar_datos()  # Actualizar tabla
                messagebox.showinfo(
                    "Éxito", "Fila eliminada correctamente.", parent=self.root)
            else:
                messagebox.showwarning(
                    "Atención", "Seleccione una fila para eliminar.", parent=self.root)

        def guardar_csv(self):
            """ Guarda el DataFrame modificado en el mismo archivo CSV """
            try:
                self.df.to_csv(self.archivo_csv, index=False, encoding="utf-8")

            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo guardar el archivo CSV.\n{str(e)}", parent=self.root)

    # Crear ventana secundaria
    ventana_csv = tk.Toplevel()  # Se crea directamente sin necesitar root
    app = CSVEditor(ventana_csv)


# ----------Ventana LogFileRegistro----------------------------------------------------------------
# Ruta del archivo CSV predeterminado
# Cambia esta ruta si es necesario


CSV2_PATH = obtener_configuracion("LogFileRegistro_csv")


def abrir_ventana_csv_registro():
    """ Función que abre la ventana secundaria para editar el CSV """
    class CSVEditor:
        def __init__(self, root):
            self.root = root
            self.root.title("Registro")

            def cerrar_root():
                root.destroy()
                inicio()
            root.protocol("WM_DELETE_WINDOW", cerrar_root)

            # Configura la ventana para que se abra en pantalla completa pero manteniendo los botones de cerrar y minimizar
            self.root.state('zoomed')  # Maximiza la ventana al abrir
            # También puedes definir un tamaño inicial si no se quiere pantalla completa
            self.root.geometry("900x500")
            self.root.attributes("-topmost", True)

            self.archivo_csv = CSV2_PATH  # Cargar automáticamente desde la ruta
            self.df = None

            # Botones de carga y guardado
            btn_frame = tk.Frame(root)
            btn_frame.pack(fill="x", padx=10, pady=5)

            self.btn_guardar = tk.Button(
                btn_frame, text="Guardar Cambios", command=self.guardar_csv, state=tk.DISABLED)
            self.btn_guardar.pack(side="right", padx=5)

            # Frame para la tabla con scroll
            table_frame = tk.Frame(root)
            table_frame.pack(expand=True, fill="both")

            # Scrollbars
            self.scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
            self.scroll_y = tk.Scrollbar(table_frame, orient="vertical")

            self.tree = ttk.Treeview(
                table_frame, yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
            self.tree.grid(row=0, column=0, sticky="nsew")

            self.scroll_x.config(command=self.tree.xview)
            self.scroll_y.config(command=self.tree.yview)

            self.scroll_x.grid(row=1, column=0, sticky="ew")
            self.scroll_y.grid(row=0, column=1, sticky="ns")

            # Configurar el diseño para expandirse
            table_frame.grid_rowconfigure(0, weight=1)
            table_frame.grid_columnconfigure(0, weight=1)

            # Eventos
            # Editar con doble clic
            self.tree.bind("<Double-1>", self.editar_celda)
            # Clic derecho para menú
            self.tree.bind("<Button-3>", self.mostrar_menu)

            # Crear menú contextual
            self.menu_contextual = tk.Menu(self.root, tearoff=0)
            self.menu_contextual.add_command(
                label="Eliminar fila", command=self.eliminar_fila)

            # Aplicar estilo al encabezado
            style = ttk.Style()
            style.configure("Treeview.Heading", font=(
                "Arial", 10, "bold"), background="lightblue", foreground="black")
            # Color de fondo del encabezado
            self.tree.tag_configure("header", background="lightblue")

            # Cargar el CSV al abrir el programa
            if os.path.exists(self.archivo_csv):
                self.cargar_csv()
            else:
                messagebox.showerror(
                    "Error", f"No se encontró el archivo: {self.archivo_csv}", parent=self.root)

        def detectar_codificacion(self, archivo):
            """ Detecta la codificación del archivo CSV """
            with open(archivo, "rb") as f:
                result = chardet.detect(f.read())
            return result["encoding"]

        def cargar_csv(self):
            """ Carga el archivo CSV y lo muestra en la tabla en orden inverso """
            try:
                encoding_detectado = self.detectar_codificacion(
                    self.archivo_csv)
                self.df = pd.read_csv(
                    self.archivo_csv, encoding=encoding_detectado)

                # Invertir el orden de las filas, excepto la primera (encabezado)
                self.df = pd.concat(
                    [self.df.iloc[:0], self.df.iloc[0:].iloc[::-1]], ignore_index=True)

                self.mostrar_datos()
                # Habilita el botón de guardar
                self.btn_guardar.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo cargar el archivo CSV.\n{str(e)}", parent=self.root)

        def mostrar_datos(self):
            """ Muestra los datos del DataFrame en el Treeview con encabezados de color """
            # Limpiar tabla
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = list(self.df.columns)
            self.tree["show"] = "headings"

            # Configurar encabezados y ancho fijo
            for col in self.df.columns:
                self.tree.heading(col, text=col, anchor="center")
                # Ancho fijo de 160 píxeles
                self.tree.column(col, width=160, anchor="center")

            # Insertar filas
            for i, row in self.df.iterrows():
                # Aplica estilo solo a la primera fila (encabezado)
                tag = "header" if i == 0 else ""
                self.tree.insert("", "end", values=list(row), tags=(tag,))

        def editar_celda(self, event):
            """ Permite editar una celda con doble clic """
            item = self.tree.identify_row(event.y)  # Obtener fila seleccionada
            column = self.tree.identify_column(
                event.x)  # Obtener columna seleccionada

            if item and column:
                col_index = int(column[1:]) - 1  # Convertir columna a índice
                # Obtener índice de fila en la tabla
                row_id = self.tree.index(item)

                # Obtener coordenadas para posicionar el Entry
                x, y, width, height = self.tree.bbox(item, column)

                # Crear un Entry en la celda
                entry = tk.Entry(self.tree)
                entry.place(x=x, y=y, width=width, height=height)
                entry.insert(0, self.tree.item(item, "values")[col_index])
                entry.focus()

                def guardar_valor(event):
                    nuevo_valor = entry.get()
                    self.tree.set(item, column, nuevo_valor)
                    # Actualiza DataFrame
                    self.df.iloc[row_id, col_index] = nuevo_valor
                    entry.destroy()

                entry.bind("<Return>", guardar_valor)
                entry.bind("<FocusOut>", lambda e: entry.destroy())

        def mostrar_menu(self, event):
            """ Muestra el menú contextual al hacer clic derecho """
            item = self.tree.identify_row(event.y)
            if item:
                # Selecciona la fila sobre la que se hizo clic
                self.tree.selection_set(item)
                self.menu_contextual.post(event.x_root, event.y_root)

        def eliminar_fila(self):
            """ Elimina la fila seleccionada """
            seleccion = self.tree.selection()
            if seleccion:
                # Obtener índice de la fila seleccionada
                row_id = self.tree.index(seleccion[0])
                # Eliminar fila del DataFrame
                self.df.drop(self.df.index[row_id], inplace=True)
                # Resetear índices
                self.df.reset_index(drop=True, inplace=True)
                self.mostrar_datos()  # Actualizar tabla
                messagebox.showinfo(
                    "Éxito", "Fila eliminada correctamente.", parent=self.root)
            else:
                messagebox.showwarning(
                    "Atención", "Seleccione una fila para eliminar.", parent=self.root)

        def guardar_csv(self):
            """ Guarda el DataFrame modificado en el mismo archivo CSV """
            try:
                self.df.to_csv(self.archivo_csv, index=False, encoding="utf-8")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo guardar el archivo CSV.\n{str(e)}", parent=self.root)

    # Crear ventana secundaria
    ventana_csv = tk.Toplevel()  # Se crea directamente sin necesitar root
    app = CSVEditor(ventana_csv)


# ----------Ventana Parámetros----------------------------------------------------------------
CSV3_PATH = obtener_configuracion("LogParameters")


def abrir_ventana_parametros():
    """ Función que abre la ventana secundaria para editar el CSV """
    class CSVEditor:
        def __init__(self, root):
            self.root = root
            self.root.title("Parámetros")

            def cerrar_root():
                root.destroy()
                obtener_configuracion("LogParameters")
                inicio()
            root.protocol("WM_DELETE_WINDOW", cerrar_root)

            # Configura la ventana para que se abra en pantalla completa pero manteniendo los botones de cerrar y minimizar
            self.root.state('zoomed')  # Maximiza la ventana al abrir
            # También puedes definir un tamaño inicial si no se quiere pantalla completa
            self.root.geometry("900x500")
            self.root.attributes("-topmost", True)

            self.archivo_csv = CSV3_PATH  # Cargar automáticamente desde la ruta
            self.df = None

            # Botones de carga y guardado
            btn_frame = tk.Frame(root)
            btn_frame.pack(fill="x", padx=10, pady=5)

            self.btn_guardar = tk.Button(
                btn_frame, text="Guardar Cambios", command=self.guardar_csv, state=tk.DISABLED)
            self.btn_guardar.pack(side="right", padx=5)

            # Frame para la tabla con scroll
            table_frame = tk.Frame(root)
            table_frame.pack(expand=True, fill="both")

            # Scrollbars
            self.scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
            self.scroll_y = tk.Scrollbar(table_frame, orient="vertical")

            self.tree = ttk.Treeview(
                table_frame, yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
            self.tree.grid(row=0, column=0, sticky="nsew")

            self.scroll_x.config(command=self.tree.xview)
            self.scroll_y.config(command=self.tree.yview)

            self.scroll_x.grid(row=1, column=0, sticky="ew")
            self.scroll_y.grid(row=0, column=1, sticky="ns")

            # Configurar el diseño para expandirse
            table_frame.grid_rowconfigure(0, weight=1)
            table_frame.grid_columnconfigure(0, weight=1)

            # Eventos
            # Editar con doble clic
            self.tree.bind("<Double-1>", self.editar_celda)
            # Clic derecho para menú
            self.tree.bind("<Button-3>", self.mostrar_menu)

            # Crear menú contextual
            self.menu_contextual = tk.Menu(self.root, tearoff=0)
            self.menu_contextual.add_command(
                label="Agregar fila", command=self.agregar_fila)
            self.menu_contextual.add_command(
                label="Eliminar fila", command=self.eliminar_fila)

            # Aplicar estilo al encabezado
            style = ttk.Style()
            style.configure("Treeview.Heading", font=(
                "Arial", 10, "bold"), background="lightblue", foreground="black")
            # Color de fondo del encabezado
            self.tree.tag_configure("header", background="lightblue")

            # Cargar el CSV al abrir el programa
            if os.path.exists(self.archivo_csv):
                self.cargar_csv()
            else:
                messagebox.showerror(
                    "Error", f"No se encontró el archivo: {self.archivo_csv}", parent=self.root)

        def detectar_codificacion(self, archivo):
            """ Detecta la codificación del archivo CSV """
            with open(archivo, "rb") as f:
                result = chardet.detect(f.read())
            return result["encoding"]

        def cargar_csv(self):
            """ Carga el archivo CSV y lo muestra en la tabla en orden inverso """
            try:
                encoding_detectado = self.detectar_codificacion(
                    self.archivo_csv)
                self.df = pd.read_csv(
                    self.archivo_csv, encoding=encoding_detectado)

                self.mostrar_datos()
                # Habilita el botón de guardar
                self.btn_guardar.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo cargar el archivo CSV.\n{str(e)}", parent=self.root)

        def mostrar_datos(self):
            """ Muestra los datos del DataFrame en el Treeview con encabezados de color """
            # Limpiar tabla
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = list(self.df.columns)
            self.tree["show"] = "headings"

            # Configurar encabezados y ancho fijo
            for col in self.df.columns:
                self.tree.heading(col, text=col, anchor="center")
                # Ancho fijo de 160 píxeles
                self.tree.column(col, width=160, anchor="center")

            # Insertar filas
            for i, row in self.df.iterrows():
                # Aplica estilo solo a la primera fila (encabezado)
                tag = "header" if i == 0 else ""
                self.tree.insert("", "end", values=list(row), tags=(tag,))

        def editar_celda(self, event):
            """ Permite editar una celda con doble clic """
            item = self.tree.identify_row(event.y)  # Obtener fila seleccionada
            column = self.tree.identify_column(
                event.x)  # Obtener columna seleccionada

            if item and column:
                col_index = int(column[1:]) - 1  # Convertir columna a índice
                # Obtener índice de fila en la tabla
                row_id = self.tree.index(item)

                # Obtener coordenadas para posicionar el Entry
                x, y, width, height = self.tree.bbox(item, column)

                # Crear un Entry en la celda
                entry = tk.Entry(self.tree)
                entry.place(x=x, y=y, width=width, height=height)
                entry.insert(0, self.tree.item(item, "values")[col_index])
                entry.focus()

                def guardar_valor(event):
                    nuevo_valor = entry.get()
                    self.tree.set(item, column, nuevo_valor)
                    # Actualiza DataFrame
                    self.df.iloc[row_id, col_index] = nuevo_valor
                    entry.destroy()

                entry.bind("<Return>", guardar_valor)
                entry.bind("<FocusOut>", lambda e: entry.destroy())

        def mostrar_menu(self, event):
            """ Muestra el menú contextual al hacer clic derecho """
            item = self.tree.identify_row(event.y)
            if item:
                # Selecciona la fila sobre la que se hizo clic
                self.tree.selection_set(item)
                self.menu_contextual.post(event.x_root, event.y_root)

        def agregar_fila(self):
            """Agrega una nueva fila con valores 'N/A' debajo de la fila seleccionada"""
            try:
                if self.df is not None:
                    # Obtener la fila seleccionada
                    seleccion = self.tree.selection()

                    if not seleccion:
                        messagebox.showwarning("Advertencia", "Seleccione una fila para insertar debajo.",
                                               parent=self.root)
                        return

                    # Obtener el índice de la fila seleccionada
                    selected_index = self.tree.index(seleccion[0])

                    # Crear nueva fila con 'N/A' en todas las columnas
                    nueva_fila = {col: 'N/A' for col in self.df.columns}

                    # Dividir el DataFrame y concatenar con la nueva fila en medio
                    self.df = pd.concat([
                        # Parte superior incluyendo la fila seleccionada
                        self.df.iloc[:selected_index + 1],
                        pd.DataFrame([nueva_fila]),  # Nueva fila
                        self.df.iloc[selected_index + 1:]  # Parte inferior
                    ], ignore_index=True)

                    # Actualizar la vista del Treeview
                    self.mostrar_datos()

                    # Seleccionar y enfocar la nueva fila
                    new_item = self.tree.get_children()[selected_index + 1]
                    self.tree.selection_set(new_item)
                    self.tree.focus(new_item)
                    self.tree.see(new_item)
                else:
                    messagebox.showwarning(
                        "Advertencia", "No hay datos cargados.", parent=self.root)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo agregar la fila: {str(e)}", parent=self.root)

        def eliminar_fila(self):
            """ Elimina la fila seleccionada """
            seleccion = self.tree.selection()
            if seleccion:
                # Obtener índice de la fila seleccionada
                row_id = self.tree.index(seleccion[0])
                # Eliminar fila del DataFrame
                self.df.drop(self.df.index[row_id], inplace=True)
                # Resetear índices
                self.df.reset_index(drop=True, inplace=True)
                self.mostrar_datos()  # Actualizar tabla
                messagebox.showinfo(
                    "Éxito", "Fila eliminada correctamente.", parent=self.root)
            else:
                messagebox.showwarning(
                    "Atención", "Seleccione una fila para eliminar.", parent=self.root)

        def guardar_csv(self):
            """ Guarda el DataFrame modificado en el mismo archivo CSV """
            try:
                self.df.to_csv(self.archivo_csv, index=False, encoding="utf-8")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo guardar el archivo CSV.\n{str(e)}", parent=self.root)

    # Crear ventana secundaria
    ventana_csv = tk.Toplevel()  # Se crea directamente sin necesitar root
    app = CSVEditor(ventana_csv)

# ---------------------------------------------------------------------------------------------------------------------


# Ruta del segundo archivo CSV
csv_file = obtener_configuracion("LogFileTotal_csv")
# Nueva configuración para el segundo archivo
csv_file2 = obtener_configuracion("LogFileRegistro_csv")

# Crear o abrir el primer archivo CSV, LogFileTotal
if not os.path.isfile(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Modelo', 'Pallet', 'Defectos', 'Estandar', 'Fecha', 'Hora', 'FPY', 'Wave1', 'Wave2', 'Flux', 'Conveyor',
                         'Falta de soldadura', 'Exceso de soldadura', 'Cortos', 'Falta de housing', 'Comp. SMT dañado',
                         'Falta comp. SMT', 'Falta de conector', 'Housing dañado', 'Comp. THT dañado', 'Falta comp. THT',
                         'Conector levantado', 'Housing quemado', 'Comp. SMT levantado', 'Comp. THT levantado', 'Bola de soldadura',
                         'Cable dañado', 'Falta de cable', 'Cable suelto', 'Cable quemado', 'Terminales iguales', 'L1 dañado', 'Pin largo', 'Falta de evidencia de pin', 'Cable invertido', 'Terminales desalineadas'])

# Crear o abrir el segundo archivo CSV, LogFileTotal2
if not os.path.isfile(csv_file2):
    with open(csv_file2, mode='w', newline='') as file2:
        writer2 = csv.writer(file2)
        writer2.writerow(['Modelo', 'Pallet', 'Defectos', 'Estandar', 'Fecha', 'Hora', 'FPY',  'Wave1', 'Wave2', 'Flux', 'Conveyor',
                          'Falta de soldadura', 'Exceso de soldadura', 'Cortos', 'Falta de housing', 'Comp. SMT dañado',
                          'Falta comp. SMT', 'Falta de conector', 'Housing dañado', 'Comp. THT dañado', 'Falta comp. THT',
                          'Conector levantado', 'Housing quemado', 'Comp. SMT levantado', 'Comp. THT levantado', 'Bola de soldadura',
                          'Cable dañado', 'Falta de cable', 'Cable suelto', 'Cable quemado', 'Terminales iguales', 'L1 dañado', 'Pin largo', 'Falta de evidencia de pin', 'Cable invertido', 'Terminales desalineadas'])

# Cargar el primer archivo CSV
data = pd.read_csv(csv_file, encoding='latin1')
data2 = pd.read_csv(csv_file2, encoding='latin1')
data['Hora'] = pd.to_datetime(data['Hora'], format='%H:%M:%S')
data2['Hora'] = pd.to_datetime(data2['Hora'], format='%H:%M:%S')


# Función para guardar los datos en el archivo CSV y limpiar las entradas


def guardar_datos(event=None):
    try:
        # Guardar datos en el archivo CSV
        Modelo = entry_modelo_con.get().strip()
        Pallet = entry_pallet.get().strip()
        Defectos = entry_defectos_con.get().strip() or "0"
        Estandar = entry_estandar_con.get().strip()
        Fecha = entry_fecha_con.get().strip()
        Hora = entry_hora_con.get().strip()
        FPY = entry_fpy_pallet_con.get().strip() or "100%"
        Wave1 = entry_wave_1_con.get().strip() or "0"
        Wave2 = entry_wave_1_con.get().strip() or "0"
        Flux = entry_flux_con.get().strip() or "0"
        Conveyor = entry_conveyor_con.get().strip() or "0"
        Defec_1 = entry_falta_de_soldadura.get().strip() or "0"
        Defec_2 = entry_exceso_de_soldadura.get().strip() or "0"
        Defec_3 = entry_cortos.get().strip() or "0"
        Defec_4 = entry_falta_de_housing.get().strip() or "0"
        Defec_5 = entry_com_smt_dañado.get().strip() or "0"
        Defec_6 = entry_falta_comp_smt.get().strip() or "0"
        Defec_7 = entry_falta_conector.get().strip() or "0"
        Defec_8 = entry_housing_dañado.get().strip() or "0"
        Defec_9 = entry_com_tht_dañado.get().strip() or "0"
        Defec_10 = entry_falta_comp_tht.get().strip() or "0"
        Defec_11 = entry_conector_levantado.get().strip() or "0"
        Defec_12 = entry_housing_quemado.get().strip() or "0"
        Defec_13 = entry_comp_smt_levantado.get().strip() or "0"
        Defec_14 = entry_comp_tht_levantado.get().strip() or "0"
        Defec_15 = entry_bola_soldadura.get().strip() or "0"
        Defec_16 = entry_cable_dañado.get().strip() or "0"
        Defec_17 = entry_falta_cable.get().strip() or "0"
        Defec_18 = entry_cable_suelto.get().strip() or "0"
        Defec_19 = entry_cable_quemado.get().strip() or "0"
        Defec_20 = entry_terminales_iguales.get().strip() or "0"
        Defec_21 = entry_l1_dañado.get().strip() or "0"
        Defec_22 = entry_pin_largo.get().strip() or "0"
        Defec_23 = entry_falta_evidencia_pin.get().strip() or "0"
        Defec_24 = entry_cable_invertido.get().strip() or "0"
        Defec_25 = entry_terminales_chuecas.get().strip() or "0"

        # Verificar si todas las entradas son válidas
        if Modelo and Pallet and Defectos and Estandar and Fecha and Hora and FPY and Wave1 and Wave2 and Flux and Conveyor and Defec_1 and Defec_2 and Defec_3 and Defec_4 and Defec_5 and Defec_6 and Defec_7 and Defec_8 and Defec_9 and Defec_10 and Defec_11 and Defec_12 and Defec_13 and Defec_14 and Defec_15 and Defec_16 and Defec_17 and Defec_18 and Defec_19 and Defec_20 and Defec_21 and Defec_22 and Defec_23 and Defec_24 and Defec_25:
            # Guardar en el primer archivo CSV
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([Modelo, Pallet, Defectos, Estandar, Fecha, Hora, FPY, Wave1, Wave2, Flux, Conveyor, Defec_1, Defec_2, Defec_3, Defec_4, Defec_5,
                                Defec_6, Defec_7, Defec_8, Defec_9, Defec_10, Defec_11, Defec_12, Defec_13, Defec_14, Defec_15,
                                Defec_16, Defec_17, Defec_18, Defec_19, Defec_20, Defec_21, Defec_22, Defec_23, Defec_24, Defec_25])

            # Guardar en el segundo archivo CSV
            with open(csv_file2, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([Modelo, Pallet, Defectos, Estandar, Fecha, Hora, FPY, Wave1, Wave2, Flux, Conveyor, Defec_1, Defec_2, Defec_3, Defec_4, Defec_5,
                                Defec_6, Defec_7, Defec_8, Defec_9, Defec_10, Defec_11, Defec_12, Defec_13, Defec_14, Defec_15,
                                Defec_16, Defec_17, Defec_18, Defec_19, Defec_20, Defec_21, Defec_22, Defec_23, Defec_24, Defec_25])

            # Limpiar las entradas
            entry_modelo_con.delete(0, tk.END)
            entry_pallet.delete(0, tk.END)
            entry_defectos_con.delete(0, tk.END)
            entry_estandar_con.delete(0, tk.END)
            entry_fpy_pallet_con.delete(0, tk.END)
            entry_wave_1_con.delete(0, tk.END)
            entry_wave_2_con.delete(0, tk.END)
            entry_flux_con.delete(0, tk.END)
            entry_conveyor_con.delete(0, tk.END)
            entry_falta_de_soldadura.delete(0, tk.END)
            entry_exceso_de_soldadura.delete(0, tk.END)
            entry_cortos.delete(0, tk.END)
            entry_falta_de_housing.delete(0, tk.END)
            entry_com_smt_dañado.delete(0, tk.END)
            entry_falta_comp_smt.delete(0, tk.END)
            entry_falta_conector.delete(0, tk.END)
            entry_housing_dañado.delete(0, tk.END)
            entry_com_tht_dañado.delete(0, tk.END)
            entry_falta_comp_tht.delete(0, tk.END)
            entry_conector_levantado.delete(0, tk.END)
            entry_housing_quemado.delete(0, tk.END)
            entry_comp_smt_levantado.delete(0, tk.END)
            entry_comp_tht_levantado.delete(0, tk.END)
            entry_bola_soldadura.delete(0, tk.END)
            entry_cable_dañado.delete(0, tk.END)
            entry_falta_cable.delete(0, tk.END)
            entry_cable_suelto.delete(0, tk.END)
            entry_cable_quemado.delete(0, tk.END)
            entry_terminales_iguales.delete(0, tk.END)
            entry_l1_dañado.delete(0, tk.END)
            entry_pin_largo.delete(0, tk.END)
            entry_falta_evidencia_pin.delete(0, tk.END)
            entry_cable_invertido.delete(0, tk.END)
            entry_terminales_chuecas.delete(0, tk.END)
            ventana.after(100, calcular_defectos)
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")


def calcular_defectos():
    try:
        data2 = pd.read_csv(csv_file2, encoding='latin1')
        data2['Hora'] = pd.to_datetime(data2['Hora'], format='%H:%M:%S')
        modelo = "Lion Mite"
        modelo2 = "ROTOZIP"
        modelo3 = "ROUTER 1617"
        modelo4 = "PR20"
        modelo5 = "FA08"
        modelo6 = "HLA"
        modelo7 = "BGA200"
        modelo8 = "FSA135"
        modelo10 = "DC-I"
        modelo11 = "LOCUS"
        fecha = entry_fecha_con.get()

        # Obtener horas y minutos de los spinboxes
        hora_inicio_1 = f"{hora_inicio_var.get()}:{minuto_inicio_var.get()} {periodo_inicio_var.get()}"
        hora_fin_1 = f"{hora_fin_var.get()}:{minuto_fin_var.get()} {periodo_fin_var.get()}"

        # Convertir horas a formato 24 horas para filtrar
        hora_inicio_1 = pd.to_datetime(hora_inicio_1, format='%I:%M %p').time()
        hora_fin_1 = pd.to_datetime(hora_fin_1, format='%I:%M %p').time()

        # Filtrar por modelo y fecha
        filtro_modelo_fecha = (data2['Modelo'] == modelo) & (
            data2['Fecha'] == fecha)

        filtro_modelo2_fecha = (data2['Modelo'] == modelo2) & (
            data2['Fecha'] == fecha)

        filtro_modelo3_fecha = (data2['Modelo'] == modelo3) & (
            data2['Fecha'] == fecha)

        filtro_modelo4_fecha = (data2['Modelo'] == modelo4) & (
            data2['Fecha'] == fecha)

        filtro_modelo5_fecha = (data2['Modelo'] == modelo5) & (
            data2['Fecha'] == fecha)

        filtro_modelo6_fecha = (data2['Modelo'] == modelo6) & (
            data2['Fecha'] == fecha)

        filtro_modelo7_fecha = (data2['Modelo'] == modelo7) & (
            data2['Fecha'] == fecha)

        filtro_modelo8_fecha = (data2['Modelo'] == modelo8) & (
            data2['Fecha'] == fecha)

        filtro_modelo10_fecha = (data2['Modelo'] == modelo10) & (
            data2['Fecha'] == fecha)

        filtro_modelo11_fecha = (data2['Modelo'] == modelo11) & (
            data2['Fecha'] == fecha)

        # Filtrar por rango de horas
        filtro_horas = data2['Hora'].dt.time.between(hora_inicio_1, hora_fin_1)

        # Aplicar filtros
        datos_filtrados = data2[filtro_modelo_fecha & filtro_horas]
        datos_filtrados2 = data2[filtro_modelo2_fecha & filtro_horas]
        datos_filtrados3 = data2[filtro_modelo3_fecha & filtro_horas]
        datos_filtrados4 = data2[filtro_modelo4_fecha & filtro_horas]
        datos_filtrados5 = data2[filtro_modelo5_fecha & filtro_horas]
        datos_filtrados6 = data2[filtro_modelo6_fecha & filtro_horas]
        datos_filtrados7 = data2[filtro_modelo7_fecha & filtro_horas]
        datos_filtrados8 = data2[filtro_modelo8_fecha & filtro_horas]
        datos_filtrados10 = data2[filtro_modelo10_fecha & filtro_horas]
        datos_filtrados11 = data2[filtro_modelo11_fecha & filtro_horas]

        # Calcular la sumatoria de defectos
        suma_defectos = datos_filtrados['Defectos'].sum()
        suma_estandar = datos_filtrados['Estandar'].sum()
        suma_defectos2 = datos_filtrados2['Defectos'].sum()
        suma_estandar2 = datos_filtrados2['Estandar'].sum()
        suma_defectos3 = datos_filtrados3['Defectos'].sum()
        suma_estandar3 = datos_filtrados3['Estandar'].sum()
        suma_defectos4 = datos_filtrados4['Defectos'].sum()
        suma_estandar4 = datos_filtrados4['Estandar'].sum()
        suma_defectos5 = datos_filtrados5['Defectos'].sum()
        suma_estandar5 = datos_filtrados5['Estandar'].sum()
        suma_defectos6 = datos_filtrados6['Defectos'].sum()
        suma_estandar6 = datos_filtrados6['Estandar'].sum()
        suma_defectos7 = datos_filtrados7['Defectos'].sum()
        suma_estandar7 = datos_filtrados7['Estandar'].sum()
        suma_defectos8 = datos_filtrados8['Defectos'].sum()
        suma_estandar8 = datos_filtrados8['Estandar'].sum()
        suma_defectos10 = datos_filtrados10['Defectos'].sum()
        suma_estandar10 = datos_filtrados10['Estandar'].sum()
        suma_defectos11 = datos_filtrados11['Defectos'].sum()
        suma_estandar11 = datos_filtrados11['Estandar'].sum()

        # Insertar el resultado en el campo correspondiente
        entry_con_def_lm.delete(0, tk.END)
        entry_con_estan_lm.delete(0, tk.END)
        entry_con_def_rz.delete(0, tk.END)
        entry_con_estan_rz.delete(0, tk.END)
        entry_con_def_router.delete(0, tk.END)
        entry_con_estan_router.delete(0, tk.END)
        entry_con_def_pr20.delete(0, tk.END)
        entry_con_estan_pr20.delete(0, tk.END)
        entry_con_def_fa08.delete(0, tk.END)
        entry_con_estan_fa08.delete(0, tk.END)
        entry_con_def_hla.delete(0, tk.END)
        entry_con_estan_hla.delete(0, tk.END)
        entry_con_def_bga200.delete(0, tk.END)
        entry_con_estan_bga200.delete(0, tk.END)
        entry_con_def_fsa135.delete(0, tk.END)
        entry_con_estan_fsa135.delete(0, tk.END)
        entry_con_def_dc_i.delete(0, tk.END)
        entry_con_estan_dc_i.delete(0, tk.END)
        entry_con_def_locus.delete(0, tk.END)
        entry_con_estan_locus.delete(0, tk.END)
        # Mostrar el resultado en el entry
        entry_con_def_lm.insert(0, str(suma_defectos))
        entry_con_estan_lm.insert(0, str(suma_estandar))
        entry_con_def_rz.insert(0, str(suma_defectos2))
        entry_con_estan_rz.insert(0, str(suma_estandar2))
        entry_con_def_router.insert(0, str(suma_defectos3))
        entry_con_estan_router.insert(0, str(suma_estandar3))
        entry_con_def_pr20.insert(0, str(suma_defectos4))
        entry_con_estan_pr20.insert(0, str(suma_estandar4))
        entry_con_def_fa08.insert(0, str(suma_defectos5))
        entry_con_estan_fa08.insert(0, str(suma_estandar5))
        entry_con_def_hla.insert(0, str(suma_defectos6))
        entry_con_estan_hla.insert(0, str(suma_estandar6))
        entry_con_def_bga200.insert(0, str(suma_defectos7))
        entry_con_estan_bga200.insert(0, str(suma_estandar7))
        entry_con_def_fsa135.insert(0, str(suma_defectos8))
        entry_con_estan_fsa135.insert(0, str(suma_estandar8))
        entry_con_def_dc_i.insert(0, str(suma_defectos10))
        entry_con_estan_dc_i.insert(0, str(suma_estandar10))
        entry_con_def_locus.insert(0, str(suma_defectos11))
        entry_con_estan_locus.insert(0, str(suma_estandar11))
        ventana.after(100, fpy_log_registro)

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")


def fpy_log_registro(*args):
    defectos_lion = int(entry_con_def_lm.get()
                        ) if entry_con_def_lm.get() else 0
    estandar_lion = int(entry_con_estan_lm.get()
                        ) if entry_con_estan_lm.get() else 0
    defectos_rz = int(entry_con_def_rz.get()
                      ) if entry_con_def_rz.get() else 0
    estandar_rz = int(entry_con_estan_rz.get()
                      ) if entry_con_estan_rz.get() else 0
    defectos_router = int(entry_con_def_router.get()
                          ) if entry_con_def_router.get() else 0
    estandar_router = int(entry_con_estan_router.get()
                          ) if entry_con_estan_router.get() else 0

    defectos_pr20 = int(entry_con_def_pr20.get()
                        ) if entry_con_def_pr20.get() else 0
    estandar_pr20 = int(entry_con_estan_pr20.get()
                        ) if entry_con_estan_pr20.get() else 0

    defectos_fa08 = int(entry_con_def_fa08.get()
                        ) if entry_con_def_fa08.get() else 0
    estandar_fa08 = int(entry_con_estan_fa08.get()
                        ) if entry_con_estan_fa08.get() else 0

    defectos_hla = int(entry_con_def_hla.get()
                       ) if entry_con_def_hla.get() else 0
    estandar_hla = int(entry_con_estan_hla.get()
                       ) if entry_con_estan_hla.get() else 0

    defectos_bga200 = int(entry_con_def_bga200.get()
                          ) if entry_con_def_bga200.get() else 0
    estandar_bga200 = int(entry_con_estan_bga200.get()
                          ) if entry_con_estan_bga200.get() else 0

    defectos_fsa135 = int(entry_con_def_fsa135.get()
                          ) if entry_con_def_fsa135.get() else 0
    estandar_fsa135 = int(entry_con_estan_fsa135.get()
                          ) if entry_con_estan_fsa135.get() else 0

    defectos_dc_i = int(entry_con_def_dc_i.get()
                        ) if entry_con_def_dc_i.get() else 0
    estandar_dc_i = int(entry_con_estan_dc_i.get()
                        ) if entry_con_estan_dc_i.get() else 0

    defectos_locus = int(entry_con_def_locus.get()
                         ) if entry_con_def_locus.get() else 0
    estandar_locus = int(entry_con_estan_locus.get()
                         ) if entry_con_estan_locus.get() else 0

    fpy = ((estandar_lion - defectos_lion) / estandar_lion) * \
        100 if estandar_lion > 0 else 0
    fpy_rz = ((estandar_rz - defectos_rz) / estandar_rz) * \
        100 if estandar_rz > 0 else 0
    fpy_router = ((estandar_router - defectos_router) / estandar_router) * \
        100 if estandar_router > 0 else 0
    fpy_pr20 = ((estandar_pr20 - defectos_pr20) / estandar_pr20) * \
        100 if estandar_pr20 > 0 else 0
    fpy_fa08 = ((estandar_fa08 - defectos_fa08) / estandar_fa08) * \
        100 if estandar_fa08 > 0 else 0
    fpy_hla = ((estandar_hla - defectos_hla) / estandar_hla) * \
        100 if estandar_hla > 0 else 0
    fpy_bga200 = ((estandar_bga200 - defectos_bga200) / estandar_bga200) * \
        100 if estandar_bga200 > 0 else 0
    fpy_fsa135 = ((estandar_fsa135 - defectos_fsa135) / estandar_fsa135) * \
        100 if estandar_fsa135 > 0 else 0
    fpy_dc_i = ((estandar_dc_i - defectos_dc_i) / estandar_dc_i) * \
        100 if estandar_dc_i > 0 else 0
    fpy_locus = ((estandar_locus - defectos_locus) / estandar_locus) * \
        100 if estandar_locus > 0 else 0

    entry_fpy_lion.delete(0, tk.END)
    entry_fpy_lion.insert(0, f"{fpy:.2f}%")
    entry_fpy_rz.delete(0, tk.END)
    entry_fpy_rz.insert(0, f"{fpy_rz:.2f}%")
    entry_fpy_router.delete(0, tk.END)
    entry_fpy_router.insert(0, f"{fpy_router:.2f}%")
    entry_fpy_pr20.delete(0, tk.END)
    entry_fpy_pr20.insert(0, f"{fpy_pr20:.2f}%")
    entry_fpy_fa08.delete(0, tk.END)
    entry_fpy_fa08.insert(0, f"{fpy_fa08:.2f}%")
    entry_fpy_hla.delete(0, tk.END)
    entry_fpy_hla.insert(0, f"{fpy_hla:.2f}%")
    entry_fpy_bga200.delete(0, tk.END)
    entry_fpy_bga200.insert(0, f"{fpy_bga200:.2f}%")
    entry_fpy_fsa135.delete(0, tk.END)
    entry_fpy_fsa135.insert(0, f"{fpy_fsa135:.2f}%")
    entry_fpy_dc_i.delete(0, tk.END)
    entry_fpy_dc_i.insert(0, f"{fpy_dc_i:.2f}%")
    entry_fpy_locus.delete(0, tk.END)
    entry_fpy_locus.insert(0, f"{fpy_locus:.2f}%")

    fpy_por_lm = obtener_configuracion("FPY_LionMite")
    fpy_por_lm = int(fpy_por_lm)

    if fpy == 0:
        entry_fpy_lion.config(fg="black", bg="white")
    elif fpy > fpy_por_lm:
        entry_fpy_lion.config(fg="green")  # Verde
        entry_fpy_lion.config(bg="#D9F2D0")
    elif fpy < fpy_por_lm:
        entry_fpy_lion.config(fg="red")  # Rojo
        entry_fpy_lion.config(bg="#FFCCCC")
    elif fpy == fpy_por_lm:
        entry_fpy_lion.config(fg="#E7601D")  # Naranja
        entry_fpy_lion.config(bg="#FBE7DD")

    fpy_por_rz = obtener_configuracion("FPY_Rotozip")
    fpy_por_rz = int(fpy_por_rz)

    if fpy_rz == 0:
        entry_fpy_rz.config(fg="black", bg="white")
    elif fpy_rz > fpy_por_rz:
        entry_fpy_rz.config(fg="green")  # Verde
        entry_fpy_rz.config(bg="#D9F2D0")
    elif fpy_rz < fpy_por_rz:
        entry_fpy_rz.config(fg="red")  # Rojo
        entry_fpy_rz.config(bg="#FFCCCC")
    elif fpy_rz == fpy_por_rz:
        entry_fpy_rz.config(fg="#E7601D")  # Naranja
        entry_fpy_rz.config(bg="#FBE7DD")

    fpy_por_router = obtener_configuracion("FPY_Router")
    fpy_por_router = int(fpy_por_router)

    if fpy_router == 0:
        entry_fpy_router.config(fg="black", bg="white")
    elif fpy_router > fpy_por_router:
        entry_fpy_router.config(fg="green")  # Verde
        entry_fpy_router.config(bg="#D9F2D0")
    elif fpy_router < fpy_por_router:
        entry_fpy_router.config(fg="red")  # Rojo
        entry_fpy_router.config(bg="#FFCCCC")
    elif fpy_router == fpy_por_router:
        entry_fpy_router.config(fg="#E7601D")  # Naranja
        entry_fpy_router.config(bg="#FBE7DD")

    fpy_por_pr20 = obtener_configuracion("FPY_PR20")
    fpy_por_pr20 = int(fpy_por_pr20)

    if fpy_pr20 == 0:
        entry_fpy_pr20.config(fg="black", bg="white")
    elif fpy_pr20 > fpy_por_pr20:
        entry_fpy_pr20.config(fg="green")  # Verde
        entry_fpy_pr20.config(bg="#D9F2D0")
    elif fpy_pr20 < fpy_por_pr20:
        entry_fpy_pr20.config(fg="red")  # Rojo
        entry_fpy_pr20.config(bg="#FFCCCC")
    elif fpy_pr20 == fpy_por_pr20:
        entry_fpy_pr20.config(fg="#E7601D")  # Naranja
        entry_fpy_pr20.config(bg="#FBE7DD")

    fpy_por_fa08 = obtener_configuracion("FPY_FA08")
    fpy_por_fa08 = int(fpy_por_fa08)

    if fpy_fa08 == 0:
        entry_fpy_fa08.config(fg="black", bg="white")
    elif fpy_fa08 > fpy_por_fa08:
        entry_fpy_fa08.config(fg="green")  # Verde
        entry_fpy_fa08.config(bg="#D9F2D0")
    elif fpy_fa08 < fpy_por_fa08:
        entry_fpy_fa08.config(fg="red")  # Rojo
        entry_fpy_fa08.config(bg="#FFCCCC")
    elif fpy_fa08 == fpy_por_fa08:
        entry_fpy_fa08.config(fg="#E7601D")  # Naranja
        entry_fpy_fa08.config(bg="#FBE7DD")

    fpy_por_hla = obtener_configuracion("FPY_HLA")
    fpy_por_hla = int(fpy_por_hla)

    if fpy_hla == 0:
        entry_fpy_hla.config(fg="black", bg="white")
    elif fpy_hla > fpy_por_hla:
        entry_fpy_hla.config(fg="green")  # Verde
        entry_fpy_hla.config(bg="#D9F2D0")
    elif fpy_hla < fpy_por_hla:
        entry_fpy_hla.config(fg="red")  # Rojo
        entry_fpy_hla.config(bg="#FFCCCC")
    elif fpy_hla == fpy_por_hla:
        entry_fpy_hla.config(fg="#E7601D")  # Naranja
        entry_fpy_hla.config(bg="#FBE7DD")

    fpy_por_bga200 = obtener_configuracion("FPY_BGA200")
    fpy_por_bga200 = int(fpy_por_bga200)

    if fpy_bga200 == 0:
        entry_fpy_bga200.config(fg="black", bg="white")
    elif fpy_bga200 > fpy_por_bga200:
        entry_fpy_bga200.config(fg="green")  # Verde
        entry_fpy_bga200.config(bg="#D9F2D0")
    elif fpy_bga200 < fpy_por_bga200:
        entry_fpy_bga200.config(fg="red")  # Rojo
        entry_fpy_bga200.config(bg="#FFCCCC")
    elif fpy_bga200 == fpy_por_bga200:
        entry_fpy_bga200.config(fg="#E7601D")  # Naranja
        entry_fpy_bga200.config(bg="#FBE7DD")

    fpy_por_fsa135 = obtener_configuracion("FPY_FSA135")
    fpy_por_fsa135 = int(fpy_por_fsa135)

    if fpy_fsa135 == 0:
        entry_fpy_fsa135.config(fg="black", bg="white")
    elif fpy_fsa135 > fpy_por_fsa135:
        entry_fpy_fsa135.config(fg="green")  # Verde
        entry_fpy_fsa135.config(bg="#D9F2D0")
    elif fpy_fsa135 < fpy_por_fsa135:
        entry_fpy_fsa135.config(fg="red")  # Rojo
        entry_fpy_fsa135.config(bg="#FFCCCC")
    elif fpy_fsa135 == fpy_por_fsa135:
        entry_fpy_fsa135.config(fg="#E7601D")  # Naranja
        entry_fpy_fsa135.config(bg="#FBE7DD")

    fpy_por_dci = obtener_configuracion("FPY_DCI")
    fpy_por_dci = int(fpy_por_dci)

    if fpy_dc_i == 0:
        entry_fpy_dc_i.config(fg="black", bg="white")
    elif fpy_dc_i > fpy_por_dci:
        entry_fpy_dc_i.config(fg="green")  # Verde
        entry_fpy_dc_i.config(bg="#D9F2D0")
    elif fpy_dc_i < fpy_por_dci:
        entry_fpy_dc_i.config(fg="red")  # Rojo
        entry_fpy_dc_i.config(bg="#FFCCCC")
    elif fpy_dc_i == fpy_por_dci:
        entry_fpy_dc_i.config(fg="#E7601D")  # Naranja
        entry_fpy_dc_i.config(bg="#FBE7DD")

    fpy_por_locus = obtener_configuracion("FPY_LOCUS")
    fpy_por_locus = int(fpy_por_locus)

    if fpy_locus == 0:
        entry_fpy_locus.config(fg="black", bg="white")
    elif fpy_locus > fpy_por_locus:
        entry_fpy_locus.config(fg="green")  # Verde
        entry_fpy_locus.config(bg="#D9F2D0")
    elif fpy_locus < fpy_por_locus:
        entry_fpy_locus.config(fg="red")  # Rojo
        entry_fpy_locus.config(bg="#FFCCCC")
    elif fpy_locus == fpy_por_locus:
        entry_fpy_locus.config(fg="#E7601D")  # Naranja
        entry_fpy_locus.config(bg="#FBE7DD")


# -------------------------------------Ventana principal---------------------------------------------------------------
# Crear la ventana principal
ventana = tk.Tk()
# Configurar la ventana para estar siempre al frente
ventana.attributes("-topmost", True)
# Iniciar en pantalla completa
ventana.attributes("-fullscreen", True)
# Mostrar los botones de minimizar y cerrar
ventana.overrideredirect(False)
# Configurar para no permitir redimensionar manualmente
ventana.resizable(False, False)
# Detectar cuando la ventana es restaurada desde la barra de tareas
ventana.bind("<Map>", on_restore)
ventana.configure(bg="#F0F0F0")  # Color ventana
# Configurar el grid de la ventana principal con diferentes pesos
ventana.grid_rowconfigure(0, weight=0)
ventana.grid_rowconfigure(1, weight=0)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure(0, weight=1)
# -------------------------------------Frame---------------------------------------------------------------------------
# Crear frame principal
frame = tk.Frame(ventana, bg="white")
frame2 = tk.Frame(ventana, bg="white")
frame3 = tk.Frame(ventana, bg="white")


# Configurar el grid para el frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)
frame.grid_columnconfigure(4, weight=1)
frame.grid_columnconfigure(5, weight=1)
frame.grid_columnconfigure(6, weight=1)
frame.grid_columnconfigure(7, weight=1)
frame.grid_columnconfigure(8, weight=1)
frame.grid_columnconfigure(9, weight=1)
frame.grid_rowconfigure(0, weight=0)
frame.grid_rowconfigure(1, weight=0)
frame.grid_rowconfigure(2, weight=0)
frame.grid_rowconfigure(3, weight=0)
frame.grid_rowconfigure(4, weight=0)
frame.grid_rowconfigure(5, weight=0)
frame.grid_rowconfigure(6, weight=0)
frame.grid_rowconfigure(7, weight=0)
frame.grid_rowconfigure(8, weight=0)

# Configurar el grid para el frame3
frame3.grid_columnconfigure(0, weight=1)
frame3.grid_columnconfigure(1, weight=1)
frame3.grid_columnconfigure(2, weight=1)
frame3.grid_columnconfigure(3, weight=1)
frame3.grid_columnconfigure(4, weight=1)
frame3.grid_columnconfigure(5, weight=1)
frame3.grid_columnconfigure(6, weight=1)
frame3.grid_columnconfigure(7, weight=1)
frame3.grid_columnconfigure(8, weight=1)
frame3.grid_columnconfigure(9, weight=1)
frame3.grid_columnconfigure(10, weight=1)
frame3.grid_columnconfigure(11, weight=1)
frame3.grid_columnconfigure(12, weight=1)
frame3.grid_columnconfigure(13, weight=1)
frame3.grid_columnconfigure(14, weight=1)
frame3.grid_columnconfigure(15, weight=1)
frame3.grid_rowconfigure(0, weight=0)

# Configurar el grid para el frame2
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
frame2.grid_columnconfigure(2, weight=1)
frame2.grid_columnconfigure(3, weight=1)
frame2.grid_columnconfigure(4, weight=1)
frame2.grid_columnconfigure(5, weight=1)
frame2.grid_columnconfigure(6, weight=1)
frame2.grid_columnconfigure(7, weight=1)
frame2.grid_columnconfigure(8, weight=1)
frame2.grid_columnconfigure(9, weight=1)
frame2.grid_columnconfigure(10, weight=1)
frame2.grid_rowconfigure(0, weight=0)
frame2.grid_rowconfigure(1, weight=0)
frame2.grid_rowconfigure(2, weight=1)
frame2.grid_rowconfigure(3, weight=1)
frame2.grid_rowconfigure(4, weight=1)
frame2.grid_rowconfigure(5, weight=0)
frame2.grid_rowconfigure(6, weight=1)
frame2.grid_rowconfigure(7, weight=1)
frame2.grid_rowconfigure(8, weight=0)
frame2.grid_rowconfigure(9, weight=0)
frame2.grid_rowconfigure(10, weight=0)


# -------------------------------------Row 0---------------------------------------------------------------------------

# Cargar de logo ELRAD
logo_elrad = Image.open(obtener_configuracion("LogoELRAD"))
logo_elrad = logo_elrad.resize((150, 75), Image.LANCZOS)  # Ajuste de tamaño
logo_elrad_tk = ImageTk.PhotoImage(logo_elrad)

# Imagen ELRAD como boton de minimizar
boton_minimizar = tk.Button(
    frame, image=logo_elrad_tk, command=toggle_minimize, borderwidth=0, bg="white")
boton_minimizar.grid(row=0, column=0, padx=0, pady=0, sticky="nw")

# Cargar de logo SEHO
logo_SEHO = Image.open(obtener_configuracion("LogoSEHO"))
logo_SEHO = logo_SEHO.resize((150, 75), Image.LANCZOS)  # Ajuste de tamaño
logo_SEHO_tk = ImageTk.PhotoImage(logo_SEHO)

# Imagen SEHO como boton de cerrado
boton_cerrar = tk.Button(
    frame, image=logo_SEHO_tk, command=cerrar_ventana, borderwidth=0, bg="white")
boton_cerrar.grid(row=0, column=9, padx=0, pady=0, sticky="ne")

# Label Titulo: Buscador de resultados FCT EC-E
label_titulo = tk.Label(
    frame, text="Registro de defectos SEHO", fg="black", bg="white")
label_titulo.grid(row=0, column=1, columnspan=8,
                  padx=0, pady=0)

# -------------------------------------Row 1---------------------------------------------------------------------------

# Label titulo defectos
label_titulo_defectos = tk.Label(
    frame, text="Defectos", fg="black", bg="#FFC000")
label_titulo_defectos.grid(row=1, column=0, columnspan=10,
                           padx=0, pady=0, sticky="nsew")

# -------------------------------------Row 2---------------------------------------------------------------------------

# label defecto: Falta de soldadura
label_falta_de_soldadura = tk.Label(
    frame, text="Falta de soldadura:", fg="black", bg="white")
label_falta_de_soldadura.grid(
    row=2, column=0, padx=0, pady=0, sticky="e")

# Entrada: Falta de soldadura
entry_falta_de_soldadura = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_de_soldadura.grid(row=2, column=1, padx=0, pady=0, sticky="w")
entry_falta_de_soldadura.bind("<KeyRelease>", actualizar_suma_defectos)

# Frame3 label: Exceso de soldadura
label_exceso_de_soldadura = tk.Label(
    frame, text="Exceso de soldadura:", fg="black", bg="white")
label_exceso_de_soldadura.grid(
    row=2, column=2, padx=0, pady=0, sticky="e")

# Entrada: Exceso de soldadura
entry_exceso_de_soldadura = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_exceso_de_soldadura.grid(row=2, column=3, padx=0, pady=0, sticky="w")
entry_exceso_de_soldadura.bind("<KeyRelease>", actualizar_suma_defectos)

# Frame3 label: Cortos
label_cortos = tk.Label(frame, text="Cortos:", fg="black", bg="white")
label_cortos.grid(row=2, column=4, padx=0, pady=0, sticky="e")

# Entrada: Cortos
entry_cortos = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_cortos.grid(row=2, column=5, padx=0, pady=0, sticky="w")
entry_cortos.bind("<KeyRelease>", actualizar_suma_defectos)

# Frame3 label: Falta de housing
label_falta_de_housing = tk.Label(
    frame, text="Falta de housing:", fg="black", bg="white")
label_falta_de_housing.grid(
    row=2, column=6, padx=0, pady=0, sticky="e")

# Entrada: Falta de housing
entry_falta_de_housing = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_de_housing.grid(row=2, column=7, padx=0, pady=0, sticky="w")
entry_falta_de_housing.bind("<KeyRelease>", actualizar_suma_defectos)

# Frame3 label defecto: Comp. SMT dañado
label_com_smt_dañado = tk.Label(
    frame, text="Comp. SMT dañado:", fg="black", bg="white")
label_com_smt_dañado.grid(row=2, column=8, padx=0, sticky="e")

# Entrada: Comp. SMT dañado
entry_com_smt_dañado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_com_smt_dañado.grid(row=2, column=9, padx=0, sticky="w")
entry_com_smt_dañado.bind("<KeyRelease>", actualizar_suma_defectos)
# -------------------------------------Row 3---------------------------------------------------------------------------
# label defecto: Falta comp. SMT
label_falta_comp_smt = tk.Label(
    frame, text="Falta comp. SMT:", fg="black", bg="white")
label_falta_comp_smt.grid(row=3, column=0, padx=0, sticky="e")

# Entrada: Falta comp. SMT:
entry_falta_comp_smt = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_comp_smt.grid(row=3, column=1, padx=0, sticky="w")
entry_falta_comp_smt.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Falta de conector
label_falta_conector = tk.Label(
    frame, text="Falta de conector:", fg="black", bg="white")
label_falta_conector.grid(row=3, column=2, padx=0, sticky="e")

# Entrada: Falta de conector
entry_falta_conector = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_conector.grid(row=3, column=3, padx=0, sticky="w")
entry_falta_conector.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Housing dañado
label_housing_dañado = tk.Label(
    frame, text="Housing dañado:", fg="black", bg="white")
label_housing_dañado.grid(row=3, column=4, padx=0, sticky="e")

# Entrada: Housing dañado
entry_housing_dañado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_housing_dañado.grid(row=3, column=5, padx=0, sticky="w")
entry_housing_dañado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Comp. THT dañado
label_com_tht_dañado = tk.Label(
    frame, text="Comp. THT dañado:", fg="black", bg="white")
label_com_tht_dañado.grid(row=3, column=6, padx=0, sticky="e")

# Entrada: Comp. THT dañado
entry_com_tht_dañado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_com_tht_dañado.grid(row=3, column=7, padx=0, sticky="w")
entry_com_tht_dañado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Falta comp. THT
label_falta_comp_tht = tk.Label(
    frame, text="Falta comp. THT:", fg="black", bg="white")
label_falta_comp_tht.grid(row=3, column=8, padx=0, sticky="e")

# Entrada: Falta comp. THT:
entry_falta_comp_tht = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_comp_tht.grid(row=3, column=9, padx=0, sticky="w")
entry_falta_comp_tht.bind("<KeyRelease>", actualizar_suma_defectos)

# -------------------------------------Row 4---------------------------------------------------------------------------

# label defecto: Conector levantado
label_conector_levantado = tk.Label(
    frame, text="Conector levantado:", fg="black", bg="white")
label_conector_levantado.grid(row=4, column=0, padx=0, sticky="e")

# Entrada: Conector levantado
entry_conector_levantado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_conector_levantado.grid(row=4, column=1, padx=0, sticky="w")
entry_conector_levantado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Housing quemado:
label_housing_quemado = tk.Label(
    frame, text="Housing quemado:", fg="black", bg="white")
label_housing_quemado.grid(row=4, column=2, padx=0, sticky="e")

# Entrada: Housing quemado
entry_housing_quemado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_housing_quemado.grid(row=4, column=3, padx=0, sticky="w")
entry_housing_quemado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Comp. SMT levantado
label_comp_smt_levantado = tk.Label(
    frame, text="Comp. SMT levantado:", fg="black", bg="white")
label_comp_smt_levantado.grid(row=4, column=4, padx=0, sticky="e")

# Entrada: Comp. SMT levantado
entry_comp_smt_levantado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_comp_smt_levantado.grid(row=4, column=5, padx=0, sticky="w")
entry_comp_smt_levantado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Comp. THT levantado
label_comp_tht_levantado = tk.Label(
    frame, text="Comp. THT levantado:", fg="black", bg="white")
label_comp_tht_levantado.grid(row=4, column=6, padx=0, sticky="e")

# Entrada: Comp. THT levantado
entry_comp_tht_levantado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_comp_tht_levantado.grid(row=4, column=7, padx=0, sticky="w")
entry_comp_tht_levantado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Bola de soldadura
label_bola_soldadura = tk.Label(
    frame, text="Bola de soldadura:", fg="black", bg="white")
label_bola_soldadura.grid(row=4, column=8, padx=0, sticky="e")

# Entrada: Bola de soldadura
entry_bola_soldadura = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_bola_soldadura.grid(row=4, column=9, padx=0, sticky="w")
entry_bola_soldadura.bind("<KeyRelease>", actualizar_suma_defectos)


# -------------------------------------Row 5---------------------------------------------------------------------------
# label defecto: Cable dañado
label_cable_dañado = tk.Label(
    frame, text="Cable dañado:", fg="black", bg="white")
label_cable_dañado.grid(row=5, column=0, padx=0, sticky="e")

# Entrada: Cable dañado
entry_cable_dañado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_cable_dañado.grid(row=5, column=1, padx=0, sticky="w")
entry_cable_dañado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Falta de cable
label_falta_cable = tk.Label(
    frame, text="Falta de cable:", fg="black", bg="white")
label_falta_cable.grid(row=5, column=2, padx=0, sticky="e")

# Entrada: Falta de cable:
entry_falta_cable = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_cable.grid(row=5, column=3, padx=0, sticky="w")
entry_falta_cable.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Cable suelto
label_cable_suelto = tk.Label(
    frame, text="Cable suelto:", fg="black", bg="white")
label_cable_suelto.grid(row=5, column=4, padx=0, sticky="e")

# Entrada: Cable suelto
entry_cable_suelto = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_cable_suelto.grid(row=5, column=5, padx=0, sticky="w")
entry_cable_suelto.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Cable quemado
label_cable_quemado = tk.Label(
    frame, text="Cable quemado:", fg="black", bg="white")
label_cable_quemado.grid(row=5, column=6, padx=0, sticky="e")

# Entrada: Cable quemado
entry_cable_quemado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_cable_quemado.grid(row=5, column=7, padx=0, sticky="w")
entry_cable_quemado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Terminales iguales
label_terminales_iguales = tk.Label(
    frame, text="Terminales iguales:", fg="black", bg="white")
label_terminales_iguales.grid(row=5, column=8, padx=0, sticky="e")

# Entrada: Terminales iguales:
entry_terminales_iguales = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_terminales_iguales.grid(row=5, column=9, padx=0, sticky="w")
entry_terminales_iguales.bind("<KeyRelease>", actualizar_suma_defectos)

# -------------------------------------Row 6---------------------------------------------------------------------------

# label defecto: L1 dañado
label_l1_dañado = tk.Label(
    frame, text="L1 dañado:", fg="black", bg="white")
label_l1_dañado.grid(row=6, column=0, padx=0, sticky="e")

# Entrada: L1 dañado
entry_l1_dañado = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_l1_dañado.grid(row=6, column=1, padx=0, sticky="w")
entry_l1_dañado.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Pin largo
label_pin_largo = tk.Label(
    frame, text="Pin largo:", fg="black", bg="white")
label_pin_largo.grid(row=6, column=2, padx=0, sticky="e")

# Entrada: Pin largo
entry_pin_largo = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_pin_largo.grid(row=6, column=3, padx=0, sticky="w")
entry_pin_largo.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Falta de evidencia de pin
label_falta_evidencia_pin = tk.Label(
    frame, text="Falta de evidencia de pin:", fg="black", bg="white")
label_falta_evidencia_pin.grid(row=6, column=4, padx=0, sticky="e")

# Entrada: Falta de evidencia de pin
entry_falta_evidencia_pin = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_falta_evidencia_pin.grid(row=6, column=5, padx=0, sticky="w")
entry_falta_evidencia_pin.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Cable invertido:
label_cable_invertido = tk.Label(
    frame, text="Cable invertido:", fg="black", bg="white")
label_cable_invertido.grid(row=6, column=6, padx=0, sticky="e")

# Entrada: Cable invertido:
entry_cable_invertido = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_cable_invertido.grid(row=6, column=7, padx=0, sticky="w")
entry_cable_invertido.bind("<KeyRelease>", actualizar_suma_defectos)

# label defecto: Terminales desalineadas:
label_terminales_chuecas = tk.Label(
    frame, text="Terminales desalineadas:", fg="black", bg="white")
label_terminales_chuecas.grid(row=6, column=8, padx=0, sticky="e")

# Entrada: Terminales desalineadas
entry_terminales_chuecas = tk.Entry(
    frame, width=5, bg="#AEAEAE", justify="center")
entry_terminales_chuecas.grid(row=6, column=9, padx=0, sticky="w")
entry_terminales_chuecas.bind("<KeyRelease>", actualizar_suma_defectos)


# -------------------------------------Row 7---------------------------------------------------------------------------
# Número de pallet:
label_numero_pallet = tk.Label(
    frame, text="Número de pallet:", fg="black", bg="white", anchor="s")
label_numero_pallet.grid(row=7, column=0, columnspan=10,
                         padx=0, pady=0, sticky="s")

# -------------------------------------Row 8---------------------------------------------------------------------------
# Entrada pallet
entry_pallet = tk.Entry(frame, width=25, justify="center", background="springgreen",
                        border=3)
entry_pallet.grid(row=8, column=0, columnspan=10, padx=0, pady=0, sticky="n")
entry_pallet.focus()
entry_pallet.bind("<KeyRelease>", fun_buscar_fpy_pallets)
entry_pallet.bind('<Return>', guardar_datos)
# -------------------------------------Frame3 Row 0--------------------------------------------------------------------

# Label titulo: Defectos
label_defectos_ti = tk.Label(
    frame3, text="Defectos:", fg="black", bg="#EAEAEA", justify="right", width=10, anchor="e")
label_defectos_ti.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")

# Contador: Defectos
entry_defectos_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_defectos_con.grid(row=0, column=1, padx=0, pady=10, sticky="nsew")

# Label titulo: Modelo
label_modelo_ti = tk.Label(
    frame3, text="Modelo:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_modelo_ti.grid(row=0, column=2, padx=0, pady=10, sticky="nsew")

# Contador: Modelo
entry_modelo_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_modelo_con.grid(row=0, column=3, padx=0, pady=10, sticky="nsew")

# Label titulo: Estandar
label_estandar_ti = tk.Label(
    frame3, text="Estandar:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_estandar_ti.grid(row=0, column=4, padx=0, pady=10, sticky="nsew")

# Contador: Estandar
entry_estandar_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_estandar_con.grid(row=0, column=5, padx=0, pady=10, sticky="nsew")

# Label titulo: FPY pallet
label_fpy_pallet_ti = tk.Label(
    frame3, text="FPY pallet:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_fpy_pallet_ti.grid(row=0, column=6, padx=0, pady=10, sticky="nsew")

# Contador: FPY pallet
entry_fpy_pallet_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_fpy_pallet_con.grid(row=0, column=7, padx=0, pady=10, sticky="nsew")

# Label titulo: Wave-1
label_wave_1_ti = tk.Label(
    frame3, text="Wave 1:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_wave_1_ti.grid(row=0, column=8, padx=0, pady=10, sticky="nsew")

# Contador: Wave-1
entry_wave_1_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_wave_1_con.grid(row=0, column=9, padx=0, pady=10, sticky="nsew")

# Label titulo: Wave-2
label_wave_2_ti = tk.Label(
    frame3, text="Wave 2:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_wave_2_ti.grid(row=0, column=10, padx=0, pady=10, sticky="nsew")

# Contador: Wave-2
entry_wave_2_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_wave_2_con.grid(row=0, column=11, padx=0, pady=10, sticky="nsew")

# Label titulo: Flux
label_flux_ti = tk.Label(
    frame3, text="Flux:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_flux_ti.grid(row=0, column=12, padx=0, pady=10, sticky="nsew")

# Contador: Flux
entry_flux_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_flux_con.grid(row=0, column=13, padx=0, pady=10, sticky="nsew")

# Label titulo: Conveyor
label_conveyor_ti = tk.Label(
    frame3, text="Conveyor:", fg="black", bg="#EAEAEA", justify="right", anchor="e")
label_conveyor_ti.grid(row=0, column=14, padx=0, pady=10, sticky="nsew")

# Contador: Conveyor
entry_conveyor_con = tk.Entry(
    frame3, width=10, bg="#AEAEAE", justify="center", bd=0)
entry_conveyor_con.grid(row=0, column=15, padx=0, pady=10, sticky="nsew")

# -------------------------------------Frame2 Row 0--------------------------------------------------------------------
# Valores iniciales
hora_inicio_var = tk.StringVar(value="12")
minuto_inicio_var = tk.StringVar(value="00")
periodo_inicio_var = tk.StringVar(value="AM")

# Label: Horario
label_horario = tk.Label(frame2, text="<- Horario ->",
                         fg="black", bg="white", width=10)
label_horario.grid(row=0, column=3, sticky="nsew")

# Seleccion: Hora de inicio
Hora_inicio = tk.Spinbox(frame2, from_=1, to=12, textvariable=hora_inicio_var,
                         wrap=True, width=3, fg="black", bg="#AEAEAE", justify="center")
Hora_inicio.grid(row=0, column=2, sticky="w")
Minuto_inicio = tk.Spinbox(frame2, from_=0, to=59, textvariable=minuto_inicio_var,
                           wrap=True, width=3, fg="black", bg="#AEAEAE", justify="center")
Minuto_inicio.grid(row=0, column=2)
Periodo_inicio = tk.Spinbox(frame2, values=("AM", "PM"), textvariable=periodo_inicio_var,
                            wrap=True, width=3, fg="black", bg="#AEAEAE", justify="center")
Periodo_inicio.grid(row=0, column=2, sticky="e")

# Valores finales
hora_fin_var = tk.StringVar(value="11")
minuto_fin_var = tk.StringVar(value="59")
periodo_fin_var = tk.StringVar(value="PM")

Hora_final = tk.Spinbox(frame2, from_=1, to=12, textvariable=hora_fin_var,
                        wrap=True, width=3, fg="black", bg="#AEAEAE", justify="center")
Hora_final.grid(row=0, column=4, sticky="w")
Minuto_final = tk.Spinbox(frame2, from_=0, to=59, textvariable=minuto_fin_var,
                          wrap=True, width=3, fg="black", bg="#AEAEAE", justify="center")
Minuto_final.grid(row=0, column=4)
Periodo_Final = tk.Spinbox(frame2, values=("PM", "AM"), textvariable=periodo_fin_var,
                           wrap=True, width=3, fg="black", bg="#AEAEAE", justify="center")
Periodo_Final.grid(row=0, column=4, sticky="e")
# -------------------------------------Frame2 Row 1--------------------------------------------------------------------

# Modelo: Lion Mite
label_lm = tk.Label(frame2, text="Lion Mite",
                    fg="black", bg="#ADD8E6", width=10)
label_lm.grid(row=1, column=1, sticky="nsew")

# Modelo: ROTOZIP
label_rz = tk.Label(frame2, text="ROTOZIP", fg="black", bg="#98FF98", width=10)
label_rz.grid(row=1, column=2, sticky="nsew")

# Modelo: Router
label_ROUTER = tk.Label(frame2, text="ROUTER",
                        fg="black", bg="#FFFACD", width=10)
label_ROUTER.grid(row=1, column=3, sticky="nsew")

# Modelo: PR20
label_pr20 = tk.Label(frame2, text="PR20",
                      fg="black", bg="#FFDAB9", width=10)
label_pr20.grid(row=1, column=4, sticky="nsew")

# Modelo: FA08
label_fa08 = tk.Label(frame2, text="FA08", fg="black", bg="#FFB6C1", width=10)
label_fa08.grid(row=1, column=5, padx=0, pady=0, sticky="nsew")

# Modelo: HLA
label_HLA = tk.Label(frame2, text="HLA", fg="black", bg="#E6E6FA", width=10)
label_HLA.grid(row=1, column=6, padx=0, pady=0, sticky="nsew")

# Modelo: BGA200
label_BGA200 = tk.Label(frame2, text="BGA200",
                        fg="black", bg="#C4DFAA", width=10)
label_BGA200.grid(row=1, column=7, padx=0, pady=0, sticky="nsew")

# Modelo: FSA135
label_FSA135 = tk.Label(frame2, text="FSA135",
                        fg="black", bg="#AFEEEE", width=10)
label_FSA135.grid(row=1, column=8, padx=0, pady=0, sticky="nsew")


# Modelo: DC-I
label_dc_i = tk.Label(frame2, text="DC-I", fg="black", bg="#B0C4DE", width=10)
label_dc_i.grid(row=1, column=9, padx=0, pady=0, sticky="nsew")

# Modelo: LOCUS
label_locus = tk.Label(frame2, text="LOCUS", fg="black",
                       bg="#FFA07A", width=10)
label_locus.grid(row=1, column=10, padx=0, pady=0, sticky="nsew")
# -------------------------------------Frame2 Row 2--------------------------------------------------------------------
# label: Defectos2
label_defectos_2 = tk.Label(frame2, text="Defectos:", fg="black",
                            bg="#FFFFC9", width=10, anchor="e")
label_defectos_2.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")

# Defectos: Lion Mite
entry_con_def_lm = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_def_lm.grid(row=2, column=1, padx=0, pady=0, sticky="nsew")

# Defectos: Rotozip
entry_con_def_rz = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_def_rz.grid(row=2, column=2, padx=0, pady=0, sticky="nsew")

# Defectos: Router
entry_con_def_router = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_def_router.grid(row=2, column=3, padx=0, pady=0, sticky="nsew")

# Defectos: PR20
entry_con_def_pr20 = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_def_pr20.grid(row=2, column=4, padx=0, pady=0, sticky="nsew")

# Defectos: FA08
entry_con_def_fa08 = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_def_fa08.grid(row=2, column=5, padx=0, pady=0, sticky="nsew")

# Defectos: HLA
entry_con_def_hla = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_def_hla.grid(row=2, column=6, padx=0, pady=0, sticky="nsew")

# Defectos: BGA200
entry_con_def_bga200 = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_def_bga200.grid(row=2, column=7, padx=0, pady=0, sticky="nsew")

# Defectos: FSA135
entry_con_def_fsa135 = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_def_fsa135.grid(row=2, column=8, padx=0, pady=0, sticky="nsew")


# Defectos: DC-I
entry_con_def_dc_i = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_def_dc_i.grid(row=2, column=9, padx=0, pady=0, sticky="nsew")

# Defectos: LOCUS
entry_con_def_locus = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_def_locus.grid(row=2, column=10, padx=0, pady=0, sticky="nsew")

# -------------------------------------Frame2 Row 3--------------------------------------------------------------------
# label: Producido
label_producido = tk.Label(frame2, text="Producido:", fg="black",
                           bg="#FFFFC9", width=10, anchor="e")
label_producido.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

# Estandar: Lion Mite
entry_con_estan_lm = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_estan_lm.grid(row=3, column=1, padx=0, pady=0, sticky="nsew")

# Estandar: Rotozip
entry_con_estan_rz = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_estan_rz.grid(row=3, column=2, padx=0, pady=0, sticky="nsew")

# Estandar: Router
entry_con_estan_router = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_estan_router.grid(row=3, column=3, padx=0, pady=0, sticky="nsew")

# Estandar: PR20
entry_con_estan_pr20 = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_estan_pr20.grid(row=3, column=4, padx=0, pady=0, sticky="nsew")

# Estandar: FA08
entry_con_estan_fa08 = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_estan_fa08.grid(row=3, column=5, padx=0, pady=0, sticky="nsew")

# Estandar: HLA
entry_con_estan_hla = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_estan_hla.grid(row=3, column=6, padx=0, pady=0, sticky="nsew")

# Estandar: BGA200
entry_con_estan_bga200 = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_estan_bga200.grid(row=3, column=7, padx=0, pady=0, sticky="nsew")

# Estandar: FSA135
entry_con_estan_fsa135 = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_estan_fsa135.grid(row=3, column=8, padx=0, pady=0, sticky="nsew")


# Estandar: DC-I
entry_con_estan_dc_i = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_con_estan_dc_i.grid(row=3, column=9, padx=0, pady=0, sticky="nsew")

# Estandar: Locus
entry_con_estan_locus = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_con_estan_locus.grid(row=3, column=10, padx=0, pady=0, sticky="nsew")

# -------------------------------------Frame2 Row 4--------------------------------------------------------------------
# label: FPY
label_Fpy = tk.Label(frame2, text="FPY:", fg="black",
                     bg="#FFFFC9", width=10, anchor="e")
label_Fpy.grid(row=4, column=0, padx=0, pady=0, sticky="nsew")

# FPY: Lion Mite
entry_fpy_lion = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_fpy_lion.grid(row=4, column=1, padx=0, pady=0, sticky="nsew")

# FPY: Rotozip
entry_fpy_rz = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_fpy_rz.grid(row=4, column=2, padx=0, pady=0, sticky="nsew")

# FPY: Router
entry_fpy_router = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_fpy_router.grid(row=4, column=3, padx=0, pady=0, sticky="nsew")

# FPY: PR20
entry_fpy_pr20 = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_fpy_pr20.grid(row=4, column=4, padx=0, pady=0, sticky="nsew")

# FPY: FA08
entry_fpy_fa08 = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_fpy_fa08.grid(row=4, column=5, padx=0, pady=0, sticky="nsew")

# FPY: HLA
entry_fpy_hla = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_fpy_hla.grid(row=4, column=6, padx=0, pady=0, sticky="nsew")

# FPY: BGA200
entry_fpy_bga200 = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_fpy_bga200.grid(row=4, column=7, padx=0, pady=0, sticky="nsew")

# FPY: FSA135
entry_fpy_fsa135 = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_fpy_fsa135.grid(row=4, column=8, padx=0, pady=0, sticky="nsew")

# FPY: DC-I
entry_fpy_dc_i = tk.Entry(
    frame2, width=10, bg="#ECECEC", justify="center", bd=0)
entry_fpy_dc_i.grid(row=4, column=9, padx=0, pady=0, sticky="nsew")

# FPY: Locus
entry_fpy_locus = tk.Entry(
    frame2, width=10, bg="#CDCDCD", justify="center", bd=0)
entry_fpy_locus.grid(row=4, column=10, padx=0, pady=0, sticky="nsew")

# -------------------------------------Frame2 Row 5--------------------------------------------------------------------
# Boton Reset: Lion Mite
reset_lm = tk.Button(frame2, text="Reset", height=0, width=0,
                     border=5, background="deepskyblue",  command=lambda: modificar_csv("Lion Mite", "ResetLion Mite"))
reset_lm.grid(row=5, column=1, padx=0, pady=0, sticky="nsew")

# Boton Reset: RotoZip
reset_rotozip = tk.Button(frame2, text="Reset", height=0, width=0,
                          border=5, background="deepskyblue", command=lambda: modificar_csv("ROTOZIP", "ResetROTOZIP"))
reset_rotozip.grid(row=5, column=2, padx=0, pady=0, sticky="nsew")

# Boton Reset: Router
reset_router = tk.Button(frame2, text="Reset", height=0, width=0,
                         border=5, background="deepskyblue", command=lambda: modificar_csv("ROUTER 1617", "ResetROUTER 1617"))
reset_router.grid(row=5, column=3, padx=0, pady=0, sticky="nsew")

# Boton Reset: PR20
reset_pr20 = tk.Button(frame2, text="Reset", height=0, width=0,
                       border=5, background="deepskyblue", command=lambda: modificar_csv("PR20", "ResetPR20"))
reset_pr20.grid(row=5, column=4, padx=0, pady=0, sticky="nsew")

# Boton Reset: FA08
reset_fa08 = tk.Button(frame2, text="Reset", height=0, width=0,
                       border=5, background="deepskyblue", command=lambda: modificar_csv("FA08", "ResetFA08"))
reset_fa08.grid(row=5, column=5, padx=0, pady=0, sticky="nsew")

# Boton Reset: HLA
reset_hla = tk.Button(frame2, text="Reset", height=0, width=0,
                      border=5, background="deepskyblue", command=lambda: modificar_csv("HLA", "ResetHLA"))
reset_hla.grid(row=5, column=6, padx=0, pady=0, sticky="nsew")

# Boton Reset: BGA200
reset_bga200 = tk.Button(frame2, text="Reset", height=0, width=0,
                         border=5, background="deepskyblue", command=lambda: modificar_csv("BGA200", "ResetBGA200"))
reset_bga200.grid(row=5, column=7, padx=0, pady=0, sticky="nsew")

# Boton Reset: FSA135
reset_fsa135 = tk.Button(frame2, text="Reset", height=0, width=0,
                         border=5, background="deepskyblue", command=lambda: modificar_csv("FSA135", "ResetFSA135"))
reset_fsa135.grid(row=5, column=8, padx=0, pady=0, sticky="nsew")

# Boton Reset: DC-I
reset_dci = tk.Button(frame2, text="Reset", height=0, width=0,
                      border=5, background="deepskyblue", command=lambda: modificar_csv("DC-I", "ResetDC-I"))
reset_dci.grid(row=5, column=9, padx=0, pady=0, sticky="nsew")

# Boton Reset: LOCUS
reset_locus = tk.Button(frame2, text="Reset", height=0, width=0,
                        border=5, background="deepskyblue", command=lambda: modificar_csv("LOCUS", "ResetLOCUS"))
reset_locus.grid(row=5, column=10, padx=0, pady=0, sticky="nsew")
# -------------------------------------Frame2 Row 6--------------------------------------------------------------------
# label: FPY_Total
label_fpyTotal = tk.Label(frame2, text="FPY Total:", fg="black",
                          bg="#E97132", width=10, anchor="e")
label_fpyTotal.grid(row=6, column=0, padx=0, pady=0, sticky="nsew")
# -------------------------------------Frame2 Row 7--------------------------------------------------------------------
# label: TopDefectos
label_TopDefectos = tk.Label(frame2, text="TopDefectos:", fg="black",
                             bg="#F2CEEF", width=10, anchor="e")
label_TopDefectos.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")
# -------------------------------------Frame2 Row 8--------------------------------------------------------------------
# label: TotalDefectos
label_TotalDefectos = tk.Label(frame2, text="TotalDefectos:", fg="black",
                               bg="#F2CEEF", width=10, anchor="e")
label_TotalDefectos.grid(row=8, column=0, padx=0, pady=0, sticky="nsew")
# -------------------------------------Frame2 Row 9-------------------------------------------------------------------
# label: TotalDefectos
label_PorDefectos = tk.Label(frame2, text="%Defectos:", fg="black",
                             bg="#F2CEEF", width=10, anchor="e")
label_PorDefectos.grid(row=9, column=0, padx=0, pady=0, sticky="nsew")
# -------------------------------------Frame2 Row 10-------------------------------------------------------------------
# Label: Fecha mostrada
entry_fecha_con = tk.Entry(
    frame2, width=10, bg="white", justify="right", bd=0)
entry_fecha_con.grid(row=10, column=0, padx=0, pady=0, sticky="sew")

# Label: Hora mostrada
entry_hora_con = tk.Entry(
    frame2, width=10, bg="white", justify="center", bd=0)
entry_hora_con.grid(row=10, column=1, padx=0, pady=0, sticky="sew")

# Boton open: Defectos
boton_defectos = tk.Button(frame2, text="Defectos", height=0, width=0,
                           border=5, bg="#4EA72E", fg="#333333")
boton_defectos.grid(row=10, column=4, padx=0, pady=0, sticky="nsew")

# Boton open: Parámetros
boton_parametros = tk.Button(frame2, text="Parámetros", height=0, width=0,
                             border=5, bg="#93D1ED", fg="#333333", command=abrir_ventana_parametros)
boton_parametros.grid(row=10, column=5, padx=0, pady=0, sticky="nsew")

# Boton open: LogFileRegistro
boton_logfileregistro = tk.Button(frame2, text="Registro", height=0, width=0,
                                  border=5, bg="#0F9ED5", fg="#333333", command=abrir_ventana_csv_registro)
boton_logfileregistro.grid(row=10, column=6, padx=0, pady=0, sticky="nsew")

# Boton open: LogFileTotal
boton_logfiletotal = tk.Button(frame2, text="LogFile", height=0, width=0,
                               border=5, bg="#E97132", fg="#333333", command=abrir_ventana_csv)
boton_logfiletotal.grid(row=10, column=7, padx=0, pady=0, sticky="nsew")


# label: By
label_By = tk.Label(frame2, text="Rev 7.0 (By:Oscar Tovar)", fg="black",
                    bg="white", width=10, anchor="e")
label_By.grid(row=10, column=9, columnspan=2, padx=0, pady=0, sticky="sew")
# ---------------------------------------------------------------------------------------------------------------------

frame.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=1, column=0, sticky="nsew")
frame2.grid(row=2, column=0, sticky="nsew")

if __name__ == "__main__":
    actualizar_fecha_hora()
    ajustar_escala()
    ventana.after(500, inicio)
    ventana.mainloop()
