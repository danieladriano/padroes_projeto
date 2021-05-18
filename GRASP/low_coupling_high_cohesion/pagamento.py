class Pagamento():
    def __init__(self, valor: float) -> None:
        self._valor = valor

    def registrar_pagamento(self, recebido: float):
        if self._valor == recebido:
            print(f"Pago valor integral R${recebido}")
        if self._valor < recebido:
            print(f"Troco {recebido - self._valor}")
        else:
            print(f"Falta R$ {self._valor - recebido}")
