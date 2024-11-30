import matplotlib.pyplot as plt
from crud import url  # type: ignore
import numpy as np
import requests

# BARRAS
def grafico_hoteis_mais_reservados():
    reservas = requests.get(url).json()

    # if reservas.status_code != 200:
    #     print("Erro: Não foi possível acessar a API")
    #     return

    hoteis = requests.get("http://localhost:3000/hotels").json()
  
    x = [] 
    y = []  

    hotel_reservas = {}

    for r in reservas:
        for h in hoteis:
            if r['hotelId'] == h['id']:  
                if h['id'] not in hotel_reservas:
                    hotel_reservas[h['id']] = 0
                hotel_reservas[h['id']] += 1

    for h in hoteis:
            x.append(h['name'])  
            y.append(hotel_reservas[h['id']])  

    fig, ax = plt.subplots()

    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(x, y, color=bar_colors)

    ax.set_ylabel('reservas')
    ax.set_title('Hotéis com mais reservas registradas')

    plt.show()



#################################################################
import requests
import matplotlib.pyplot as plt
import numpy as np

import requests
import matplotlib.pyplot as plt
import numpy as np

def grafico_quartos_mais_reservados():
    hotel = int(input("Id do hotel: "))


    todasReservas = requests.get(url).json()

    reservas = []

    for r in todasReservas:
        if int(r['hotelId']) == hotel:
            reservas.append(r)


    print(reservas)

    quarto_reservas = {}

    for r in reservas:
        room_id = r["room"]["id"]  
        if room_id not in quarto_reservas:
            quarto_reservas[room_id] = 0
        quarto_reservas[room_id] += 1

    quartos_ordenados = sorted(quarto_reservas.items(), key=lambda x: x[1], reverse=True)

    ids_quartos = [quarto[0] for quarto in quartos_ordenados]
    reservas_count = [quarto[1] for quarto in quartos_ordenados]
    numeros_quartos = [next(r['room']['number'] for r in reservas if r['room']['id'] == id_quarto) for id_quarto in ids_quartos]


    fig, ax = plt.subplots()
    y_pos = np.arange(len(ids_quartos))
    ax.barh(y_pos, reservas_count, align='center')
    ax.set_yticks(y_pos, labels=numeros_quartos) 
    ax.set_xlabel('Número de Reservas')
    ax.set_title(f'Quartos mais reservados no hotel {hotel}')

    plt.show()




# Se posteriormente der pau, dá pra usar:

    # fig, ax = plt.subplots()

    # bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    # x_pos = np.arange(len(ids_quartos))
    # ax.bar(x_pos, reservas_count, color=bar_colors)
    # ax.set_xticks(x_pos)
    # ax.set_xticklabels(numeros_quartos)
    # ax.set_xlabel('Número do Quarto')
    # ax.set_ylabel('Número de Reservas')
    # ax.set_title(f'Quartos mais reservados no hotel {hotel}')

    # plt.show()
    



