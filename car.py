class Car(object):

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formated descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milege."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

### Creating a subclass
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)

''' 
new_car = Car('McLaren', 'P1', '2013')
print(new_car.get_descriptive_name())
new_car.update_odometer(67)
new_car.read_odometer()
new_car.increment_odometer(100)
new_car.read_odometer()
'''

elec_car = ElectricCar('tesla', 'model s', 2016)
print(elec_car.get_descriptive_name())
