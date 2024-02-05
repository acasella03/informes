from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("Factura.pdf", pagesize=A4)
c.drawString(100, 750, "FACTURA SIMPLIFICADA")
c.line(100, 740, 500, 740)










c.showPage()
c.save()








