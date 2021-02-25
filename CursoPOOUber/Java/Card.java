package CursoPOOUber.Java;


public class Card extends Payment {
    String number;
    int cvv;
    String date;
    public Card(int id, String number, int cvv,String date){
        super(id);
        this.number = number;
        this.cvv = cvv;
        this.date = date;
    }
    
}