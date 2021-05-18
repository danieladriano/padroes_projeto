from produto import Produto
from venda import Venda


class Post():
    def registrar_produtos(self, produtos):
        self._produtos = produtos

    def buscar_produtos(self):
        return self._produtos

    def registrar_nova_venda(self):
        self._venda = Venda()
    
    def adicionar_produto(self, produto, qtd):
        self._venda.criar_item_venda(qtd, produto)

    def buscar_total_venda(self):
        return self._venda.total()

    def registrar_pagamento(self, valor):
        return self._venda.pagar(valor)

def main():
    post = Post()

    banana = Produto("Banana", 4.5, "123123123")
    maca = Produto("Maca", 2.5, "213123123123")
    mamao = Produto("Mamao", 3.0, "12344253413")
    _produtos = [banana, maca, mamao]

    post.registrar_produtos(_produtos)
    produtos = post.buscar_produtos()

    while True:
        print("--------------------")
        print("1 - Registrar venda")
        print("0 - Sair")
        opcao = int(input("Opcao: "))

        if opcao == 0:
            break

        # Iniciar nova venda
        post.registrar_nova_venda()

        while True:
            # Listar produtos
            for i, produto in enumerate(produtos):
                print(f"{i + 1} - {produto.get_descricao()}")
            print(f"Para finalizar digite 0 (zero)")
            opcao_prod = int(input("Selecione o produto: "))

            if opcao_prod == 0:
                break

            quantidade = int(input("Informe a quantidade: "))
            post.adicionar_produto(produtos[opcao_prod - 1], quantidade)

        print("======================================")
        print(f"Valor total R${post.buscar_total_venda()}")
        while True:
            valor_recebido = float(input("Valor recebido R$: "))
            if post.registrar_pagamento(valor_recebido):
                break
        print("======================================")

        print("--------------------")

if __name__ == "__main__":
    main()
