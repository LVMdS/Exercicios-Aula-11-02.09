import unicodedata
import time

def remover_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    texto_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return texto_sem_acento

print('''
      Bem-vindo! 
      
      Vamos lá para nosso Quiz?!
      ''')

time.sleep(2)

quiz = [
    {"pergunta": "Qual é a capital da França?", "resposta": "Paris", "pontuacao": 10},
    {"pergunta": "Qual é o maior oceano do mundo?", "resposta": "Pacífico", "pontuacao": 15},
    {"pergunta": "Quem escreveu 'Dom Quixote'?", "resposta": "Miguel de Cervantes", "pontuacao": 20},
    {"pergunta": "Em que ano o homem pisou na Lua pela primeira vez?", "resposta": "1969", "pontuacao": 15},
    {"pergunta": "Qual é o planeta mais próximo do Sol?", "resposta": "Mercúrio", "pontuacao": 10},
    {"pergunta": "Na matemática, o que resulta a soma dos quadrados dos catetos?","resposta": "Hipotenusa", "pontuacao":30}
]

def executar_quiz():
    score = 0  
    respostas = [None] * len(quiz)
    pergunta_atual = 0

    try:
        while True:
            item = quiz[pergunta_atual]
            print(f"\nPergunta {pergunta_atual + 1}: {item['pergunta']}")
            print()
            print("1. Responder")
            print("2. Voltar para Pergunta Anterior")
            print("3. Finalizar Quiz")
            opcao = input("Escolha uma opção (1/2/3): ").strip()
            print()

            if opcao == '3':
                break

            if opcao == '2':
                if pergunta_atual > 0:
                    pergunta_atual -= 1
                    continue
                else:
                    print("Não há perguntas anteriores.")
                    continue

            if opcao == '1':
                resposta_jogador = input("Sua resposta: ").strip()
                respostas[pergunta_atual] = resposta_jogador

                resposta_normalizada = remover_acentos(respostas[pergunta_atual]).lower()
                resposta_correta_normalizada = remover_acentos(item["resposta"]).lower()

                if resposta_normalizada == resposta_correta_normalizada:
                    print("Correto!")
                    score += item["pontuacao"]
                else:
                    print(f"Errado! A resposta correta é: {item['resposta']}")

                pergunta_atual += 1
                if pergunta_atual >= len(quiz):
                    print(f"\nFim do jogo! Sua pontuação total é: {score}")
                    print()
                    break
            else:
                print("Opção inválida, por favor, escolha 1, 2 ou 3.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
executar_quiz()
