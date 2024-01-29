from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = [] # Lista de imágenes
imagen = Image(0,0,300,281,"gatito.png") # Crear un objeto imagen
dibujo = Drawing(400,200) # Crear un objeto dibujo
dibujo.add(imagen) # Agregar la imagen al dibujo

dibujo.translate(200,400) # Mover el dibujo a la posición (0,400)
imagenes.append(dibujo) # Agregar el dibujo a la lista de imágenes

dibujo = Drawing() # Crear un objeto dibujo
dibujo.add(imagen) # Agregar la imagen al dibujo
dibujo.rotate(45) # Rotar el dibujo 90 grados
dibujo.scale(1.5,0.5) # Escalar el dibujo
dibujo.translate(0,0) # Mover el dibujo a la posición (0,0)
imagenes.append(dibujo) # Agregar el dibujo a la lista de imágenes

dibujo = Drawing(A4[0],A4[1]) # Crear un objeto dibujo

for auxiliar in imagenes: # Iterar la lista de imágenes
    dibujo.add(auxiliar) # Agregar la imagen al dibujo

renderPDF.drawToFile(dibujo,"ejemploImageRpl.pdf") # Guardar el documento en formato PDF