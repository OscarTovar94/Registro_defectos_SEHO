"""Mantenimiento preventivo de pallets (SEHO Rev9.2).

La cantidad total se obtiene de Register.csv. Maintenance.csv registra el
punto de corte del contador y mantiene el historial sin alterar producción.
"""
import csv as _csv_mto
from pathlib import Path as _Path_mto
from datetime import datetime as _datetime_mto
import tkinter as _tk_mto
from tkinter import ttk as _ttk_mto, messagebox as _msg_mto
from tkcalendar import Calendar as _Calendar_mto
from matplotlib.figure import Figure as _Figure_mto
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as _FigureCanvas_mto

_MTO_COLS = ["Pallet", "Fecha de mantenimiento",
             "Vueltas realizadas", "Vueltas totales al mantenimiento"]


def _mto_paths():
    register = _Path_mto(csv_file2)
    parametros = _Path_mto(settings_root("Parameters"))
    return register, parametros, register.with_name("Maintenance.csv")


def _mto_pallet(valor):
    valor = str(valor).strip()
    try:
        return str(int(valor)) if float(valor).is_integer() else valor
    except (ValueError, OverflowError):
        return valor


def _mto_limite(valor):
    try:
        numero = int(str(valor).strip())
        return numero if numero > 0 else 30
    except (ValueError, TypeError):
        return 30


def _mto_lectura_csv(ruta):
    if not ruta.exists():
        return []
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        return list(_csv_mto.DictReader(archivo))


def _mto_fecha(texto):
    try:
        return _datetime_mto.strptime(str(texto).strip(), "%d/%m/%Y %H:%M:%S")
    except (ValueError, TypeError):
        return None


def obtener_estado_mantenimiento():
    """Devuelve dict de pallets con sus ciclos y estado actual."""
    ruta_registro, ruta_parametros, ruta_mantenimiento = _mto_paths()
    parametros = {}
    for fila in _mto_lectura_csv(ruta_parametros):
        pallet = _mto_pallet(fila.get("Pallet", ""))
        if pallet:
            parametros[pallet] = {"modelo": fila.get("Modelo", ""),
                                  "limite": _mto_limite(fila.get("Mantenimientos", ""))}

    registros = {}
    for fila in _mto_lectura_csv(ruta_registro):
        pallet = _mto_pallet(fila.get("Pallet", ""))
        if not pallet:
            continue
        datos = registros.setdefault(pallet, {"total": 0, "fechas": []})
        datos["total"] += 1
        fecha = _mto_fecha(fila.get("Fecha/Hora", ""))
        if fecha:
            datos["fechas"].append(fecha)

    ultimo_mantenimiento = {}
    conteo_mantenimientos = {}
    for fila in _mto_lectura_csv(ruta_mantenimiento):
        pallet = _mto_pallet(fila.get("Pallet", ""))
        fecha = _mto_fecha(fila.get("Fecha de mantenimiento", ""))
        if not pallet or fecha is None:
            continue
        conteo_mantenimientos[pallet] = conteo_mantenimientos.get(
            pallet, 0) + 1
        previo = ultimo_mantenimiento.get(pallet)
        if previo is None or fecha >= previo[0]:
            try:
                base = int(fila.get("Vueltas totales al mantenimiento", 0))
            except (ValueError, TypeError):
                base = 0
            ultimo_mantenimiento[pallet] = (fecha, max(0, base))

    estados = {}
    for pallet in set(parametros) | set(registros):
        datos = registros.get(pallet, {"total": 0, "fechas": []})
        config = parametros.get(
            pallet, {"modelo": "(sin configurar)", "limite": 30})
        ultimo = ultimo_mantenimiento.get(pallet)
        total = datos["total"]
        # Fecha real del mantenimiento: una captura tardía no debe borrar
        # las vueltas realizadas después de la intervención.
        if ultimo:
            ciclo = sum(f > ultimo[0] for f in datos["fechas"])
            # Si existen filas antiguas sin fecha válida, conservarlas en el ciclo.
            ciclo += total - len(datos["fechas"])
        else:
            ciclo = total
        fechas_ciclo = [f for f in datos["fechas"]
                        if not ultimo or f > ultimo[0]]
        inicio = min(fechas_ciclo).strftime(
            "%d/%m/%Y %H:%M:%S") if fechas_ciclo else "—"
        limite = config["limite"]
        estado = "VENCIDO" if ciclo >= limite else "PRÓXIMO" if ciclo >= limite * 0.8 else "NORMAL"
        estados[pallet] = {
            "pallet": pallet, "modelo": config["modelo"], "ciclo": ciclo,
            "total": total, "limite": limite, "inicio": inicio,
            "ultimo": ultimo[0].strftime("%d/%m/%Y %H:%M:%S") if ultimo else "—",
            "mantenimientos": conteo_mantenimientos.get(pallet, 0), "estado": estado,
        }
    return estados


