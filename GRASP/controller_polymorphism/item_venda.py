class ItemVenda():
    def __init__(self, qtd, prod):
        self._quantidade = qtd
        self._produto = prod

    def subtotal(self):
        return self._produto.get_preco() * self._quantidade
