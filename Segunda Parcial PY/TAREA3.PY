#Se desea conocer de (n) alumnos:
#Promedio general, calificación mayor y menor.
#Cuantos alumnos aprobaron y cuantos reprobaron.
from guizero import App, TextBox, Text, PushButton
nombres = []
calificaciones = []
def calcular_estadisticas():
    if not nombres or not calificaciones:
        resultado.value = "No hay datos de alumnos."
        return
    
    promedio_general = sum(calificaciones) / len(calificaciones)
    calificacion_max = max(calificaciones)
    calificacion_min = min(calificaciones)
    
    aprobados = sum(1 for cal in calificaciones if cal >= 7)
    reprobados = len(calificaciones) - aprobados

    resultado.value = (f"El promedio general es: {promedio_general:}\n")
    resultado.value += (f"Calificación Más Alta Es: {calificacion_max}\n")
    resultado.value += (f"Calificación Más Baja Es: {calificacion_min}\n")
    resultado.value += (f"Alumnos Aprobados: {aprobados}\n")
    resultado.value += (f"Alumnos Reprobados: {reprobados}")
    
def borrar_datos():
    if nombres or calificaciones:
        resultado.value = (f"datos reseteados, ingrese más datos")
 
app = App("Calificaciones de alumnos")

calcular_button = PushButton(app, text="Calcular Resultados de evaluación", command=calcular_estadisticas)
borrar_button = PushButton(app, text="borrar datos", command=borrar_datos)
resultado = Text(app, "", size=20)

def agregar_alumno():
    nombre:str = nombre_input.value
    if nombre.isalpha():
     calificacion = float(calificacion_input.value)
     if calificacion <0:
         resultado.value = (f"calificaciones incorrectas")
         return
        
     nombres.append(nombre)
     calificaciones.append(calificacion)
    else:
     resultado.value = (f"ingresaste un número en el nombre 0_0?")   
     nombre_input.clear()
     calificacion_input.clear()
        

    nombre_input.clear()
    calificacion_input.clear()

agregar_label = Text(app, "Agregar Alumno")
nombre_label = Text(app, "Nombre:")
nombre_input = TextBox(app)
calificacion_label = Text(app, "Calificación:")
calificacion_input = TextBox(app)
agregar_button = PushButton(app, text="Siguiente Alumno:", command=agregar_alumno)

app.display()
