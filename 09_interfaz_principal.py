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
Frame1.grid_rowconfigure(9, weight=1)
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
Frame4.grid_rowconfigure(11, weight=0)
Frame4.grid_rowconfigure(12, weight=0)
Frame4.grid_rowconfigure(13, weight=0)
Frame4.grid_rowconfigure(14, weight=0)
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

# ----- Defecto 31
# label_181: Defacto 31
label_181 = tk.Label(Frame1, text=f"{defect31}:",
                     fg="black", bg=color_1)
label_181.grid(row=7, column=0, padx=0, pady=0, sticky="e")

# entry_31: Defecto 31
entry_31 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_31.grid(row=7, column=1, padx=0, pady=0, sticky="w")

# ----- Defecto 32
# label_182: Defacto 32
label_182 = tk.Label(Frame1, text=f"{defect32}:",
                     fg="black", bg=color_1)
label_182.grid(row=7, column=2, padx=0, pady=0, sticky="e")

# entry_32: Defecto 32
entry_32 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_32.grid(row=7, column=3, padx=0, pady=0, sticky="w")

# ----- Defecto 33
# label_183: Defacto 33
label_183 = tk.Label(Frame1, text=f"{defect33}:",
                     fg="black", bg=color_1)
label_183.grid(row=7, column=4, padx=0, pady=0, sticky="e")

# entry_33: Defecto 33
entry_33 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_33.grid(row=7, column=5, padx=0, pady=0, sticky="w")

# ----- Defecto 34
# label_184: Defacto 34
label_184 = tk.Label(Frame1, text=f"{defect34}:",
                     fg="black", bg=color_1)
label_184.grid(row=7, column=6, padx=0, pady=0, sticky="e")

# entry_34: Defecto 34
entry_34 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_34.grid(row=7, column=7, padx=0, pady=0, sticky="w")

# ----- Defecto 35
# label_185: Defacto 35
label_185 = tk.Label(Frame1, text=f"{defect35}:",
                     fg="black", bg=color_1)
label_185.grid(row=7, column=8, padx=0, pady=0, sticky="e")

# entry_35: Defecto 35
entry_35 = tk.Entry(Frame1, width=5, bg=color_2, justify="center")
entry_35.grid(row=7, column=9, padx=0, pady=0, sticky="w")

# --------------------------
label_32 = tk.Label(Frame1, text="Número de pallet:",
                    fg="black", bg=color_1)
label_32.grid(row=8, column=0, padx=0, columnspan=10, pady=0, sticky="s")

entry_30 = tk.Entry(Frame1, width=25, justify="center",
                    background="springgreen", border=3)
entry_30.grid(row=9, column=0, columnspan=10, padx=0, pady=0, sticky="n")

entry_30.focus()
# -------------------------

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


def reiniciar():
    """Reset the labels and buttons to their initial state."""
    for label in (label_186, label_187, label_188, label_189, label_190, label_191, label_192,
                  label_193, label_194, label_195, label_196, label_197, label_200, label_201, label_202, label_203, label_204, label_205, label_206,
                  label_207, label_208, label_209, label_210, label_211, label_213, label_214, label_215, label_216, label_217, label_218, label_219,
                  label_220, label_221, label_222, label_223, label_224):
        label.config(text="", bg=color_1)

    calcular_defectos()


button_17 = tk.Button(Frame3, text="Actualizar", height=0, width=0,
                      border=3, background="#00B050", command=reiniciar)
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

# --------------------------- Insertar aquí los nuevos botones de cambio de número de orden.

color_button_norden = "#F1A983"
color_button_orden_ok = "#F2CEEF"
color_label_part = "#F2CEEF"
color_label_part_ok = "#F2CEEF"

# -------------------------------------------------------------------------------------------
label_198 = tk.Label(Frame4, text="No. Parte",
                     fg="black", bg="#47D359", anchor="e")
label_198.grid(row=5, column=0, padx=0, pady=0, sticky="nsew")

label_186 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_186.grid(row=5, column=1, padx=0, pady=0, sticky="nsew")

