public class Truck implements Transport{

    private float cost;
    
    public Truck(){
        cost = 10;
    }

    @Override
    public float deliver(float distance){
        toDrive(distance);
        return distance * cost;
    }

    private void toDrive(float distance){
        System.out.println("Deliver by roads in a box. Distance: " + distance + " Km.");
    }
}