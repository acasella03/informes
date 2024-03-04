from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4


c = canvas.Canvas("Factura.pdf", pagesize=A4)
c.setFont("Helvetica", 20)
c.drawString(340, 750, "FACTURA SIMPLIFICADA")

c.setFont("Helvetica", 20)
c.drawString(100,700, "Nombre de tu Empresa")

c.drawImage( "gatito.png",500,700, 40,40)

c.setFont("Helvetica", 14)
c.drawString(100,680, "Dirección: ")


c.line(100, 200, 575, 200)

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








