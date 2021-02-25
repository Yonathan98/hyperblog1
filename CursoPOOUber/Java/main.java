package CursoPOOUber.Java;

class main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        UberX uberX = new UberX("AMQ123",new Account ("Andres Herrera", "And123"), "Chevrolet", "Sonic ");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGH345", new Account ("Andres Herrera", "And123"));
        uberX.setPassenger(6);
        uberX.printDataCar();
     
    }
    
}
