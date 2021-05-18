from produto import Produto
from venda import Venda

class Post():
    def registrar_produtos(self):
        banana = Produto("banana", 4.5, "1234556")
        maca = Produto("maca", 1.5, "1234212")
        mamao = Produto("mamao", 2.0, "488485")
        goiaba = Produto("goiaba", 5.0, "585488656")
        self._produtos = [banana, maca, mamao, goiaba]

    def buscar_produtos(self):
        return self._produtos
    
    def registrar_nova_venda(self):
        self._venda = Venda()
    
    def adicionar_produto(self, produto, qtd):
        self._venda.criar_item_venda(qtd, produto)

    def buscar_total_venda(self):
        return self._venda.total()

    def registrar_pagamento(self, valor):
        print(f"Venda realizada em: {self._venda.data_hora()}")
        print(f"Total venda R${self._venda.total()}")
        self._venda.registrar_pagamento(valor)


def main():
    post = Post()

    post.registrar_produtos()
    produtos = post.buscar_produtos()
    post.registrar_nova_venda()
    post.adicionar_produto(produtos[0], 2)
    post.adicionar_produto(produtos[1], 3)
    print(f"Total da venda {post.buscar_total_venda()}")
    post.registrar_pagamento(20)

if __name__ == "__main__":
    main()
