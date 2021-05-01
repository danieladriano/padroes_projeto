public class RoadStrategy implements RouteStrategy{
    @Override
    public void buildRoute(String pointA, String pointB){
        System.out.println("Roteiro do " + pointA + " até " + pointB + " utilizando carro!");
    }
}
