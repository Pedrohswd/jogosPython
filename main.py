import random
print("*******************************")
print("Jogo de adivinhação")
print("*******************************")

numeroSecreto = random.random() * 100
numeroSecreto = round(numeroSecreto)

numeroDeTentativas = 0
pontos = 1000


print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = input("Defina: ")
nivel = int(nivel)

if (nivel == 1):
    numeroDeTentativas = 20
    print("Dificuldade definida como fácil!")
if (nivel == 2):
    numeroDeTentativas = 5
    print("Dificuldade definida como Médio!")
if (nivel == 3):
    numeroDeTentativas = 3
    print("Dificuldade definida como Difícil!")
print("Lembrando que sua pontuação incial é de 1000 pontos")
print("A cada erro, você perde a diferença do número que chutou ao número secreto")
print("Boa sorte!")

for tentativa in range(1, numeroDeTentativas+1):
    # format() faz a formatação em ordem substrituindo o {}
    print("Rodada {} de {}".format(tentativa, numeroDeTentativas))
    chute = input("Digite o seu número: ")
    chute = int(chute)
    print("Você digitou: ", chute)
    if chute < 1 or chute > 100:
        print("Número inválido! Digite um número entre 1 e 100")
        continue
    if (numeroSecreto == chute):
        print('Você acertou! Parabéns!')
        print('Sua pontuação foi de:', pontos)
        break
    else:
        pontos = pontos - abs((numeroSecreto - chute))
        if (chute > numeroSecreto):
            print("Muito alto, tente um pouco menos")
        else:
            print("Muito baixo, tente um pouco mais")
print("Fim de jogo")
