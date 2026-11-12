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
                col_fecha = "Fecha/Hora"

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
                self.tree.insert("", "end", values=["" if pd.isna(v) else v for v in row], tags=tag)

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
                col_fecha = "Fecha/Hora"

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
                self.tree.insert("", "end", values=["" if pd.isna(v) else v for v in row], tags=tag)

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


