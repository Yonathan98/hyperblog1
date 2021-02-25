from payment import Payment

class card(Payment):
    number = str
    cvv = str
    date = str
    def__init__(self,id, number, cvv, date): #Constructor
        super().__init__(id) #Herencia
        self.number = number
        self.cvv = cvv
        self.date = date