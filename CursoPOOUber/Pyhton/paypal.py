from payment import Payment

class paypal(Payment):
    email = str
    def__init__(self,id, email): #Constructor
        super().__init__(id) #Herencia
        self.email = email
        