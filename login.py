from crud import titulo, url_login
import pwinput
import requests

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
        global usuario_id
        global token
        usuario_id = resposta['id']
        token = resposta['token']
        print(f"Bem vindo de volta, {resposta['name']}")
    else:
        print("Email ou senha incorretos")