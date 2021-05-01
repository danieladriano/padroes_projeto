public class Navigator{
    private RouteStrategy routeStrategy;

    public void setRouteStrategy(RouteStrategy strategy){
        this.routeStrategy = strategy;
    }

    public void buildRoute(String pointA, String pointB){
        this.routeStrategy.buildRoute(pointA, pointB);
    }
}