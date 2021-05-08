from produto import Produto
from venda import Venda


def main():
    banana = Produto("banana", 4.5, "1234556")
    maca = Produto("maca", 1.5, "1234212")
    mamao = Produto("mamao", 2.0, "488485")
    goiaba = Produto("goiaba", 5.0, "585488656")

    venda = Venda()
    venda.criar_item_venda(2, banana)
    venda.criar_item_venda(3, goiaba)
    print(f"Venda realizada em: {venda.data_hora()}")
    print(f"Total venda R${venda.total()}")

    venda = Venda()
    venda.criar_item_venda(1, mamao)
    venda.criar_item_venda(5, maca)
    print(f"Venda realizada em: {venda.data_hora()}")
    print(f"Total venda R${venda.total()}")

if __name__ == "__main__":
    main()
