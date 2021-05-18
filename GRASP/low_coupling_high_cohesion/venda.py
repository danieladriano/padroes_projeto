from item_venda import ItemVenda
from pagamento import Pagamento
from datetime import date
from datetime import datetime


class Venda():
    def __init__(self):
        self._data = date.today().strftime("%d/%m/%Y")
        self._hora = datetime.now().strftime("%H:%M:%S")
        self._itens_venda = []

    def criar_item_venda(self, qtd, produto):
        self._itens_venda.append(ItemVenda(qtd, produto))

    def total(self):
        total = 0
        for item_venda in self._itens_venda:
            total += item_venda.subtotal()
        return total

    def data_hora(self):
        return f"{self._data} às {self._hora}"

    def registrar_pagamento(self, valor):
        pagamento = Pagamento(self.total())
        pagamento.registrar_pagamento(valor)
