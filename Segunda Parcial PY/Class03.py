#optener el promedio de n números positivos
from guizero import App, Text, PushButton, TextBox

def calcular_promedio():
    numeros = entrada_numeros.value.split()
    numeros = [float(num) for num in numeros if float(num) >= 0]
    if numeros:
        promedio = sum(numeros) / len(numeros)
        resultado.value = f"El promedio es: {promedio:.2f}"
    else:
        resultado.value = "No se ingresaron números positivos."

app = App("Calculadora de Promedio")


instrucciones = Text(app, "Ingrese números positivos separados por espacios:")
entrada_numeros = TextBox(app)
calcular_button = PushButton(app, text="Calcular Promedio", command=calcular_promedio)
resultado = Text(app, "")

app.display()


