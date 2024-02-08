from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.piecharts import Pie, Pie3d

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

# Crear datos de temperaturas
temperaturas = [
               ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
               [15, 16, 20, 28, 30, 32, 35, 36, 34, 30, 20, 18],
               [-3, -4, -1, 18, 20, 22, 25, 26, 24, 20, 2, -2]
               ]

# Graficas de barras
dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
grafica = VerticalBarChart() # Crear un objeto de tipo VerticalBarChart
grafica.x = 50 # Posición en x de la gráfica
grafica.y = 50 # Posición en y de la gráfica
grafica.height = 125 # Altura de la gráfica
grafica.width = 300 # Ancho de la gráfica
grafica.data = temperaturas[1:] # Datos de la gráfica donde 1: es para omitir la primera fila de la tabla
grafica.strokeColor = colors.black # Color del borde de la gráfica
grafica.valueAxis.valueMin = -5 # Valor mínimo del eje vertical de la gráfica
grafica.valueAxis.valueMax = 40 # Valor máximo del eje vertical de la gráfica
grafica.valueAxis.valueStep = 5 # Paso del eje vertical de la gráfica
grafica.categoryAxis.labels.boxAnchor = 'ne' # Posición de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.dx = 8 # Distancia en x de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.dy = -10 # Distancia en y de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.angle = 30 # Ángulo de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.categoryNames = temperaturas[0] # Nombres de las categorías del eje horizontal de la gráfica
grafica.groupSpacing = 10 # Espacio entre grupos de barras de la gráfica
grafica.barSpacing = 2 # Espacio entre barras de la gráfica
dibujo.add(grafica) # Agregar la gráfica al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

elementosDoc.append(Spacer(1, 12)) # Agregar un espacio en blanco a la lista de elementos

# Graficas de líneas
dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
grafica1 = HorizontalLineChart() # Crear un objeto de tipo HorizontalLineChart
grafica1.x = 30 # Posición en x de la gráfica
grafica1.y = 50 # Posición en y de la gráfica
grafica1.height = 125 # Altura de la gráfica
grafica1.width = 350 # Ancho de la gráfica
# grafica1.data = [temperaturas[1]] # Datos de la gráfica de la serie de las temperaturas máximas si quiero que refleje las dos series debo colocar esto: grafica1.data = temperaturas[1:]
grafica1.data = temperaturas[1:] # Datos de la gráfica donde 1: es para omitir la primera fila de la tabla
grafica1.categoryAxis.categoryNames = temperaturas[0] # Nombres de las categorías del eje horizontal de la gráfica
grafica1.categoryAxis.labels.angle = 30 # Ángulo de las etiquetas del eje horizontal de la gráfica
grafica1.categoryAxis.labels.dx = 10 # Distancia en x de las etiquetas del eje horizontal de la gráfica
grafica1.categoryAxis.labels.dy = -10 # Distancia en y de las etiquetas del eje horizontal de la gráfica
grafica1.categoryAxis.labels.boxAnchor = 'n' # Posición de las etiquetas del eje horizontal de la gráfica donde 'n' es para norte
grafica1.valueAxis.valueMin = 0 # Valor mínimo del eje vertical de la gráfica
grafica1.valueAxis.valueMax = 40 # Valor máximo del eje vertical de la gráfica
grafica1.valueAxis.valueStep = 10 # Paso del eje vertical de la gráfica
grafica1.lines[0].strokeWidth = 1 # Grosor de la línea de la gráfica
grafica1.lines[0].symbol = makeMarker('FilledCircle') # Símbolo de la línea de la gráfica
grafica1.lines[1].strokeWidth = 5 # Grosor de la línea de la gráfica
dibujo.add(grafica1) # Agregar la gráfica al dibujo

leyenda = LineLegend() # Crear un objeto de tipo LineLegend
leyenda.fontSize = 8 # Tamaño de la fuente de la leyenda
leyenda.fontName = 'Helvetica' # Tipo de fuente de la leyenda
leyenda.alignment = 'right' # Alineación de la leyenda
leyenda.x = 0 # Posición en x de la leyenda
leyenda.y = 0 # Posición en y de la leyenda
leyenda.columnMaximum = 2 # Número máximo de columnas de la leyenda
series = ['Temperatura máxima', 'Temperatura mínima'] # Series de la leyenda
leyenda.colorNamePairs = [(grafica1.lines [i].strokeColor, series[i]) for i in range(len(grafica1.data))] # Colores y nombres de las series de la leyenda
# ('red', 'Temperatura máxima'), ('green', 'Temperatura mínima') es lo que se obtiene con el for anterior
dibujo.add(leyenda) # Agregar la leyenda al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

elementosDoc.append(Spacer(30, 30)) # Agregar un espacio en blanco a la lista de elementos

# Grafica en forma de tarta
dibujo = Drawing(300, 200) # Crear un objeto de tipo Drawing
tarta = Pie() # Crear un objeto de tipo Pie
tarta.x = 65 # Posición en x de la tarta
tarta.y = 15 # Posición en y de la tarta
tarta.data = [10, 5, 20, 25, 40] # Datos de la tarta
tarta.labels = ['Edge', 'Brave', 'Firefox', 'Safari', 'Chrome'] # Etiquetas de la tarta
tarta.slices.strokeWidth = 0.5 # Grosor del borde de las rebanadas de la tarta
tarta.slices[3].popout = 10 # Separación de la rebanada de la tarta
tarta.slices[3].strokeWidth = 2 # Grosor del borde de la rebanada de la tarta
tarta.slices[3].strokeDashArray = [2, 2] # Tipo de línea del borde de la rebanada de la tarta
tarta.slices[3].labelRadius = 2 # Radio de la etiqueta de la rebanada de la tarta
tarta.slices[3].fontColor = colors.red # Color de la fuente de la etiqueta de la rebanada de la tarta
tarta.sideLabels = 1 # Mostrar etiquetas de lado
dibujo.add(tarta) # Agregar la tarta al dibujo

