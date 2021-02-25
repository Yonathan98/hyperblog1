class UberX extends car {
    constructor(license, driver, brand, model){ // metodo de contructor
        super(license, driver) //herencia de la clase car.js
        this.brand = brand;
        this.model = model;
    }
}