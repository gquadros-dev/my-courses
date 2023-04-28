print(34*'=')
print('Bem-vindo ao jogo de adivinhação!')
print(34*'=')

numero_secreto = 42
total_tentativas = 3

for rodada in range(1, (total_tentativas+1)):
    print(f'Tentativa {rodada} de {total_tentativas}')
    chute = int(input('Digite um número de 1 a 100: '))
    # print(f'Você digitou {chute}!')

    if chute < 1 or chute > 100:
        print('Você deve digitar um número entre 1 e 100! \n')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Você errou! O seu chute foi maior! \n')
        elif menor:
            print('Você errou! O seu chute foi menor! \n')
print('Fim de jogo!')


# while rodada <= total_tentativas:
#     print(f'Tentativa {rodada} de {total_tentativas}')
#     chute = int(input('Digite seu número: '))
#     # print(f'Você digitou {chute}!')
#
#     acertou = chute == numero_secreto
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto
#
#     if acertou:
#         rodada += 20
#         print('Você acertou!')
#     else:
#         if maior:
#             print('Você errou! O seu chute foi maior! \n')
#         elif menor:
#             print('Você errou! O seu chute foi menor! \n')
#     rodada += 1
# print('Fim de jogo!')





# import random
# loop = 0
# num_ran = random.randint(1, 10)
#
# while loop == 0:
#     chute = int(input('Digite um número: '))
#     acertou = chute == num_ran
#     maior = chute > num_ran
#     menor = chute < num_ran
#
#     if acertou:
#         loop = 1
#         print("você acertou!")
#     elif maior:
#         print('Seu chute foi maior, tente novamente!')
#         loop = 0
#     elif menor:
#         print('Seu chute foi menor, tente novamente!')
#         loop = 0
#     else:
#         print('Você errou, tente novamente!')
#         loop = 0