label_187 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_187.grid(row=5, column=2, padx=0, pady=0, sticky="nsew")

label_188 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_188.grid(row=5, column=3, padx=0, pady=0, sticky="nsew")

label_189 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_189.grid(row=5, column=4, padx=0, pady=0, sticky="nsew")

label_190 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_190.grid(row=5, column=5, padx=0, pady=0, sticky="nsew")

label_191 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_191.grid(row=5, column=6, padx=0, pady=0, sticky="nsew")

label_192 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_192.grid(row=5, column=7, padx=0, pady=0, sticky="nsew")

label_193 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_193.grid(row=5, column=8, padx=0, pady=0, sticky="nsew")

label_194 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_194.grid(row=5, column=9, padx=0, pady=0, sticky="nsew")

label_195 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_195.grid(row=5, column=10, padx=0, pady=0, sticky="nsew")

label_196 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_196.grid(row=5, column=11, padx=0, pady=0, sticky="nsew")

label_197 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_197.grid(row=5, column=12, padx=0, pady=0, sticky="nsew")

# -------------------------------------------------------------------------------------------

label_199 = tk.Label(Frame4, text="No. Orden",
                     fg="black", bg="#47D359", anchor="e")
label_199.grid(row=6, column=0, padx=0, pady=0, sticky="nsew")

label_200 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_200.grid(row=6, column=1, padx=0, pady=0, sticky="nsew")

label_201 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_201.grid(row=6, column=2, padx=0, pady=0, sticky="nsew")

label_202 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_202.grid(row=6, column=3, padx=0, pady=0, sticky="nsew")

label_203 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_203.grid(row=6, column=4, padx=0, pady=0, sticky="nsew")

label_204 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_204.grid(row=6, column=5, padx=0, pady=0, sticky="nsew")

label_205 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_205.grid(row=6, column=6, padx=0, pady=0, sticky="nsew")

label_206 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_206.grid(row=6, column=7, padx=0, pady=0, sticky="nsew")

label_207 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_207.grid(row=6, column=8, padx=0, pady=0, sticky="nsew")

label_208 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_208.grid(row=6, column=9, padx=0, pady=0, sticky="nsew")

label_209 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_209.grid(row=6, column=10, padx=0, pady=0, sticky="nsew")

label_210 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_210.grid(row=6, column=11, padx=0, pady=0, sticky="nsew")

label_211 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_211.grid(row=6, column=12, padx=0, pady=0, sticky="nsew")

# -------------------------------------------------------------------------------------------

label_212 = tk.Label(Frame4, text="No. Operador",
                     fg="black", bg="#47D359", anchor="e")
label_212.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")

label_213 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_213.grid(row=7, column=1, padx=0, pady=0, sticky="nsew")

label_214 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_214.grid(row=7, column=2, padx=0, pady=0, sticky="nsew")

label_215 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_215.grid(row=7, column=3, padx=0, pady=0, sticky="nsew")

label_216 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_216.grid(row=7, column=4, padx=0, pady=0, sticky="nsew")

label_217 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_217.grid(row=7, column=5, padx=0, pady=0, sticky="nsew")

label_218 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_218.grid(row=7, column=6, padx=0, pady=0, sticky="nsew")

label_219 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_219.grid(row=7, column=7, padx=0, pady=0, sticky="nsew")

label_220 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_220.grid(row=7, column=8, padx=0, pady=0, sticky="nsew")

label_221 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_221.grid(row=7, column=9, padx=0, pady=0, sticky="nsew")

label_222 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_222.grid(row=7, column=10, padx=0, pady=0, sticky="nsew")

label_223 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_223.grid(row=7, column=11, padx=0, pady=0, sticky="nsew")

label_224 = tk.Label(Frame4,
                     fg="black", bg=color_1)
label_224.grid(row=7, column=12, padx=0, pady=0, sticky="nsew")

# -------------------------------------------------------------------------------------------


