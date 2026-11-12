"""SEHO Rev9.1 - arranque modular de compatibilidad.
Las partes se ejecutan en el mismo espacio de nombres, en orden original.
Es una etapa transitoria; no son módulos independientes todavía.
"""
from pathlib import Path
BASE = Path(__file__).resolve().parent
PARTES = ['00_inicio.py', '01_configuracion_y_utilidades.py', '02_parametros.py', '03_ventanas_registros.py', '04_soporte.py', '05_dashboard.py', '06_definiciones_y_csv.py', '07_calculos.py', '08_comunicaciones.py', '10_mantenimiento.py', '09_interfaz_principal.py']
for nombre in PARTES:
    archivo = BASE / nombre
    exec(compile(archivo.read_text(encoding="utf-8"), str(archivo), "exec"), globals())