leyenda1 = Legend() # Crear un objeto de tipo Legend
leyenda1.x = 300 # Posición en x de la leyenda
leyenda1.y = 100 # Posición en y de la leyenda
leyenda1.dx = 10 # Distancia en x de la leyenda
leyenda1.dy = 10 # Distancia en y de la leyenda
leyenda1.fontName = 'Helvetica' # Tipo de fuente de la leyenda
leyenda1.fontSize = 8 # Tamaño de la fuente de la leyenda
leyenda1.boxAnchor = 'n' # Posición de la caja de la leyenda
leyenda1.columnMaximum = 15 # Número máximo de columnas de la leyenda
leyenda1.strokeWidth = 0.5 # Grosor del borde de la leyenda
leyenda1.strokeColor = colors.grey # Color del borde de la leyenda
leyenda1.autoXPadding = 5 # Relleno automático en x de la leyenda
leyenda1.yGap = 1 # Espacio en y de la leyenda
leyenda1.dxTextSpace = 3 # Espacio en x del texto de la leyenda
leyenda.alignment = 'right' # Alineación de la leyenda
leyenda1.dividerLines = 1|2|4 # Líneas divisorias de la leyenda
leyenda1.dividerOffsY = 4.5 # Separación de las líneas divisorias de la leyenda
leyenda1.subCols.rpad = 30 # Relleno derecho de las subcolumnas de la leyenda

paraColorLeyenda = list()
colores = [colors.blue, colors.red, colors.pink, colors.yellow, colors.green] # Colores de las rebanadas de la tarta
for i, color in enumerate(colores): # Recorrer los colores
    tarta.slices[i].fillColor = color # Asignar el color a la rebanada de la tarta
    paraColorLeyenda.append((color, tarta.labels[i])) # Agregar el color y la etiqueta a la leyenda
leyenda1.colorNamePairs = paraColorLeyenda # Colores y nombres de la leyenda
dibujo.add(leyenda1) # Agregar la leyenda al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

# Grafica en forma de tarta en 3D
dibujo = Drawing(300, 200) # Crear un objeto de tipo Drawing
tarta1 = Pie3d() # Crear un objeto de tipo Pie
tarta1.x = 65 # Posición en x de la tarta
tarta1.y = 15 # Posición en y de la tarta
tarta1.data = [10, 5, 20, 25, 40] # Datos de la tarta
tarta1.labels = ['Edge', 'Brave', 'Firefox', 'Safari', 'Chrome'] # Etiquetas de la tarta
tarta1.slices.strokeWidth = 0.5 # Grosor del borde de las rebanadas de la tarta
tarta1.slices[3].popout = 10 # Separación de la rebanada de la tarta
tarta1.slices[3].strokeWidth = 2 # Grosor del borde de la rebanada de la tarta
tarta1.slices[3].strokeDashArray = [2, 2] # Tipo de línea del borde de la rebanada de la tarta
tarta1.slices[3].labelRadius = 2 # Radio de la etiqueta de la rebanada de la tarta
tarta1.slices[3].fontColor = colors.red # Color de la fuente de la etiqueta de la rebanada de la tarta
tarta1.sideLabels = 1 # Mostrar etiquetas de lado
dibujo.add(tarta1) # Agregar la tarta al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

leyenda2 = Legend() # Crear un objeto de tipo Legend
leyenda2.x = 350 # Posición en x de la leyenda
leyenda2.y = 20 # Posición en y de la leyenda
leyenda2.dx = 10 # Distancia en x de la leyenda
leyenda2.dy = 10 # Distancia en y de la leyenda
leyenda2.fontName = 'Helvetica' # Tipo de fuente de la leyenda
leyenda2.fontSize = 8 # Tamaño de la fuente de la leyenda
leyenda2.boxAnchor = 'n' # Posición de la caja de la leyenda
leyenda2.columnMaximum = 15 # Número máximo de columnas de la leyenda
leyenda2.strokeWidth = 0.5 # Grosor del borde de la leyenda
leyenda2.strokeColor = colors.grey # Color del borde de la leyenda
leyenda2.autoXPadding = 5 # Relleno automático en x de la leyenda
leyenda2.yGap = 1 # Espacio en y de la leyenda
leyenda2.dxTextSpace = 3 # Espacio en x del texto de la leyenda
leyenda.alignment = 'right' # Alineación de la leyenda
leyenda2.dividerLines = 1|2|4 # Líneas divisorias de la leyenda
leyenda2.dividerOffsY = 4.5 # Separación de las líneas divisorias de la leyenda
leyenda2.subCols.rpad = 30 # Relleno derecho de las subcolumnas de la leyenda

paraColorLeyenda2 = list()
for i, color in enumerate(colores): # Recorrer los colores
    tarta1.slices[i].fillColor = color # Asignar el color a la rebanada de la tarta
    paraColorLeyenda2.append((color, tarta1.labels[i])) # Agregar el color y la etiqueta a la leyenda
leyenda2.colorNamePairs = paraColorLeyenda2 # Colores y nombres de la leyenda
dibujo.add(leyenda2) # Agregar la leyenda al dibujo

documento = SimpleDocTemplate("ejemploGraficasRpl.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos