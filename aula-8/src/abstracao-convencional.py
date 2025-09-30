class Animal:
    def fazer_som(self) -> None:
        print("Animal: Fazendo som")

        # estoura um erro
        raise ValueError("O método deve ser impletado")


class Cachorro(Animal):
    def fazer_som(self) -> None:
        print("Cachorro: Fazendo som")

