class Paypal extends Payment {
    constructor(id,email){ //Constructor
        super(id);//Herencia
        this.email=email;
    }
}