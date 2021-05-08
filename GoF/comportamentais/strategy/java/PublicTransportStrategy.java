public class PublicTransportStrategy implements RouteStrategy{
    @Override
    public void buildRoute(String pointA, String pointB){
        System.out.println("Roteiro do " + pointA + " até " + pointB + " utilizando transporte publico!");
    }
}
