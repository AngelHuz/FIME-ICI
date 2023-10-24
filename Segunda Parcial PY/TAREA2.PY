##La fime quiere dar una beca a su mejor estudiante, para eso les preguntó:
##Sus 6 calificaciones y sus nombres
##Son (N) alumnos, diga el nombre y el promedio del alumno que debe recibir la beca

from guizero import App, TextBox, PushButton, Text
##Lista
personas = []

def calcular_promedio():
    nombre:str = nombre_input.value
    calificaciones:float = calificaciones_input.value.split()
    calificaciones:float = [float(cal) for cal in calificaciones]
    promedio:float = sum(calificaciones) / len(calificaciones)
    personas.append((nombre, promedio))
    #append es para la lista
    
    nombre_input.clear()
    calificaciones_input.clear()
    
def determinar_mejor_promedio():
    if personas:
        mejor_persona = max(personas, key=lambda x: x[1])
        resultado.value = (f"Mejor promedio es: {mejor_persona[0]} con {mejor_persona[1]:}")

app = App("¿Quién ganará la beca?")

nombre_label = Text(app, "Nombre:")
nombre_input = TextBox(app)
calificaciones_label = Text(app, " ingrese las Calificaciones (separadas por espacio):")
calificaciones_input = TextBox(app)
calcular_button = PushButton(app, text="Siguiente persona", command=calcular_promedio)
resultado = Text(app, "", size=20)
mejor_button = PushButton(app, text="GANADOR:", command=determinar_mejor_promedio)

app.display()
