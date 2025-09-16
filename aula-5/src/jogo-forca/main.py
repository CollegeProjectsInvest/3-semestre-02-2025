# ler arquivo .txt
palavra_secreta = input("Digite a palavra secreta: ")
palavra_tentativa = []
letras_tentadas = []
tentativas_total: int = 5
tentativa_atual: int = 0


def inicializar_palavra_tentativa() -> None:
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    for _ in palavra_secreta:
        palavra_tentativa.append("_")


def imprimir_palavra_tentativa() -> str:
   palavra = "".join(palavra_tentativa)
   return palavra


def pedir_letra() -> bool:
    letra_tentativa = input("Digite uma letra: ")
    tem_letra = False
    if letra_tentativa not in letras_tentadas:
        for index, letra in enumerate(palavra_secreta):
            if letra == letra_tentativa:
                palavra_tentativa[index] = letra
                tem_letra = True
        letras_tentadas.append(letra_tentativa)
    else:
        tem_letra = True
        print(f"Letra '{letra_tentativa}' já foi tentada!")
        print(letras_tentadas)
    return tem_letra


def imprimir_forca() -> None:
   if tentativa_atual == 0:
       print("""
              |-------|
              |       |
              |
              |
              |
           ___|____
       """)
   elif tentativa_atual == 1:
        print("""
               |-------|
               |       |
               |      (_)
               |
               |
            ___|____
        """)
   elif tentativa_atual == 2:
        print("""
               |-------|
               |       |
               |      (_)
               |       |
               |
            ___|____
        """)
   elif tentativa_atual == 3:
        print("""
            |--------
            |       |
            |      (_)
            |      /|\\
            |
         ___|____
        """)
   elif tentativa_atual == 4:
        print("""
               |--------
               |       |
               |      (_)
               |      /|\\
               |       |
            ___|____
        """)
   elif tentativa_atual == 5:
        print("""
               |--------
               |       |
               |      (_)
               |      /|\\
               |       |
            ___|____  / \\
        """)


inicializar_palavra_tentativa()


while True:
    print(imprimir_palavra_tentativa())

    tem_letra = pedir_letra()
    if not tem_letra:
        tentativa_atual += 1

    imprimir_forca()

    print(f"Suas tentativas: {tentativa_atual}")
    if tentativa_atual >= tentativas_total:
        print("Game Over!")
        break

    if imprimir_palavra_tentativa() == palavra_secreta:
        print("Parabéns você ganhou!!")
        print(f"Palavra secreta: {palavra_secreta}")
        break
