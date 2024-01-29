from reportlab.pdfgen import canvas

auxiliar = canvas.Canvas("primerDocumento.pdf") # Crear un objeto canvas

auxiliar.drawString(0, 0, "Posición origen (X,Y) = (0,0)") # Dibujar texto en la posición (0,0)
auxiliar.drawString(50,100,"Posición (X,Y) = (50,100)") # Dibujar texto en la posición (50,100)
auxiliar.drawString(150,20,"Posición (X,Y) = (150,20)") # Dibujar texto en la posición (150,20)
auxiliar.drawImage("gatito.png",250,700,100,100) # Dibujar una imagen en la posición (250,300) con un tamaño de 100x100
auxiliar.drawImage("check-mark.png",250,200,100,100) # Dibujar una imagen en la posición (250,200) con un tamaño de 100x100

auxiliar.showPage() # Cambiar de página
auxiliar.save() # Guardar el documento