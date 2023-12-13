from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/Web_Prueba/')
def index():
    return render_template('index.html')

@app.route('/Web_Prueba/process', methods=['POST'])
def process():
    if request.method == 'POST':
        # Aquí puedes procesar los datos del formulario enviado desde la página web
        data = request.form.get('data')
        # Realiza alguna lógica con los datos, por ejemplo, guarda en una base de datos o realiza cálculos.
        return "Procesamiento exitoso"

if __name__ == '__main__':
    app.run(debug=True)