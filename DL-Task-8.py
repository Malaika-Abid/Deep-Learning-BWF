# Classes in Pyhton
class person():
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is "+self.name)
        print("I am "+str(self.age)+" years old")
    def edu(self):
        print(self.name +" is a Software engineer")

a=person('Sam', 12)
a.info()
a.edu()
a=person('Huma', 16)
a.info()
a.edu()

#TRY IT YOURSELF
class Resturant():
        def __init__(self, name, cuisine):
            self.name=name
            self.cuisine=cuisine
        def describe_restautrant(self):
            print("Welcome to "+ self.name+" !")
            print("Would you like to try our "+self.cuisine)
        def open(self):
            print(self.name+" is opened.")
ins=Resturant('Koffee net', 'french cuisine'   )
ins.open()
ins.describe_restautrant()
#creating instances of above class
ins =Resturant('Monal', 'japanese')
ins.describe_restautrant()
ins=Resturant('ABC', "ashdiuh")
ins.describe_restautrant()

#TRY IT YOURSELF
class user():
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print("Hi! I am "+ self.first_name +" " +self.last_name)
    def greet(self):
        print("Welcome "+ self.first_name +" "+ self.last_name)
    
ex=user('Hina', 'Khan')
ex.describe_user()
ex.greet()
ex=user("Sara", "ALi")
ex.describe_user()
ex.greet()
ex= user('Faiza', "akbar")
ex.describe_user()
ex.greet()

#Inheritance In classes
#TRY IT YOURSELF 9-6
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor)

# Example usage
my_ice_cream_stand = IceCreamStand("Scoops")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()

#TRY IT YOURSELF 9-7
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} ({self.email})")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

class Admin(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print("- " + privilege)

# Example usage
my_admin = Admin("Malaika", "Abid", "MalaikaAbid@gmail.com", "password123")
my_admin.describe_user()
my_admin.show_privileges()

#TRY IT YOURSELF 9-8
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} ({self.email})")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.privileges = Privileges()

# Example usage
my_admin = Admin("Malaika", "Abid", "MalaikaAbid@gmail.com", "password123")
my_admin.describe_user()
my_admin.privileges.show_privileges()

#TRY IT YOURSELF 9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 85:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# Example usage
my_electric_car = ElectricCar("Tesla", "Model S", 2022)
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()

