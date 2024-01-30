from reportlab.pdfgen import canvas

frase = 'Esta es una bonita frase, para ver los distintos tipos de letra'

auxiliar = canvas.Canvas("tiposLetra.pdf") # Crear un objeto canvas
objetoTexto = auxiliar.beginText() # Crear un objeto texto
objetoTexto.setTextOrigin(20,700) # Posición del texto
# objetoTexto.setFillColor("pink") # Color de relleno en formato hexadecimal
objetoTexto.setFillColorRGB(0.2,0,150) # Color de relleno en RGB
espacioCaracteres = 0 # Espacio entre caracteres
for tipoLetra in auxiliar.getAvailableFonts(): # Iterar la lista de tipos de letra
    objetoTexto.setCharSpace(espacioCaracteres) # Espacio entre caracteres
    objetoTexto.setFont(tipoLetra, 12) # Tipo de letra y tamaño
    objetoTexto.textLine(tipoLetra + ": " + frase) # Agregar una línea de texto
    objetoTexto.moveCursor(15, 10) # Mover el cursor 15 puntos a la derecha y 10 hacia abajo
    espacioCaracteres += 1 # Incrementar el espacio entre caracteres

objetoTexto.setFillGray(0.5) # Color de relleno en escala de grises (0-1)
objetoTexto.setFont("Helvetica", 16) # Tipo de letra y tamaño
objetoTexto.setCharSpace(0) # Espacio entre caracteres (0-1)
objetoTexto.setTextOrigin(20,300) # Posición del texto 20 puntos a la derecha y 200 hacia abajo
for i in range(10): # Iterar 10 veces
    objetoTexto.setWordSpace(i) # Espacio entre palabras
    objetoTexto.textLine(frase) # Agregar una línea de texto


auxiliar.drawText(objetoTexto) # Dibujar el texto
auxiliar.showPage() # Cambiar de página
auxiliar.save() # Guardar el documento