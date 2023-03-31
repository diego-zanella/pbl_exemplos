from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

registered_orders = []

hrefs = ["/pedidos", "/clientes", "/funcionarios", "/register_order","/admin"]
descriptions = ["Listar Pedidos","Listar Clientes", "Listar Funcionários", "Registrar Pedidos", "acessar administrador"]

@app.route('/')
def index():
    return render_template('index.html', hrefs=hrefs, descriptions=descriptions)

@app.route('/pedidos')
def pedidos():
    global registered_orders
    return render_template('pedidos.html',hrefs=hrefs, descriptions=descriptions, orders = registered_orders)

@app.route('/clientes')
def clientes():
    customers = ["Jonathan Jeremias","Fernando Moro","Diego Candido","Diego Zanella"]
    return render_template('clientes.html', clientes = customers)

@app.route('/funcionarios')
def funcionarios():
    employees = ["Camila","Osmar","Niuza","Heitor"]
    return render_template('funcionarios.html', funcionarios = employees)

@app.route('/register_order')
def register_order():
    return render_template('register_order.html', hrefs=hrefs, descriptions=descriptions)

@app.route('/save_orders', methods=["POST","GET"])
def save_order():
    name = request.form.get("name", None)
    ticket = request.form.get("ticket", None)

    global registered_orders
    registered_orders.append(name+", comanda " + ticket)

    return redirect(url_for("pedidos"))

if __name__ == "__main__":
    app.run()
