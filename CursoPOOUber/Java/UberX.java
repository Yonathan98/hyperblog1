package CursoPOOUber.Java;
class UberX extends Car {
    String brand;
    String model;

    public UberX(String license, Account driver, String brand, String model){
        super(license,driver); // Atributos de la super clase en este caso seria car seria 
        this.brand = brand; // Atributos de la clase uberx
        this.model = model;

    }
    @Override
    void printDataCar() {
        // TODO Auto-generated method stub
        super.printDataCar();
        System.out.println("Modelo: " + model + "Marca: " + brand );
    }
}