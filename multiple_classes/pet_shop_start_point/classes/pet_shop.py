class PetShop:
    def __init__(self,shop_name,pet_list,shop_cash):
        self.name = shop_name
        self.pets = pet_list
        self.total_cash = shop_cash
        self.pets_sold = 0
        
    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self,value):
        self.total_cash += value
    
    def remove_pet(self,pet_remove):
        self.pets.remove(pet_remove)

    def find_pet_by_name(self,pet_name):
            for pet in self.pets:
                 if pet.name == pet_name:
                      return pet

    def sell_pet_to_customer(self,pet_name, customer):
         
        pet = self.find_pet_by_name(pet_name)
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        self.remove_pet(pet)
        customer.add_pet(pet)