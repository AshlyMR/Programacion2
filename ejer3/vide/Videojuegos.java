package ejer3.vide;
import java.util.Scanner;

public class Videojuegos {
    public String nombre;
    public String plataforma;
    public int cantidadDeJugadores;
    public Videojuegos(String nombre, String plataforma  ){
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadDeJugadores = 0;
    }
    public Videojuegos(String nombre, String plataforma, int Masjugadores){
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadDeJugadores = Masjugadores;
    }
    public void agregaJugadores(){
        this.cantidadDeJugadores = this.cantidadDeJugadores +1;
    }
    public void agregarJugadores(int cantJugadoresporT){
        this.cantidadDeJugadores = this.cantidadDeJugadores + cantJugadoresporT;
    }
    @Override
    public String toString(){
        return "videojuegos [ nombre=" + nombre + ",plataforma=" + plataforma + ", jugadores=" + cantidadDeJugadores +"]";
    }
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        Videojuegos juego1 = new Videojuegos("Dota","LAPTOP",5);
        Videojuegos juego2 = new Videojuegos("wii","consola",6);
        
        juego1.agregaJugadores();    
        
        System.out.println(juego1);
        System.out.print("Ingrese cantidad de jugadores a agregar por teclado: ");
        int n = teclado.nextInt();

        juego2.agregarJugadores(n);

        // mostrar resultados
        System.out.println(juego1);
        System.out.println(juego2);
        
    }
    
}
