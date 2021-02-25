package CursoPOOUber.Java;
class UberPool extends Car {
    String brand;
    String model;

    public UberPool(String license, Account driver, String brand, String model){
        super(license,driver); // Atributos de la super clase en este caso seria car seria 
        this.brand = brand; // Atributos de la clase uberx
        this.model = model;

    }
}