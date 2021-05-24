class Produto():
    def __init__(self, descricao, preco, upc):
        self._descricao = descricao
        self._preco = preco
        self._upc = upc

    def get_preco(self):
        return self._preco

    def get_descricao(self):
        return self._descricao