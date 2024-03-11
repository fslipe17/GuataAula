print("================================")
print("Bem-vindo ao jogo de Adivinhação")
print("================================")


import random

numero = random.randint(0, 100)

print("")

tentativas = 10
rodada = 1

while (rodada <= tentativas):
    print("Tentativa {} de 10".format(rodada, tentativas))

    chute_str = input("Digite o seu numero: ")
    print("Você Digitou", chute_str)
    chute = int(chute_str)

    acertou = chute == numero
    maior = chute < numero
    menor = chute > numero

    if(acertou):
        print("Parabéns!! Você acertou ;)")
        rodada = rodada + 11111111111111111111111111111111111111111111111111
    else:
        if(maior):
            print("O número é maior que", chute)
        elif(menor):
            print("O numero é menor que", chute)

    rodada = rodada + 1

print("Fim de jogo")