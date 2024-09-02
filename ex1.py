jogada_computador = "tesoura"

jogada_jogador = input("Escolha pedra, papel, tesoura: ").lower()

if jogada_jogador == "tesouta":
    print("Empate")
elif jogada_jogador == "pedra" :
    print("Você venceu!")
elif jogada_jogador == "papel":
    print("Você perdeu!")
else:
    print("Entrada invalida, jogo encerrado.")