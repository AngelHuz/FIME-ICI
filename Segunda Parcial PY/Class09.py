##Obtenga la suma de 5 números positivos capturados entre 5 y 10 "inclusive"

from guizero import Text, TextBox, App, PushButton
def sumatoria():
 numeros:int = entrada_numeros.value.split()
 numeros:int = [int(num) for num in numeros if int(num) >= 0]
 if numeros:
  sumar:int = sum(numeros)
  resultado.value = (f"La sumatoria de los valores es: {sumar}")
          

app = App("S U M A R")

instrucciones = Text(app, "Ingrese los valores a SUMAR dejando espacios (SOLO VALORES POSITIVOS):")
entrada_numeros = TextBox(app)
calcular_button = PushButton(app, text="S u m a r", command=sumatoria)
resultado = Text(app, "")

app.display()
        