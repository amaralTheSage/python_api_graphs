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
    senha = pwinput.pwinput(prompt='Senha....: ')

    response = requests.post(url_login, json={
        "email": email,
        "senha": senha
    })

    if response.status_code == 200:
        resposta = response.json()
        global usuario_id
        global token
        usuario_id = resposta['id']
        token = resposta['token']
        print(f"Bem vindo de volta, {resposta['nome']}")
    else:
        print("Email ou senha incorretos")