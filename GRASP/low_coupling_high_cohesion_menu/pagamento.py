class Pagamento():
    def __init__(self, valor):
        self._valor_divida = valor

    def registrar_pagamento(self, valor_recebido):
        if self._valor_divida == valor_recebido:
            print(f"Pago o valor total da venda R${valor_recebido}")
            return True
        elif self._valor_divida < valor_recebido:
            print(f"Pago o valor total da venda R${self._valor_divida}")
            print(f"Troco de {valor_recebido - self._valor_divida}")
            return True
        else:
            print(f"Faltam R${self._valor_divida - valor_recebido}")
            return False
