#Verificar edad
from guizero import App, Text, TextBox, PushButton

def verificar_edad():
    edad = int(input_edad.value)
    if edad < 0 or edad >120:
     mensaje.value = "Edad incorrecta."
    if edad >= 18 and edad <= 120:
        mensaje.value = "Eres mayor de edad."
    elif edad < 18 and edad >= 0:
        mensaje.value = "Debes ser mayor de edad."

app = App("Verificador de Edad")

mensaje = Text(app, text="Ingresa tu edad:", size=12)
input_edad = TextBox(app, width=30)
verificar_button = PushButton(app, text="Verificar", command=verificar_edad)
mensaje_respuesta = Text(app, text="", size=12)

app.display()


