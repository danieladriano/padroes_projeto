public class Ship implements Transport{

    private float cost;
    
    public Ship(){
        cost = 10;
    }

    @Override
    public float deliver(float distance){
        toSail(distance);
        return distance * cost;
    }

    private void toSail(float distance){
        System.out.println("Deliver by sea in a container. Distance: " + distance + " Km.");
    }
}