from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

# Crear datos de temperaturas
temperaturas = [
               ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
               ['Máximas', 15, 16, 20, 28, 30, 32, 35, 36, 34, 30, 20, 18],
               ['Mínimas', -3, -4, -1, 18, 20, 22, 25, 26, 24, 20, 2, -2]
               ]

# Crear estilo para la tabla, se lee (columna, fila)
estilo = [
         ('TEXTCOLOR',(0,0),(-1,0), colors.grey), # Darle color desde la columna 0 hasta la última columna (-1) de la primera fila (0)
         ('TEXTCOLOR',(0,1),(0,-1), colors.grey), # Darle color desde la fila 1 hasta la última fila (-1) de la primera columna (0)
         ('BOX', (1,1), (-1,-1), 1.50, colors.grey), # Darle color desde la columna 1 y fila 1 hasta la última columna y fila (-1)
         ('INNERGRID', (1,1),(-1,-1), 0.50, colors.lightgrey) # Darle color a la segunda fila de la tabla (1,1) hasta (-1,-1)
         ]

for i, fila in enumerate(temperaturas): # Recorrer las filas de la tabla
    for j, temperatura in enumerate(fila): # Recorrer las temperaturas de la fila actual de la tabla
        if type(temperatura) == int:
            if temperatura > 0:
                estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.black)) # Darle color a las temperaturas de la tabla
                if temperatura > 30:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.fidred)) # Darle color de fondo a las temperaturas de la tabla
                elif temperatura <= 30 and temperatura > 20:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange)) # Darle color de fondo a las temperaturas de la tabla
                elif temperatura <= 20 and temperatura > 10:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.yellow)) # Darle color de fondo a las temperaturas de la tabla
                elif temperatura <= 10 and temperatura > 0:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.green)) # Darle color de fondo a las temperaturas de la tabla
            else:
                estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.blue)) # Darle color a las temperaturas de la tabla
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey)) # Darle color de fondo a las temperaturas de la tabla


tabla = Table(data=temperaturas, style=estilo) # Crear la tabla con los datos y darle formato
# tabla.setStyle(estilo) # Otra forma de darle formato a la tabla

elementosDoc.append(tabla) # Agregar la tabla a la lista de elementos

documento = SimpleDocTemplate("ejemploTablaTemperaturas.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos