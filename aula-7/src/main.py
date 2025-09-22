class Pessoa:
    __nome: str  # atributo privado
    __email: str  # atributo protegido
    __idade: int   # atributo público

    # get e set
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome


def main() -> None:
    pessoa = Pessoa()
    pessoa.set_nome("Marcos")
    print(pessoa.get_nome())


if __name__ == '__main__':
    main()
