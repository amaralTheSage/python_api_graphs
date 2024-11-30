from crud import alteracao, exclusao, inclusao, listagem, titulo
from graphs import grafico_hoteis_mais_reservados, grafico_quartos_mais_reservados
from login import login

while True:
    titulo("Reservas em Hóteis")
    print("1. Login do Usuário")
    print("2. Inclusão de Reservas")
    print("3. Listagem de Reservas")
    print("4. Alteração de RoomId")
    print("5. Exclusão de Reserva")
    print("6. Hotéis mais reservados (Gráfico)")
    print("7. Quartos mais reservados (Gráfico)")
    print("0. Finalizar")
    opcao = int(input("Opção: "))

    if opcao == 1:
        login()
    elif opcao == 2:
        inclusao()
    elif opcao == 3:
        listagem()
    elif opcao == 4:
        alteracao()
    elif opcao == 5:
        exclusao()
    elif opcao == 6:
        grafico_hoteis_mais_reservados()
    elif opcao == 7:
        grafico_quartos_mais_reservados()
    else:
        break
