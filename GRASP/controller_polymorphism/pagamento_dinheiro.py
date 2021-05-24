from pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def autorizar(self, valor_recebido):
        if self._valor_divida == valor_recebido:
            print(f"Pago o valor total da venda R${valor_recebido}")
        elif self._valor_divida < valor_recebido:
            print(f"Pago o valor total da venda R${self._valor_divida}")
            print(f"Troco de {valor_recebido - self._valor_divida}")
        else:
            print(f"Faltam R${self._valor_divida - valor_recebido}")
