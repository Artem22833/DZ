class Human:
  def __init__(self, name):
    self.name = name

class Place:
    def __init__(self, place):
     self.place = place
     self.chair = []
class Auto:
  def __init__(self, brand):
    self.brand = brand
    self.passengers = []
  def add_passenger(self, human):
    self.passengers.append(human)

  def print_passengers(self):
    if self.passengers != []:
      print(f"В машині {self.brand} такі пасажири:")
      for passenger in self.passengers:
        print(passenger.name)
    else:
      print(f"В машині {self.brand} немає пасажирів. Всі втікли!")

car = Auto('Nissan GTR')
car.add_passenger(Human("Oleg"))
car.add_passenger(Human("Igor"))
car.add_passenger(Human("Vlad"))
car.add_passenger(Human("Valentyn"))
class Chair(Place, Auto):
  def add_chair(self, chair):
      self.chair.append(chair)

  def print_place(self):
      if self.chair != []:
       print(f"В машині {self.brand} стільки крісел {self.chair}")
      for chair in self.chair:
            print(chair.name)
      else:
       print(f"В машині {self.brand} немає стіки крісел!Всі не сядуть!")
place = Place()
place.add_chair(Place(4))
place.print_place()
car.print_passengers()




































