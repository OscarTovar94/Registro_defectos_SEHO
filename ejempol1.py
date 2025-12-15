import tkinter as tk
from tkcalendar import DateEntry  # Importa el widget DateEntry


def obtener_fecha_seleccionada():
    fecha = cal.get()  # Obtiene la fecha del widget
    print(f"Fecha seleccionada: {fecha}")  # Imprime la fecha en la consola


# Configurar la ventana principal
root = tk.Tk()
root.title("Selector de Fecha Tkinter")
root.geometry("300x200")

# Crear el widget DateEntry
# date_pattern='dd/mm/yyyy' para formato día/mes/año
cal = DateEntry(root, width=12, background='darkblue',
                foreground='white', borderwidth=2,
                date_pattern='dd/mm/yyyy')
cal.pack(pady=20)

# Botón para obtener la fecha
boton_obtener = tk.Button(root, text="Obtener Fecha",
                          command=obtener_fecha_seleccionada)
boton_obtener.pack(pady=10)

# Iniciar el bucle principal de Tkinter
root.mainloop()
