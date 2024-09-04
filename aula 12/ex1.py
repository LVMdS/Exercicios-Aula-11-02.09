# Jogo de Perguntas e Respostas

# Lista de perguntas e respostas
quiz = [
    {"pergunta": "Qual é a capital da França?", "resposta": "Paris"},
    {"pergunta": "Qual é o maior oceano do mundo?", "resposta": "Pacifico"},
    {"pergunta": "Quem escreveu 'Dom Quixote'?", "resposta": "Miguel de Cervantes"},
    {"pergunta": "Em que ano o homem pisou na Lua pela primeira vez?", "resposta": "1969"},
    {"pergunta": "Qual é o planeta mais próximo do Sol?", "resposta": "Mercurio"},
]

def executar_quiz():
    score = 0 
    
    for item in quiz:
        print(item["pergunta"])
        resposta_jogador = input("Sua resposta: ").strip()
        
        if resposta_jogador.lower() == item["resposta"].lower():
            print("Correto!")
            score += 1
        else:
            print(f"Errado! A resposta correta é: {item['resposta']}")
        
        print()
    
    # Mostrar pontuação final
    print(f"Fim do jogo! Você acertou {score} de {len(quiz)} perguntas.")

executar_quiz()
