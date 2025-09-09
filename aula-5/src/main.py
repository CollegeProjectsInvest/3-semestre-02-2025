# classe
class Pessoa:
    # atributos
    nome: str       # público
    _email: str     # protegido, apenas como descrição
    __idade: int = 10    # privado, apenas como descrição

    # método construtor
    # inicializa a classe
    def __init__(self,
        nome: str,
        email: str,
        idade: int
    ) -> None:
        self.nome = nome
        self._email = email
        self.__idade = idade

    # métodos
    def cadastrar(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Email: {self._email}")
        print(f"Idade: {self.__idade}")


class Animal:
    def __init__(self) -> None:
        self.name = "Cachorro"

    def print_nome(self) -> None:
        print(self.name)


def main() -> None:
    pessoa = Pessoa(
        nome="Marcos",
        email="teste@mail.com",
        idade=10
    )     # Objeto
    pessoa.cadastrar()

    animal: Animal = Animal()
    animal.print_nome()


if __name__ == "__main__":
    main()
