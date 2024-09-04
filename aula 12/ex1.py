pergunta = "Qual é a capital do Brasil?"
resposta_correta = "Brasília"

print(pergunta)
resposta = input("Sua resposta: ")

if resposta.lower() == resposta_correta.lower():
    print("Correto!")
else:
    print("Errado! A resposta correta é Brasília.")
