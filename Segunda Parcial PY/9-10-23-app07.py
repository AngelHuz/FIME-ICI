from guizero import TextBox, PushButton, App, Text
app = App(title = "Cuadrado de un numero")
message = Text(app, text = "dame un número")
name = TextBox(app, width= 30)
button = PushButton(app,text = "enviar")
app.display()