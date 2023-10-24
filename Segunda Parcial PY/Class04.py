#edad promedio de las edades de n personas:
from guizero import Text, TextBox, App, PushButton
def calcular_promedioedad():
    numeros:int = entrada_numeros.value.split()
    numeros:int = [int(num) for num in numeros if int(num) >= 0]
    if numeros:
        promedio:int = sum(numeros) / len(numeros)
        if promedio:float 
        promedio = int(promedio)
        resultado.value = (f"El promedio es: {promedio}")
    else:
        resultado.value = "No se ingresaron números positivos."
        
app = App("Calculadora de Promedio")

instrucciones = Text(app, "Ingrese las edades separadas por espacios:")
entrada_numeros = TextBox(app)
calcular_button = PushButton(app, text="Calcular edad Promedio", command=calcular_promedioedad)
resultado = Text(app, "")

app.display()