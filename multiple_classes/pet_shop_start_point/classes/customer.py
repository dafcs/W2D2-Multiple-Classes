
class Customer:
    def __init__(self,customer_name,customer_cash): #constructor function
        self.name = customer_name
        self.cash = customer_cash
        self.pets = []

    def reduce_cash(self,cash_amount):
        self.cash -= cash_amount

    def pet_count(self):
        counter = 0
        for pet in self.pets:
            counter +=1
        return counter 
    
    # return (len(self.pets)) # -> also works

    def add_pet(self,new_pet):
        self.pets.append(new_pet)

    def get_total_value_of_pets(self):
        total_value = 0
        for pet in self.pets:
            total_value += pet.price
        return total_value