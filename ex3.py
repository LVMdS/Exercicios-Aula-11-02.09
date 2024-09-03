import random

def jogador_escolha():
    escolha = input("Escolha pedra, papel ou tesoura (ou digite 'sair' para sair): ").lower()
    if escolha not in ['pedra', 'papel', 'tesoura', 'sair']:
        print("Escolha inválida! Tente novamente.")
        return jogador_escolha()
    return escolha

def computador_escolha():
    return random.choice(['pedra', 'papel', 'tesoura'])

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def jogar_jogo():
    tentativas_max = 3
    tentativas = 0
    vitorias_jogador = 0
    vitorias_computador = 0
    
    while tentativas < tentativas_max:
        jogador = jogador_escolha()
        
        if jogador == 'sair':
            print("Você saiu do jogo. O computador saiu.")
            return False
        
        computador = computador_escolha()
        print(f"Computador escolheu: {computador}")
        resultado = determinar_vencedor(jogador, computador)
        print(resultado)
        
        if resultado == "Você ganhou!":
            vitorias_jogador += 1
        elif resultado == "Você perdeu!":
            vitorias_computador += 1
        
        tentativas += 1
        
        if tentativas < tentativas_max:
            print(f"Placar atual - Você: {vitorias_jogador} | Computador: {vitorias_computador}")
            print(f"Você tem {tentativas_max - tentativas} tentativas restantes.")
    
    # Verifica se há necessidade de rodada de desempate
    if vitorias_jogador == vitorias_computador:
        print("Empate após 3 rodadas! Jogando rodada de desempate...")
        jogador = jogador_escolha()
        
        if jogador == 'sair':
            print("Você saiu do jogo. O computador saiu.")
            return False
        
        computador = computador_escolha()
        print(f"Computador escolheu: {computador}")
        resultado = determinar_vencedor(jogador, computador)
        print(resultado)
        
        if resultado == "Você ganhou!":
            vitorias_jogador += 1
        elif resultado == "Você perdeu!":
            vitorias_computador += 1
    
    print(f"Placar final - Você: {vitorias_jogador} | Computador: {vitorias_computador}")
    if vitorias_jogador > vitorias_computador:
        print("Você venceu a melhor de 3!")
    elif vitorias_jogador < vitorias_computador:
        print("O computador venceu a melhor de 3!")
    else:
        print("Empate na melhor de 3!")

    return True

def main():
    print("Bem-vindo ao jogo de Jokenpo!")
    
    jogar_novamente = True
    while jogar_novamente:
        jogar_novamente = jogar_jogo()
        if jogar_novamente:
            resposta = input("Deseja jogar novamente? (s/n): ").lower()
            if resposta != 's':
                jogar_novamente = False
                print("Obrigado por jogar! Até a próxima!")

if __name__ == "__main__":
    main()