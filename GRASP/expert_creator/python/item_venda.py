class ItemVenda():
    def __init__(self, quantidade, produto):
        self._quantidade = quantidade
        self._produto = produto

    def subtotal(self):
        return self._produto.get_preco() * self._quantidade
