from guizero import App, Text, TextBox, PushButton
import pyttsx3

def calcular_cuadrado():
    try:
        numero = float(entrada_numero.value)
        cuadrado = numero ** 2
        resultado_cuadrado.value = f"El cuadrado de {numero} es: {cuadrado:.2f}"
        if numero < 0:
            resultado_cuadrado.value = "valor incorrecto"
        else:
            engine = pyttsx3.init()
            engine.say(f"El cuadrado de {numero} es {cuadrado:.2f}")
            engine.runAndWait()
    except ValueError:
        resultado_cuadrado.value = "Por favor, ingrese un número válido."

app = App("Calculadora del Cuadrado", width=300, height=150)

instruccion = Text(app, "Ingrese un número:")
entrada_numero = TextBox(app)
calcular_button = PushButton(app, text="Calcular Cuadrado", command=calcular_cuadrado)
resultado_cuadrado = Text(app, "")

app.display()
