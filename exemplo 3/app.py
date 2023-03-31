from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def pagina_inicial():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    orders = ["Combo 1, comanda 2.","Combo 2, comanda 5.","Executivo 2, comanda 3",
    "Refri laranja, comanda 134","cerveja, comanda 12","batata frita, comanda 14"]
    return render_template('pedidos.html', pedidos = orders)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

if __name__ == "__main__":
    app.run()
    #app.debug = True
    #app.testing = True
