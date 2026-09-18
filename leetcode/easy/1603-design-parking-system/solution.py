class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if not (1 <= carType <= 3):
            return False
            
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False