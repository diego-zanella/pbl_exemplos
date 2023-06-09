from flask import Flask

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return """<html>
                <head>
                    <title>Meu restaurante</title>
                </head>
                <body>
                    <h1>Meu restaurante</h1>
                    <h3>Acesse o Menu</h3>
                    <ul>
                        <li><a href="/pedidos">Listar pedidos</a></li>
                        <li><a href="/clientes">Listar clientes</a></li>
                        <li><a href="/funcionarios">Listar funcionarios</a></li>
                        
                    </ul>
                    <p>Lembre-se de tudo</p>
                </body>
            </html>"""

@app.route('/pedidos')
def pedidos():
    return """<html>
                <head>
                    <title>Meu restaurante</title>
                </head>
                <body>
                    <h1>Pedidos</h1>
                    <ul>
                        <li>Combo 1, comanda 2.</li>
                        <li>Combo 2, comanda 5.</li>
                        <li>Executivo 2, comanda 3</li>
                        <li>Refri laranja, comanda 134</li>
                        <li>cerveja, comanda 12</li>
                        <li>batata frita, comanda 14</li>   
                    </ul>
                    <p>Voltar para <a href="/">pagina inicial</a></p>
                </body>
            </html>"""

@app.route('/clientes')
def clientes():
    return """<html>
                <head>
                    <title>Meu restaurante</title>
                </head>
                <body>
                    <h1>Clientes</h1>
                    <ul>
                        <li>Cliente 1</li>
                        <li>Cliente 2</li>
                        <li>Cliente 3</li>
                        <li>Cliente 4</li>
                        <li>Cliente 5</li>
                        <li>Cliente 6</li>   
                    </ul>
                    <p>Voltar para <a href="/">pagina inicial</a></p>
                </body>
            </html>"""

@app.route('/funcionarios')
def funcionarios():
    return """<html>
                <head>
                    <title>Meu restaurante</title>
                </head>
                <body>
                    <h1>Funcionarios</h1>
                    <ul>
                        <li>Funcionario 1</li>
                        <li>Funcionario 2</li>
                        <li>Funcionario 3</li>
                        <li>Funcionario 4</li>
                        <li>Funcionario 5</li>
                        <li>Funcionario 6</li>   
                    </ul>
                    <p>Voltar para <a href="/">pagina inicial</a></p>
                </body>
            </html>"""

if __name__ == "__main__":
    app.run()
