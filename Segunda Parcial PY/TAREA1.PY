##Una empresa desea saber el sueldo de una persona bajo los siguientes rubros:
## 5% de canasta básica 3% de prima de antiguedad 
## Si el salario base excede de los 10mil el icr será del 30%
## Si elimpuesto base es menor a 10mil el icr será del 20%

from guizero import App, Text, TextBox, PushButton

def calcular_salario():
    sueldo = float(input_box.value)
    if sueldo < 0:
        result_text.value = (f"salario incorrecto")
    elif sueldo <= 10000:
        salario_neto = sueldo * 0.72
        sat = sueldo * 0.28
        result_text.value = (f"Salario Neto: ${salario_neto:}, Impuesto a pagar: ${sat:}")
    elif sueldo > 10000:    
        sat = sueldo * 0.38
        salario_neto = sueldo * 0.62 
        result_text.value = (f"Salario Neto: ${salario_neto:}, Impuesto a pagar: ${sat:}")
    
app = App("Impuesto Sobre la renta", width=300, height=150)

instrucción = Text(app, "Ingresa el sueldo base:")
input_box = TextBox(app)
calculate_button = PushButton(app, text="Calcular", command=calcular_salario)
result_text = Text(app, text="Nomina:")

app.display()
