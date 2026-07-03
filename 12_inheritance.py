class vehicle:
    def start(self):
        return("Vehicle is starting")

class Car(vehicle):
    def start(self):
        original=super().start() # extend the parents behaviour without replacing it.
        print (f"{original}\nVehicle is car")

c=Car()
c.start()