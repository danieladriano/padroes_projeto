public class RoadLogistics extends Logistics{
    @Override
    public Transport getTransport(){
        return new Truck();
    }
}