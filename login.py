import pwinput
import requests
from utils.titulo import titulo

url_login = "http://localhost:3000/login"

# Variáveis redefinidas após um login bem sucedido
usuario_id = 0
token = ""

def login():
    # {
    #     lorenzo@gmail.com
    #     Lo12345@
    # }

    titulo("Login do Usuário")

    email = input("E-mail...: ")
    password = pwinput.pwinput(prompt='Senha....: ')

    response = requests.post(url_login, json={
        "email": email,
        "password": password
    })

    if response.status_code == 200:
        resposta = response.json()
        set_usuario_id(resposta['id'])
        set_token(resposta['token'])
        print(f"Bem vindo de volta, {resposta['name']}")
    else:
        print("Email ou senha incorretos")


def set_usuario_id(id):
    global usuario_id
    usuario_id = id

def set_token(t):
    global token
    token = t

def get_usuario_id():
    return usuario_id

def get_token():
    return token