def solicitar_orden_produccion(label_orden, label_parte, label_operador):
    """Solicita orden de producción, número de parte y operador."""

    ventana = tk.Toplevel(label_orden.winfo_toplevel())
    ventana.title("Datos de producción")
    ventana.geometry("430x310")
    ventana.resizable(False, False)
    ventana.configure(bg="#F2F2F2")

    # Mantener ventana modal
    ventana.transient(label_orden.winfo_toplevel())
    ventana.grab_set()

    # Permitir cerrar con la X
    def cerrar_ventana():
        ventana.grab_release()
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Centrar ventana
    ventana.update_idletasks()

    x = (ventana.winfo_screenwidth() - 430) // 2
    y = (ventana.winfo_screenheight() - 310) // 2

    ventana.geometry(f"430x310+{x}+{y}")

    # ==============================
    # NÚMERO DE ORDEN
    # ==============================

    tk.Label(
        ventana,
        text="Ingrese o escanee el número de orden:",
        font=("Arial", 11),
        bg="#F2F2F2"
    ).pack(pady=5)

    entry_orden = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center",
        width=25
    )
    entry_orden.pack(pady=10)

    # ==============================
    # NÚMERO DE PARTE
    # ==============================

    tk.Label(
        ventana,
        text="Ingrese o escanee el número de parte:",
        font=("Arial", 11),
        bg="#F2F2F2"
    ).pack(pady=5)

    entry_part = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center",
        width=25
    )
    entry_part.pack(pady=10)

    # ==============================
    # NÚMERO DE OPERADOR
    # ==============================

    tk.Label(
        ventana,
        text="Ingrese o escanee el número de operador:",
        font=("Arial", 11),
        bg="#F2F2F2"
    ).pack(pady=5)

    entry_operador = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center",
        width=25
    )
    entry_operador.pack(pady=10)

    # ==============================
    # VALIDAR ORDEN
    # ==============================

    def validar_orden():
        numero_orden = entry_orden.get().strip()

        if (
            len(numero_orden) != 9
            or not numero_orden[:2].isascii()
            or not numero_orden[:2].isalpha()
            or not numero_orden[:2].isupper()
        ):
            messagebox.showwarning(
                "Orden no válida",
                "La orden debe tener 9 caracteres y comenzar "
                "con dos letras mayúsculas.",
                parent=ventana
            )
            entry_orden.delete(0, tk.END)
            entry_orden.focus_set()
            return None

        return numero_orden

    # ==============================
    # CONFIRMAR ORDEN
    # ==============================

    def confirmar_orden(event=None):
        if validar_orden() is not None:
            entry_part.focus_set()

    # ==============================
    # VALIDAR NÚMERO DE PARTE
    # ==============================

    def validar_parte():
        numero_part = entry_part.get().strip()

        if (
            len(numero_part) < 6
            or not numero_part[:6].isascii()
            or not numero_part[:6].isdigit()
        ):
            messagebox.showwarning(
                "Número de parte no válido",
                "El número de parte debe contener al menos "
                "6 caracteres y los primeros 6 deben ser números.",
                parent=ventana
            )
            entry_part.delete(0, tk.END)
            entry_part.focus_set()
            return None

        return numero_part[:6]

    # ==============================
    # CONFIRMAR NÚMERO DE PARTE
    # ==============================

    def confirmar_part(event=None):
        if validar_parte() is not None:
            entry_operador.focus_set()

    # ==============================
    # CONFIRMAR OPERADOR Y GUARDAR
    # ==============================

    def confirmar_operador(event=None):

        numero_orden = validar_orden()
        if numero_orden is None:
            return

        numero_part = validar_parte()
        if numero_part is None:
            return

        numero_operador = entry_operador.get().strip()

        if (
            not 1 <= len(numero_operador) <= 4
            or not numero_operador.isascii()
            or not numero_operador.isdigit()
        ):
            messagebox.showwarning(
                "Número de operador no válido",
                "El número de operador debe contener "
                "entre 1 y 4 dígitos numéricos.",
                parent=ventana
            )
            entry_operador.delete(0, tk.END)
            entry_operador.focus_set()
            return

        # Guardar datos únicamente cuando los tres son válidos
        # Actualizar etiqueta de orden (el botón solo abre el formulario)
        label_orden.config(
            text=numero_orden,
            bg=color_button_orden_ok,
            fg="black"
        )

        # Actualizar número de parte
        label_parte.config(
            text=numero_part,
            bg=color_label_part_ok
        )

        # Actualizar número de operador
        label_operador.config(
            text=numero_operador,
            bg=color_label_part_ok
        )

        cerrar_ventana()

    # ==============================
    # BOTÓN CONFIRMAR
    # ==============================

    tk.Button(
        ventana,
        text="CONFIRMAR",
        font=("Arial", 11, "bold"),
        bg="#4CAF50",
        fg="white",
        width=18,
        command=confirmar_operador
    ).pack(pady=10)

    # ==============================
    # EVENTOS ENTER
    # ==============================

    entry_orden.bind("<Return>", confirmar_orden)
    entry_orden.bind("<KP_Enter>", confirmar_orden)

    entry_part.bind("<Return>", confirmar_part)
    entry_part.bind("<KP_Enter>", confirmar_part)

    entry_operador.bind("<Return>", confirmar_operador)
    entry_operador.bind("<KP_Enter>", confirmar_operador)

    # Enfoque inicial
    ventana.after(100, entry_orden.focus_force)

    # Esperar hasta cerrar ventana
    ventana.wait_window()


