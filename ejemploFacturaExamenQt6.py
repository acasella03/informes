import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLabel, QLineEdit
from PyQt6.QtCore import Qt, QAbstractTableModel
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class InvoiceModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Facturas")

        self.table_data = [
            ["Producto 1", "100", "2", "200"],
            ["Producto 2", "50", "1", "50"]
        ]

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Campos de texto
        self.text_fields = [QLineEdit() for _ in range(7)]

        # Diseño de etiquetas y campos de texto
        label_layout = QVBoxLayout()
        labels = ["Dirección", "Ciudad", "CIF/NIF", "Teléfono", "Mail", "Fecha de Emisión", "Número de Factura"]

        for label, field in zip(labels, self.text_fields):
            label_layout.addWidget(QLabel(label))
            label_layout.addWidget(field)

        # Agregar el diseño de etiquetas y campos de texto al diseño general
        layout.addLayout(label_layout)

        # Agregar la tabla al diseño general
        self.table_view = QTableView()
        self.table_view.setModel(InvoiceModel(self.table_data))
        layout.addWidget(self.table_view)

        # Botón de generación de factura
        self.generate_button = QPushButton("Generar Factura")
        self.generate_button.clicked.connect(self.generate_invoice)
        layout.addWidget(self.generate_button)

    def generate_invoice(self):
        try:
            # Aquí iría la lógica para generar la factura en PDF usando ReportLab
            print("Generando factura...")
            # Recoger los datos de los campos de texto
            address = self.text_fields[0].text()
            city = self.text_fields[1].text()
            cif_nif = self.text_fields[2].text()
            phone = self.text_fields[3].text()
            email = self.text_fields[4].text()
            issue_date = self.text_fields[5].text()
            invoice_number = self.text_fields[6].text()

            # Crear el archivo PDF
            c = canvas.Canvas("ejemploFacturaExamenQt6.pdf", pagesize=letter)

            # Agregar información de la factura
            c.drawString(100, 700, f"Factura Número: {invoice_number}")
            c.drawString(100, 680, f"Fecha de Emisión: {issue_date}")
            c.drawString(100, 660, f"CIF/NIF: {cif_nif}")
            c.drawString(100, 640, f"Dirección: {address}")
            c.drawString(100, 620, f"Ciudad: {city}")
            c.drawString(100, 600, f"Teléfono: {phone}")
            c.drawString(100, 580, f"Email: {email}")

            # Agregar elementos de la factura
            for i, row in enumerate(self.table_data, start=1):
                c.drawString(100, 560 - (i * 20), f"{row[0]}: {row[1]} x {row[2]} = {row[3]}")

            # Guardar y cerrar el archivo PDF
            c.save()
            print("Factura generada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
