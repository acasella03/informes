from reportlab.pdfgen import canvas

frase = ['Esta es una bonita frase, ','para tener distintas partes','las que incluir en nuestro','texto de ejemplo.']

auxiliar = canvas.Canvas("ejemploTextoRpl.pdf") # Crear un objeto canvas
objetoTexto = auxiliar.beginText() # Crear un objeto texto
objetoTexto.setTextOrigin(100,500) # Posición del texto
objetoTexto.setFont("Helvetica", 16) # Tipo de letra y tamaño
for linea in frase: # Iterar la lista de frases
    objetoTexto.textLine(linea) # Agregar una línea de texto

objetoTexto.setFillGray(0.5) # Color de relleno

parrafo = '''
Este es un texto de ejemplo para mostrar como se puede 
incluir un párrafo en un documento PDF. Este texto se 
puede dividir en varias líneas, las cuales se pueden 
alinear a la izquierda, derecha o centradas. También se 
puede cambiar el tipo de letra y el tamaño de la misma.
'''

objetoTexto.textLines(parrafo) # Agregar un párrafo de texto
auxiliar.drawText(objetoTexto) # Dibujar el texto
auxiliar.showPage() # Cambiar de página
auxiliar.save() # Guardar el documento