button_18 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_200, label_186, label_213))
button_18.grid(row=8, column=1, padx=0, pady=0, sticky="nsew")


button_19 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(
                          label_201, label_187, label_214)
                      )
button_19.grid(row=8, column=2, padx=0, pady=0, sticky="nsew")

button_20 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_202, label_188, label_215))
button_20.grid(row=8, column=3, padx=0, pady=0, sticky="nsew")

button_21 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_203, label_189, label_216))
button_21.grid(row=8, column=4, padx=0, pady=0, sticky="nsew")

button_22 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_204, label_190, label_217))
button_22.grid(row=8, column=5, padx=0, pady=0, sticky="nsew")

button_23 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_205, label_191, label_218))
button_23.grid(row=8, column=6, padx=0, pady=0, sticky="nsew")

button_24 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_206, label_192, label_219))
button_24.grid(row=8, column=7, padx=0, pady=0, sticky="nsew")

button_25 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_207, label_193, label_220))
button_25.grid(row=8, column=8, padx=0, pady=0, sticky="nsew")

button_26 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_208, label_194, label_221))
button_26.grid(row=8, column=9, padx=0, pady=0, sticky="nsew")

button_27 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_209, label_195, label_222))
button_27.grid(row=8, column=10, padx=0, pady=0, sticky="nsew")

button_28 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_210, label_196, label_223))
button_28.grid(row=8, column=11, padx=0, pady=0, sticky="nsew")

button_29 = tk.Button(Frame4, text="Dat. Prod.", height=0, width=0,
                      border=3, background=color_button_norden,
                      command=lambda: solicitar_orden_produccion(label_211, label_197, label_224))
button_29.grid(row=8, column=12, padx=0, pady=0, sticky="nsew")


# -------------------------------------------------------------------------------------------

label_101 = tk.Label(Frame4, text="FPY Total:",
                     fg="black", bg="#CAEDFB", anchor="e")
label_101.grid(row=9, column=0, padx=0, pady=0, sticky="nsew")
label_102 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_102.grid(row=9, column=1, padx=0, pady=0, sticky="nsew")
label_103 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_103.grid(row=9, column=2, padx=0, pady=0, sticky="nsew")
label_104 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_104.grid(row=9, column=3, padx=0, pady=0, sticky="nsew")
label_105 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_105.grid(row=9, column=4, padx=0, pady=0, sticky="nsew")
label_106 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_106.grid(row=9, column=5, padx=0, pady=0, sticky="nsew")
label_107 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_107.grid(row=9, column=6, padx=0, pady=0, sticky="nsew")
label_108 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_108.grid(row=9, column=7, padx=0, pady=0, sticky="nsew")
label_109 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_109.grid(row=9, column=8, padx=0, pady=0, sticky="nsew")
label_110 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_110.grid(row=9, column=9, padx=0, pady=0, sticky="nsew")
label_111 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_111.grid(row=9, column=10, padx=0, pady=0, sticky="nsew")
label_112 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_112.grid(row=9, column=11, padx=0, pady=0, sticky="nsew")
label_113 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_113.grid(row=9, column=12, padx=0, pady=0, sticky="nsew")
# label_114: Total Defect:
label_114 = tk.Label(Frame4, text="Total Defect:",
                     fg="black", bg="#CAEDFB", anchor="e")
