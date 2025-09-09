class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self) -> None:
       print(f"Nome: {self.nome}")
       print(f"Idade: {self.idade}")


nome = input("Digite o nome do animal")
idade = int(input("Digite a idade do animal"))
to_to = Animal(nome, idade)
to_to.mostrar_dados()
