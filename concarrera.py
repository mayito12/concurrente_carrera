import threading
import time
import random

class Parking():
    def __init__(self, cont=0, cont2=0, parkingCar=0, parkingTruck=0):
        self.locked = threading.Lock()
        self.conta1 = cont
        self.conta2 = cont2
        self.place1 = parkingCar
        self.place2 = parkingTruck

    def carParking(self, car):
        self.locked.acquire()
        try:
            self.place1 += car
            self.conta1 += 1
            print(f"Carro{self.conta1} entro en el parking - {self.place1} \n Cupo de camiones en espera")
        finally:
            self.locked.release()

    def truckParking(self, truck):
        self.locked.acquire()
        try:
            self.place2 += truck
            self.conta1 += 1
            print(f"Camion{self.conta1} entro en el parking - {self.place2} \n Cupo de carros en espera")
        finally:
            self.locked.release()

def entry(parking):
    for i in range(2):
        car = 0
        car = random.randint(1,2)
        time.sleep(1)
        parking.carParking(car)
        car = random.randint(1,2)
        parking.truckParking(car)

    # for i in range(2):
    #     truck = 0
    #     truck = random.randint(1,2)
    #     time.sleep(1)
    #     parking.truckParking(truck)


if __name__ == "__main__":
    parking = Parking()
    for y in range (3):
        client1 = threading.Thread(target=entry, args=(parking,))
        client1.start()