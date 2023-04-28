from random import choice

def jogar():
    titulo()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra? ").strip().upper()

        if(chute in palavra_secreta):
            marca_letra(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 8
        acertou = "_" not in letras_acertadas
        forca(erros)
        print(''.join(letras_acertadas))

    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


def titulo():
    print("*"*37 + "\n")
    print("**   Bem vindo ao jogo da Forca!   ** \n")
    print("*"*37 + '\n')


def carrega_palavra_secreta():
    palavras = []
    arquivo = open(r"g:\Meu Drive\Estudos de programacao\Python\Python - Alura\avançando em python\palavra.txt", "r", encoding="UTF-8")
    for linha in arquivo:
        palavras.append(linha.strip().upper())
    arquivo.close()
    palavra_secreta = choice(palavras)
    return palavra_secreta


def inicializa_letras_acertadas(aaa):
    return ["_" for letra in aaa]


def marca_letra(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def mensagem_perdedor(palavra_secreta):
    print(f'Você enforcou!!! A palavra era {palavra_secreta.capitalize()}\n')
    print(r"    _______________         ")
    print(r"   /               \       ")
    print(r"  /                 \      ")
    print(r"//                   \/\  ")
    print(r"\|   XXXX     XXXX   | /   ")
    print(r" |   XXXX     XXXX   |/     ")
    print(r" |   XXX       XXX   |      ")
    print(r" |                   |      ")
    print(r" \__      XXX      __/     ")
    print(r"   |\     XXX     /|       ")
    print(r"   | |           | |        ")
    print(r"   | I I I I I I I |        ")
    print(r"   |  I I I I I I  |        ")
    print(r"   \_             _/       ")
    print(r"     \_         _/         ")
    print(r"       \_______/           ")


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |")
        print(" |")
        print(" |")
        print(" |")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(r" |      \|     ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(r" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(r" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(r" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(r" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(r" |      \|/   ")
        print(" |       |    ")
        print(r" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()