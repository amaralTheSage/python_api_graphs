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

usuario_id = 1
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTG9nSWQiOjEsInVzZXJMb2dOYW1lIjoiTG9yZW56byIsImlhdCI6MTczMzAwNzIwMCwiZXhwIjoxNzMzMDEwODAwfQ.4y8F2PVY7mI3IUaosTnTFUatfbOacxk2pimbtHN6z4k"




#### POST
def inclusao():
    titulo("Fazer uma reserva", "=")

    if token == "":
        print("Você precisa ter feito login para fazer uma reserva")
        return


    descricao = input("Descricao......: ")
    qtdDias = int(input("qtdDias.......: "))
    roomId = int(input("roomId: "))
    hotelId = int(input("hotelId: "))

    response = requests.post(url,
                             headers={"Authorization": f"Bearer {token}"},
                             json={
                                 "descricao": descricao,
                                 "qtdDias": qtdDias,
                                 "userId": usuario_id,
                                 "roomId": roomId,
                                 "hotelId": hotelId,
                             })
    
    reserva = response.json()
    print(reserva)




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
            f"{reserva['id']:4d} {reserva['descricao']:20s} {reserva['qtdDias']:4d} {reserva['userId']:4d} {reserva['roomId']:9.2f}")



#### UPDATE
def alteracao():
    listagem()

    if not token:
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
    print(f"RoomId: {float(reserva[0]['roomId'])}")

    novaQtdDias = int(input("Nova quantidade de dias: "))

    response = requests.put(url+"/"+str(id),
                              headers={"Authorization": f"Bearer {token}"},
                              json={"qtdDias": novaQtdDias})
     
    print(response.json())



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





