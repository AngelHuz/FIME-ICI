##Indique cuantos años va a cumplir la persana dado el año de nacimiento
from guizero import App, Text, TextBox, PushButton
a_actual = 2023
a_minimo = 1900
def verificar_edad():
    nacimiento = int(input_nacimiento.value)
    if nacimiento >= a_minimo and nacimiento <= a_actual:
        mensaje.value = (f"CUMPLIRAS: {a_actual-nacimiento+1} AÑOS!!!")
    else:
        mensaje.value = ("Verifica tu año de nacimiento porfavor ._.?")
app = App("Verificador de Edad")

mensaje = Text(app, text="Ingresa tu año de nacimiento:", size=12)
input_nacimiento = TextBox(app, width=30)
verificar_button = PushButton(app, text="Verificar", command=verificar_edad)
mensaje_respuesta = Text(app, text="", size=12)

app.display()


