from guizero import Text, TextBox, PushButton, App
##Se desea saber la cantidad de alumnos que pasaron una materia
##Son 25 alumnos y la calificación aprobatoría es 7

def contar_aprobados_reprobados():
    calificaciones:float = [float(entrada.value) for entrada in entradas]
    aprobados:int = (sum for calificacion in calificaciones if calificacion >= 7)
    reprobados:int = 25 - aprobados
    resultado_aprobados.value = (f"Aprobados: {aprobados} alumnos")
    resultado_reprobados.value = (f"Reprobados: {reprobados} alumnos")

app = App("Contador de Alumnos Aprobados/Reprobados", width=300, height=300)

instruccion = Text(app, "Ingrese la calificación de cada alumno (0-10):")
entradas = [TextBox(app) for _ in range(25)]

calcular_button = PushButton(app, text="Calcular", command=contar_aprobados_reprobados)
resultado_aprobados = Text(app, "")
resultado_reprobados = Text(app, "")

app.display()
