import java.util.Scanner;

class Main {
  public static void main(String[] args) {

    Navigator navigator = new Navigator();
   
    Scanner sc= new Scanner(System.in);
    System.out.print("1 - Carro\n");
    System.out.print("2 - Transporte publico\n");
    String opcao = sc.nextLine();
    
    RouteStrategy strategy;

    if (Integer.parseInt(opcao) == 1) {
        strategy = new RoadStrategy();
    } else {
        strategy = new PublicTransportStrategy();
    }

    navigator.setRouteStrategy(strategy);
    navigator.buildRoute("Beira-mar", "Estacio");
  }
}