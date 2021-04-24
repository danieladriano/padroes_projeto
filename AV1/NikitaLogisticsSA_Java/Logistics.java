public class Logistics{
    public float planDelivery(float distance){
        Transport transport = getTransport();
        return transport.deliver(distance);
    }

    public Transport getTransport(){
        return null;
    }
}