# Creación de aplicación de registros de defectos SEHO en python para no depender de Excel
# ------- libraries
import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
from tkinter import ttk
import time
import sys
from PIL import Image, ImageTk
import pandas as pd
import chardet
from tkcalendar import DateEntry
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import io
import matplotlib.colors as mcolors
import socket
import tkinter.font as tkfont


# ------------------------------------- Logic -------------------------------------------------------------------------
def bloquear_instancia():
    """Función para evitar abrir varias veces el programa"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("127.0.0.1", 65432))  # Puerto único
    except socket.error:
        messagebox.showinfo("El programa ya está abierto.")
        sys.exit()


bloquear_instancia()


def settings_root(clave):
    """Function to load settings."""
    try:
        with open("C:/Registro_defectos_SEHO/root_settings.ini", "r",  encoding="utf-8") as config:
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


# Ruta del segundo archivo CSV
csv_file = settings_root("LogFile")
csv_file2 = settings_root("Registro")
guardando_en_progreso = False

# ==============================
# CACHE GLOBAL MULTI CSV
# ==============================

df_cache = None
defect_names_cache = None

csv_files = [csv_file, csv_file2]

csv_cache_mtime = {}


def cargar_datos_cache():

    global df_cache
    global defect_names_cache
    global csv_cache_mtime

    recargar = False

    # ==============================
    # VERIFICAR SI CAMBIO ALGUN CSV
    # ==============================

    for file in csv_files:

        mtime = os.path.getmtime(file)

        if file not in csv_cache_mtime or csv_cache_mtime[file] != mtime:

            csv_cache_mtime[file] = mtime

            recargar = True

    # ==============================
    # CARGAR CSV SI CAMBIO
    # ==============================

    if df_cache is None or recargar:

        lista_df = []

        for file in csv_files:

            df_temp = pd.read_csv(file, encoding="utf-8")

            df_temp.columns = df_temp.columns.str.strip()

            df_temp["Fecha/Hora"] = pd.to_datetime(
                df_temp["Fecha/Hora"],
                format="%d/%m/%Y %H:%M:%S"
            )

            lista_df.append(df_temp)

        # unir todos

        df_cache = pd.concat(lista_df, ignore_index=True)

    # ==============================
    # DEFECTOS
    # ==============================

    if defect_names_cache is None:

        defect_names_cache = []

        with open("C:/Registro_defectos_SEHO/defects.ini", encoding="utf-8") as f:

            for line in f:

                line = line.strip()

                if not line or "=" not in line:
                    continue

                _, value = line.split("=", 1)

                defect_names_cache.append(value.strip())

    return df_cache, defect_names_cache


def settings_defects(clave):
    """Función para cargar defectos."""
    try:
        with open("C:/Registro_defectos_SEHO/defects.ini", "r",  encoding="utf-8") as config:
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


def settings_part_numbers(clave):
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


def settings_limits(clave):
    """Función para cargar defectos."""
    try:
        with open("C:/Registro_defectos_SEHO/limits.ini", "r",  encoding="utf-8") as config:
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


def toggle_minimize():
    """Function minimize root."""
    root.iconify()


def cerrar_ventana():
    """Function closed root."""
    enviar_comando_rb(b"H\r")
    root.destroy()
    sys.exit()


def root_scale():
    """Function root scale."""

    # Obtener el tamaño de la pantalla
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()

    # Calcular el factor de escala basado en una resolución de referencia (1920x1080)
    escala_x = pantalla_ancho / 1920
    escala_y = pantalla_alto / 1080
    escala = min(escala_x, escala_y)
    Frame0.config(padx=0 * escala, pady=0 * escala)
    Frame1.config(padx=0 * escala, pady=0 * escala)
    Frame2.config(padx=0 * escala, pady=0 * escala)
    Frame3.config(padx=0 * escala, pady=0 * escala)
    Frame4.config(padx=0 * escala, pady=0 * escala)
    Frame5.config(padx=0 * escala, pady=0 * escala)

    # Ajustar el tamaño de la fuente
    fuente_8 = int(8 * escala)
    fuente_10 = int(10 * escala)
    fuente_12 = int(12 * escala)
    fuente_14 = int(14 * escala)
    fuente_16 = int(16 * escala)
    fuente_20 = int(20 * escala)
    fuente_22 = int(22 * escala)
    fuente_28 = int(28 * escala)
    fuente_30 = int(30 * escala)
    fuente_40 = int(40 * escala)
    fuente_50 = int(50 * escala)
    fuente_70 = int(70 * escala)
    defct = int(18 * escala)
    part_number = int(14 * escala)
    datos = int(16 * escala)
    horarios = int(14 * escala)
    etiquetas_parte_1 = int(13 * escala)
    bloque_1 = int(20 * escala)
    button_reset = int(12 * escala)
    button_ventanas = int(10 * escala)
    etiquetas_parte_2 = int(11 * escala)
    bloque_2 = int(14 * escala)
    etiquetas_parte_3 = int(10 * escala)
    bloque_3 = int(10 * escala)
    bloque_4 = int(8 * escala)

    # --- label's
    label_0.config(font=("Arial", fuente_40, "bold"))  # Título
    label_1.config(font=("Arial", fuente_16, "bold"))  # Defectos
    label_2.config(font=("Arial", defct, "bold"))  # Defect
    label_3.config(font=("Arial", defct, "bold"))  # Defect
    label_4.config(font=("Arial", defct, "bold"))  # Defect
    label_5.config(font=("Arial", defct, "bold"))  # Defect
    label_6.config(font=("Arial", defct, "bold"))  # Defect
    label_7.config(font=("Arial", defct, "bold"))  # Defect
    label_8.config(font=("Arial", defct, "bold"))  # Defect
    label_9.config(font=("Arial", defct, "bold"))  # Defect
    label_10.config(font=("Arial", defct, "bold"))  # Defect
    label_11.config(font=("Arial", defct, "bold"))  # Defect
    label_12.config(font=("Arial", defct, "bold"))  # Defect
    label_13.config(font=("Arial", defct, "bold"))  # Defect
    label_14.config(font=("Arial", defct, "bold"))  # Defect
    label_15.config(font=("Arial", defct, "bold"))  # Defect
    label_16.config(font=("Arial", defct, "bold"))  # Defect
    label_17.config(font=("Arial", defct, "bold"))  # Defect
    label_18.config(font=("Arial", defct, "bold"))  # Defect
    label_19.config(font=("Arial", defct, "bold"))  # Defect
    label_20.config(font=("Arial", defct, "bold"))  # Defect
    label_21.config(font=("Arial", defct, "bold"))  # Defect
    label_22.config(font=("Arial", defct, "bold"))  # Defect
    label_23.config(font=("Arial", defct, "bold"))  # Defect
    label_24.config(font=("Arial", defct, "bold"))  # Defect
    label_25.config(font=("Arial", defct, "bold"))  # Defect
    label_26.config(font=("Arial", defct, "bold"))  # Defect
    label_27.config(font=("Arial", defct, "bold"))  # Defect
    label_28.config(font=("Arial", defct, "bold"))  # Defect
    label_29.config(font=("Arial", defct, "bold"))  # Defect
    label_30.config(font=("Arial", defct, "bold"))  # Defect
    label_31.config(font=("Arial", defct, "bold"))  # Defect
    label_32.config(font=("Arial", fuente_10, "bold"))  # Número de pallet
    label_33.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Defectos
    label_34.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # Defectos_resultado
    label_35.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Modelo
    label_36.config(font=("Arial", fuente_12, "bold"), bd=.5,
                    relief="ridge")  # Modelo_resultado
    label_37.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Estandar
    label_38.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # Estandar_resultado
    label_39.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # FPY pallet
    label_40.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # FPY pallet_resultado
    label_41.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Wave 1
    label_42.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # Wave 1_resultado
    label_43.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Wave 2
    label_44.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # Wave 2_resultado
    label_45.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Flux
    label_46.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # Flux_resultado
    label_47.config(font=("Arial", datos, "bold"),
                    bd=.5,  relief="ridge")  # Conveyor
    label_48.config(font=("Arial", datos, "bold"), bd=.5,
                    relief="ridge")  # Conveyor_resultado
    label_49.config(font=("Arial", horarios, "bold"))  # Horario
    label_50.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#44B3E1")  # Part#1
    label_51.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#CAEDFB")  # Part#2
    label_52.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#44B3E1")  # Part#3
    label_53.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#CAEDFB")  # Part#4
    label_54.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#44B3E1")  # Part#5
    label_55.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#CAEDFB")  # Part#6
    label_56.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#44B3E1")  # Part#7
    label_57.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#CAEDFB")  # Part#8
    label_58.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#44B3E1")  # Part#9
    label_59.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#CAEDFB")  # Part#10
    label_60.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#44B3E1")  # Part#11
    label_61.config(font=("Arial", part_number, "bold"), bd=.5,
                    relief="ridge", bg="#CAEDFB")  # Part#12
    label_62.config(font=("Arial", etiquetas_parte_1, "bold"))  # Defectos
    label_63.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#1
    label_64.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#2
    label_65.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#3
    label_66.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#4
    label_67.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#5
    label_68.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#6
    label_69.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#7
    label_70.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#8
    label_71.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#9
    label_72.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#10
    label_73.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#11
    label_74.config(font=("Arial", bloque_1, "bold"))  # Defectos Part#12
    label_75.config(font=("Arial", etiquetas_parte_1, "bold"))  # Producido
    label_76.config(font=("Arial", bloque_1, "bold"))  # Producido Part#1
    label_77.config(font=("Arial", bloque_1, "bold"))  # Producido Part#2
    label_78.config(font=("Arial", bloque_1, "bold"))  # Producido Part#3
    label_79.config(font=("Arial", bloque_1, "bold"))  # Producido Part#4
    label_80.config(font=("Arial", bloque_1, "bold"))  # Producido Part#5
    label_81.config(font=("Arial", bloque_1, "bold"))  # Producido Part#6
    label_82.config(font=("Arial", bloque_1, "bold"))  # Producido Part#7
    label_83.config(font=("Arial", bloque_1, "bold"))  # Producido Part#8
    label_84.config(font=("Arial", bloque_1, "bold"))  # Producido Part#9
    label_85.config(font=("Arial", bloque_1, "bold"))  # Producido Part#10
    label_86.config(font=("Arial", bloque_1, "bold"))  # Producido Part#11
    label_87.config(font=("Arial", bloque_1, "bold"))  # Producido Part#12
    label_88.config(font=("Arial", etiquetas_parte_1, "bold"))  # FPY
    label_89.config(font=("Arial", bloque_1, "bold"))  # FPY Part#1
    label_90.config(font=("Arial", bloque_1, "bold"))  # FPY Part#2
    label_91.config(font=("Arial", bloque_1, "bold"))  # FPY Part#3
    label_92.config(font=("Arial", bloque_1, "bold"))  # FPY Part#4
    label_93.config(font=("Arial", bloque_1, "bold"))  # FPY Part#5
    label_94.config(font=("Arial", bloque_1, "bold"))  # FPY Part#6
    label_95.config(font=("Arial", bloque_1, "bold"))  # FPY Part#7
    label_96.config(font=("Arial", bloque_1, "bold"))  # FPY Part#8
    label_97.config(font=("Arial", bloque_1, "bold"))  # FPY Part#9
    label_98.config(font=("Arial", bloque_1, "bold"))  # FPY Part#10
    label_99.config(font=("Arial", bloque_1, "bold"))  # FPY Part#11
    label_100.config(font=("Arial", bloque_1, "bold"))  # FPY Part#12
    label_101.config(font=("Arial", etiquetas_parte_2, "bold"))  # FPY Total
    label_102.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#1
    label_103.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#2
    label_104.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#3
    label_105.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#4
    label_106.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#5
    label_107.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#6
    label_108.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#7
    label_109.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#8
    label_110.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#9
    label_111.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#10
    label_112.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#11
    label_113.config(font=("Arial", bloque_2, "bold"))  # FPY Total Part#12
    label_114.config(font=("Arial", etiquetas_parte_2, "bold"))  # Total Defect
    label_115.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#1
    label_116.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#2
    label_117.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#3
    label_118.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#4
    label_119.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#5
    label_120.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#6
    label_121.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#7
    label_122.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#8
    label_123.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#9
    label_124.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#10
    label_125.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#11
    label_126.config(font=("Arial", bloque_2, "bold"))  # Total Defect Part#12
    label_127.config(font=("Arial", etiquetas_parte_2, "bold")
                     )  # Total Produc
    label_128.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#1
    label_129.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#2
    label_130.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#3
    label_131.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#4
    label_132.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#5
    label_133.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#6
    label_134.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#7
    label_135.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#8
    label_136.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#9
    label_137.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#10
    label_138.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#11
    label_139.config(font=("Arial", bloque_2, "bold"))  # Total Produc Part#12
    label_140.config(font=("Arial", etiquetas_parte_3, "bold"))  # TopDefect
    label_141.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#1
    label_142.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#2
    label_143.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#3
    label_144.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#4
    label_145.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#5
    label_146.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#6
    label_147.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#7
    label_148.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#8
    label_149.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#9
    label_150.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#10
    label_151.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#11
    label_152.config(font=("Arial", bloque_4, "bold"))  # TopDefect Part#12
    label_153.config(font=("Arial", etiquetas_parte_3, "bold")
                     )  # Cant.Defect Part#1
    label_154.config(font=("Arial", bloque_3, "bold"))  # Cant.pDefect Part#1
    label_155.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_156.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_157.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_158.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_159.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_160.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_161.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_162.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_163.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_164.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_165.config(font=("Arial", bloque_3, "bold"))  # Cant.Defect Part#1
    label_166.config(font=("Arial", etiquetas_parte_3, "bold")
                     )  # %Defect Part#1
    label_167.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_168.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_169.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_170.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_171.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_172.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_173.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_174.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_175.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_176.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_177.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_178.config(font=("Arial", bloque_3, "bold"))  # %Defect Part#1
    label_179.config(font=("Arial", fuente_12, "bold"))  # Fecha/Hora
    label_180.config(font=("Arial", fuente_8, "bold"))  # Rev

    # --- entry's
    entry_0.config(font=("Arial", defct, "bold"))  # Defect
    entry_1.config(font=("Arial", defct, "bold"))  # Defect
    entry_2.config(font=("Arial", defct, "bold"))  # Defect
    entry_3.config(font=("Arial", defct, "bold"))  # Defect
    entry_4.config(font=("Arial", defct, "bold"))  # Defect
    entry_5.config(font=("Arial", defct, "bold"))  # Defect
    entry_6.config(font=("Arial", defct, "bold"))  # Defect
    entry_7.config(font=("Arial", defct, "bold"))  # Defect
    entry_8.config(font=("Arial", defct, "bold"))  # Defect
    entry_9.config(font=("Arial", defct, "bold"))  # Defect
    entry_10.config(font=("Arial", defct, "bold"))  # Defect
    entry_11.config(font=("Arial", defct, "bold"))  # Defect
    entry_12.config(font=("Arial", defct, "bold"))  # Defect
    entry_13.config(font=("Arial", defct, "bold"))  # Defect
    entry_14.config(font=("Arial", defct, "bold"))  # Defect
    entry_15.config(font=("Arial", defct, "bold"))  # Defect
    entry_16.config(font=("Arial", defct, "bold"))  # Defect
    entry_17.config(font=("Arial", defct, "bold"))  # Defect
    entry_18.config(font=("Arial", defct, "bold"))  # Defect
    entry_19.config(font=("Arial", defct, "bold"))  # Defect
    entry_20.config(font=("Arial", defct, "bold"))  # Defect
    entry_21.config(font=("Arial", defct, "bold"))  # Defect
    entry_22.config(font=("Arial", defct, "bold"))  # Defect
    entry_23.config(font=("Arial", defct, "bold"))  # Defect
    entry_24.config(font=("Arial", defct, "bold"))  # Defect
    entry_25.config(font=("Arial", defct, "bold"))  # Defect
    entry_26.config(font=("Arial", defct, "bold"))  # Defect
    entry_27.config(font=("Arial", defct, "bold"))  # Defect
    entry_28.config(font=("Arial", defct, "bold"))  # Defect
    entry_29.config(font=("Arial", defct, "bold"))  # Defect
    entry_30.config(font=("Arial", fuente_28, "bold"))  # Pallet

    # --- spinbox's
    spinbox_0.config(font=("Arial", horarios, "bold"))  # Hora inicial
    spinbox_1.config(font=("Arial", horarios, "bold"))  # Minuto inicial
    spinbox_2.config(font=("Arial", horarios, "bold"))  # Periodo inicial
    spinbox_3.config(font=("Arial", horarios, "bold"))  # Hora final
    spinbox_4.config(font=("Arial", horarios, "bold"))  # Minuto final
    spinbox_5.config(font=("Arial", horarios, "bold"))  # Periodo final

    # --- button's
    button_0.config(font=("Arial", button_reset, "bold"))  # Reset Part#1
    button_1.config(font=("Arial", button_reset, "bold"))  # Reset Part#2
    button_2.config(font=("Arial", button_reset, "bold"))  # Reset Part#3
    button_3.config(font=("Arial", button_reset, "bold"))  # Reset Part#4
    button_4.config(font=("Arial", button_reset, "bold"))  # Reset Part#5
    button_5.config(font=("Arial", button_reset, "bold"))  # Reset Part#6
    button_6.config(font=("Arial", button_reset, "bold"))  # Reset Part#7
    button_7.config(font=("Arial", button_reset, "bold"))  # Reset Part#8
    button_8.config(font=("Arial", button_reset, "bold"))  # Reset Part#9
    button_9.config(font=("Arial", button_reset, "bold"))  # Reset Part#10
    button_10.config(font=("Arial", button_reset, "bold"))  # Reset Part#11
    button_11.config(font=("Arial", button_reset, "bold"))  # Reset Part#12
    button_12.config(font=("Arial", button_ventanas, "bold"))  # Defectos
    button_13.config(font=("Arial", button_ventanas, "bold"))  # Soprte
    button_14.config(font=("Arial", button_ventanas, "bold"))  # Parámetros
    button_15.config(font=("Arial", button_ventanas, "bold"))  # Registros
    button_16.config(font=("Arial", button_ventanas, "bold"))  # LogFile
    button_17.config(font=("Arial", fuente_10, "bold"))  # Actualizar


def suma_defectos(*args):
    """Function suma defec."""
    try:
        defecto_1 = int(entry_0.get() or 0)
        defecto_2 = int(entry_1.get() or 0)
        defecto_3 = int(entry_2.get() or 0)
        defecto_4 = int(entry_3.get() or 0)
        defecto_5 = int(entry_4.get() or 0)
        defecto_6 = int(entry_5.get() or 0)
        defecto_7 = int(entry_6.get() or 0)
        defecto_8 = int(entry_7.get() or 0)
        defecto_9 = int(entry_8.get() or 0)
        defecto_10 = int(entry_9.get() or 0)
        defecto_11 = int(entry_10.get() or 0)
        defecto_12 = int(entry_11.get() or 0)
        defecto_13 = int(entry_12.get() or 0)
        defecto_14 = int(entry_13.get() or 0)
        defecto_15 = int(entry_14.get() or 0)
        defecto_16 = int(entry_15.get() or 0)
        defecto_17 = int(entry_16.get() or 0)
        defecto_18 = int(entry_17.get() or 0)
        defecto_19 = int(entry_18.get() or 0)
        defecto_20 = int(entry_19.get() or 0)
        defecto_21 = int(entry_20.get() or 0)
        defecto_22 = int(entry_21.get() or 0)
        defecto_23 = int(entry_22.get() or 0)
        defecto_24 = int(entry_23.get() or 0)
        defecto_25 = int(entry_24.get() or 0)
        defecto_26 = int(entry_25.get() or 0)
        defecto_27 = int(entry_26.get() or 0)
        defecto_28 = int(entry_27.get() or 0)
        defecto_29 = int(entry_28.get() or 0)
        defecto_30 = int(entry_29.get() or 0)

        suma_defec = defecto_1 + defecto_2 + defecto_3 + defecto_4 + defecto_5 + defecto_6 + defecto_7 + defecto_8 + \
            defecto_9 + defecto_10 + defecto_11 + defecto_12 + defecto_13 + defecto_14 + defecto_15 + defecto_16 + \
            defecto_17 + defecto_18 + defecto_19 + defecto_20 + defecto_21 + defecto_22 + defecto_23 + defecto_24 + \
            defecto_25 + defecto_26 + defecto_27 + defecto_28 + defecto_29 + defecto_30

        label_34.config(text=str(suma_defec))

    except ValueError:
        label_34.config(text="0")


def buscar_pallets(event):
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

    fpy_pallets()


def fpy_pallets(*args):
    """Función calcular fpy de pallets"""
    defectos_pallet = label_34.cget("text").strip() or "0"
    estandar_pallet = label_38.cget("text").strip() or "0"

    defectos_pallet = int(defectos_pallet)
    estandar_pallet = int(estandar_pallet)

    fpy = ((estandar_pallet - defectos_pallet) / estandar_pallet) * \
        100 if estandar_pallet > 0 else 0

    fpy_por_pallet = settings_limits("FPY_PALLET")
    fpy_por_pallet = int(fpy_por_pallet)

    if fpy == 0:
        label_40.config(fg="black", bg="#D0D0D0")
        label_40.config(text="")
    elif fpy > fpy_por_pallet:
        label_40.config(fg="green", bg="#D9F2D0")
        label_40.config(text=f"{fpy:.2f}%")
    elif fpy < fpy_por_pallet:
        label_40.config(fg="red", bg="#FFCCCC")
        label_40.config(text=f"{fpy:.2f}%")
    elif fpy == fpy_por_pallet:
        label_40.config(fg="#E7601D", bg="#FBE7DD")
        label_40.config(text=f"{fpy:.2f}%")


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


def root_parametros():
    """ Función que abre la ventana secundaria para editar el CSV """
    class CSVEditor:
        def __init__(self, root):
            self.root = root
            self.root.title("Parámetros")

            def cerrar_root():
                root.destroy()
                root.protocol("WM_DELETE_WINDOW", cerrar_root)

            self.root.attributes("-fullscreen", True)
            self.root.attributes("-topmost", True)

            # Cargar automáticamente desde la ruta
            self.archivo_csv = settings_root("Parameters")
            self.df = None

            # Botones
            btn_frame = tk.Frame(root)
            btn_frame.pack(fill="x", padx=10, pady=5)

            self.btn_guardar = tk.Button(
                btn_frame, text="Guardar", command=self.guardar_csv, font=("Arial", 12, "bold"), bg="green", fg="white", state=tk.DISABLED)
            self.btn_guardar.pack(side="left", padx=5)

            label_centro = tk.Label(
                btn_frame, text="Parámetros", font=("Arial", 18, "bold"))
            label_centro.pack(side="left", expand=True)

            btn_cerrar = tk.Button(
                btn_frame, text="Cerrar", bg="red", fg="white", font=("Arial", 12, "bold"),
                command=root.destroy)
            btn_cerrar.pack(side="right", padx=5)

            # Frame para la tabla con scroll
            table_frame = tk.Frame(root)
            table_frame.pack(expand=True, fill="both")

            # Scrollbars
            self.scroll_x = tk.Scrollbar(
                table_frame, orient="horizontal")
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
            self.menu_contextual = tk.Menu(
                self.root, tearoff=0)
            self.menu_contextual.add_command(
                label="Agregar fila", command=self.agregar_fila)
            self.menu_contextual.add_command(
                label="Eliminar fila", command=self.eliminar_fila)

            # Aplicar estilo al encabezado
            style = ttk.Style()
            style.theme_use("alt")
            style.configure("Treeview.Heading", font=(
                "Arial", 14, "bold"), foreground="white", background="#4472C4")

            style.configure("Treeview", font=("Arial", 12), rowheight=32, )

            style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=28,
                            fieldbackground="white")

            style.map("Treeview", background=[("selected", "#C9DAF8")])

            # Estilos para filas alternadas
            self.tree.tag_configure(
                "evenrow", background=color_1)  # Gris claro
            self.tree.tag_configure("oddrow", background="white")     # Blanco

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
            """ Carga el archivo CSV y lo muestra en la tabla ordenado ascendente por la columna 0 """
            try:
                encoding_detectado = self.detectar_codificacion(
                    self.archivo_csv)
                self.df = pd.read_csv(
                    self.archivo_csv, encoding=encoding_detectado)

                # Nombre de la primera columna
                col0 = self.df.columns[0]

                # Intentar ordenar numéricamente cuando sea posible
                # Convertimos a numérico (coerce convierte lo no-convertible a NaN)
                col_numeric = pd.to_numeric(self.df[col0], errors="coerce")

                if col_numeric.notna().any():  # hay al menos algún número => ordenar usando la versión numérica
                    # Usamos una key que prioriza valores numéricos y deja el resto al final en orden lexicográfico
                    # Para asegurar comportamiento estable convertimos nans a +inf para que queden al final
                    sort_series = col_numeric.fillna(float("inf"))
                    self.df = self.df.iloc[sort_series.argsort()].reset_index(
                        drop=True)
                else:
                    # Ningún valor es numérico: orden lexicográfico por la columna 0
                    self.df = self.df.sort_values(
                        by=col0, kind="mergesort", ignore_index=True)

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
                if i % 2 == 0:
                    tag = ("evenrow",)
                else:
                    tag = ("oddrow",)

                self.tree.insert("", "end", values=list(row), tags=tag)

        def editar_celda(self, event):
            """ Permite editar una celda con doble clic """
            item = self.tree.identify_row(event.y)  # Obtener fila seleccionada
            column = self.tree.identify_column(
                event.x)  # Obtener columna seleccionada

            if item and column:
                col_index = int(column[1:]) - 1  # Convertir columna a índice
                row_id = self.tree.index(item)  # Índice de fila en el Treeview

                x, y, width, height = self.tree.bbox(item, column)

                entry = tk.Entry(self.tree)
                entry.place(x=x, y=y, width=width, height=height)
                entry.insert(0, self.tree.item(item, "values")[col_index])
                entry.focus()

                def guardar_valor(event):
                    nuevo_valor = entry.get()

                    # -------------------------------------------
                    # Detectar tipo real de la columna en el DataFrame
                    # -------------------------------------------
                    col_dtype = str(self.df.dtypes.iloc[col_index])

                    try:
                        if col_dtype == "int64":
                            nuevo_valor = int(nuevo_valor)
                        elif col_dtype == "float64":
                            nuevo_valor = float(nuevo_valor)
                        # Puedes agregar más tipos si los necesitas
                    except ValueError:
                        messagebox.showerror(
                            "Error",
                            f"El valor '{nuevo_valor}' no es válido para el tipo {col_dtype}.",
                            parent=self.root
                        )
                        entry.destroy()
                        return

                    # Actualizar Treeview
                    self.tree.set(item, column, nuevo_valor)

                    # Actualizar DataFrame sin warnings
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
                    nueva_fila = {col: '0' for col in self.df.columns}

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
                messagebox.showinfo(
                    "Éxito", "Datos guardados correctamente.", parent=self.root)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo guardar el archivo CSV.\n{str(e)}", parent=self.root)

    # Crear ventana secundaria
    ventana_csv = tk.Toplevel()  # Se crea directamente sin necesitar root
    app = CSVEditor(ventana_csv)


def root_registros(on_close_callback=None):
    """ Función que abre la ventana secundaria para editar el CSV """
    class CSVEditor:
        def __init__(self, root, on_close_callback=None):
            self.root = root
            self.on_close_callback = on_close_callback
            self.root.title("Registros")

            def cerrar_root():
                root.destroy()
                root.protocol("WM_DELETE_WINDOW", cerrar_root)

            self.root.attributes("-fullscreen", True)
            self.root.attributes("-topmost", True)

            # Cargar automáticamente desde la ruta
            self.archivo_csv = settings_root("Registro")
            self.df = None

            # Botones
            btn_frame = tk.Frame(root)
            btn_frame.pack(fill="x", padx=10, pady=5)

            self.btn_guardar = tk.Button(
                btn_frame, text="Guardar", command=self.guardar_csv, font=("Arial", 12, "bold"), bg="green", fg="white", state=tk.DISABLED)
            self.btn_guardar.pack(side="left", padx=5)

            label_centro = tk.Label(
                btn_frame, text="Registros", font=("Arial", 18, "bold"))
            label_centro.pack(side="left", expand=True)

            btn_cerrar = tk.Button(
                btn_frame, text="Cerrar", bg="red", fg="white", font=("Arial", 12, "bold"),
                command=self.cerrar_ventana)
            btn_cerrar.pack(side="right", padx=5)

            # Frame para la tabla con scroll
            table_frame = tk.Frame(root)
            table_frame.pack(expand=True, fill="both")

            # Scrollbars
            self.scroll_x = tk.Scrollbar(
                table_frame, orient="horizontal")
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
            self.menu_contextual = tk.Menu(
                self.root, tearoff=0)
            self.menu_contextual.add_command(
                label="Agregar fila", command=self.agregar_fila)
            self.menu_contextual.add_command(
                label="Eliminar fila", command=self.eliminar_fila)

            # Aplicar estilo al encabezado
            style = ttk.Style()
            style.theme_use("alt")
            style.configure("Treeview.Heading", font=(
                "Arial", 14, "bold"), foreground="white", background="#4472C4")

            style.configure("Treeview", font=("Arial", 12), rowheight=32, )

            style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=28,
                            fieldbackground="white")

            style.map("Treeview", background=[("selected", "#C9DAF8")])

            # Estilos para filas alternadas
            self.tree.tag_configure(
                "evenrow", background=color_1)  # Gris claro
            self.tree.tag_configure("oddrow", background="white")     # Blanco

            # Cargar el CSV al abrir el programa
            if os.path.exists(self.archivo_csv):
                self.cargar_csv()
            else:
                messagebox.showerror(
                    "Error", f"No se encontró el archivo: {self.archivo_csv}", parent=self.root)

        def cerrar_ventana(self):
            if self.on_close_callback:
                self.on_close_callback()
            self.root.destroy()

        def detectar_codificacion(self, archivo):
            """ Detecta la codificación del archivo CSV """
            with open(archivo, "rb") as f:
                result = chardet.detect(f.read())
            return result["encoding"]

        def cargar_csv(self):
            """ Carga el archivo CSV y lo muestra en la tabla ordenado por fecha descendente """
            try:
                encoding_detectado = self.detectar_codificacion(
                    self.archivo_csv)
                self.df = pd.read_csv(
                    self.archivo_csv, encoding=encoding_detectado)

                # Columna 4 tiene la fecha/hora
                col_fecha = self.df.columns[4]

                # Convertir la columna a datetime
                self.df[col_fecha] = pd.to_datetime(
                    self.df[col_fecha],
                    format="%d/%m/%Y %H:%M:%S",
                    errors="coerce"
                )

                # Ordenar (más reciente → más antiguo)
                self.df = self.df.sort_values(
                    by=col_fecha,
                    ascending=False,
                    ignore_index=True
                )

                # 🔥 IMPORTANTE: volver a convertir a TEXTO en el formato deseado
                self.df[col_fecha] = self.df[col_fecha].dt.strftime(
                    "%d/%m/%Y %H:%M:%S")

                self.mostrar_datos()
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

                # 🔥 Evitar que las columnas se compriman
                self.tree.column(col, width=160, minwidth=160,
                                 stretch=False, anchor="center")

            # Insertar filas
            for i, row in self.df.iterrows():
                tag = ("evenrow",) if i % 2 == 0 else ("oddrow",)
                self.tree.insert("", "end", values=list(row), tags=tag)

        def editar_celda(self, event):
            """ Permite editar una celda con doble clic """
            item = self.tree.identify_row(event.y)  # Obtener fila seleccionada
            column = self.tree.identify_column(
                event.x)  # Obtener columna seleccionada

            if item and column:
                col_index = int(column[1:]) - 1  # Convertir columna a índice
                row_id = self.tree.index(item)  # Índice de fila en el Treeview

                x, y, width, height = self.tree.bbox(item, column)

                entry = tk.Entry(self.tree)
                entry.place(x=x, y=y, width=width, height=height)
                entry.insert(0, self.tree.item(item, "values")[col_index])
                entry.focus()

                def guardar_valor(event):
                    nuevo_valor = entry.get()

                    # -------------------------------------------
                    # Detectar tipo real de la columna en el DataFrame
                    # -------------------------------------------
                    col_dtype = str(self.df.dtypes.iloc[col_index])

                    try:
                        if col_dtype == "int64":
                            nuevo_valor = int(nuevo_valor)
                        elif col_dtype == "float64":
                            nuevo_valor = float(nuevo_valor)
                        # Puedes agregar más tipos si los necesitas
                    except ValueError:
                        messagebox.showerror(
                            "Error",
                            f"El valor '{nuevo_valor}' no es válido para el tipo {col_dtype}.",
                            parent=self.root
                        )
                        entry.destroy()
                        return

                    # Actualizar Treeview
                    self.tree.set(item, column, nuevo_valor)

                    # Actualizar DataFrame sin warnings
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
                    nueva_fila = {col: '0' for col in self.df.columns}

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
                messagebox.showinfo(
                    "Éxito", "Datos guardados correctamente.", parent=self.root)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo guardar el archivo CSV.\n{str(e)}", parent=self.root)

    # Crear ventana secundaria
    ventana_csv = tk.Toplevel()  # Se crea directamente sin necesitar root
    app = CSVEditor(ventana_csv, on_close_callback)


def root_logfile(on_close_callback=None):
    """ Función que abre la ventana secundaria para editar el CSV """
    class CSVEditor:
        def __init__(self, root, on_close_callback=None):
            self.root = root
            self.on_close_callback = on_close_callback
            self.root.title("LogFile")

            self.root.attributes("-fullscreen", True)
            self.root.attributes("-topmost", True)

            # Cargar automáticamente desde la ruta
            self.archivo_csv = settings_root("LogFile")
            self.df = None

            # Botones
            btn_frame = tk.Frame(root)
            btn_frame.pack(fill="x", padx=10, pady=5)

            self.btn_guardar = tk.Button(
                btn_frame, text="Guardar", command=self.guardar_csv, font=("Arial", 12, "bold"), bg="green", fg="white", state=tk.DISABLED)
            self.btn_guardar.pack(side="left", padx=5)

            label_centro = tk.Label(
                btn_frame, text="LogFile", font=("Arial", 18, "bold"))
            label_centro.pack(side="left", expand=True)

            btn_cerrar = tk.Button(
                btn_frame, text="Cerrar", bg="red", fg="white", font=("Arial", 12, "bold"),
                command=self.cerrar_ventana)
            btn_cerrar.pack(side="right", padx=5)

            # Frame para la tabla con scroll
            table_frame = tk.Frame(root)
            table_frame.pack(expand=True, fill="both")

            # Scrollbars
            self.scroll_x = tk.Scrollbar(
                table_frame, orient="horizontal")
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
            self.menu_contextual = tk.Menu(
                self.root, tearoff=0)
            self.menu_contextual.add_command(
                label="Agregar fila", command=self.agregar_fila)
            self.menu_contextual.add_command(
                label="Eliminar fila", command=self.eliminar_fila)

            # Aplicar estilo al encabezado
            style = ttk.Style()
            style.theme_use("alt")
            style.configure("Treeview.Heading", font=(
                "Arial", 14, "bold"), foreground="white", background="#4472C4")

            style.configure("Treeview", font=("Arial", 12), rowheight=32, )

            style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=28,
                            fieldbackground="white")

            style.map("Treeview", background=[("selected", "#C9DAF8")])

            # Estilos para filas alternadas
            self.tree.tag_configure(
                "evenrow", background=color_1)  # Gris claro
            self.tree.tag_configure("oddrow", background="white")     # Blanco

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

        def cerrar_ventana(self):
            if self.on_close_callback:
                self.on_close_callback()
            self.root.destroy()

        def cargar_csv(self):
            """ Carga el archivo CSV y lo muestra en la tabla ordenado por fecha descendente """
            try:
                encoding_detectado = self.detectar_codificacion(
                    self.archivo_csv)
                self.df = pd.read_csv(
                    self.archivo_csv, encoding=encoding_detectado)

                # Columna 4 tiene la fecha/hora
                col_fecha = self.df.columns[4]

                # Convertir la columna a datetime
                self.df[col_fecha] = pd.to_datetime(
                    self.df[col_fecha],
                    format="%d/%m/%Y %H:%M:%S",
                    errors="coerce"
                )

                # Ordenar (más reciente → más antiguo)
                self.df = self.df.sort_values(
                    by=col_fecha,
                    ascending=False,
                    ignore_index=True
                )

                # 🔥 IMPORTANTE: volver a convertir a TEXTO en el formato deseado
                self.df[col_fecha] = self.df[col_fecha].dt.strftime(
                    "%d/%m/%Y %H:%M:%S")

                self.mostrar_datos()
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

                # 🔥 Evitar que las columnas se compriman
                self.tree.column(col, width=160, minwidth=160,
                                 stretch=False, anchor="center")

            # Insertar filas
            for i, row in self.df.iterrows():
                tag = ("evenrow",) if i % 2 == 0 else ("oddrow",)
                self.tree.insert("", "end", values=list(row), tags=tag)

        def editar_celda(self, event):
            """ Permite editar una celda con doble clic """
            item = self.tree.identify_row(event.y)  # Obtener fila seleccionada
            column = self.tree.identify_column(
                event.x)  # Obtener columna seleccionada

            if item and column:
                col_index = int(column[1:]) - 1  # Convertir columna a índice
                row_id = self.tree.index(item)  # Índice de fila en el Treeview

                x, y, width, height = self.tree.bbox(item, column)

                entry = tk.Entry(self.tree)
                entry.place(x=x, y=y, width=width, height=height)
                entry.insert(0, self.tree.item(item, "values")[col_index])
                entry.focus()

                def guardar_valor(event):
                    nuevo_valor = entry.get()

                    # -------------------------------------------
                    # Detectar tipo real de la columna en el DataFrame
                    # -------------------------------------------
                    col_dtype = str(self.df.dtypes.iloc[col_index])

                    try:
                        if col_dtype == "int64":
                            nuevo_valor = int(nuevo_valor)
                        elif col_dtype == "float64":
                            nuevo_valor = float(nuevo_valor)
                        # Puedes agregar más tipos si los necesitas
                    except ValueError:
                        messagebox.showerror(
                            "Error",
                            f"El valor '{nuevo_valor}' no es válido para el tipo {col_dtype}.",
                            parent=self.root
                        )
                        entry.destroy()
                        return

                    # Actualizar Treeview
                    self.tree.set(item, column, nuevo_valor)

                    # Actualizar DataFrame sin warnings
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
                    nueva_fila = {col: '0' for col in self.df.columns}

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
                messagebox.showinfo(
                    "Éxito", "Datos guardados correctamente.", parent=self.root)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo guardar el archivo CSV.\n{str(e)}", parent=self.root)

    # Crear ventana secundaria
    ventana_csv = tk.Toplevel()  # Se crea directamente sin necesitar root
    app = CSVEditor(ventana_csv, on_close_callback)


def actualizar_principal():
    calcular_defectos()


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
        label_rd_4.config(font=("Arial", defectos_menu, "bold"),
                          bd=1,  relief="ridge")  # Defectos
        label_rd_5.config(font=("Arial", defectos_menu, "bold"),
                          bd=1,  relief="ridge")  # Cantidad
        label_rd_6.config(font=("Arial", defectos, "bold"),
                          bd=1,  relief="ridge")  # Defecto1
        label_rd_7.config(font=("Arial", defectos, "bold"),
                          bd=1,  relief="ridge")  # Defecto2
        label_rd_8.config(font=("Arial", defectos, "bold"),
                          bd=1,  relief="ridge")  # Defecto3
        label_rd_9.config(font=("Arial", defectos, "bold"),
                          bd=1,  relief="ridge")  # Defecto4
        label_rd_10.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto5
        label_rd_11.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto6
        label_rd_12.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto7
        label_rd_13.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto8
        label_rd_14.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto9
        label_rd_15.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto10
        label_rd_16.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto11
        label_rd_17.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto12
        label_rd_18.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto13
        label_rd_19.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto14
        label_rd_20.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto15
        label_rd_21.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto16
        label_rd_22.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto17
        label_rd_23.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto18
        label_rd_24.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto19
        label_rd_25.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto20
        label_rd_26.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto21
        label_rd_27.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto22
        label_rd_28.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto23
        label_rd_29.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto24
        label_rd_30.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto25
        label_rd_31.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto26
        label_rd_32.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto27
        label_rd_33.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto28
        label_rd_34.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto29
        label_rd_35.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Defecto30
        label_rd_36.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto1
        label_rd_37.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto2
        label_rd_38.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto3
        label_rd_39.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto4
        label_rd_40.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto5
        label_rd_41.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto6
        label_rd_42.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto7
        label_rd_43.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto8
        label_rd_44.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto9
        label_rd_45.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto10
        label_rd_46.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto11
        label_rd_47.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto12
        label_rd_48.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto13
        label_rd_49.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto14
        label_rd_50.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto15
        label_rd_51.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto16
        label_rd_52.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto17
        label_rd_53.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto18
        label_rd_54.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto19
        label_rd_55.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto20
        label_rd_56.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto21
        label_rd_57.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto22
        label_rd_58.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto23
        label_rd_59.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto24
        label_rd_60.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto25
        label_rd_61.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto26
        label_rd_62.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto27
        label_rd_63.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto28
        label_rd_64.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto29
        label_rd_65.config(font=("Arial", defectos, "bold"),
                           bd=1,  relief="ridge")  # Cantidad_defecto30
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
                fpy_meta = int(settings_limits("FPY_MODEL"))
            except:
                fpy_meta = 95

            # Lógica de Emojis y Colores
            if fpy > fpy_meta:
                estado, emoji, color_kpi = "BUENO", "😊", "#2ECC71"  # Verde
            elif fpy == fpy_meta:
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
            ax1.set_title(f"Calidad vs Meta ({fpy_meta}%)", pad=5)

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
                label_rd_60, label_rd_61, label_rd_62, label_rd_63, label_rd_64, label_rd_65
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
            fpy_por_pallet = int(settings_limits("FPY_MODEL"))

            if total_producido == 0:
                label_rd_79.config(text="N/A", fg="black", bg=color_3)
            else:
                if fpy > fpy_por_pallet:
                    label_rd_79.config(
                        text=f"{fpy:.2f}%", fg="green", bg="#D9F2D0")
                elif fpy < fpy_por_pallet:
                    label_rd_79.config(
                        text=f"{fpy:.2f}%", fg="red", bg="#FFCCCC")
                else:
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
    'Modelo', 'Pallet', 'Defectos', 'Estandar', 'Fecha/Hora', 'FPY',
    'Wave1', 'Wave2', 'Flux', 'Conveyor',
    defect1, defect2, defect3, defect4, defect5, defect6, defect7, defect8,
    defect9, defect10, defect11, defect12, defect13, defect14, defect15,
    defect16, defect17, defect18, defect19, defect20, defect21, defect22,
    defect23, defect24, defect25, defect26, defect27, defect28, defect29, defect30
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


def guardar_datos(event=None):
    """Función para guardar registros en csv de forma segura"""
    global guardando_en_progreso

    # Si ya se está ejecutando un guardado, ignorar nuevas peticiones
    if guardando_en_progreso:
        return

    try:
        guardando_en_progreso = True

        # 1. Recolectar datos de forma limpia
        # Usamos una lista para que sea más fácil de manejar y leer
        datos = [
            label_36.cget("text").strip() or "0",  # Modelo
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

        # Agregar los 30 defectos de los entries (entry_0 a entry_29)
        entries_defectos = [
            entry_0, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9,
            entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18, entry_19,
            entry_20, entry_21, entry_22, entry_23, entry_24, entry_25, entry_26, entry_27, entry_28, entry_29
        ]

        for entry in entries_defectos:
            datos.append(entry.get().strip() or "0")

        # 2. Validación: Verificar que el Pallet y Modelo no estén vacíos
        # (dat1 y dat2 en tu código original)
        if not datos[0] or datos[1] == "0" or datos[1] == "":
            messagebox.showwarning(
                "Atención", "El número de Pallet es obligatorio.")
            guardando_en_progreso = False
            return

        # 3. Escritura en archivos (Usando context manager 'with' para cierre automático)
        archivos = [csv_file, csv_file2]
        for ruta in archivos:
            with open(ruta, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(datos)

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
        fpy_model = int(settings_limits("FPY_MODEL"))

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
            elif fpy > fpy_model:
                lbl.config(fg="green", bg="#D9F2D0",
                           text=texto, bd=.5, relief="ridge", justify="center")
            elif fpy < fpy_model:
                lbl.config(fg="red", bg="#FFCCCC",
                           text=texto, bd=.5, relief="ridge", justify="center")
            else:  # fpy == fpy_model
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
        fpy_model = int(settings_limits("FPY_MODEL"))

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
            elif fpy > fpy_model:
                lbl.config(fg="green", bg="#D9F2D0",
                           text=texto, bd=.5, relief="ridge", justify="center")
            elif fpy < fpy_model:
                lbl.config(fg="red", bg="#FFCCCC",
                           text=texto, bd=.5, relief="ridge", justify="center")
            else:  # fpy == fpy_model
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

    fpy_model = float(settings_limits("FPY_MODEL"))

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
    if valor_minimo > fpy_model:
        enviar_comando_rb(b"A\r")
    elif valor_minimo < fpy_model:
        enviar_comando_rb(b"C\r")
    else:
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
root = tk.Tk()
root.attributes("-topmost", True)
root.attributes("-fullscreen", True)
root.configure(bg=color_1)
# ------- grid
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=0)
root.grid_columnconfigure(0, weight=1)
# ------- Frame
Frame0 = tk.Frame(root, bg=color_1)
Frame1 = tk.Frame(root, bg=color_1)
Frame2 = tk.Frame(root, bg=color_1)
Frame3 = tk.Frame(root, bg=color_1)
Frame4 = tk.Frame(root, bg=color_1)
Frame5 = tk.Frame(root, bg=color_1)
# ------- Frame0
Frame0.grid_columnconfigure(0, weight=1)
Frame0.grid_columnconfigure(1, weight=1)
Frame0.grid_columnconfigure(2, weight=1)
Frame0.grid_rowconfigure(0, weight=1)
# ------- Frame1
Frame1.grid_columnconfigure(0, weight=1)
Frame1.grid_columnconfigure(1, weight=1)
Frame1.grid_columnconfigure(2, weight=1)
Frame1.grid_columnconfigure(3, weight=1)
Frame1.grid_columnconfigure(4, weight=1)
Frame1.grid_columnconfigure(5, weight=1)
Frame1.grid_columnconfigure(6, weight=1)
Frame1.grid_columnconfigure(7, weight=1)
Frame1.grid_columnconfigure(8, weight=1)
Frame1.grid_columnconfigure(9, weight=1)
Frame1.grid_rowconfigure(0, weight=0)
Frame1.grid_rowconfigure(1, weight=1)
Frame1.grid_rowconfigure(2, weight=1)
Frame1.grid_rowconfigure(3, weight=1)
Frame1.grid_rowconfigure(4, weight=1)
Frame1.grid_rowconfigure(5, weight=1)
Frame1.grid_rowconfigure(6, weight=1)
Frame1.grid_rowconfigure(7, weight=1)
Frame1.grid_rowconfigure(8, weight=1)
# ------- Frame2
Frame2.grid_columnconfigure(0, weight=1)
Frame2.grid_columnconfigure(1, weight=1)
Frame2.grid_columnconfigure(2, weight=1)
Frame2.grid_columnconfigure(3, weight=1)
Frame2.grid_columnconfigure(4, weight=1)
Frame2.grid_columnconfigure(5, weight=1)
Frame2.grid_columnconfigure(6, weight=1)
Frame2.grid_columnconfigure(7, weight=1)
Frame2.grid_columnconfigure(8, weight=1)
Frame2.grid_columnconfigure(9, weight=1)
Frame2.grid_columnconfigure(10, weight=1)
Frame2.grid_columnconfigure(11, weight=1)
Frame2.grid_columnconfigure(12, weight=1)
Frame2.grid_columnconfigure(13, weight=1)
Frame2.grid_columnconfigure(14, weight=1)
Frame2.grid_columnconfigure(15, weight=1)
Frame2.grid_rowconfigure(0, weight=1)
for col in range(0, 16):
    Frame2.grid_columnconfigure(col, weight=1, uniform="cols")
# ------- Frame3
Frame3.grid_columnconfigure(0, weight=0)
Frame3.grid_columnconfigure(1, weight=0)
Frame3.grid_columnconfigure(2, weight=0)
Frame3.grid_columnconfigure(3, weight=0)
Frame3.grid_columnconfigure(4, weight=0)
Frame3.grid_columnconfigure(5, weight=0)
Frame3.grid_columnconfigure(6, weight=0)
Frame3.grid_columnconfigure(7, weight=0)
Frame3.grid_rowconfigure(0, weight=1)
# ------- Frame4
Frame4.grid_columnconfigure(0, weight=0)
Frame4.grid_columnconfigure(1, weight=1)
Frame4.grid_columnconfigure(2, weight=1)
Frame4.grid_columnconfigure(3, weight=1)
Frame4.grid_columnconfigure(4, weight=1)
Frame4.grid_columnconfigure(5, weight=1)
Frame4.grid_columnconfigure(6, weight=1)
Frame4.grid_columnconfigure(7, weight=1)
Frame4.grid_columnconfigure(8, weight=1)
Frame4.grid_columnconfigure(9, weight=1)
Frame4.grid_columnconfigure(10, weight=1)
Frame4.grid_columnconfigure(11, weight=1)
Frame4.grid_columnconfigure(12, weight=1)
Frame4.grid_rowconfigure(0, weight=0)
Frame4.grid_rowconfigure(1, weight=1)
Frame4.grid_rowconfigure(2, weight=1)
Frame4.grid_rowconfigure(3, weight=1)
Frame4.grid_rowconfigure(4, weight=0)
Frame4.grid_rowconfigure(5, weight=0)
Frame4.grid_rowconfigure(6, weight=0)
Frame4.grid_rowconfigure(7, weight=0)
Frame4.grid_rowconfigure(8, weight=0)
Frame4.grid_rowconfigure(9, weight=0)
Frame4.grid_rowconfigure(10, weight=0)
for col in range(1, 13):
    Frame4.grid_columnconfigure(col, weight=1, uniform="cols")
# ------- Frame5
Frame5.grid_columnconfigure(0, weight=1)
Frame5.grid_columnconfigure(1, weight=1)
Frame5.grid_columnconfigure(2, weight=1)
Frame5.grid_columnconfigure(3, weight=1)
Frame5.grid_columnconfigure(4, weight=1)
Frame5.grid_columnconfigure(5, weight=1)
Frame5.grid_columnconfigure(6, weight=1)
Frame5.grid_rowconfigure(0, weight=1)
# ------------ Frame0_Row0
# Cargar logo ELRAD
logo_elrad = Image.open(settings_root("LogoELRAD"))
logo_elrad = logo_elrad.resize((100, 50), Image.Resampling.LANCZOS)
logo_elrad_tk = ImageTk.PhotoImage(logo_elrad)

# Imagen ELRAD como botón de minimizar
boton_minimizar = tk.Button(Frame0, image=logo_elrad_tk,
                            command=toggle_minimize, borderwidth=0, bg=color_1)
boton_minimizar.grid(row=0, column=0, padx=0, pady=0, sticky="nw")

# label_0: Titulo
label_0 = tk.Label(Frame0, text="Registro de defectos SEHO",
                   fg="black", bg=color_1)
label_0.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

# Cargar logo SEHO
logo_seho = Image.open(settings_root("LogoSEHO"))
logo_seho = logo_seho.resize(
    (100, 50), Image.Resampling.LANCZOS)  # Ajuste de tamaño
logo_seho_tk = ImageTk.PhotoImage(logo_seho)

# Imagen SEHO como boton de cerrado
boton_cerrar = tk.Button(Frame0, image=logo_seho_tk,
                         command=cerrar_ventana, borderwidth=0, bg=color_1)
boton_cerrar.grid(row=0, column=2, padx=0, pady=0, sticky="ne")

# ------------ Frame1_Row0
# label_1: Defectos
label_1 = tk.Label(Frame1, text="DEFECTOS",
                   fg="black", bg="#FFCB25")
label_1.grid(row=0, column=0, columnspan=10, padx=0, pady=0, sticky="nsew")

# ------------ Frame1_Row1
# ----- Defecto 1
# label_2: Defacto 1
label_2 = tk.Label(Frame1, text=f"{defect1}:",
                   fg="black", bg=color_1)
label_2.grid(row=1, column=0, padx=0, pady=0, sticky="e")

# entry_0: Defecto 1
entry_0 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_0.grid(row=1, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 2
# label_3: Defacto 2
label_3 = tk.Label(Frame1, text=f"{defect2}:",
                   fg="black", bg=color_1)
label_3.grid(row=1, column=2, padx=0, pady=0, sticky="e")

# entry_1: Defecto 2
entry_1 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_1.grid(row=1, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 3
# label_4: Defacto 3
label_4 = tk.Label(Frame1, text=f"{defect3}:",
                   fg="black", bg=color_1)
label_4.grid(row=1, column=4, padx=0, pady=0, sticky="e")

# entry_2: Defecto 3
entry_2 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_2.grid(row=1, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 4
# label_5: Defacto 4
label_5 = tk.Label(Frame1, text=f"{defect4}:",
                   fg="black", bg=color_1)
label_5.grid(row=1, column=6, padx=0, pady=0, sticky="e")

# entry_3: Defecto 4
entry_3 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_3.grid(row=1, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 5
# label_6: Defacto 5
label_6 = tk.Label(Frame1, text=f"{defect5}:",
                   fg="black", bg=color_1)
label_6.grid(row=1, column=8, padx=0, pady=0, sticky="e")

# entry_4: Defecto 5
entry_4 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_4.grid(row=1, column=9, padx=0, pady=0, sticky="w")

# ------------ Frame1_Row2
# ----- Defecto 6
# label_7: Defacto 6
label_7 = tk.Label(Frame1, text=f"{defect6}:",
                   fg="black", bg=color_1)
label_7.grid(row=2, column=0, padx=0, pady=0, sticky="e")

# entry_5: Defecto 6
entry_5 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_5.grid(row=2, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 7
# label_8: Defacto 7
label_8 = tk.Label(Frame1, text=f"{defect7}:",
                   fg="black", bg=color_1)
label_8.grid(row=2, column=2, padx=0, pady=0, sticky="e")

# entry_6: Defecto 7
entry_6 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_6.grid(row=2, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 8
# label_9: Defacto 8
label_9 = tk.Label(Frame1, text=f"{defect8}:",
                   fg="black", bg=color_1)
label_9.grid(row=2, column=4, padx=0, pady=0, sticky="e")

# entry_7: Defecto 8
entry_7 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_7.grid(row=2, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 9
# label_10: Defacto 9
label_10 = tk.Label(Frame1, text=f"{defect9}:",
                    fg="black", bg=color_1)
label_10.grid(row=2, column=6, padx=0, pady=0, sticky="e")

# entry_8: Defecto 9
entry_8 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_8.grid(row=2, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 10
# label_11: Defacto 10
label_11 = tk.Label(Frame1, text=f"{defect10}:",
                    fg="black", bg=color_1)
label_11.grid(row=2, column=8, padx=0, pady=0, sticky="e")

# entry_9: Defecto 10
entry_9 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_9.grid(row=2, column=9, padx=0, pady=0, sticky="w")

# ------------ Frame1_Row3
# ----- Defecto 11
# label_12: Defacto 11
label_12 = tk.Label(Frame1, text=f"{defect11}:",
                    fg="black", bg=color_1)
label_12.grid(row=3, column=0, padx=0, pady=0, sticky="e")

# entry_10: Defecto 11
entry_10 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_10.grid(row=3, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 12
# label_13: Defacto 12
label_13 = tk.Label(Frame1, text=f"{defect12}:",
                    fg="black", bg=color_1)
label_13.grid(row=3, column=2, padx=0, pady=0, sticky="e")

# entry_11: Defecto 12
entry_11 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_11.grid(row=3, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 13
# label_14: Defacto 13
label_14 = tk.Label(Frame1, text=f"{defect13}:",
                    fg="black", bg=color_1)
label_14.grid(row=3, column=4, padx=0, pady=0, sticky="e")

# entry_12: Defecto 13
entry_12 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_12.grid(row=3, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 14
# label_15: Defacto 14
label_15 = tk.Label(Frame1, text=f"{defect14}:",
                    fg="black", bg=color_1)
label_15.grid(row=3, column=6, padx=0, pady=0, sticky="e")

# entry_13: Defecto 14
entry_13 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_13.grid(row=3, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 15
# label_16: Defacto 15
label_16 = tk.Label(Frame1, text=f"{defect15}:",
                    fg="black", bg=color_1)
label_16.grid(row=3, column=8, padx=0, pady=0, sticky="e")

# entry_14: Defecto 15
entry_14 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_14.grid(row=3, column=9, padx=0, pady=0, sticky="w")

# ------------ Frame1_Row4
# ----- Defecto 16
# label_17: Defacto 16
label_17 = tk.Label(Frame1, text=f"{defect16}:",
                    fg="black", bg=color_1)
label_17.grid(row=4, column=0, padx=0, pady=0, sticky="e")

# entry_15: Defecto 16
entry_15 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_15.grid(row=4, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 17
# label_18: Defacto 17
label_18 = tk.Label(Frame1, text=f"{defect17}:",
                    fg="black", bg=color_1)
label_18.grid(row=4, column=2, padx=0, pady=0, sticky="e")

# entry_16: Defecto 17
entry_16 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_16.grid(row=4, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 18
# label_19: Defacto 18
label_19 = tk.Label(Frame1, text=f"{defect18}:",
                    fg="black", bg=color_1)
label_19.grid(row=4, column=4, padx=0, pady=0, sticky="e")

# entry_17: Defecto 18
entry_17 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_17.grid(row=4, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 19
# label_20: Defacto 19
label_20 = tk.Label(Frame1, text=f"{defect19}:",
                    fg="black", bg=color_1)
label_20.grid(row=4, column=6, padx=0, pady=0, sticky="e")

# entry_18: Defecto 19
entry_18 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_18.grid(row=4, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 20
# label_21: Defacto 20
label_21 = tk.Label(Frame1, text=f"{defect20}:",
                    fg="black", bg=color_1)
label_21.grid(row=4, column=8, padx=0, pady=0, sticky="e")

# entry_19: Defecto 20
entry_19 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_19.grid(row=4, column=9, padx=0, pady=0, sticky="w")

# ------------ Frame1_Row5
# ----- Defecto 21
# label_22: Defacto 21
label_22 = tk.Label(Frame1, text=f"{defect21}:",
                    fg="black", bg=color_1)
label_22.grid(row=5, column=0, padx=0, pady=0, sticky="e")

# entry_20: Defecto 21
entry_20 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_20.grid(row=5, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 22
# label_23: Defacto 22
label_23 = tk.Label(Frame1, text=f"{defect22}:",
                    fg="black", bg=color_1)
label_23.grid(row=5, column=2, padx=0, pady=0, sticky="e")

# entry_21: Defecto 22
entry_21 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_21.grid(row=5, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 23
# label_24: Defacto 23
label_24 = tk.Label(Frame1, text=f"{defect23}:",
                    fg="black", bg=color_1)
label_24.grid(row=5, column=4, padx=0, pady=0, sticky="e")

# entry_22: Defecto 23
entry_22 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_22.grid(row=5, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 24
# label_25: Defacto 24
label_25 = tk.Label(Frame1, text=f"{defect24}:",
                    fg="black", bg=color_1)
label_25.grid(row=5, column=6, padx=0, pady=0, sticky="e")

# entry_23: Defecto 24
entry_23 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_23.grid(row=5, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 25
# label_26: Defacto 25
label_26 = tk.Label(Frame1, text=f"{defect25}:",
                    fg="black", bg=color_1)
label_26.grid(row=5, column=8, padx=0, pady=0, sticky="e")

# entry_24: Defecto 25
entry_24 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_24.grid(row=5, column=9, padx=0, pady=0, sticky="w")

# ------------ Frame1_Row6
# ----- Defecto 26
# label_27: Defacto 26
label_27 = tk.Label(Frame1, text=f"{defect26}:",
                    fg="black", bg=color_1)
label_27.grid(row=6, column=0, padx=0, pady=0, sticky="e")

# entry_25: Defecto 26
entry_25 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_25.grid(row=6, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 27
# label_28: Defacto 27
label_28 = tk.Label(Frame1, text=f"{defect27}:",
                    fg="black", bg=color_1)
label_28.grid(row=6, column=2, padx=0, pady=0, sticky="e")

# entry_26: Defecto 27
entry_26 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_26.grid(row=6, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 28
# label_29: Defacto 28
label_29 = tk.Label(Frame1, text=f"{defect28}:",
                    fg="black", bg=color_1)
label_29.grid(row=6, column=4, padx=0, pady=0, sticky="e")

# entry_27: Defecto 28
entry_27 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_27.grid(row=6, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 29
# label_30: Defacto 29
label_30 = tk.Label(Frame1, text=f"{defect29}:",
                    fg="black", bg=color_1)
label_30.grid(row=6, column=6, padx=0, pady=0, sticky="e")

# entry_28: Defecto 29
entry_28 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_28.grid(row=6, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 30
# label_31: Defacto 30
label_31 = tk.Label(Frame1, text=f"{defect30}:",
                    fg="black", bg=color_1)
label_31.grid(row=6, column=8, padx=0, pady=0, sticky="e")

# entry_29: Defecto 30
entry_29 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_29.grid(row=6, column=9, padx=0, pady=0, sticky="w")
label_32 = tk.Label(Frame1, text="Número de pallet:",
                    fg="black", bg=color_1)
label_32.grid(row=7, column=0, padx=0, columnspan=10, pady=0, sticky="s")
entry_30 = tk.Entry(Frame1, width=25, justify="center",
                    background="springgreen", border=3)
entry_30.grid(row=8, column=0, columnspan=10, padx=0, pady=0, sticky="n")
entry_30.focus()
label_33 = tk.Label(Frame2, text="Defectos:",
                    fg="black", bg=color_2)
label_33.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")
label_34 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_34.grid(row=0, column=1, padx=0, pady=5, sticky="nsew")
label_35 = tk.Label(Frame2, text="Modelo:",
                    fg="black", bg=color_2)
label_35.grid(row=0, column=2, padx=0, pady=5, sticky="nsew")
label_36 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_36.grid(row=0, column=3, padx=0, pady=5, sticky="nsew")
label_37 = tk.Label(Frame2, text="Estandar:",
                    fg="black", bg=color_2)
label_37.grid(row=0, column=4, padx=0, pady=5, sticky="nsew")
label_38 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_38.grid(row=0, column=5, padx=0, pady=5, sticky="nsew")
label_39 = tk.Label(Frame2, text="FPY pallet:",
                    fg="black", bg=color_2)
label_39.grid(row=0, column=6, padx=0, pady=5, sticky="nsew")
label_40 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_40.grid(row=0, column=7, padx=0, pady=5, sticky="nsew")
label_41 = tk.Label(Frame2, text="Wave 1:",
                    fg="black", bg=color_2)
label_41.grid(row=0, column=8, padx=0, pady=5, sticky="nsew")
label_42 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_42.grid(row=0, column=9, padx=0, pady=5, sticky="nsew")
label_43 = tk.Label(Frame2, text="Wave 2:",
                    fg="black", bg=color_2)
label_43.grid(row=0, column=10, padx=0, pady=5, sticky="nsew")
label_44 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_44.grid(row=0, column=11, padx=0, pady=5, sticky="nsew")
label_45 = tk.Label(Frame2, text="Flux:",
                    fg="black", bg=color_2)
label_45.grid(row=0, column=12, padx=0, pady=5, sticky="nsew")
label_46 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_46.grid(row=0, column=13, padx=0, pady=5, sticky="nsew")
label_47 = tk.Label(Frame2, text="Conveyor:",
                    fg="black", bg=color_2)
label_47.grid(row=0, column=14, padx=0, pady=5, sticky="nsew")
label_48 = tk.Label(Frame2,
                    fg="black", bg="#D0D0D0")
label_48.grid(row=0, column=15, padx=0, pady=5, sticky="nsew")

# Configuración de estilo para que no se vea "viejo"
style = ttk.Style()
# Usar 'default' permite personalizar más colores
style.theme_use('default')
style.configure("Custom.TCombobox", fieldbackground="white",
                foreground="black", padding=2)

# Horas con formato 1, 2, 12...
horas_vals = [str(i) for i in range(1, 13)]
# Minutos con formato 00, 01, 02...
minutos_vals = ["00", "10", "20", "30", "40", "50", "59"]
# Opciones de periodo
lista_periodos = ["AM", "PM"]

hora_inicial = tk.StringVar(value="6")
minuto_inicial = tk.StringVar(value="00")
periodo_inicial = tk.StringVar(value="AM")

spinbox_0 = ttk.Combobox(Frame3, values=horas_vals, style="Custom.TCombobox", textvariable=hora_inicial,
                         width=4, state="readonly", justify="center")
spinbox_0.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")

spinbox_1 = ttk.Combobox(Frame3, values=minutos_vals, style="Custom.TCombobox", textvariable=minuto_inicial,
                         width=4, state="readonly", justify="center")
spinbox_1.grid(row=0, column=1, padx=2, pady=5, sticky="nsew")

spinbox_2 = ttk.Combobox(Frame3, values=lista_periodos, style="Custom.TCombobox", textvariable=periodo_inicial,
                         width=4, state="readonly", justify="center")
spinbox_2.grid(row=0, column=2, padx=2, pady=5, sticky="nsew")


label_49 = tk.Label(Frame3, text="<- Horario ->",
                    fg="black", bg=color_1)
label_49.grid(row=0, column=3, padx=0, pady=5, sticky="nsew")

hora_final = tk.StringVar(value="3")
minuto_final = tk.StringVar(value="00")
periodo_final = tk.StringVar(value="PM")

spinbox_3 = ttk.Combobox(Frame3, values=horas_vals, style="Custom.TCombobox", textvariable=hora_final,
                         width=4, state="readonly", justify="center")
spinbox_3.grid(row=0, column=4, padx=2, pady=5, sticky="nsew")

spinbox_4 = ttk.Combobox(Frame3, values=minutos_vals, style="Custom.TCombobox", textvariable=minuto_final,
                         width=4, state="readonly", justify="center")
spinbox_4.grid(row=0, column=5, padx=2, pady=5, sticky="nsew")

spinbox_5 = ttk.Combobox(Frame3, values=lista_periodos, style="Custom.TCombobox", textvariable=periodo_final,
                         width=4, state="readonly", justify="center")
spinbox_5.grid(row=0, column=6, padx=2, pady=5, sticky="nsew")

button_17 = tk.Button(Frame3, text="Actualizar", height=0, width=0,
                      border=3, background="#00B050", command=calcular_defectos)
button_17.grid(row=0, column=7, padx=2, pady=5, sticky="nsew")
label_50 = tk.Label(Frame4, text=part_1,
                    fg="black")
label_50.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
label_51 = tk.Label(Frame4, text=part_2,
                    fg="black")
label_51.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
label_52 = tk.Label(Frame4, text=part_3,
                    fg="black")
label_52.grid(row=0, column=3, padx=0, pady=0, sticky="nsew")
label_53 = tk.Label(Frame4, text=part_4,
                    fg="black")
label_53.grid(row=0, column=4, padx=0, pady=0, sticky="nsew")
label_54 = tk.Label(Frame4, text=part_5,
                    fg="black")
label_54.grid(row=0, column=5, padx=0, pady=0, sticky="nsew")
label_55 = tk.Label(Frame4, text=part_6,
                    fg="black")
label_55.grid(row=0, column=6, padx=0, pady=0, sticky="nsew")
label_56 = tk.Label(Frame4, text=part_7,
                    fg="black")
label_56.grid(row=0, column=7, padx=0, pady=0, sticky="nsew")
label_57 = tk.Label(Frame4, text=part_8,
                    fg="black")
label_57.grid(row=0, column=8, padx=0, pady=0, sticky="nsew")
label_58 = tk.Label(Frame4, text=part_9,
                    fg="black")
label_58.grid(row=0, column=9, padx=0, pady=0, sticky="nsew")
label_59 = tk.Label(Frame4, text=part_10,
                    fg="black")
label_59.grid(row=0, column=10, padx=0, pady=0, sticky="nsew")
label_60 = tk.Label(Frame4, text=part_11,
                    fg="black")
label_60.grid(row=0, column=11, padx=0, pady=0, sticky="nsew")
label_61 = tk.Label(Frame4, text=part_12,
                    fg="black")
label_61.grid(row=0, column=12, padx=0, pady=0, sticky="nsew")
label_62 = tk.Label(Frame4, text="Defectos:",
                    fg="black", bg="#FFFFC9", anchor="e")
label_62.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
label_63 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_63.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")
label_64 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_64.grid(row=1, column=2, padx=0, pady=0, sticky="nsew")
label_65 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_65.grid(row=1, column=3, padx=0, pady=0, sticky="nsew")
label_66 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_66.grid(row=1, column=4, padx=0, pady=0, sticky="nsew")
label_67 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_67.grid(row=1, column=5, padx=0, pady=0, sticky="nsew")
label_68 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_68.grid(row=1, column=6, padx=0, pady=0, sticky="nsew")
label_69 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_69.grid(row=1, column=7, padx=0, pady=0, sticky="nsew")
label_70 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_70.grid(row=1, column=8, padx=0, pady=0, sticky="nsew")
label_71 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_71.grid(row=1, column=9, padx=0, pady=0, sticky="nsew")
label_72 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_72.grid(row=1, column=10, padx=0, pady=0, sticky="nsew")
label_73 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_73.grid(row=1, column=11, padx=0, pady=0, sticky="nsew")
label_74 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_74.grid(row=1, column=12, padx=0, pady=0, sticky="nsew")
label_75 = tk.Label(Frame4, text="Producido:",
                    fg="black", bg="#FFFFC9", anchor="e")
label_75.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
label_76 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_76.grid(row=2, column=1, padx=0, pady=0, sticky="nsew")
label_77 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_77.grid(row=2, column=2, padx=0, pady=0, sticky="nsew")
label_78 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_78.grid(row=2, column=3, padx=0, pady=0, sticky="nsew")
label_79 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_79.grid(row=2, column=4, padx=0, pady=0, sticky="nsew")
label_80 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_80.grid(row=2, column=5, padx=0, pady=0, sticky="nsew")
label_81 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_81.grid(row=2, column=6, padx=0, pady=0, sticky="nsew")
label_82 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_82.grid(row=2, column=7, padx=0, pady=0, sticky="nsew")
label_83 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_83.grid(row=2, column=8, padx=0, pady=0, sticky="nsew")
label_84 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_84.grid(row=2, column=9, padx=0, pady=0, sticky="nsew")
label_85 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_85.grid(row=2, column=10, padx=0, pady=0, sticky="nsew")
label_86 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_86.grid(row=2, column=11, padx=0, pady=0, sticky="nsew")
label_87 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_87.grid(row=2, column=12, padx=0, pady=0, sticky="nsew")
label_88 = tk.Label(Frame4, text="FPY:",
                    fg="black", bg="#FFFFC9", anchor="e")
label_88.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")
label_89 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_89.grid(row=3, column=1, padx=0, pady=0, sticky="nsew")
label_90 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_90.grid(row=3, column=2, padx=0, pady=0, sticky="nsew")
label_91 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_91.grid(row=3, column=3, padx=0, pady=0, sticky="nsew")
label_92 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_92.grid(row=3, column=4, padx=0, pady=0, sticky="nsew")
label_93 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_93.grid(row=3, column=5, padx=0, pady=0, sticky="nsew")
label_94 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_94.grid(row=3, column=6, padx=0, pady=0, sticky="nsew")
label_95 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_95.grid(row=3, column=7, padx=0, pady=0, sticky="nsew")
label_96 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_96.grid(row=3, column=8, padx=0, pady=0, sticky="nsew")
label_97 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_97.grid(row=3, column=9, padx=0, pady=0, sticky="nsew")
label_98 = tk.Label(Frame4,
                    fg="black", bg=color_3)
label_98.grid(row=3, column=10, padx=0, pady=0, sticky="nsew")
label_99 = tk.Label(Frame4,
                    fg="black", bg=color_2)
label_99.grid(row=3, column=11, padx=0, pady=0, sticky="nsew")
label_100 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_100.grid(row=3, column=12, padx=0, pady=0, sticky="nsew")
button_0 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_1, "Reset"))
button_0.grid(row=4, column=1, padx=0, pady=0, sticky="nsew")
button_1 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_2, "Reset"))
button_1.grid(row=4, column=2, padx=0, pady=0, sticky="nsew")
button_2 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_3, "Reset"))
button_2.grid(row=4, column=3, padx=0, pady=0, sticky="nsew")
button_3 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_4, "Reset"))
button_3.grid(row=4, column=4, padx=0, pady=0, sticky="nsew")
button_4 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_5, "Reset"))
button_4.grid(row=4, column=5, padx=0, pady=0, sticky="nsew")
button_5 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_6, "Reset"))
button_5.grid(row=4, column=6, padx=0, pady=0, sticky="nsew")
button_6 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_7, "Reset"))
button_6.grid(row=4, column=7, padx=0, pady=0, sticky="nsew")
button_7 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_8, "Reset"))
button_7.grid(row=4, column=8, padx=0, pady=0, sticky="nsew")
button_8 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_9, "Reset"))
button_8.grid(row=4, column=9, padx=0, pady=0, sticky="nsew")
button_9 = tk.Button(Frame4, text="Reset", height=0, width=0,
                     border=3, background="deepskyblue", command=lambda: reset(part_10, "Reset"))
button_9.grid(row=4, column=10, padx=0, pady=0, sticky="nsew")
button_10 = tk.Button(Frame4, text="Reset", height=0, width=0,
                      border=3, background="deepskyblue", command=lambda: reset(part_11, "Reset"))
button_10.grid(row=4, column=11, padx=0, pady=0, sticky="nsew")
button_11 = tk.Button(Frame4, text="Reset", height=0, width=0,
                      border=3, background="deepskyblue", command=lambda: reset(part_12, "Reset"))
button_11.grid(row=4, column=12, padx=0, pady=0, sticky="nsew")
label_101 = tk.Label(Frame4, text="FPY Total:",
                     fg="black", bg="#CAEDFB", anchor="e")
label_101.grid(row=5, column=0, padx=0, pady=0, sticky="nsew")
label_102 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_102.grid(row=5, column=1, padx=0, pady=0, sticky="nsew")
label_103 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_103.grid(row=5, column=2, padx=0, pady=0, sticky="nsew")
label_104 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_104.grid(row=5, column=3, padx=0, pady=0, sticky="nsew")
label_105 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_105.grid(row=5, column=4, padx=0, pady=0, sticky="nsew")
label_106 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_106.grid(row=5, column=5, padx=0, pady=0, sticky="nsew")
label_107 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_107.grid(row=5, column=6, padx=0, pady=0, sticky="nsew")
label_108 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_108.grid(row=5, column=7, padx=0, pady=0, sticky="nsew")
label_109 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_109.grid(row=5, column=8, padx=0, pady=0, sticky="nsew")
label_110 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_110.grid(row=5, column=9, padx=0, pady=0, sticky="nsew")
label_111 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_111.grid(row=5, column=10, padx=0, pady=0, sticky="nsew")
label_112 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_112.grid(row=5, column=11, padx=0, pady=0, sticky="nsew")
label_113 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_113.grid(row=5, column=12, padx=0, pady=0, sticky="nsew")
# label_114: Total Defect:
label_114 = tk.Label(Frame4, text="Total Defect:",
                     fg="black", bg="#CAEDFB", anchor="e")
label_114.grid(row=6, column=0, padx=0, pady=0, sticky="nsew")
label_115 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_115.grid(row=6, column=1, padx=0, pady=0, sticky="nsew")
label_116 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_116.grid(row=6, column=2, padx=0, pady=0, sticky="nsew")
label_117 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_117.grid(row=6, column=3, padx=0, pady=0, sticky="nsew")
label_118 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_118.grid(row=6, column=4, padx=0, pady=0, sticky="nsew")
label_119 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_119.grid(row=6, column=5, padx=0, pady=0, sticky="nsew")
label_120 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_120.grid(row=6, column=6, padx=0, pady=0, sticky="nsew")
label_121 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_121.grid(row=6, column=7, padx=0, pady=0, sticky="nsew")
label_122 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_122.grid(row=6, column=8, padx=0, pady=0, sticky="nsew")
label_123 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_123.grid(row=6, column=9, padx=0, pady=0, sticky="nsew")
label_124 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_124.grid(row=6, column=10, padx=0, pady=0, sticky="nsew")
label_125 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_125.grid(row=6, column=11, padx=0, pady=0, sticky="nsew")
label_126 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_126.grid(row=6, column=12, padx=0, pady=0, sticky="nsew")
label_127 = tk.Label(Frame4, text="Total Produc:",
                     fg="black", bg="#CAEDFB", anchor="e")
label_127.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")
label_128 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_128.grid(row=7, column=1, padx=0, pady=0, sticky="nsew")
label_129 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_129.grid(row=7, column=2, padx=0, pady=0, sticky="nsew")
label_130 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_130.grid(row=7, column=3, padx=0, pady=0, sticky="nsew")
label_131 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_131.grid(row=7, column=4, padx=0, pady=0, sticky="nsew")
label_132 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_132.grid(row=7, column=5, padx=0, pady=0, sticky="nsew")
label_133 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_133.grid(row=7, column=6, padx=0, pady=0, sticky="nsew")
label_134 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_134.grid(row=7, column=7, padx=0, pady=0, sticky="nsew")
label_135 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_135.grid(row=7, column=8, padx=0, pady=0, sticky="nsew")
label_136 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_136.grid(row=7, column=9, padx=0, pady=0, sticky="nsew")
label_137 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_137.grid(row=7, column=10, padx=0, pady=0, sticky="nsew")
label_138 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_138.grid(row=7, column=11, padx=0, pady=0, sticky="nsew")
label_139 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_139.grid(row=7, column=12, padx=0, pady=0, sticky="nsew")
label_140 = tk.Label(Frame4, text="TopDefect:",
                     fg="black", bg="#FBE2D5", anchor="e")
label_140.grid(row=8, column=0, padx=0, pady=0, sticky="nsew")
label_141 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_141.grid(row=8, column=1, padx=0, pady=0, sticky="nsew")
label_142 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_142.grid(row=8, column=2, padx=0, pady=0, sticky="nsew")
label_143 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_143.grid(row=8, column=3, padx=0, pady=0, sticky="nsew")
label_144 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_144.grid(row=8, column=4, padx=0, pady=0, sticky="nsew")
label_145 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_145.grid(row=8, column=5, padx=0, pady=0, sticky="nsew")
label_146 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_146.grid(row=8, column=6, padx=0, pady=0, sticky="nsew")
label_147 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_147.grid(row=8, column=7, padx=0, pady=0, sticky="nsew")
label_148 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_148.grid(row=8, column=8, padx=0, pady=0, sticky="nsew")
label_149 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_149.grid(row=8, column=9, padx=0, pady=0, sticky="nsew")
label_150 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_150.grid(row=8, column=10, padx=0, pady=0, sticky="nsew")
label_151 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_151.grid(row=8, column=11, padx=0, pady=0, sticky="nsew")
label_152 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_152.grid(row=8, column=12, padx=0, pady=0, sticky="nsew")
label_153 = tk.Label(Frame4, text="Cant.Defect:",
                     fg="black", bg="#FBE2D5", anchor="e")
label_153.grid(row=9, column=0, padx=0, pady=0, sticky="nsew")
label_154 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_154.grid(row=9, column=1, padx=0, pady=0, sticky="nsew")
label_155 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_155.grid(row=9, column=2, padx=0, pady=0, sticky="nsew")
label_156 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_156.grid(row=9, column=3, padx=0, pady=0, sticky="nsew")
label_157 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_157.grid(row=9, column=4, padx=0, pady=0, sticky="nsew")
label_158 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_158.grid(row=9, column=5, padx=0, pady=0, sticky="nsew")
label_159 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_159.grid(row=9, column=6, padx=0, pady=0, sticky="nsew")
label_160 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_160.grid(row=9, column=7, padx=0, pady=0, sticky="nsew")
label_161 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_161.grid(row=9, column=8, padx=0, pady=0, sticky="nsew")
label_162 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_162.grid(row=9, column=9, padx=0, pady=0, sticky="nsew")
label_163 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_163.grid(row=9, column=10, padx=0, pady=0, sticky="nsew")
label_164 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_164.grid(row=9, column=11, padx=0, pady=0, sticky="nsew")
label_165 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_165.grid(row=9, column=12, padx=0, pady=0, sticky="nsew")
label_166 = tk.Label(Frame4, text="%Defect:",
                     fg="black", bg="#FBE2D5", anchor="e")
label_166.grid(row=10, column=0, padx=0, pady=0, sticky="nsew")
label_167 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_167.grid(row=10, column=1, padx=0, pady=0, sticky="nsew")
label_168 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_168.grid(row=10, column=2, padx=0, pady=0, sticky="nsew")
label_169 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_169.grid(row=10, column=3, padx=0, pady=0, sticky="nsew")
label_170 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_170.grid(row=10, column=4, padx=0, pady=0, sticky="nsew")
label_171 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_171.grid(row=10, column=5, padx=0, pady=0, sticky="nsew")
label_172 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_172.grid(row=10, column=6, padx=0, pady=0, sticky="nsew")
label_173 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_173.grid(row=10, column=7, padx=0, pady=0, sticky="nsew")
label_174 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_174.grid(row=10, column=8, padx=0, pady=0, sticky="nsew")
label_175 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_175.grid(row=10, column=9, padx=0, pady=0, sticky="nsew")
label_176 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_176.grid(row=10, column=10, padx=0, pady=0, sticky="nsew")
label_177 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_177.grid(row=10, column=11, padx=0, pady=0, sticky="nsew")
label_178 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_178.grid(row=10, column=12, padx=0, pady=0, sticky="nsew")
label_179 = tk.Label(Frame5, fg="black", bg=color_1, anchor="sw")
label_179.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")
button_12 = tk.Button(Frame5, text="Defectos", height=0, width=0,
                      border=3, background="yellow", command=defect_root)
button_12.grid(row=0, column=1, padx=2, pady=5, sticky="nsew")
button_13 = tk.Button(Frame5, text="Soporte", height=0, width=0,
                      border=3, background="red", command=lambda: support_root(soporte_andon))
button_13.grid(row=0, column=2, padx=2, pady=5, sticky="nsew")
button_14 = tk.Button(Frame5, text="Parámetros", height=0, width=0,
                      border=3, background="#D86DCD", command=root_parametros)
button_14.grid(row=0, column=3, padx=2, pady=5, sticky="nsew")
button_15 = tk.Button(Frame5, text="Registros", height=0, width=0,
                      border=3, background="#0070C0", command=lambda: root_registros(actualizar_principal))
button_15.grid(row=0, column=4, padx=2, pady=5, sticky="nsew")
button_16 = tk.Button(Frame5, text="LogFile", height=0, width=0,
                      border=3, background="#00B050", command=lambda: root_logfile(actualizar_principal))
button_16.grid(row=0, column=5, padx=2, pady=5, sticky="nsew")
label_180 = tk.Label(Frame5, text="Registros SEHO Rev8.0 (By: Oscar Tovar)",
                     fg="black", bg=color_1, anchor="se")
label_180.grid(row=0, column=6, padx=0, pady=5, sticky="nsew")

# ---------------------------------------------------------------------------------------------------------------------
entry_0.bind("<KeyRelease>", suma_defectos)
entry_1.bind("<KeyRelease>", suma_defectos)
entry_2.bind("<KeyRelease>", suma_defectos)
entry_3.bind("<KeyRelease>", suma_defectos)
entry_4.bind("<KeyRelease>", suma_defectos)
entry_5.bind("<KeyRelease>", suma_defectos)
entry_6.bind("<KeyRelease>", suma_defectos)
entry_7.bind("<KeyRelease>", suma_defectos)
entry_8.bind("<KeyRelease>", suma_defectos)
entry_9.bind("<KeyRelease>", suma_defectos)
entry_10.bind("<KeyRelease>", suma_defectos)
entry_11.bind("<KeyRelease>", suma_defectos)
entry_12.bind("<KeyRelease>", suma_defectos)
entry_13.bind("<KeyRelease>", suma_defectos)
entry_14.bind("<KeyRelease>", suma_defectos)
entry_15.bind("<KeyRelease>", suma_defectos)
entry_16.bind("<KeyRelease>", suma_defectos)
entry_17.bind("<KeyRelease>", suma_defectos)
entry_18.bind("<KeyRelease>", suma_defectos)
entry_19.bind("<KeyRelease>", suma_defectos)
entry_20.bind("<KeyRelease>", suma_defectos)
entry_21.bind("<KeyRelease>", suma_defectos)
entry_22.bind("<KeyRelease>", suma_defectos)
entry_23.bind("<KeyRelease>", suma_defectos)
entry_24.bind("<KeyRelease>", suma_defectos)
entry_25.bind("<KeyRelease>", suma_defectos)
entry_26.bind("<KeyRelease>", suma_defectos)
entry_27.bind("<KeyRelease>", suma_defectos)
entry_28.bind("<KeyRelease>", suma_defectos)
entry_29.bind("<KeyRelease>", suma_defectos)
entry_30.bind("<KeyRelease>", buscar_pallets)
entry_30.bind('<Return>', guardar_datos)
# ---------------------------------------------------------------------------------------------------------------------
Frame0.grid(row=0, column=0, sticky="nsew")
Frame1.grid(row=1, column=0, sticky="nsew")
Frame2.grid(row=2, column=0, sticky="nsew")
Frame3.grid(row=3, column=0, sticky="nsew")
Frame4.grid(row=4, column=0, sticky="nsew")
Frame5.grid(row=5, column=0, sticky="nsew")

if __name__ == "__main__":
    actualizar_fecha_hora()
    root_scale()
    root.after(1000, calcular_defectos)
    root.mainloop()
