from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

imagen = Image('check-mark.png')
estiloCuerpoTexto= hojaEstilo['BodyText'] # Obtener el estilo de la hoja de estilo
estiloCuerpoTexto.textColor = colors.blue # Darle color al texto
parrafo = Paragraph('Optare', estiloCuerpoTexto)


datos = [
         ['Empresas', 'Candidato 1', 'Candidato 2', 'Especificaciones'],
         ['Ayco','Marcos','Rubén','Desarrollo web con PHP'],
         ['Iterat','Borja','Juan','Reconocimiento de imágenes con OpenCV'],
         [[parrafo, imagen],'Lidier','Lucas','Aplicaciones para las Telecomunicaciones']
         ]


estilo = [
          ('TEXTCOLOR',(0,0),(0,-1),colors.blue), # Darle color a la primera columna de la tabla (0,0) hasta (0,-1)
          ('TEXTCOLOR',(1,0),(-1,0),colors.blueviolet), # Darle color a la primera fila de la tabla (1,0) hasta (-1,0)
          ('TEXTCOLOR',(1,1),(-1,-1),colors.grey), # Darle color a la segunda fila de la tabla (1,1) hasta (-1,-1)
          ('BOX',(1,1),(-1,-1),1,colors.grey), # Darle color a la segunda fila de la tabla (1,1) hasta (-1,-1)
          ('INNERGRID',(1,1),(-1,-1),1.25,colors.grey), # Darle color a la segunda fila de la tabla (1,1) hasta (-1,-1)
          ('VALING',(0,0),(-1,-1),'MIDDLE'), # Alinear verticalmente el contenido de la tabla
          ]

tabla = Table(data=datos, style=estilo) # Crear la tabla con los datos y darle formato
# tabla.setStyle(estilo) # Otra forma de darle formato a la tabla

elementosDoc.append(tabla) # Agregar la tabla a la lista de elementos

documento = SimpleDocTemplate("ejemploTablasRpl.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos