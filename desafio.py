import random
import os

# Nome do arquivo onde os dados serão armazenados
ARQUIVO_ESTADO = 'estado_jogo.txt'

def ler_estado():
    """Lê o estado do jogo a partir de um arquivo."""
    if not os.path.exists(ARQUIVO_ESTADO):
        return {'vitorias_jogador': 0, 'vitorias_computador': 0}
    
    with open(ARQUIVO_ESTADO, 'r') as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) == 2:
            return {
                'vitorias_jogador': int(linhas[0].strip()),
                'vitorias_computador': int(linhas[1].strip())
            }
    return {'vitorias_jogador': 0, 'vitorias_computador': 0}

def escrever_estado(vitorias_jogador, vitorias_computador):
    """Escreve o estado do jogo em um arquivo."""
    with open(ARQUIVO_ESTADO, 'w') as arquivo:
        arquivo.write(f"{vitorias_jogador}\n")
        arquivo.write(f"{vitorias_computador}\n")

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

def jogar_jogo(vitorias_jogador, vitorias_computador):
    tentativas_max = 3
    tentativas = 0
    
    while tentativas < tentativas_max:
        jogador = jogador_escolha()
        
        if jogador == 'sair':
            print("Você saiu do jogo. O computador saiu.")
            return vitorias_jogador, vitorias_computador, False
        
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
            return vitorias_jogador, vitorias_computador, False
        
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

    return vitorias_jogador, vitorias_computador, True

def main():
    print("Bem-vindo ao jogo de Jokenpo!")
    
    estado = ler_estado()
    vitorias_jogador = estado['vitorias_jogador']
    vitorias_computador = estado['vitorias_computador']
    
    jogar_novamente = True
    while jogar_novamente:
        vitorias_jogador, vitorias_computador, continuar = jogar_jogo(vitorias_jogador, vitorias_computador)
        if continuar:
            resposta = input("Deseja jogar novamente? (s/n): ").lower()
            if resposta != 's':
                jogar_novamente = False
                print("Obrigado por jogar! Até a próxima!")
        else:
            jogar_novamente = False
    
    escrever_estado(vitorias_jogador, vitorias_computador)

if __name__ == "__main__":
    main()
