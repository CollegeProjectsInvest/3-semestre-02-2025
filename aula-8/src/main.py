from abc import ABC, abstractmethod


# Class abstrata
class Animal(ABC):
    @abstractmethod
    def fazer_som(self) -> None:
        pass


class Cachorro(Animal):
    def fazer_som(self) -> None:
        print("Cachorro: fazendo som")


def main() -> None:
    cachorro = Cachorro()
    cachorro.fazer_som()


if __name__ == '__main__':
    main()
