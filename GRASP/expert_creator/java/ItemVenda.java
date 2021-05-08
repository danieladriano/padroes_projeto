public class ItemVenda{
    private int quantidade;
    private Produto produto;

    public ItemVenda(int quantidade, Produto produto){
        this.quantidade = quantidade;
        this.produto = produto;
    }

    public float subtotal(){
        return this.produto.getPreco() * this.quantidade;
    }
}