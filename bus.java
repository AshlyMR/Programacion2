public class bus {
    private int capacidadTotal;
    private int pasajeros;
    private double precioPasaje;
    
    public bus(int capacidadTotal){
        this.capacidadTotal = capacidadTotal;
        this.pasajeros= 0;
        this.precioPasaje =1.50;
    }
    public void subirPasajeros(int x){
        if(pasajeros + x <= capacidadTotal){
            pasajeros = pasajeros + x;
        } else {
            System.out.println("NO HAY ASIENTOS");
        }
    }
    public double cobrarPasaje(){
    return pasajeros * precioPasaje;
    }
    public int asientosDisponibles(){
        return capacidadTotal - pasajeros;
    }
    public int getCapacidadTotal(){
         return capacidadTotal;
    }
    public int getPasajeros() {
        return pasajeros;
    }

    public double getPrecioPasaje() {
        return precioPasaje;
    }


    @Override
    public String toString() {
        return "Capacidad: " + capacidadTotal +", Pasajeros: " + pasajeros +", Precio pasaje: " + precioPasaje;
    }
    


public static void main(String[] args) {
        bus b1 = new bus(40);
        b1.subirPasajeros(15);
        System.out.println(b1);
        System.out.println("Asientos disponibles: " + b1.asientosDisponibles());
        System.out.println("Total recaudado: " + b1.cobrarPasaje());

    }
}
