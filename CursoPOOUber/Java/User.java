package CursoPOOUber.Java;

public class User extends Account{
    int id;
    public User(String name, String document, int id){
        super(name,document);
        this.id= id;
    }
    
}