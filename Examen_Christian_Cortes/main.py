from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def PaginaPrincipal():
    """Renderiza la página principal (PaginaPrincipal.html)."""
    return render_template('PaginaPrincipal.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    """
    Renderiza la página del ejercicio 1 (ejercicio1.html) y procesa el formulario.

    Si el método de la petición es POST, calcula el total de la compra con descuento
    basado en la edad y la cantidad, y pasa el resultado al template.
    Si es GET, simplemente renderiza el template.
    """
    resultado = None  # Inicializa resultado en None para evitar errores si es un GET
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'monto_descuento': monto_descuento,
            'total_con_descuento': total_con_descuento
        }
    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None  # Inicializa mensaje en None para evitar errores si es un GET
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuarios = {
            'juan': 'admin',
            'pepe': 'user'
        }
        if username in usuarios and usuarios[username] == password:
            mensaje = f'Bienvenido {username}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