label_114.grid(row=10, column=0, padx=0, pady=0, sticky="nsew")
label_115 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_115.grid(row=10, column=1, padx=0, pady=0, sticky="nsew")
label_116 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_116.grid(row=10, column=2, padx=0, pady=0, sticky="nsew")
label_117 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_117.grid(row=10, column=3, padx=0, pady=0, sticky="nsew")
label_118 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_118.grid(row=10, column=4, padx=0, pady=0, sticky="nsew")
label_119 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_119.grid(row=10, column=5, padx=0, pady=0, sticky="nsew")
label_120 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_120.grid(row=10, column=6, padx=0, pady=0, sticky="nsew")
label_121 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_121.grid(row=10, column=7, padx=0, pady=0, sticky="nsew")
label_122 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_122.grid(row=10, column=8, padx=0, pady=0, sticky="nsew")
label_123 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_123.grid(row=10, column=9, padx=0, pady=0, sticky="nsew")
label_124 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_124.grid(row=10, column=10, padx=0, pady=0, sticky="nsew")
label_125 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_125.grid(row=10, column=11, padx=0, pady=0, sticky="nsew")
label_126 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_126.grid(row=10, column=12, padx=0, pady=0, sticky="nsew")
label_127 = tk.Label(Frame4, text="Total Produc:",
                     fg="black", bg="#CAEDFB", anchor="e")
label_127.grid(row=11, column=0, padx=0, pady=0, sticky="nsew")
label_128 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_128.grid(row=11, column=1, padx=0, pady=0, sticky="nsew")
label_129 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_129.grid(row=11, column=2, padx=0, pady=0, sticky="nsew")
label_130 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_130.grid(row=11, column=3, padx=0, pady=0, sticky="nsew")
label_131 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_131.grid(row=11, column=4, padx=0, pady=0, sticky="nsew")
label_132 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_132.grid(row=11, column=5, padx=0, pady=0, sticky="nsew")
label_133 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_133.grid(row=11, column=6, padx=0, pady=0, sticky="nsew")
label_134 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_134.grid(row=11, column=7, padx=0, pady=0, sticky="nsew")
label_135 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_135.grid(row=11, column=8, padx=0, pady=0, sticky="nsew")
label_136 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_136.grid(row=11, column=9, padx=0, pady=0, sticky="nsew")
label_137 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_137.grid(row=11, column=10, padx=0, pady=0, sticky="nsew")
label_138 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_138.grid(row=11, column=11, padx=0, pady=0, sticky="nsew")
label_139 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_139.grid(row=11, column=12, padx=0, pady=0, sticky="nsew")
label_140 = tk.Label(Frame4, text="TopDefect:",
                     fg="black", bg="#FBE2D5", anchor="e")