def alerta_mantenimiento(pallet, despues_de_guardar=False):
    """Aviso no bloqueante para producción; solo se muestra cuando corresponde."""
    estado = obtener_estado_mantenimiento().get(_mto_pallet(pallet))
    if not estado or estado["estado"] != "VENCIDO":
        return
    # Antes de guardar: avisar si ya estaba vencido; después: avisar al llegar justo al límite.
    if despues_de_guardar and estado["ciclo"] != estado["limite"]:
        return
    _msg_mto.showwarning(
        "Mantenimiento requerido",
        f"Pallet: {estado['pallet']} | Modelo: {estado['modelo']}\n"
        f"Vueltas del ciclo: {estado['ciclo']} / {estado['limite']}\n"
        f"Excedidas: {max(0, estado['ciclo'] - estado['limite'])}\n\n"
        "Este pallet requiere mantenimiento preventivo.\n"
        "Puede continuar con el registro. La alerta seguirá apareciendo "
        "hasta registrar el mantenimiento.", parent=root)


def _mto_registrar(pallet, ventana, fecha_real=None):
    estados = obtener_estado_mantenimiento()
    estado = estados.get(_mto_pallet(pallet))
    if estado is None:
        _msg_mto.showwarning(
            "Pallet", "Seleccione un pallet válido.", parent=ventana)
        return
    fecha = fecha_real or _datetime_mto.now()
    if fecha > _datetime_mto.now():
        _msg_mto.showwarning(
            "Fecha", "No puede registrar un mantenimiento con fecha futura.", parent=ventana)
        return

    ruta_registro, _, ruta = _mto_paths()
    anteriores = [f for f in _mto_lectura_csv(ruta)
                  if _mto_pallet(f.get("Pallet", "")) == estado["pallet"]]
    fechas_anteriores = [_mto_fecha(
        f.get("Fecha de mantenimiento")) for f in anteriores]
    fechas_anteriores = [f for f in fechas_anteriores if f]
    if fechas_anteriores and fecha <= max(fechas_anteriores):
        _msg_mto.showwarning(
            "Fecha", "La fecha debe ser posterior al último mantenimiento registrado de este pallet.", parent=ventana)
        return

    fechas_registro = [_mto_fecha(f.get("Fecha/Hora")) for f in _mto_lectura_csv(ruta_registro)
                       if _mto_pallet(f.get("Pallet", "")) == estado["pallet"]]
    total_hasta_fecha = sum(f is not None and f <=
                            fecha for f in fechas_registro)
    inicio_ciclo = max(fechas_anteriores) if fechas_anteriores else None
    vueltas_realizadas = sum(f is not None and f <= fecha and (inicio_ciclo is None or f > inicio_ciclo)
                             for f in fechas_registro)
    posteriores = sum(f is not None and f > fecha for f in fechas_registro)

    if not _msg_mto.askyesno("Confirmar mantenimiento",
                             f"¿Confirma que se REALIZÓ el mantenimiento del pallet {pallet}?\\n\\n"
                             f"Fecha real: {fecha.strftime('%d/%m/%Y %H:%M:%S')}\\n"
                             f"Vueltas del ciclo finalizado: {vueltas_realizadas}\\n"
                             f"Vueltas históricas hasta esa fecha: {total_hasta_fecha}\\n"
                             f"Vueltas posteriores (nuevo ciclo): {posteriores}\\n\\n"
                             "Se conservará el historial y el contador del nuevo ciclo comenzará "
                             "desde la fecha real del mantenimiento.", parent=ventana):
        return
    existe = ruta.exists() and ruta.stat().st_size > 0
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("a", newline="", encoding="utf-8") as archivo:
            writer = _csv_mto.DictWriter(archivo, fieldnames=_MTO_COLS)
            if not existe:
                writer.writeheader()
            writer.writerow({"Pallet": estado["pallet"],
                             "Fecha de mantenimiento": fecha.strftime("%d/%m/%Y %H:%M:%S"),
                             "Vueltas realizadas": vueltas_realizadas,
                             "Vueltas totales al mantenimiento": total_hasta_fecha})
    except OSError as exc:
        _msg_mto.showerror(
            "Error", f"No se pudo guardar el mantenimiento:\\n{exc}", parent=ventana)
        return
    _msg_mto.showinfo(
        "Mantenimiento", f"Mantenimiento del pallet {pallet} registrado.", parent=ventana)
    ventana._mto_refrescar()


