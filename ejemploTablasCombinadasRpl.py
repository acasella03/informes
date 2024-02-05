from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

datos = [
        ['Arriba\nIzquierda', '', '02', '03', '04'],
        ['', '', '12', '13', '14'],
        ['20', '21', '22', 'Abajo\nDerecha', ''],
        ['30', '31', '32', '', '']
        ]

# Crear estilo para la tabla, se lee (columna, fila)(columna, fila)
estilo = [
         ('GRID',(0,0),(-1,-1), 1, colors.grey), # Darle color a todas las celdas de la tabla
         ('BACKGROUND',(0,0),(1,1), colors.lavender), # Darle color de fondo a las celdas (0,0) hasta (1,1)
         ('SPAN', (0,0), (1,1)), # Expandir las celdas (0,0) hasta (1,1)
         ('BACKGROUND', (-2,-2),(-1,-1), colors.lavenderblush), # Darle color de fondo a las celdas (-2,-2) hasta (-1,-1)
         ('SPAN', (-2,-2),(-1,-1)) # Expandir las celdas (-2,-2) hasta (-1,-1)
         ]


tabla = Table(data=datos, style=estilo) # Crear la tabla con los datos y darle formato
# tabla.setStyle(estilo) # Otra forma de darle formato a la tabla

elementosDoc.append(tabla) # Agregar la tabla a la lista de elementos

documento = SimpleDocTemplate("ejemploTablasCombinadasRpl.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos