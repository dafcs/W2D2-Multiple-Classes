class Bus:
    def __init__(self,bus_number,end_station):
        self.route_number = bus_number
        self.destination = end_station
        self.passengers = []
    
    def drive(self):
        return "Brum brum"

    def pick_up(self,passenger):
        self.passengers.append(passenger)

    def passenger_count(self):
        return len(self.passengers)

    def drop_off(self,passenger):
        self.passengers.remove(passenger)

    def empty_bus(self):
        self.passengers.clear()
    
    def pick_up_from_stop(self,bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)

        