def _mto_seleccionar_fecha(ventana, pallet):
    """Diálogo modal para registrar una intervención realizada en otra fecha."""
    # DateEntry crea un calendario emergente que utiliza su propio grab.
    # Liberar el grab de la ventana principal antes de abrir el selector.
    if ventana.grab_current() is not None:
        ventana.grab_release()
    dialogo = _tk_mto.Toplevel(ventana)
    dialogo.title(f"Fecha de mantenimiento — Pallet {pallet}")
    dialogo.geometry("440x410")
    dialogo.resizable(False, False)
    dialogo.transient(ventana)
    dialogo.lift()
    dialogo.focus_force()
    # No usar grab_set aquí: el calendario queda integrado en el diálogo.
    dialogo.configure(bg="#F1F1F1")
    _tk_mto.Label(dialogo, text=f"Fecha real del mantenimiento — Pallet {pallet}",
                  font=("Arial", 12, "bold"), bg="#F1F1F1").pack(pady=(15, 12))
    # Calendario integrado: no utiliza popup ni grab adicional.
    # Evita que el selector se cierre al hacer clic sobre una fecha.
    selector = _Calendar_mto(dialogo, selectmode="day",
                             date_pattern="dd/mm/yyyy")
    selector.pack(pady=5, padx=12, fill="both", expand=True)
    _tk_mto.Label(dialogo, text="Hora (HH:MM:SS)",
                  bg="#F1F1F1").pack(pady=(8, 2))
    hora = _tk_mto.Entry(dialogo, justify="center", width=15)
    hora.insert(0, _datetime_mto.now().strftime("%H:%M:%S"))
    hora.pack()
    acciones = _tk_mto.Frame(dialogo, bg="#F1F1F1")
    acciones.pack(pady=18)

    def cerrar_dialogo():
        if dialogo.winfo_exists():
            dialogo.destroy()
        if ventana.winfo_exists():
            ventana.grab_set()
            ventana.lift()

    def guardar():
        try:
            fecha = _datetime_mto.strptime(
                f"{selector.get_date()} {hora.get().strip()}",
                "%d/%m/%Y %H:%M:%S")
        except ValueError:
            _msg_mto.showwarning(
                "Fecha", "Ingrese una hora válida en formato HH:MM:SS.", parent=dialogo)
            return
        # Restaurar el grab de la ventana principal antes de confirmar.
        cerrar_dialogo()
        _mto_registrar(pallet, ventana, fecha)
    _tk_mto.Button(acciones, text="Confirmar fecha", bg="#2E8B57", fg="white",
                   command=guardar).pack(side="left", padx=8)
    _tk_mto.Button(acciones, text="Cancelar",
                   command=cerrar_dialogo).pack(side="left", padx=8)
    dialogo.protocol("WM_DELETE_WINDOW", cerrar_dialogo)
    # No utilizar wait_window: el diálogo funciona con callbacks y permanece
    # abierto mientras se elige la fecha, hasta confirmar o cancelar.


