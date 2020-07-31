
def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))

    if escolha == 1:
        print("\nPartida Isolada!")
        partida()
    else:
        if escolha == 2:
            print("\nVocê escolheu um Campeonato!")
            campeonato()


def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m + 1) > 0:
            return n % (m + 1)
        return m


def usuario_escolhe_jogada(n, m):
    tirar = int(input("Quantas peças você vai tirar?"))
    while tirar > m or tirar <= 0 or tirar > n:
        print("Oops! Jogada inválida! Tente de novo.")
        tirar = int(input("Quantas peças você vai tirar?"))
    return tirar


def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    # Condição para decidir se o usuário começa.
    if (n % (m + 1)) == 0:  # User começa.
        print("\nVoce começa!\n")
        while n > 0:
            userjoga1 = usuario_escolhe_jogada(n, m)
            if userjoga1 == 1:
                print("\nVoce tirou uma peça.")
            else:
                print("\nVoce tirou", userjoga1, "peças.")
            n = n - userjoga1
            if n == 1:
                print("Agora resta uma peça no tabuleiro.\n")
            else:
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.\n")
            if n == 0:
                print("Fim do jogo! Voce ganhou")
                return 1

            if n > 0:
                pcjoga1 = computador_escolhe_jogada(n, m)
                if pcjoga1 <= 1:
                    print("Computador tirou uma peça.")
                else:
                    print("Computador tirou", pcjoga1, "peças")
                n = n - pcjoga1
                if n == 1:
                    print("Agora resta uma peça no tabuleiro")
                else:
                    if n > 1:
                        print("Agora restam", n, "peças no tabuleiro.\n")

                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                    return 2

    else:  # Computador começa.
        print("\nComputador começa!\n")
        while n > 0:
            pcjoga = computador_escolhe_jogada(n, m)
            if pcjoga <= 1:
                print("Computador tirou uma peça.")
            else:
                print("Computador tirou", pcjoga, "peças.")
            n = n - pcjoga
            if n == 1:
                print("Agora resta uma peça no tabuleiro")
            else:
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.\n")

            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return 2

            if n > 0:
                userjoga = usuario_escolhe_jogada(n, m)
                if userjoga <= 1:
                    print("Voce tirou uma peça")
                else:
                    print("\nVoce tirou", userjoga, "peças.")
                n = n - userjoga
                if n == 1:
                    print("Agora resta uma peça no tabuleiro.\n")
                else:
                    if n > 1:
                        print("Agora restam", n, "peças no tabuleiro.\n")
                if n == 0:
                    print("Fim do jogo! Você ganhou")
                    return 1


def campeonato():
    contpartida = 1
    pluser = 0
    plpc = 0
    while contpartida < 4:
        print("\n**** Rodada", contpartida,"****\n")
        if partida() == 1:
            pluser += 1
        else:
            plpc += 1
        contpartida += 1
    print("\n**** Final do campeonato ****\n")
    print("Placar: Você", pluser, "X", plpc, "Computador")

main()

