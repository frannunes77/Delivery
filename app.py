from flask import Flask
from models.categorias.controller import categoria_controller
from models.produtos.controller import produtos_controller

app = Flask(__name__)

app.register_blueprint(categoria_controller)
app.register_blueprint(produtos_controller)


app.run(host='127.0.0.1', port=5001, debug=True)