"""SEHO Rev9.1 - arranque modular de compatibilidad.
Las partes se ejecutan en el mismo espacio de nombres, en orden original.
Es una etapa transitoria; no son módulos independientes todavía.
"""
from pathlib import Path
BASE = Path(__file__).resolve().parent
PARTES = ['C:/Registro_defectos_SEHO/SystemFiles/00_inicio.py',
          'C:/Registro_defectos_SEHO/SystemFiles/01_configuracion_y_utilidades.py',
          'C:/Registro_defectos_SEHO/SystemFiles/02_parametros.py',
          'C:/Registro_defectos_SEHO/SystemFiles/03_ventanas_registros.py',
          'C:/Registro_defectos_SEHO/SystemFiles/04_soporte.py',
          'C:/Registro_defectos_SEHO/SystemFiles/05_dashboard.py',
          'C:/Registro_defectos_SEHO/SystemFiles/06_definiciones_y_csv.py',
          'C:/Registro_defectos_SEHO/SystemFiles/07_calculos.py',
          'C:/Registro_defectos_SEHO/SystemFiles/08_comunicaciones.py',
          'C:/Registro_defectos_SEHO/SystemFiles/09_mantenimiento.py',
          'C:/Registro_defectos_SEHO/SystemFiles/10_interfaz_principal.py']
for nombre in PARTES:
    archivo = BASE / nombre
    exec(compile(archivo.read_text(encoding="utf-8"),
         str(archivo), "exec"), globals())
