palavra_secreta: str = input("Digite a palavra secreta: ")
tentativa_palavra: str = "_" * len(palavra_secreta)

print(tentativa_palavra)
print(f"{len(tentativa_palavra)} letras")

letras_tentadas: str = ""
tentativas_maxima: int = 7
tentativas: int = 0

while tentativas <= tentativas_maxima:
    if tentativa_palavra == palavra_secreta:
        print("Ganhou!!!")
        break

    print(f"Tentativas: {tentativas}/{tentativas_maxima}")
    chute_letra: str = input("Escolha uma letra: ")

    if chute_letra in letras_tentadas:
        print(f"Letra '{chute_letra}' já foi utilizada.")
        print(f"Letras utilizadas: {letras_tentadas}")
    else:
        letras_tentadas += chute_letra

        if chute_letra in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == chute_letra:
                    tentativa_palavra = tentativa_palavra[:index] + chute_letra + tentativa_palavra[index+1:]
            print(tentativa_palavra)
        else:
            print(f"Não tem a letra: {chute_letra}")
            tentativas += 1

print(f"A palavra secreta era: {palavra_secreta}")
