class Car():
    no_of_wheels=4
    
    def __init__(self,colour,make,year):
        self.colour=colour
        self.make=make
        self.year=year
    def drive(self,acceleration):
        print("You cant drive this car...")
        pass
    def am(self):
        pass
    
myCar= Car("white","Toyota",2012)
myCar2= Car("Yellow","mazda",2014)
print(myCar.no_of_wheels, " ",myCar.year," ",myCar2.make, " \n")

print(myCar2.no_of_wheels, " ",myCar2.colour, " \n")

myCar2.drive(45)

myCar.no_of_wheels=12
myCar2.no_of_wheels=7
print(myCar.no_of_wheels, " ",myCar.year," ",myCar2.make, " \n")

print(myCar2.no_of_wheels, " ",myCar2.colour, " \n")

myCar2.drive(45)
