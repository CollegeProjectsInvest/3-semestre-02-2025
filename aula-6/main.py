from classe_pai import ClassePai


class ClasseMae:
    def __init__(self):
        # método super, chama o construtor da Classe Pai
        super().__init__()


    def imprimir_mae(self):
        print("Hello mãe")


# permite múltiplas heranças
class ClasseFilha(ClassePai, ClasseMae):
    pass


classe_filha = ClasseFilha()
classe_filha.imprimir_pai()
classe_filha.imprimir_mae()
