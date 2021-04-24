class App {
    private Logistics logistics;

    public App(Logistics logi){
        logistics = logi;
    }

    public void run(float distance){
        float cost = logistics.planDelivery(distance);
        System.out.println("Transport cost $" + cost);
    }
}

class Main {
  public static void main(String[] args) {
    RoadLogistics road = new RoadLogistics();
    App app = new App(road);
    app.run(500);

    System.out.println("--------------------");

    SeaLogistics sea = new SeaLogistics();
    app = new App(sea);
    app.run(5000);
  }
}