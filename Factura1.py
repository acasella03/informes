from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

c = canvas.Canvas("Factura1.pdf", pagesize=A4)
c.setFont("Helvetica", 20)
c.drawString(50, 750, "FACTURA Proforma")

c.drawImage( "logo.png",350,740, 200,50)

# Lado izquierdo
c.setFont("Helvetica", 14)
c.drawString(50,700, "FACTURA A:")

c.setFont("Helvetica", 14)
c.drawString(50,660,"Cliente: ")
cliente = c.beginText(100, 660)
cliente.textLine("Francisco Javier Sánchez Temprano")
c.drawText(cliente)

c.setFont("Helvetica", 14)
c.drawString(50,645,"Domicilio: ")
domicilio = c.beginText(120, 645)
domicilio.textLine("Miradoiro 3")
c.drawText(domicilio)

c.setFont("Helvetica", 14)
c.drawString(50,630,"CP/Ciudad: ")
cp_ciudad = c.beginText(130, 630)
cp_ciudad.textLine("36210 - Vigo")
c.drawText(cp_ciudad)

c.setFont("Helvetica", 14)
c.drawString(50,615,"(NIF): ")
nif = c.beginText(130, 615)
nif.textLine("123456789")
c.drawText(nif)

# Lado derecho
c.setFont("Helvetica", 16)
nFactura = c.beginText(350,700)
nFactura.textLine("Nº DE FACTURA")
c.drawText(nFactura)

c.setFont("Helvetica", 14)
c.drawString(350,680,"Fecha: ")
fecha = c.beginText(450, 680)
fecha.textLine("07/03/2024")
c.drawText(fecha)

c.setFont("Helvetica", 14)
c.drawString(350,660,"Nº de pedido: ")
nPedido = c.beginText(450, 660)
nPedido.textLine("A0002")
c.drawText(nPedido)

c.setFont("Helvetica", 14)
c.drawString(350,640,"Fecha de vencimiento: ")
vencimiento = c.beginText(500, 640)
vencimiento.textLine("07/04/2024")
c.drawText(vencimiento)

c.setFont("Helvetica", 14)
c.drawString(350,620,"Condiciones de pago: ")
pago = c.beginText(500, 620)
pago.textLine("Crédito")
c.drawText(pago)

# Datos para la tabla
table_data = [
    ["Pos.", "Concepto/Descripción", "Cantidad", "Unidad", "Precio Unitario", "Importe"],
    [1, "Producto A", 2, "unidad", 10.0, 20.0],
    [2, "Producto B", 1, "kg", 5.0, 5.0],
    [3, "Producto C", 3, "litro", 8.0, 24.0],
]

# Configuración del estilo de la tabla
table_style = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Fondo gris claro para la primera fila (encabezado)
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación centrada para el contenido
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Líneas de la tabla con color negro
]

# Crear el objeto Table
table = Table(table_data, colWidths=[40, 200, 60, 60, 80, 80])

# Aplicar el estilo a la tabla
table.setStyle(TableStyle(table_style))

# Dibujar la tabla en el lienzo
table.wrapOn(c, 0, 0)
table.drawOn(c, 50, 500)  # Ajusta las coordenadas según tu diseño

# Datos para la segunda tabla
table2_data = [
    ["Importe neto", ""],
    ["+ IVA de ___%", ""],
    ["- IRPF de ___%", ""],
    ["IMPORTE BRUTO", ""],
]

# Configuración del estilo de la segunda tabla
table2_style = [
    ('BACKGROUND', (0, -1), (-1, -1), colors.grey),  # Fondo gris claro para la última fila (encabezado)
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación centrada para el contenido
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Líneas de la tabla con color negro
]

# Crear el objeto Table para la segunda tabla
table2 = Table(table2_data, colWidths=[140, 80])

# Aplicar el estilo a la segunda tabla
table2.setStyle(TableStyle(table2_style))

# Dibujar la segunda tabla en el lienzo
table2.wrapOn(c, 0, 0)
table2.drawOn(c, 350, 300)  # Ajusta las coordenadas según tu diseño

# Datos para la tercera tabla
table3_data = [
    ["Método de pago:", "", ""],
    ["", "", ""],
    ["", "", ""],
]

# Configuración del estilo de la tercera tabla
table3_style = [
    ('SPAN', (0, 0), (-3, -3)),  # Líneas internas sin color (se combinan)
    ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Contorno exterior de la tabla
]

# Crear el objeto Table para la tercera tabla
table3 = Table(table3_data, colWidths=[40, 150, 60])

# Aplicar el estilo a la tercera tabla
table3.setStyle(TableStyle(table3_style))

# Dibujar la tercera tabla en el lienzo
table3.wrapOn(c, 0, 0)
table3.drawOn(c, 50, 300)  # Ajusta las coordenadas según tu diseño

c.showPage()
c.save()