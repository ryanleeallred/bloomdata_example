# When Classes inherit from one another.
# We will see a more specific class inheriting functionality form the 
# more generic / general class. 

# The more generic class is called "Parent" class
class Vehicle:
    def __init__(self, color, make, model, mileage=0):
        self.color = color
        self.make = make
        self.model = model
        self.mileage = mileage

    def honk(self):
        return 'HOOOOOOOOONK!'
    
    def drive(self, miles_driven):
        # self.mileage = self.mileage + miles_driven
        self.mileage += miles_driven 
        return self.mileage


# the more specific class is called "Child" class
class Car(Vehicle):
    # Static Attribute
    # this attribute can't be changed through the constructor
    num_wheels = 4

    def __init__(self, 
                color, 
                make, 
                model, 
                style, 
                transmission='manual', 
                mileage=0):
        # "super" refers to the parent class
        # inherit attributes from the parent class
        super().__init__(color, make, model, mileage)
        self.style = style
        self.transmission = transmission

    def __repr__(self):
        return f"<A {self.color} {self.make} {self.model} with {self.mileage} miles>"

    # Methods get inherited automatically

if __name__ == "__main__":
    ryan_car = Car('gray', 'toyota', 'camry', 'sedan')
    # print(ryan_car.num_wheels)
    # ryan_car.num_wheels = 3
    print(ryan_car.num_wheels)
    print(ryan_car.honk())
    print(ryan_car.style)
    print(ryan_car.mileage)
    print(ryan_car.transmission)