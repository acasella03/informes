from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

cabecera = hojaEstilo['Heading4'] # Estilo de la cabecera
cabecera.pageBreakBefore = 0 # No iniciar la cabecera en una página nueva
cabecera.keepWithNext = 0 # No separar la cabecera del siguiente elemento
cabecera.fontSize = 20 # Tamaño de la fuente de la cabecera
cabecera.backColor = colors.dimgray # Color de fondo de la cabecera

parrafo = Paragraph("CABECERA DEL DOCUMENTO", cabecera) # Crear un objeto de tipo Paragraph
elementosDoc.append(parrafo) # Agregar el objeto a la lista de elementos
elementosDoc.append(Spacer(0, 10)) # Agregar un espacio vertical de 10 puntos

contenidoDocumento = "Este es el contenido del documento, el cual va a ocupar multiples líneas." * 100 # Contenido del documento (100 líneas)

estiloCuerpoTexto = hojaEstilo['BodyText'] # Estilo del cuerpo del text
parrafo = Paragraph(contenidoDocumento, estiloCuerpoTexto) # Crear un objeto de tipo Paragraph con el contenido del documento y el estilo del cuerpo del texto
elementosDoc.append(parrafo) # Agregar el objeto a la lista de elementos
elementosDoc.append(Spacer(0, 20)) # Agregar un espacio vertical de 20 puntos

imagen = Image("gatito.png", width=100, height=100) # Crear un objeto de tipo Image con la imagen del gatito
elementosDoc.append(imagen) # Agregar el objeto a la lista de elementos

documento = SimpleDocTemplate("ejemploDocPlatypus.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos
