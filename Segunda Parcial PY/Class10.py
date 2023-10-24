##PREGUNTA UN DÍA Y DETERMINAR QUE DÍA DE LA SEMANA ES:
from guizero import Text, App, TextBox, PushButton 
lunes:int = 1
martes:int = 2
miercoles:int = 3
jueves:int = 4
viernes:int = 5
sabado:int = 6
domingo:int = 7   
def dias_semana():
    dia = int(input_dia.value)
    if dia == 1:
        mensaje.value = (f"LUNES")
    if dia == 2:
        mensaje.value = (f"MARTES")
    if dia == 3:
        mensaje.value = (f"MIERCOLES")
    if dia == 4:
        mensaje.value = (f"JUEVES")            
    if dia == 5:
        mensaje.value = (f"VIERNES")            
    if dia == 6:
        mensaje.value = (f"SABADO")
    if dia == 7:
        mensaje.value = (f"DOMINGO")       
    elif dia < 1 or dia > 7:
        mensaje.value = (f"Ingresa un numero del rango -_-")                                     
     
app = App("D Í A S DE LA S E M A N A")
mensaje = Text(app, "Ingrese un número entre el 1 y 7:")
calcular_button = PushButton(app, text="¿DÍA?", command=dias_semana)
input_dia = TextBox(app, width=30)
resultado = Text(app, "")

app.display()    