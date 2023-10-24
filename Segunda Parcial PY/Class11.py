##Genere una secuencia de numeros ceros y unos 
from guizero import Text, App, TextBox, PushButton 
secuencia = "01"
def cuantas_veces():
  veces = int(input_veces.value)
  if veces:
     resultado.value = f"01{secuencia * veces}" 
     
    
app = App("S U M A R")
mensaje = Text(app, "Cuantas veces desea generarlo?")
input_veces = TextBox(app)
calcular_button = PushButton(app, text="generar", command=cuantas_veces)
resultado = Text(app, "")
app.display()
        