import matplotlib.pyplot as plt
from crud import url  # type: ignore

# BARRAS
def grafico_hoteis_mais_reservados():
    # reservas = requests.get(url)

    # if reservas.status_code != 200:
    #     print("Erro: Não foi possível acessar a API")
    #     return

    # reservas = reservas.json()

    # hoteis = requests.get("http://localhost:3000/hotels").json()

    # Pegar as reservas e descobrir o nome do hotel a qual pertencem usando a relação,
    # depois montar gráfico com o nome do hotel no eixo x e o número de reservas marcadas nele no eixo y.
  
    reservas = [
        {"hotelId": 1, "roomId": 101},
        {"hotelId": 1, "roomId": 102},
        {"hotelId": 2, "roomId": 201},
        {"hotelId": 3, "roomId": 301},
        {"hotelId": 1, "roomId": 103},
        {"hotelId": 2, "roomId": 202}
    ]

    hoteis = [
        {"id": 1, "name": "Hotel A"},
        {"id": 2, "name": "Hotel B"},
        {"id": 3, "name": "Hotel C"}
    ]

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
        