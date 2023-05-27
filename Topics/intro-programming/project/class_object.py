class Car:
    
    def __init__(self, co, m, y, mi, sp):
        self.color = co
        self.make = m
        self.year = y
        self.milage = mi
        self.speed = sp
        
    def accelerate(self, mile_per_hour):
        self.speed = self.speed + mile_per_hour


    def brake(self, mile_per_hour):
         self.speed = self.speed - mile_per_hour


    def read_milage(self):
        print(f"the current milage is: {self.milage}")


    def change_color(self, new_color):
        self.color = new_color

        return self.color

    def display_information(self):
        information_dict = {"Color":self.color, "Make": self.make, "Year": self.year, "Milage": self.milage, "Speed": self.speed}
        return information_dict









    
    
ford_object = Car("Blue", "Ford", 2016, 4000, 0)
jeep_object = Car("Silver", "Jeep", 2009, 20000, 0)

print(ford_object.display_information())
ford_object.accelerate(10)
print(ford_object.display_information())

ford_object.brake(5)
print(ford_object.display_information())

print(jeep_object.display_information())



