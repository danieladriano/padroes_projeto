public class Produto{
    private String descricao;
    private float preco;
    private String upc;

    public Produto(String descricao, float preco, String upc) {
        this.descricao = descricao;
        this.preco = preco;
        this.upc = upc;
    }

    public float getPreco()   {
        return this.preco;
    }
}