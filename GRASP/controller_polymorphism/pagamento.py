class Pagamento():
    def __init__(self, valor):
        self._valor_divida = valor

    def autorizar(self, valor_recebido):
        raise Exception("Tipo de pagamento não permitido")
