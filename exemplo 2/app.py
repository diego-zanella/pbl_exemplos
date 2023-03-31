from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

if __name__ == "__main__":
    app.run()
