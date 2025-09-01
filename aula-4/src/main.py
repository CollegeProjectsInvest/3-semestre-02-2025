# lista: list = [1, True, "Teste", 2, 2.0]
# numeros: list[int] = [1, 2, 3, 4]

# numeros.append(5)
# numeros.insert(0, -1)
# numeros.remove(-1)
# # numeros.clear()

# print(numeros[2])

# from typing import Tuple

# coordenadas: Tuple[int, int, int] = (10, 100, 1001)
# print(coordenadas[0])

# a: set[int] = {1, 2, 3}
# b: set[int] = {3, 4, 5}

# print(a | b)
# print(a & b)
# print(a - b)

# pessoa = {
#     "nome": "Marcos",
#     "email": "marcos@mail.com",
#     "idade": 23 + 1
# }
# print(pessoa["nome"])
# pessoa["cidade"] = "Cuiabá"
# print(pessoa)

# database_user = [
#     { "id": "1", "nome": "Marcos" },
#     { "id": "2", "nome": "Marcos" },
#     { "id": "3", "nome": "Marcos" }
# ]

# for user in database_user:
#     if user["id"] == "1":
#         print("O primeiro")

# def ola_mundo(*numeros: int) -> None:
#     print(sum(numeros))

# ola_mundo(1, 2, 3, 4, 5, 10, 2, 3, 4123, 4123)

def soma(*numeros: int) -> int:
    return sum(numeros)
