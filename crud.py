import requests
import matplotlib.pyplot as plt
import numpy as np
from login import get_token, get_usuario_id, token, usuario_id
from utils.titulo import titulo


url = "http://localhost:3000/reservations"

#### POST
def inclusao():
    titulo("Fazer uma reserva")

    print(f"usuario_id: {get_usuario_id()}, token: {get_token()}")
    if get_token() == "":
        print("Você precisa ter feito login para fazer uma reserva")
        return

    descricao = input("Descricao......: ")
    qtdDias = int(input("qtdDias.......: "))
    roomId = int(input("roomId: "))
    hotelId = int(input("hotelId: "))

    response = requests.post(url,
                             headers={"Authorization": f"Bearer {get_token()}"},
                             json={
                                 "descricao": descricao,
                                 "qtdDias": qtdDias,
                                 "userId": get_usuario_id(),
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

    print(f"{'Id':<4} {'Descricao':<20} {'QtdDias':<10} {'UserId':<10} {'RoomId':<10}  {'HotelId':<10}")
    print("-" * 74) 

    for reserva in reservas:
        print(f"{reserva['id']:<4} {reserva['descricao']:<20} {reserva['qtdDias']:<10} {reserva['userId']:<10} {reserva['room']['id']:<10} {reserva['hotel']['id']:<10}")



#### UPDATE
def alteracao():
    listagem()

    if not get_token():
        print("Você precisa estar logado para alterar reservas")
        return

    id = int(input("\nQual o ID da reserva a ser alterada? (0 para sair) -- "))

    reserva = requests.get(f"{url}/{id}").json()
    
    print(f"\nDescricao..: {reserva['descricao']}")
    print(f"qtdDias...: {reserva['qtdDias']}")
    print(f"userId.....: {reserva['userId']}")
    print(f"RoomId: {(reserva['roomId'])}")

    novaQtdDias = int(input("Nova quantidade de dias: "))

    response = requests.put(f"{url}/{id}",
                              headers={"Authorization": f"Bearer {get_token()}"},
                              json={"qtdDias": novaQtdDias})
     
    print(response.json())



#### DELETE
def exclusao():
    if get_token() == "":
        print("Você precisa estar logado para excluir reservas")
        return

    listagem()

    id = int(input("\nQual o ID da reserva a ser excluida? (0 para sair) -- "))

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
                                   headers={"Authorization": f"Bearer {get_token()}"})

        if response.status_code == 200:
            reserva = response.json()
            print("Ok! Reserva excluída com sucesso!")
        else:
            print("Não foi possível excluir esta reserva")





