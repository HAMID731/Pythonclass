from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Car going")
    def stop(self):
        print("Car stopped")

car = Car()
car.go()
car.stop()