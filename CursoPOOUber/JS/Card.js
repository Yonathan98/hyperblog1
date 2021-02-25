class Card extends Payment {
    constructor(id,number, cvv,date){ //Constructor
        super(id);//Herencia
        this.number=number;
        this.cvv=cvv;
        this.date=date;
    }
}