def root_mantenimiento():
    ventana = _tk_mto.Toplevel(root)
    ventana.title("Mantenimiento de pallets")
    # ventana.geometry("1180x650")
    # ventana.minsize(850, 450)
    ventana.transient(root)
    ventana.update_idletasks()
    try:
        ventana.attributes("-fullscreen", True)
    except _tk_mto.TclError:
        ventana.state("zoomed")

    ventana.lift()
    ventana.focus_force()
    # Modal: no permite interactuar con la ventana principal.
    ventana.grab_set()
    ventana.protocol("WM_DELETE_WINDOW", ventana.destroy)
    ventana.bind("<Escape>", lambda evento: ventana.destroy())
    ventana.configure(bg="#F1F1F1")
    encabezado = _tk_mto.Frame(ventana, bg="#F1F1F1")
    encabezado.pack(fill="x", padx=12, pady=12)
    _tk_mto.Label(encabezado, text="Mantenimiento de pallets", font=(
        "Arial", 18, "bold"), bg="#F1F1F1").pack(side="left")
    _tk_mto.Button(encabezado, text="Cerrar", bg="#CF4444", fg="white",
                   command=ventana.destroy).pack(side="right", padx=5)
    _tk_mto.Button(encabezado, text="Actualizar", bg="#4472C4", fg="white",
                   command=lambda: refrescar()).pack(side="right", padx=5)
    # Panel superior compacto: indicadores y gráfica, sin cambiar el cálculo.
    superior = _tk_mto.Frame(ventana, bg="#F1F1F1")
    superior.pack(fill="x", padx=12, pady=(0, 8))
    tarjetas = _tk_mto.Frame(superior, bg="#F1F1F1")
    tarjetas.pack(side="left", fill="y", padx=(0, 12))
    indicadores = {}
    for i, (clave, titulo, color) in enumerate((
        ("total", "TOTAL PALLETS", "#415A77"),
        ("normal", "OPERATIVOS", "#278A65"),
        ("proximos", "PRÓXIMOS", "#D69B2D"),
        ("vencidos", "VENCIDOS", "#C64A4A"),
    )):
        tarjeta = _tk_mto.Frame(tarjetas, bg=color, width=138, height=100)
        tarjeta.grid(row=i // 2, column=i % 2, padx=4, pady=4, sticky="nsew")
        tarjeta.pack_propagate(False)
        _tk_mto.Label(tarjeta, text=titulo, bg=color, fg="white",
                      font=("Arial", 9, "bold")).pack(pady=(12, 2))
        valor = _tk_mto.Label(tarjeta, text="0", bg=color, fg="white",
                              font=("Arial", 22, "bold"))
        valor.pack()
        indicadores[clave] = valor

    grafica_marco = _tk_mto.Frame(superior, bg="white", bd=1, relief="solid")
    grafica_marco.pack(side="left", fill="both", expand=True, padx=(4, 0))
    figura = _Figure_mto(figsize=(8, 2.15), dpi=95, facecolor="white")
    eje = figura.add_subplot(111)
    figura.subplots_adjust(left=0.13, right=0.96, top=0.83, bottom=0.16)
    canvas_grafica = _FigureCanvas_mto(figura, master=grafica_marco)
    canvas_grafica.get_tk_widget().configure(height=210)
    canvas_grafica.get_tk_widget().pack(fill="both", expand=True)

    marco = _tk_mto.Frame(ventana)
    marco.pack(fill="both", expand=True, padx=12)
    columnas = ("Pallet", "Modelo", "Vueltas ciclo", "Vueltas totales",
                "Fecha de inicio", "Fecha de mantenimiento", "Estado")
    tabla = _ttk_mto.Treeview(marco, columns=columnas,
                              show="headings", selectmode="browse")
    for col, ancho in zip(columnas, (90, 170, 130, 130, 190, 190, 130)):
        tabla.heading(col, text=col)
        tabla.column(col, width=ancho, anchor="center", minwidth=85)
    sy = _tk_mto.Scrollbar(marco, orient="vertical", command=tabla.yview)
    sx = _tk_mto.Scrollbar(marco, orient="horizontal", command=tabla.xview)
    tabla.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
    # Desplazamiento con rueda del ratón (Windows/macOS) y Linux.
    # Vinculado únicamente a la tabla: no interfiere con el calendario
    # ni con otros controles de la ventana.

    def _rueda_pallets(evento):
        if getattr(evento, "num", None) == 4:
            unidades = -1
        elif getattr(evento, "num", None) == 5:
            unidades = 1
        else:
            delta = getattr(evento, "delta", 0)
            if not delta:
                return
            unidades = -1 if delta > 0 else 1
            if abs(delta) >= 120:
                unidades *= max(1, abs(delta) // 120)
        tabla.yview_scroll(unidades, "units")
        return "break"

    for widget in (tabla, sy):
        widget.bind("<MouseWheel>", _rueda_pallets)
        widget.bind("<Button-4>", _rueda_pallets)
        widget.bind("<Button-5>", _rueda_pallets)
    tabla.grid(row=0, column=0, sticky="nsew")
    sy.grid(row=0, column=1, sticky="ns")
    sx.grid(row=1, column=0, sticky="ew")
    marco.rowconfigure(0, weight=1)
    marco.columnconfigure(0, weight=1)
    tabla.tag_configure("VENCIDO", background="#F4AAAA", foreground="#700000")
    tabla.tag_configure("PRÓXIMO", background="#FFE7A3", foreground="#6E4900")
    tabla.tag_configure("NORMAL", background="white", foreground="black")
    detalle = _tk_mto.Label(ventana, text="Seleccione un pallet para consultar su historial.",
                            bg="#E7EDF4", fg="#263C52", anchor="w",
                            font=("Arial", 10, "bold"), padx=12, pady=8)
    detalle.pack(fill="x", padx=12, pady=(6, 0))
    pie = _tk_mto.Frame(ventana, bg="#F1F1F1")
    pie.pack(fill="x", padx=12, pady=12)
    _tk_mto.Label(pie, text="Seleccione un pallet y registre la fecha real del mantenimiento.",
                  bg="#F1F1F1").pack(anchor="center", pady=(0, 8))
    botones = _tk_mto.Frame(pie, bg="#F1F1F1")
    botones.pack(anchor="center")

    def registrar_seleccionado():
        seleccion = tabla.selection()
        if not seleccion:
            _msg_mto.showwarning(
                "Mantenimiento", "Seleccione un pallet de la tabla.", parent=ventana)
            return
        _mto_registrar(tabla.item(seleccion[0], "values")[0], ventana)

    def registrar_fecha_manual():
        seleccion = tabla.selection()
        if not seleccion:
            _msg_mto.showwarning(
                "Mantenimiento", "Seleccione un pallet de la tabla.", parent=ventana)
            return
        _mto_seleccionar_fecha(ventana, tabla.item(seleccion[0], "values")[0])
    _tk_mto.Button(botones, text="Registrar mantenimiento (ahora)", bg="#2E8B57", fg="white",
                   font=("Arial", 11, "bold"), padx=16, pady=7,
                   command=registrar_seleccionado).pack(side="left", padx=10)
    _tk_mto.Button(botones, text="Registrar con fecha manual", bg="#4472C4", fg="white",
                   font=("Arial", 11, "bold"), padx=16, pady=7,
                   command=registrar_fecha_manual).pack(side="left", padx=10)
    estados_actuales = {}

    def actualizar_detalle(evento=None):
        seleccion = tabla.selection()
        if not seleccion:
            detalle.configure(
                text="Seleccione un pallet para consultar su historial.")
            return
        pallet = str(tabla.item(seleccion[0], "values")[0])
        estado = estados_actuales.get(_mto_pallet(pallet))
        if estado:
            detalle.configure(
                text=f"Pallet {estado['pallet']}  |  Modelo: {estado['modelo']}  |  "
                     f"Vueltas totales: {estado['total']}  |  "
                     f"Mantenimientos realizados: {estado['mantenimientos']}  |  "
                     f"Último mantenimiento: {estado['ultimo']}"
            )
    tabla.bind("<<TreeviewSelect>>", actualizar_detalle)

    def refrescar():
        try:
            estados = obtener_estado_mantenimiento()
        except (OSError, UnicodeError, _csv_mto.Error) as exc:
            _msg_mto.showerror("Error de lectura", str(exc), parent=ventana)
            return
        pallet_seleccionado = None
        seleccion = tabla.selection()
        if seleccion:
            pallet_seleccionado = str(tabla.item(seleccion[0], "values")[0])
        estados_actuales.clear()
        estados_actuales.update(estados)
        tabla.delete(*tabla.get_children())
        prioridad = {"VENCIDO": 0, "PRÓXIMO": 1, "NORMAL": 2}
        ordenados = sorted(estados.values(), key=lambda d: (
            prioridad[d["estado"]], -(d["ciclo"]-d["limite"]), -d["ciclo"], d["pallet"]))
        for e in ordenados:
            item = tabla.insert("", "end", values=(
                e["pallet"], e["modelo"], f'{e["ciclo"]} / {e["limite"]}',
                e["total"], e["inicio"], e["ultimo"], e["estado"]),
                tags=(e["estado"],))
            if e["pallet"] == pallet_seleccionado:
                tabla.selection_set(item)
                tabla.see(item)
        indicadores["total"].configure(text=str(len(estados)))
        indicadores["normal"].configure(
            text=str(sum(x["estado"] == "NORMAL" for x in estados.values())))
        indicadores["proximos"].configure(
            text=str(sum(x["estado"] == "PRÓXIMO" for x in estados.values())))
        indicadores["vencidos"].configure(
            text=str(sum(x["estado"] == "VENCIDO" for x in estados.values())))
        actualizar_detalle()

        # Gráfica de 10 pallets más urgentes: porcentajes comparables aun
        # cuando cada pallet tenga un límite de mantenimiento diferente.
        top = sorted(estados.values(),
                     key=lambda e: (e["ciclo"] / e["limite"], e["ciclo"]),
                     reverse=True)[:10]
        eje.clear()
        eje.set_title("Top 10 · Uso del ciclo respecto al límite", fontsize=10,
                      color="#263C52", loc="left", pad=8)
        if top:
            top = list(reversed(top))
            porcentajes = [100 * e["ciclo"] / e["limite"] for e in top]
            colores = ["#C64A4A" if x >= 100 else "#D69B2D" if x >= 80
                       else "#278A65" for x in porcentajes]
            posiciones = list(range(len(top)))
            eje.barh(posiciones, porcentajes, color=colores, height=0.67)
            eje.set_yticks(
                posiciones, [f"Pallet {e['pallet']}" for e in top], fontsize=8)
            eje.set_xlim(0, max(115, max(porcentajes) * 1.14))
            for y, porcentaje in enumerate(porcentajes):
                eje.text(porcentaje + 1.5, y, f"{porcentaje:.0f}%",
                         va="center", fontsize=8, color="#263C52")
        else:
            eje.text(0.5, 0.5, "Sin registros de pallets", transform=eje.transAxes,
                     ha="center", va="center", color="#667788")
            eje.set_yticks([])
        eje.axvline(100, color="#B93C3C", linestyle="--", linewidth=1)
        eje.spines[["top", "right", "left"]].set_visible(False)
        eje.tick_params(axis="both", length=0, labelsize=8)
        eje.grid(axis="x", alpha=0.13)
        eje.set_axisbelow(True)
        canvas_grafica.draw_idle()

    ventana._mto_refrescar = refrescar
    refrescar()
