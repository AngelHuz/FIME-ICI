from guizero import App, Text, PushButton
def change_message():
    message.value = "Flor de loto"
app = App(title="Hola ici")
message = Text(app,text="Welcome to ici world")
button = PushButton(app,text = "click here", command = change_message)         
app.display()