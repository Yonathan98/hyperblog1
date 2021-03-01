from payment import Payment

class cash(Payment):
    def __init__(self,id): #Constructor
        super().__init__(id) #Herencia