from produto import Produto
from venda import Venda
from pagamento_dinheiro import PagamentoDinheiro
from pagamento_cartao import PagamentoCartao


produtos = []


class ProdutosController():
    def registrar_produto(self, produto):
        produtos.append(produto)

    def buscar_produtos(self):
        return produtos

class VendasController():
    def registrar_nova_venda(self):
        self._venda = Venda()

    def adicionar_item_venda(self, produto, qtd):
        self._venda.criar_item_venda(qtd, produto)
    
    def buscar_total_venda(self):
        return self._venda.total()

    def buscar_venda(self):
        return self._venda

class PagamentoController():
    def registrar_pagamento(self, venda, pagamento, valor_recebido):
        venda.pagar(pagamento, valor_recebido)


def main():
    # Inserir em estoque
    estoque = ProdutosController()
    estoque.registrar_produto(Produto("Banana", 4.5, "123123123"))
    estoque.registrar_produto(Produto("Maca", 2.5, "213123123123"))
    estoque.registrar_produto(Produto("Mamao", 3.0, "12344253413"))

    _produtos = estoque.buscar_produtos()

    while True:
        print("--------------------")
        print("1 - Registrar venda")
        print("0 - Sair")
        opcao = int(input("Opcao: "))
        print("--------------------")

        if opcao == 0:
            break

        # Iniciar nova venda
        venda_controller = VendasController()
        venda_controller.registrar_nova_venda()

        while True:
            # Listar produtos
            for i, produto in enumerate(_produtos):
                print(f"{i + 1} - {produto.get_descricao()}")
            print(f"Para finalizar digite 0 (zero)")
            opcao_prod = int(input("Selecione o produto: "))

            if opcao_prod == 0:
                break

            quantidade = int(input("Informe a quantidade: "))
            venda_controller.adicionar_item_venda(_produtos[opcao_prod - 1], quantidade)

        print("======================================")
        print(f"Valor total R${venda_controller.buscar_total_venda()}")
        while True:
            print(f"1 - Dinheiro")
            print(f"2 - Cartao")
            op = int(input("Opcao: "))
            if op == 1:
                valor_recebido = float(input("Valor recebido R$: "))
                tipo_pagamento = PagamentoDinheiro(venda_controller.buscar_total_venda())
            elif op == 2:
                valor_recebido = venda_controller.buscar_total_venda()
                tipo_pagamento = PagamentoCartao(venda_controller.buscar_total_venda())

            pagamento = PagamentoController()
            pagamento.registrar_pagamento(venda_controller.buscar_venda(), tipo_pagamento, valor_recebido)
            break
        print("======================================")

        print("--------------------")

if __name__ == "__main__":
    main()
