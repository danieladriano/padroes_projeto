import java.time.*;
import java.util.ArrayList;

public class Venda{
    private LocalTime hora;
    private LocalDate data;
    private ArrayList<ItemVenda> itensVenda;

    public Venda(){ 
        this.data = java.time.LocalDate.now();
        this.hora = java.time.LocalTime.now();
        this.itensVenda = new ArrayList<>();
    }

    public void criarItemVenda(int quantidade, Produto produto){
        this.itensVenda.add(new ItemVenda(quantidade, produto));
    }

    public float total(){
        float total = 0;
        for (ItemVenda item: this.itensVenda){
            total += item.subtotal();
        }
        return total;
    }

    public String dataHora(){
        return this.data + " às " + this.hora;
    }
}