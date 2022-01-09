from flask import Blueprint, request, Response
from flask_restx import Namespace, Resource

login_controller = Blueprint('login_controller', __name__)

api = Namespace('Login', description='Realizar login na aplicação')

@api.route('/login', methods=['POST'])
class Login(Resource):
    def post(self):

        body = request.get_json()

        if not body or "login" not in body or "senha" not in body:
            return Response("Parâmetros de senha inválidos", status=400, mimetype='application/json')

        return "OK"