# Classe Pessoa
class Pessoa:
    # Atributos
    nome: str
    cpf: str
    idade: int
    endereco = "Av. asdasda"

    # Métodos
    # método sem retorno
    def cadastrar(self) -> None:
        print(self.endereco)

    # método retorna uma string
    def retorna_name(self) -> str:
        return self.nome

    # método com parâmetro
    def funcao_parametro(self, nome: str, idade: int):
        print(nome)
        print(idade)


# Método main (método principal, ponto de partida)
def main() -> None:
    # Tudo aqui dentro será executado
    print("Hello")

    # Objeto
    pessoa = Pessoa()
    pessoa.cadastrar()


if __name__ == "__main__":
    main()
