package CursoPOOUber.Java;
import java.util.ArrayList;
import java.util.Map;
class UberBlack extends Car {
    Map<String, Map<String,Integer>>typeCarAccepted;
    ArrayList<String> seatsMaterial;
    public UberBlack(String license, Account driver, Map<String, 
    Map<String,Integer>>typeCarAccepted, ArrayList<String> seatsMaterial ){
        super(license,driver); // Atributos de la super clase en este caso seria car seria 
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;

    }
    
}
