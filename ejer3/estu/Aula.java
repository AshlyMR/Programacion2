package ejer3.estu;

public class Aula {
    public String nombredelaula;
    public int pisoenelqueseencuentra;
    public String[][] estudiante;
    public Aula(String nombredelaula, int piso, String[][] estudiantes){
        this.nombredelaula = nombredelaula;
        this.pisoenelqueseencuentra = piso;
        this.estudiante = estudiantes;
    }
    public void mostrardatos(){
        System.out.println("Aula: " + nombredelaula);
        System.out.println("Piso: " + pisoenelqueseencuentra);
        System.out.println("Estudiante y notas: ");
    
        for(int i = 0; i < estudiante.length; i++){
        System.out.println(estudiante[i][0]+ "-"+ estudiante[i][1]);
    }
    }
    public void mostrarDatos(int x){
        for(int i = 0; i< estudiante.length; i++){
            int nota = Integer.parseInt(estudiante[i][1]);
            
            if(nota >= 51){
                System.out.println(estudiante[i][0]+"-APROBADO");
            }else{
                System.out.println(estudiante[i][0]+"-REPROBADO");
            }
        }
    }
    public static void main(String[] args) {
        String[][] datos = {
            {"Maya","98"},
            {"Paya","56"}
        };

        Aula aula1 = new Aula("Aula 101", 2, datos);

        System.out.println("DATOS DEL AULA");
        aula1.mostrardatos();

        System.out.println("\nESTADO DE ESTUDIANTES");
        aula1.mostrarDatos(0);
    }
    
}