label_140.grid(row=12, column=0, padx=0, pady=0, sticky="nsew")
label_141 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_141.grid(row=12, column=1, padx=0, pady=0, sticky="nsew")
label_142 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_142.grid(row=12, column=2, padx=0, pady=0, sticky="nsew")
label_143 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_143.grid(row=12, column=3, padx=0, pady=0, sticky="nsew")
label_144 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_144.grid(row=12, column=4, padx=0, pady=0, sticky="nsew")
label_145 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_145.grid(row=12, column=5, padx=0, pady=0, sticky="nsew")
label_146 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_146.grid(row=12, column=6, padx=0, pady=0, sticky="nsew")
label_147 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_147.grid(row=12, column=7, padx=0, pady=0, sticky="nsew")
label_148 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_148.grid(row=12, column=8, padx=0, pady=0, sticky="nsew")
label_149 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_149.grid(row=12, column=9, padx=0, pady=0, sticky="nsew")
label_150 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_150.grid(row=12, column=10, padx=0, pady=0, sticky="nsew")
label_151 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_151.grid(row=12, column=11, padx=0, pady=0, sticky="nsew")
label_152 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_152.grid(row=12, column=12, padx=0, pady=0, sticky="nsew")
label_153 = tk.Label(Frame4, text="Cant.Defect:",
                     fg="black", bg="#FBE2D5", anchor="e")
label_153.grid(row=13, column=0, padx=0, pady=0, sticky="nsew")
label_154 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_154.grid(row=13, column=1, padx=0, pady=0, sticky="nsew")
label_155 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_155.grid(row=13, column=2, padx=0, pady=0, sticky="nsew")
label_156 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_156.grid(row=13, column=3, padx=0, pady=0, sticky="nsew")
label_157 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_157.grid(row=13, column=4, padx=0, pady=0, sticky="nsew")
label_158 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_158.grid(row=13, column=5, padx=0, pady=0, sticky="nsew")
label_159 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_159.grid(row=13, column=6, padx=0, pady=0, sticky="nsew")
label_160 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_160.grid(row=13, column=7, padx=0, pady=0, sticky="nsew")
label_161 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_161.grid(row=13, column=8, padx=0, pady=0, sticky="nsew")
label_162 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_162.grid(row=13, column=9, padx=0, pady=0, sticky="nsew")
label_163 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_163.grid(row=13, column=10, padx=0, pady=0, sticky="nsew")
label_164 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_164.grid(row=13, column=11, padx=0, pady=0, sticky="nsew")
label_165 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_165.grid(row=13, column=12, padx=0, pady=0, sticky="nsew")
label_166 = tk.Label(Frame4, text="%Defect:",
                     fg="black", bg="#FBE2D5", anchor="e")
label_166.grid(row=14, column=0, padx=0, pady=0, sticky="nsew")
label_167 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_167.grid(row=14, column=1, padx=0, pady=0, sticky="nsew")
label_168 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_168.grid(row=14, column=2, padx=0, pady=0, sticky="nsew")
label_169 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_169.grid(row=14, column=3, padx=0, pady=0, sticky="nsew")
label_170 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_170.grid(row=14, column=4, padx=0, pady=0, sticky="nsew")
label_171 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_171.grid(row=14, column=5, padx=0, pady=0, sticky="nsew")
label_172 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_172.grid(row=14, column=6, padx=0, pady=0, sticky="nsew")
label_173 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_173.grid(row=14, column=7, padx=0, pady=0, sticky="nsew")
label_174 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_174.grid(row=14, column=8, padx=0, pady=0, sticky="nsew")
label_175 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_175.grid(row=14, column=9, padx=0, pady=0, sticky="nsew")
label_176 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_176.grid(row=14, column=10, padx=0, pady=0, sticky="nsew")
label_177 = tk.Label(Frame4,
                     fg="black", bg=color_2)
label_177.grid(row=14, column=11, padx=0, pady=0, sticky="nsew")
label_178 = tk.Label(Frame4,
                     fg="black", bg=color_3)
label_178.grid(row=14, column=12, padx=0, pady=0, sticky="nsew")

# ---------------------------------------------------------------------------------------------------------------------

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
label_180 = tk.Label(Frame5, text="Rev9.0 (By: Oscar Tovar)",
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
entry_31.bind("<KeyRelease>", suma_defectos)
entry_32.bind("<KeyRelease>", suma_defectos)
entry_33.bind("<KeyRelease>", suma_defectos)
entry_34.bind("<KeyRelease>", suma_defectos)
entry_35.bind("<KeyRelease>", suma_defectos)
entry_30.bind("<KeyRelease>", escribir_pallet)
entry_30.bind("<FocusIn>", regreso_pallet)
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
