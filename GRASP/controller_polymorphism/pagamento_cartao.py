from pagamento import Pagamento


class PagamentoCartao(Pagamento):
    _limite = 100

    def autorizar(self, valor_recebido):
        if self._valor_divida > self._limite:
            print("Operação não autorizada")
        else:
            print(f"Pagamento por cartão R${valor_recebido}")
