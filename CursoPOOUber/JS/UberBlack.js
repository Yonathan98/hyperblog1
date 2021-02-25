class UberBlack extends car {
    constructor(license, driver, typeCarAccepted, seatsMaterial){ // metodo de contructor
        super(license, driver) //herencia de la clase car.js
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}