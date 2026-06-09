from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QFrame
)

from PySide6.QtCore import Qt
import sys


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Defectos SEHO")
        self.showMaximized()

        # =========================
        # LAYOUT PRINCIPAL
        # =========================
        layout_principal = QGridLayout()
        self.setLayout(layout_principal)

        # =========================
        # TITULO
        # =========================
        titulo = QLabel("Registro de defectos SEHO")
        titulo.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: red;
        """)

        layout_principal.addWidget(titulo, 0, 0, 1, 4)

        # =========================
        # PANEL DEFECTOS
        # =========================
        panel_defectos = QFrame()
        panel_defectos.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #D1D5DB;
            }
        """)

        layout_defectos = QGridLayout()
        panel_defectos.setLayout(layout_defectos)

        defectos = [
            "Cortos",
            "Falta SMT",
            "Housing dañado",
            "Cable quemado",
            "Bola de soldadura",
            "Pin largo"
        ]

        self.entries = []

        fila = 0
        columna = 0

        for defecto in defectos:

            label = QLabel(defecto)
            label.setStyleSheet("font-size: 16px;")

            entry = QLineEdit()
            entry.setPlaceholderText("0")
            entry.setFixedWidth(80)

            entry.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #CBD5E1;
                    border-radius: 8px;
                    padding: 5px;
                    font-size: 15px;
                    background-color: #F8FAFC;
                }
            """)

            layout_defectos.addWidget(label, fila, columna)
            layout_defectos.addWidget(entry, fila, columna + 1)

            self.entries.append(entry)

            fila += 1

            if fila > 2:
                fila = 0
                columna += 2

        layout_principal.addWidget(panel_defectos, 1, 0, 1, 4)

        # =========================
        # PALLET
        # =========================
        label_pallet = QLabel("Número de pallet:")
        label_pallet.setStyleSheet("font-size: 18px;")

        self.entry_pallet = QLineEdit()
        self.entry_pallet.setPlaceholderText("Escanea el pallet aquí")

        self.entry_pallet.setStyleSheet("""
            QLineEdit {
                border: 2px solid #22C55E;
                border-radius: 12px;
                padding: 10px;
                font-size: 18px;
                background-color: white;
            }
        """)

        layout_principal.addWidget(label_pallet, 2, 0)
        layout_principal.addWidget(self.entry_pallet, 2, 1, 1, 3)

        # =========================
        # BOTONES
        # =========================
        btn_guardar = QPushButton("Guardar")
        btn_reset = QPushButton("Reset")

        estilo_boton = """
            QPushButton {
                background-color: #16A34A;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #15803D;
            }
        """

        btn_guardar.setStyleSheet(estilo_boton)
        btn_reset.setStyleSheet(estilo_boton)

        layout_principal.addWidget(btn_guardar, 3, 2)
        layout_principal.addWidget(btn_reset, 3, 3)

        # =========================
        # ESPACIADO
        # =========================
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setHorizontalSpacing(15)
        layout_principal.setVerticalSpacing(15)


app = QApplication(sys.argv)

ventana = Ventana()
ventana.showMaximized()

sys.exit(app.exec())
