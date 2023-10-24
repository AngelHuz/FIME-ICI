from guizero import App, Text, PushButton, TextBox

app = App(title="Hola ici")
message = Text(app,text="Dame tu nombre")
name = TextBox(app,width=30)

app.display()