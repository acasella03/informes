from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


c = canvas.Canvas("Factura.pdf", pagesize=A4)
c.setFont("Helvetica", 20)
c.drawString(340, 750, "FACTURA SIMPLIFICADA")

c.setFont("Helvetica", 20)
c.drawString(100,700, "Nombre de tu Empresa")

c.drawImage( "gatito.png",500,700, 40,40)

c.setFont("Helvetica", 14)
c.drawString(100,680, "Dirección: ")
direccion = c.beginText(200, 680)
direccion.textLine("Miradoiro 3")
c.drawText(direccion)

c.setFont("Helvetica", 14)
c.drawString(100,660, "Ciudad y País: ")
ciudadPais = c.beginText(200, 660)
ciudadPais.textLine("Vigo, España")
c.drawText(ciudadPais)

c.setFont("Helvetica", 14)
c.drawString(100,640, "CIF/NIF: ")
cifNif = c.beginText(200, 640)
cifNif.textLine("123456789-F")
c.drawText(cifNif)

c.setFont("Helvetica", 14)
c.drawString(100,620, "Teléfono: ")
telefono = c.beginText(200, 620)
telefono.textLine("986 123 654")
c.drawText(telefono)

c.setFont("Helvetica", 14)
c.drawString(100,600, "Mail: ")
mail = c.beginText(200, 600)
mail.textLine("acasella@gmail.com")
c.drawText(mail)

c.setFont("Helvetica", 14)
c.drawRightString(500,650, "Fecha Emisión: ")
fechaEmision = c.beginText(500, 650)
fechaEmision.textLine("05/03/2024")
c.drawText(fechaEmision)

c.setFont("Helvetica", 14)
c.drawRightString(500,630, "Número de Factura: ")
numeroFactura = c.beginText(500, 630)
numeroFactura.textLine("A0001")
c.drawText(numeroFactura)

# Crear datos para la tabla
datos = [
         ['Descripción', 'Importe', 'Cantidad', 'Total'],
         ['Producto 1','3,2','5','16,00'],
         ['Producto 2','2,1','3','6,30'],
         ['Producto 3','2,9','76','220,40'],
         ['Producto 4','5','23','115,00'],
         ['Producto 5','4,95','3','14,85'],
         ['Producto 6','6','2','12,00'],
         ['','','TOTAL','385 €']
         ]

# Configurar el estilo de la tabla
# Cada tupla tiene el formato ('PROP', (start_col, start_row), (end_col, end_row), value), donde PROP es la propiedad que estás configurando, y (start_col, start_row) y (end_col, end_row) son las coordenadas de inicio y final para aplicar esa propiedad. En este caso, (-1, 0) representa la última columna y la primera fila, y (-1, -1) representa todas las columnas y filas de datos.
estilo = TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.darkgreen), # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR',(0,0),(-1,0),colors.white), # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), # Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                ('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND',(0,1),(-1,-2),colors.lightgreen), # Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                ('BACKGROUND',(0,-1),(-1,-1),colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                ('TEXTCOLOR',(0,-1),(-1,-1),colors.white), # Establece el color del texto en blanco para la última fila
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                ('BACKGROUND',(0,-1),(1,-1),colors.white), # Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN',(0,0),(-1,-1),'CENTER'), # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),   # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, -1), 1, colors.white),  # Agrega bordes a todas las celdas
                    ])

# Crear la tabla y aplicar el estilo
tabla = Table(data=datos, colWidths=[200, 70, 70, 70])  # Ajusta los anchos de las columnas según sea necesario
tabla.setStyle(estilo)

# Añadir la tabla al lienzo
tabla.wrapOn(c,0,0)
tabla.drawOn(c, 100,300) # Ajusta las coordenadas

c.line(100, 200, 575, 200)


c.setFont("Helvetica-Bold", 16)
c.drawRightString(450,150, "GRACIAS POR SU CONFIANZA")


# Creación de rectángulos verticales para el diseño de la hoja
c.setFillColorRGB(38/255,78/255,17/255,1.0) # se repinta con lo de abajo
c.setStrokeColorRGB(38/255,78/255,17/255,1.0)
c.rect(20, 750, 30, 50, fill=True, stroke=1) # se repinta con lo de abajo
c.setFillColorRGB(183/255,215/255,169/255,1.0)
c.setStrokeColorRGB(183/255,215/255,169/255,1.0)
c.rect(20,400,30,400, fill=True, stroke=1)
c.setFillColorRGB(183/255,215/255,169/255,1.0)
c.setStrokeColorRGB(183/255,215/255,169/255,1.0)
c.rect(20,100,30,290, fill=True, stroke=1)


c.showPage()
c.save()








