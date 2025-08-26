import random

numero_aleatorio: int = random.randint(1, 100)

while True:
    chute: int = int(input("Escolha um número: "))

    if chute > numero_aleatorio:
        print("O número é menor.")
    elif chute < numero_aleatorio:
        print("O número é maior.")
    else:
        print(f"Ganhoou! O número era: {numero_aleatorio}")
        break
