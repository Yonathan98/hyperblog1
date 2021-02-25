package CursoPOOUber.Java;


public class Paypal extends Payment {
    String email;
    public Paypal(int id, String email){
        super(id);
        this.email = email;
        
    }
    
}