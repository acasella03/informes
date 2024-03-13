import sys
from PyQt6.QtCore import QSize, Qt, QAbstractTableModel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox,  QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView)
#from modeloTaboa import ModeloTaboa
from conexionBD   import ConexionBD
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class ModeloTaboa(QAbstractTableModel):
    """Modelo que representa una tabla"""
    def __init__(self, datos):
        """Inicializa la tabla

        :param datos: lista de datos
        """
        super().__init__()
        self.datos = datos

    def rowCount(self, index):
        """Retorna el total de filas de la tabla

        :param index: índice de la tabla
        :return: el total de filas de la tabla
        """
        return len(self.datos)

    def columnCount(self, index):
        """Retorna el total de columnas de la tabla

        :param index: índice de la tabla
        :return: el total de columnas de la tabla
        """
        return len(self.datos[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Retorna el valor de la tabla

        :param index: índice del dato de la tabla
        :param role: indica el valor de la tabla
        :return: valor de la tabla
        """
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self.datos[index.row()][index.column()]
                return str(value)

    def setData(self, index, value, role):
        """Retorna el valor de la tabla de datos de un archivo

        :param index: índice del archivo que se encuentra el valor de la tabla de datos
        :param value: valor de la tabla de datos de un archivo
        :param role: indica el valor de la tabla de datos
        :return: None se encuentra el valor de la tabla de datos
        """
        if role == Qt.ItemDataRole.EditRole:
            self.datos[index.row()][index.column()] = value
            return True
        return False


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        """Inicializa la clase principal"""
        super().__init__()

        self.setWindowTitle("Exame 12-03-2024")

        self.estado= 'None'


        caixaV = QVBoxLayout()
        grid = QGridLayout()


        gpbCliente = QGroupBox("Cliente")
        gpbCliente.setLayout(grid)
        caixaV.addWidget(gpbCliente)

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")
        lblCodigoPostal = QLabel("Código postal")
        lblTelefono = QLabel("Teléfono")
        lblPais = QLabel ("País")
        lblAxenteComercial = QLabel("AxenteComercial")
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()
        self.txtProvinciaEstado = QLineEdit()
        self.txtCodigoPostal = QLineEdit()
        self.txtTelefono = QLineEdit()
        self.txtPais = QLineEdit()
        self.txtAxenteComercial = QLineEdit()


        grid.addWidget(lblNumeroCliente, 0,0,1,1)
        grid.addWidget(self.txtNumeroCliente, 0, 1, 1, 1)
        grid.addWidget(lblNomeCliente, 0,2,1,1)
        grid.addWidget(self.txtNomeCliente, 0, 3, 1, 1)
        grid.addWidget(lblApelidosCliente, 2,0,1,1)
        grid.addWidget(self.txtApelidosCliente, 2,1,1,3)
        grid.addWidget(lblDirección, 3,0,1,1)
        grid.addWidget(self.txtDireccion, 3,1,1,3)
        grid.addWidget(lblCidade,4, 0, 1,1)
        grid.addWidget(self.txtCidade, 4, 1, 1,1)
        grid.addWidget(lblProvinciaEstado, 4,2, 1,1)
        grid.addWidget(self.txtProvinciaEstado, 4,3, 1,1)
        grid.addWidget(lblCodigoPostal, 5,0,1,1)
        grid.addWidget(self.txtCodigoPostal, 5,1,1,1)
        grid.addWidget(lblTelefono, 5, 2, 1, 1)
        grid.addWidget(self.txtTelefono, 5, 3, 1, 1)
        grid.addWidget(lblPais,6,0,1,1)
        grid.addWidget(self.txtPais,6,1,1,1)
        grid.addWidget(lblAxenteComercial,6,2,1,1)
        grid.addWidget(self.txtAxenteComercial,6,3,1,1)


        caixaHTaboa = QHBoxLayout()


        self.tvwClientes = QTableView()
        self.tvwClientes.verticalHeader().hide()
        self.tvwClientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tvwClientes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        caixaHTaboa.addWidget(self.tvwClientes)
        conxBD = ConexionBD("modelosClasicos.dat")
        conxBD.conectaBD()
        conxBD.creaCursor()

        clientes = conxBD.consultaSenParametros("Select * from clientes")
        conxBD.pechaBD()

        self.tabla_data = clientes

        self.columna0 = []
        self.columna1 = []
        self.columna2 = []
        self.columna3 = []
        self.columna4 = []
        self.columna5 = []
        self.columna6 = []
        self.columna7 = []
        self.columna8 = []
        self.columna9 = []



        for fila in clientes:
            self.columna0.append(fila[0])  # Suponiendo que la primera columna es la columna 1
            self.columna1.append(fila[1])  # Suponiendo que la segunda columna es la columna 2
            self.columna2.append(fila[2])  # Suponiendo que la tercera columna es la columna 3
            self.columna3.append(fila[3])
            self.columna4.append(fila[4])
            self.columna5.append(fila[5])
            self.columna6.append(fila[6])
            self.columna7.append(fila[7])
            self.columna8.append(fila[8])
            self.columna9.append(fila[9])



        self.modelo = ModeloTaboa(clientes)
        self.tvwClientes.setModel(self.modelo)
        self.seleccion = self.tvwClientes.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_modelo_selectionChanged)



        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.setEnabled(True)
        self.btnEngadir.pressed.connect(self.on_btnEngadir_pressed)
        self.btnEditar = QPushButton("Editar")
        self.btnEditar.setEnabled(False)
        self.btnEditar.pressed.connect(self.on_btnEditar_pressed)
        self.btnBorrar = QPushButton("Borrar")
        self.btnBorrar.setEnabled(False)
        self.btnBorrar.pressed.connect(self.on_btnBorrar_pressed)

        caixaBotonsCorreo = QVBoxLayout()
        caixaBotonsCorreo.setAlignment(Qt.AlignmentFlag.AlignTop)
        caixaBotonsCorreo.addWidget(self.btnEngadir)
        caixaBotonsCorreo.addWidget(self.btnEditar)
        caixaBotonsCorreo.addWidget(self.btnBorrar)

        caixaHTaboa.addLayout(caixaBotonsCorreo)

        caixaV.addLayout(caixaHTaboa)

        caixaBtnAceptar = QHBoxLayout()
        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.pressed.connect(self.on_btnAceptar_pressed)
        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.pressed.connect(self.on_btnCancelar_pressed)
        caixaBtnAceptar.setAlignment(Qt.AlignmentFlag.AlignRight)
        caixaBtnAceptar.addWidget(self.btnCancelar)
        caixaBtnAceptar.addWidget(self.btnAceptar)
        caixaV.addLayout(caixaBtnAceptar)
        # BOTÓN GENERAR FACTURA
        self.botonGenerarFactura=QPushButton("Generar Factura")
        self.botonGenerarFactura.clicked.connect(self.on_botonGenerarFactura_clicked)
        caixaV.addWidget(self.botonGenerarFactura)


        contedor = QWidget()

        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)

        #self.setFixedSize (400,300)
        self.show()

    def on_btnEngadir_pressed(self):
        """Agrega datos en la tabla que se encuentra en la IU"""
        self.estado = 'Engadir'
        self.borrarCampos()
        self.btnEngadir.setEnabled(False)
        self.btnEditar.setEnabled(False)
        self.btnBorrar.setEnabled(False)


    def on_btnEditar_pressed(self):
        """Edita datos de la tabla que se encuentra en la IU"""
        if self.seleccion.hasSelection():
            self.estado = 'Editar'
            self.cargarCamposDendeSeleccion()
            self.btnEngadir.setEnabled(False)
            self.btnEditar.setEnabled(False)
            self.btnBorrar.setEnabled(False)

    def on_btnBorrar_pressed(self):
        """Borrar datos de la tabla que se encuentra en la IU"""
        if self.seleccion.hasSelection():
            self.estado ="Borrar"
            self.cargarCamposDendeSeleccion()
            self.btnEngadir.setEnabled(False)
            self.btnEditar.setEnabled(False)
            self.btnBorrar.setEnabled(False)


    def on_btnAceptar_pressed(self):
        """Acepta datos de la tabla que se encuentra en la IU y los inserta en la base de datos
        Edita datos de la tabla que se encuentra en la IU y los edita en la base de datos
        Borra datos de la tabla que se encuentra en la IU y los edita en la base de datos
        """
        if self.estado == 'Engadir':
            conxBD = ConexionBD("modelosClasicos.dat")
            conxBD.conectaBD()
            conxBD.creaCursor()
            conxBD.engadeRexistro("""INSERT INTO clientes (numeroCliente, nomeCliente, apelidosCliente, telefono, direccion, cidade, provinciaEstado, codigoPostal, pais, axenteComercial)
                                           VALUES (?,?,?,?,?,?,?,?,?,?)""",
                                  int(self.txtNumeroCliente.text()),
                                  self.txtNomeCliente.text(),
                                  self.txtApelidosCliente.text(),
                                  self.txtTelefono.text(),
                                  self.txtDireccion.text(),
                                  self.txtCidade.text(),
                                  self.txtProvinciaEstado.text(),
                                  self.txtCodigoPostal.text(),
                                  self.txtPais.text(),
                                  int(self.txtAxenteComercial.text()))
            self.modelo.datos.append((int(self.txtNumeroCliente.text()),
                                      self.txtNomeCliente.text(),
                                      self.txtApelidosCliente.text(),
                                      self.txtTelefono.text(),
                                      self.txtDireccion.text(),
                                      self.txtCidade.text(),
                                      self.txtProvinciaEstado.text(),
                                      self.txtCodigoPostal.text(),
                                      self.txtPais.text(),
                                      int(self.txtAxenteComercial.text())))
            self.modelo.layoutChanged.emit()

        elif self.estado == 'Borrar':
            filas = self.seleccion.selectedRows()
            for fila in filas:
                i = fila.row()
                conxBD = ConexionBD("modelosClasicos.dat")
                conxBD.conectaBD()
                conxBD.creaCursor()
                conxBD.borraRexistro("DELETE FROM clientes WHERE numeroCliente = ?", self.modelo.datos[i][0] )
                del (self.modelo.datos[i])
                self.modelo.layoutChanged.emit()

        elif self.estado == 'Editar':
            filas =self.seleccion.selectedRows()
            for fila in filas:
                i = fila.row()
                conxBD = ConexionBD("modelosClasicos.dat")
                conxBD.conectaBD()
                conxBD.creaCursor()
                conxBD.actualizaRexistro("""UPDATE clientes SET 
                                                nomeCliente = ?,
                                                apelidosCliente = ?,
                                                telefono = ?,
                                                direccion = ?,
                                                cidade = ?,
                                                provinciaEstado = ?,
                                                codigoPostal = ?,
                                                pais = ?,
                                                axenteComercial = ?
                                            Where numeroCliente = ?""",
                                              self.txtNomeCliente.text(),
                                              self.txtApelidosCliente.text(),
                                              self.txtTelefono.text(),
                                              self.txtDireccion.text(),
                                              self.txtCidade.text(),
                                              self.txtProvinciaEstado.text(),
                                              self.txtCodigoPostal.text(),
                                              self.txtPais.text(),
                                              int(self.txtAxenteComercial.text()),
                                              int(self.txtNumeroCliente.text())
                                            )
                self.modelo.datos [i] = (
                self.modelo.datos[i][0],
                self.txtNomeCliente.text(),
                self.txtApelidosCliente.text(),
                self.txtTelefono.text(),
                self.txtDireccion.text(),
                self.txtCidade.text(),
                self.txtProvinciaEstado.text(),
                self.txtCodigoPostal.text(),
                self.txtPais.text(),
                int(self.txtAxenteComercial.text())
                )
                self.modelo.layoutChanged.emit()

        self.seleccion.clear()
        self.borrarCampos()
        self.estado= 'None'
        self.btnEngadir.setEnabled(True)
    def on_btnCancelar_pressed(self):
        self.seleccion.clear()
        self.btnEngadir.setEnabled(True)
        self.btnEditar.setEnabled (False)
        self.btnBorrar.setEnabled(False)
        self.borrarCampos()


    def on_modelo_selectionChanged(self):
        self.btnEngadir.setEnabled(True)
        self.btnBorrar.setEnabled (True)
        self.btnEditar.setEnabled(True)


    def cargarCamposDendeSeleccion(self):
        filas = self.seleccion.selectedRows()
        for fila in filas:
            i = fila.row()
            self.txtNumeroCliente.setText(str(self.modelo.datos[i][0]))
            self.txtNomeCliente.setText(self.modelo.datos[i][1])
            self.txtApelidosCliente.setText(self.modelo.datos[i][2])
            self.txtTelefono.setText(self.modelo.datos[i][3])
            self.txtDireccion.setText(self.modelo.datos[i][4])
            self.txtCidade.setText(self.modelo.datos[i][5])
            self.txtProvinciaEstado.setText(self.modelo.datos[i][6])
            self.txtCodigoPostal.setText(self.modelo.datos[i][7])
            self.txtPais.setText(self.modelo.datos[i][8])
            self.txtAxenteComercial.setText(str(self.modelo.datos[i][9]))

    def borrarCampos(self):
        self.txtNumeroCliente.setText('')
        self.txtNomeCliente.setText('')
        self.txtApelidosCliente.setText('')
        self.txtTelefono.setText('')
        self.txtDireccion.setText('')
        self.txtCidade.setText('')
        self.txtProvinciaEstado.setText('')
        self.txtCodigoPostal.setText('')
        self.txtPais.setText('')
        self.txtAxenteComercial.setText('')

    def on_botonGenerarFactura_clicked(self):  # Fichas de todos los clientes en la misma hojas
        try:
            print("Generando factura...")

            # Obtener todos los datos de los clientes
            clientes_datos = self.modelo.datos

            # Crear el documento PDF
            doc = SimpleDocTemplate("fichas_clientes.pdf", pagesize=A4)

            # Lista para almacenar los elementos del documento (tablas)
            elements = []

            for i, cliente_datos in enumerate(clientes_datos):
                # Definir los datos de la tabla para este cliente
                data = [
                    ['Número Cliente', cliente_datos[0], 'Nome', cliente_datos[1]],
                    ['Apelidos', cliente_datos[2], '', ''],
                    ['Dirección', cliente_datos[4], '', ''],
                    ['Cidade', cliente_datos[5], 'Provincia', cliente_datos[6]],
                    ['Código postal', cliente_datos[7], 'Telefono', cliente_datos[3]],
                    ['País', cliente_datos[8], 'AxenteComercial', cliente_datos[9]],
                ]

                # Crear la tabla
                table = Table(data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                    ('BACKGROUND', (2, 0), (2, 0), colors.lightgrey),
                    ('BACKGROUND', (2, 3), (2, -1), colors.lightgrey),
                    ('SPAN', (1, 1), (3, 1)),
                    ('SPAN', (1, 2), (3, 2)),
                    ('GRID', (0, 0), (-1, -1), 1, colors.grey)
                ]))

                # Añadir la tabla al documento
                elements.append(table)

                # Añadir un espacio entre las tablas para evitar que se superpongan
                elements.append(Spacer(1, 20))

            # Añadir las tablas al documento y guardarlo
            doc.build(elements)

            print("Factura generada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")

    def on_Factura_clicked(self): # Fichas de todos los clientes en hojas separadas
        """Generar factura al hacer clic en el botón."""
        try:
            print("Generando factura...")

            # Obtener todos los datos de los clientes
            clientes_datos = self.modelo.datos  # Asegúrate de que 'self.modelo.datos' contiene todos los datos de los clientes

            for i, cliente_datos in enumerate(clientes_datos):
                # Definir los datos de la tabla
                data = [
                    ['Número Cliente', cliente_datos[0],'Nome',cliente_datos[1]],
                    ['Apelidos', cliente_datos[2],'',''],
                    ['Dirección', cliente_datos[4],'',''],
                    ['Cidade', cliente_datos[5],'Provincia', cliente_datos[6]],
                    ['Código postal', cliente_datos[7],'Telefono', cliente_datos[3]],
                    ['País', cliente_datos[8],'AxenteComercial', cliente_datos[9]],
                ]

                # Crear el documento PDF
                doc = SimpleDocTemplate(f"ficha_cliente_{i+1}.pdf", pagesize=A4)

                # Crear la tabla
                table = Table(data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                    ('BACKGROUND', (2, 0), (2, 0), colors.lightgrey),
                    ('BACKGROUND', (2, 3), (2, -1), colors.lightgrey),
                    ('SPAN', (1,1),(3,1)),
                    ('SPAN', (1, 2), (3, 2)),
                    ('GRID', (0, 0), (-1, -1), 1, colors.grey)
                ]))

                # Añadir la tabla al documento
                elements = []
                elements.append(table)
                doc.build(elements)

            print("Factura generada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")

    def on_GenerarFactura_clicked(self): # Por cada cliente seleccionado de la tabla
        """Generar factura al hacer clic en el botón."""
        try:
            print("Generando factura...")

            # Obtener los datos del cliente seleccionado
            filas = self.seleccion.selectedRows()
            if not filas:
                return  # No hay fila seleccionada
            fila = filas[0]
            i = fila.row()
            cliente_datos = self.modelo.datos[i]

            # Definir los datos de la tabla
            data = [
                ['Número Cliente', cliente_datos[0],'Nome',cliente_datos[1]],
                ['Apelidos', cliente_datos[2],'',''],
                ['Dirección', cliente_datos[4],'',''],
                ['Cidade', cliente_datos[5],'Provincia', cliente_datos[6]],
                ['Código postal', cliente_datos[7],'Telefono', cliente_datos[3]],
                ['País', cliente_datos[8],'AxenteComercial', cliente_datos[9]],
            ]

            # Crear el documento PDF
            doc = SimpleDocTemplate("ficha_cliente.pdf", pagesize=A4)

            # Crear la tabla
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                ('BACKGROUND', (2, 0), (2, 0), colors.lightgrey),
                ('BACKGROUND', (2, 3), (2, -1), colors.lightgrey),
                ('SPAN', (1,1),(3,1)),
                ('SPAN', (1, 2), (3, 2)),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey)
            ]))

            # Añadir la tabla al documento
            elements = []
            elements.append(table)
            doc.build(elements)

            print("Factura generada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")

if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()