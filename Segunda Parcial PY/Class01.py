#Calcular la edad de una persona con el año actual y el año de nacimiento de esa persona
#usar guizero para generarlo en una ventana
from guizero import App, Box, Text, PushButton, TextBox
def calcular_edad():
        año_actual = int(input_año_actual.value)
        año_nacimiento = int(input_año_nacimiento.value)
        resultado.value = (f"Edad: {año_actual - año_nacimiento} años")

app = App("Calculadora de Edad", layout="grid")

entrada_box = Box(app, layout="grid", grid=[0, 0])
resultado = Text(app, text="", grid=[0, 1])

Text(entrada_box, text="Año Actual:", grid=[0, 0])
input_año_actual = TextBox(entrada_box, grid=[1, 0])
Text(entrada_box, text="Año de Nacimiento:", grid=[0, 1])
input_año_nacimiento = TextBox(entrada_box, grid=[1, 1])

calcular_button = PushButton(entrada_box, text="Calcular Edad", grid=[0, 2, 2, 1], command=calcular_edad)

app.display()
 
 #NOTAS Y OBSERVACIONES DE RETROALIMENTACIÓN Y APRENDIZAJE:
##Falta Condicionar los valores para que al ingresar valores no correctos genere un error al usuario.