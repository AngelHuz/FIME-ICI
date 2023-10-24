#Obtenga la suma de todos los cuadrados de n números

from guizero import Text, TextBox, App, PushButton
def calcular_promedio():
    numeros:int = entrada_numeros.value.split()
    numeros:int = [int(num) for num in numeros if int(num) >= 0]
    if numeros:
        promedio:int = sum(numeros) / len(numeros)
        resultado.value = (f"El promedio es: {promedio}")
    else:
        resultado.value = "No se ingresaron números positivos."
        
app = App("Calculadora de Promedio")

instrucciones = Text(app, "Ingrese los valores a calcular dejando espacios:")
entrada_numeros = TextBox(app)
calcular_button = PushButton(app, text="Calcular el Promedio", command=calcular_promedio)
resultado = Text(app, "")

app.display()
        
         
 