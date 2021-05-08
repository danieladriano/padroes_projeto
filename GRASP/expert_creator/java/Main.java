class Main {
    public static void main(String[] args) {
        Produto banana = new Produto("banana", 4.5f, "1234556");
        Produto maca = new Produto("maca", 1.5f, "1234212");
        Produto mamao = new Produto("mamao", 2.0f, "488485");
        Produto goiaba = new Produto("goiaba", 5.0f, "585488656");

        Venda venda = new Venda();
        venda.criarItemVenda(2, banana);
        venda.criarItemVenda(3, goiaba);
        System.out.println("Venda realizada em " + venda.dataHora());
        System.out.println("Total venda R$" + venda.total());

        venda = new Venda();
        venda.criarItemVenda(1, mamao);
        venda.criarItemVenda(5, maca);
        System.out.println("Venda realizada em " + venda.dataHora());
        System.out.println("Total venda R$" + venda.total());
    }
}