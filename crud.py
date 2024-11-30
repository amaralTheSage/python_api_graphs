import requests
import matplotlib.pyplot as plt
import numpy as np
import pwinput # type: ignore
def titulo(texto, traco="-"):
    print()
    print(texto)
    print(traco*40)

url = "http://localhost:3000/reservations"
url_login = "http://localhost:3000/login"

usuario_id = "3"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTG9nSWQiOjMsInVzZXJMb2dOYW1lIjoiTG9yZW56byIsImlhdCI6MTczMjk5NzkxNywiZXhwIjoxNzMzMDAxNTE3fQ.ppUrR45HcjYAzJwpXXcgRcmbjnOVPdqF1rP9NOG9Ewk"




#### POST
def inclusao():
    titulo("Fazer uma reserva", "=")

    if token == "":
        print("Você precisa ter feito login para fazer uma reserva")
        return


    descricao = input("Descricao......: ")
    qtdDias = input("qtdDias.......: ")
    userId = int(input("userId.........: "))
    roomId = int(input("roomId: "))

    response = requests.post(url,
                             headers={"Authorization": f"Bearer {token}"},
                             json={
                                 "descricao": descricao,
                                 "qtdDias": qtdDias,
                                 "userId": userId,
                                 "roomId": roomId,
                             })

    if response.status_code == 201:
        reserva = response.json()
        print(f"Ok! Reserva cadastrado com código: {reserva['id']}")
    else:
        print("Erro... Não foi possível incluir o reserva")



#### READ
def listagem():
    titulo("Listagem das Reservas")

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro... Não foi possível acessar a API")
        return

    reservas = response.json()

    print("Id....: Descricao.............: qtdDias.........: userId.........: roomId...:")
    print("----------------------------------------------------------------------------")

    for reserva in reservas:
        print(
            f"{reserva['id']:4d} {reserva['descricao']:20s} {reserva['qtdDias']:15s} {reserva['userId']:4d} {reserva['roomId']:9.2f}")



#### UPDATE
def alteracao():
    listagem()

    if token == "":
        print("Você precisa estar logado para alterar reservas")
        return

    id = int(input("\nQual o ID da reserva a ser alterada? (0 para sair)"))

    response = requests.get(url)
    reservas = response.json()

    reserva = [x for x in reservas if x['id'] == id]

    if len(reserva) == 0:
        print("Erro. Informe um código existente")
        return

    print(f"\nDescricao..: {reserva[0]['descricao']}")
    print(f"qtdDias...: {reserva[0]['qtdDias']}")
    print(f"userId.....: {reserva[0]['userId']}")
    print(f"RoomId: {float(reserva[0]['roomId']):9.2f}")

    novaQtdDias = int(input("Nova quantidade de dias: "))

    response = requests.put(url+"/"+str(id),
                              headers={"Authorization": f"Bearer {token}"},
                              json={"qtdDias": novaQtdDias})

    if response.status_code == 200:
        reserva = response.json()
        print("Ok! Reserva alterado com sucesso!")
    else:
        print("Não foi possível alterar a quantidade de dias da reserva")



#### DELETE
def exclusao():
    if token == "":
        print("Você precisa estar logado para excluir reservas")
        return

    listagem()

    id = int(input("\nQual o ID da reserva a ser excluida? (0 para sair)"))

    if id == 0:
        return

    response = requests.get(url)
    reservas = response.json()

    reserva = [x for x in reservas if x['id'] == id]

    if len(reserva) == 0:
        print("Erro. Informe um código existente. ")
        return

    print(f"\nDescricao..: {reserva[0]['descricao']}")
    print(f"qtdDias...: {reserva[0]['qtdDias']}")
    print(f"userId.....: {reserva[0]['userId']}")
    print(f"RoomId : {float(reserva[0]['roomId']):9.2f}")

    confirma = input("Confirma a exclusão (S/N)? ").upper()

    if confirma == "S":
        response = requests.delete(url+"/"+str(id), 
                                   headers={"Authorization": f"Bearer {token}"})

        if response.status_code == 200:
            reserva = response.json()
            print("Ok! Reserva excluída com sucesso!")
        else:
            print("Não foi possível excluir esta reserva")





