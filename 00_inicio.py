import tkinter.font as tkfont
import socket
import matplotlib.colors as mcolors
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import serial
from tkcalendar import DateEntry
import chardet
import pandas as pd
from PIL import Image, ImageTk
import time
from tkinter import ttk
from datetime import datetime
import os
import csv
from tkinter import messagebox
import tkinter as tk
import sys
import win32event
import win32api
import winerror

# ---- Control de instancia única ----
mutex = win32event.CreateMutex(None, False, "DefectosSEHO_UnicaInstancia")
last_error = win32api.GetLastError()

if last_error == winerror.ERROR_ALREADY_EXISTS:
    sys.exit(0)
# ------- libraries


# ------------------------------------- Logic -------------------------------------------------------------------------

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

csv_files = [csv_file]

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


