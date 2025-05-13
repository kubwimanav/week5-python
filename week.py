# Assignment 1: Design Your Own Class with Inheritance
# Creating a Smartphone class hierarchy with attributes, methods, and inheritance

class Smartphone:
    """Base class for all smartphones"""
    
    def __init__(self, brand, model, screen_size, battery_capacity, price):
        """Constructor to initialize smartphone attributes"""
        self.brand = brand
        self.model = model
        self.screen_size = screen_size  # in inches
        self.battery_capacity = battery_capacity  # in mAh
        self.price = price
        self.is_powered_on = False
        self._apps = []  # Encapsulated list of installed apps
    
    def power_toggle(self):
        """Toggle power state of the smartphone"""
        self.is_powered_on = not self.is_powered_on
        if self.is_powered_on:
            return f"{self.brand} {self.model} is now powered on."
        else:
            return f"{self.brand} {self.model} is now powered off."
    
    def install_app(self, app_name):
        """Install a new app on the smartphone"""
        if app_name not in self._apps:
            self._apps.append(app_name)
            return f"{app_name} has been installed on {self.brand} {self.model}."
        else:
            return f"{app_name} is already installed on {self.brand} {self.model}."
    
    def list_apps(self):
        """List all installed apps"""
        if not self._apps:
            return f"No apps installed on {self.brand} {self.model}."
        return f"Apps installed on {self.brand} {self.model}: {', '.join(self._apps)}"
    
    def make_call(self, number):
        """Make a phone call"""
        if self.is_powered_on:
            return f"Calling {number} from {self.brand} {self.model}..."
        else:
            return f"Cannot make call. {self.brand} {self.model} is powered off."
    
    def get_specs(self):
        """Return the specifications of the smartphone"""
        return {
            "Brand": self.brand,
            "Model": self.model,
            "Screen Size": f"{self.screen_size} inches",
            "Battery": f"{self.battery_capacity} mAh",
            "Price": f"${self.price}"
        }


class AndroidPhone(Smartphone):
    """Derived class for Android smartphones"""
    
    def __init__(self, brand, model, screen_size, battery_capacity, price, android_version):
        # Call the parent class constructor
        super().__init__(brand, model, screen_size, battery_capacity, price)
        self.android_version = android_version
        self.google_services = True
    
    def get_specs(self):
        """Override parent method to include Android-specific details"""
        specs = super().get_specs()
        specs["OS"] = f"Android {self.android_version}"
        specs["Google Services"] = "Enabled" if self.google_services else "Disabled"
        return specs
    
    def enable_developer_mode(self):
        """Android-specific method to enable developer mode"""
        return f"Developer mode enabled on {self.brand} {self.model} running Android {self.android_version}."


class IPhone(Smartphone):
    """Derived class for iPhones"""
    
    def __init__(self, model, screen_size, battery_capacity, price, ios_version):
        # For iPhones, brand is always "Apple"
        super().__init__("Apple", model, screen_size, battery_capacity, price)
        self.ios_version = ios_version
    
    def get_specs(self):
        """Override parent method to include iPhone-specific details"""
        specs = super().get_specs()
        specs["OS"] = f"iOS {self.ios_version}"
        return specs
    
    def activate_siri(self):
        """iPhone-specific method to activate Siri"""
        if self.is_powered_on:
            return "Hey Siri, how can I help you?"
        else:
            return f"Cannot activate Siri. {self.brand} {self.model} is powered off."


# Activity 2: Polymorphism Challenge
# Creating vehicle classes with the same method name but different implementations

class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def move(self):
        """Base movement method to be overridden by child classes"""
        return "The vehicle is moving."
    
    def get_info(self):
        """Return basic information about the vehicle"""
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """Car class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    
    def move(self):
        """Override move method for cars"""
        return f"Driving the {self.get_info()} on the road. 🚗"
    
    def honk(self):
        """Car-specific method"""
        return "Beep beep! 📢"


class Boat(Vehicle):
    """Boat class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, boat_type):
        super().__init__(make, model, year)
        self.boat_type = boat_type
    
    def move(self):
        """Override move method for boats"""
        return f"Sailing the {self.get_info()} across the water. 🚢"
    
    def anchor(self):
        """Boat-specific method"""
        return "Dropping anchor. ⚓"


class Plane(Vehicle):
    """Plane class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.max_altitude = max_altitude  # in feet
    
    def move(self):
        """Override move method for planes"""
        return f"Flying the {self.get_info()} through the air at {self.max_altitude} feet. ✈️"
    
    def land(self):
        """Plane-specific method"""
        return "Preparing for landing. 🛬"


# Demonstrate the classes

def demonstrate_smartphones():
    print("===== SMARTPHONE CLASS DEMONSTRATION =====")
    
    # Create an Android phone
    pixel = AndroidPhone("Google", "Pixel 7", 6.3, 4355, 599, 13)
    print(f"Created: {pixel.brand} {pixel.model}")
    print(pixel.power_toggle())
    print(pixel.install_app("Gmail"))
    print(pixel.install_app("YouTube"))
    print(pixel.list_apps())
    print(pixel.make_call("555-123-4567"))
    print("Specifications:")
    for key, value in pixel.get_specs().items():
        print(f"  {key}: {value}")
    print(pixel.enable_developer_mode())
    
    print("\n")
    
    # Create an iPhone
    iphone = IPhone("14 Pro", 6.1, 3200, 999, 16)
    print(f"Created: {iphone.brand} {iphone.model}")
    print(iphone.power_toggle())
    print(iphone.install_app("Safari"))
    print(iphone.install_app("Maps"))
    print(iphone.list_apps())
    print("Specifications:")
    for key, value in iphone.get_specs().items():
        print(f"  {key}: {value}")
    print(iphone.activate_siri())
    
    print("\n")


def demonstrate_vehicles():
    print("===== POLYMORPHISM DEMONSTRATION WITH VEHICLES =====")
    
    # Create different vehicle objects
    car = Car("Toyota", "Corolla", 2023, "Hybrid")
    boat = Boat("Bayliner", "Element", 2022, "Speedboat")
    plane = Plane("Boeing", "747", 2020, 35000)
    
    # Store vehicles in a list to demonstrate polymorphism
    vehicles = [car, boat, plane]
    
    # Demonstrate polymorphism by calling the same method on different objects
    for vehicle in vehicles:
        print(f"\nVehicle: {vehicle.get_info()}")
        print(f"Movement: {vehicle.move()}")
        
        # Call type-specific methods
        if isinstance(vehicle, Car):
            print(f"Car action: {vehicle.honk()}")
        elif isinstance(vehicle, Boat):
            print(f"Boat action: {vehicle.anchor()}")
        elif isinstance(vehicle, Plane):
            print(f"Plane action: {vehicle.land()}")


# Run the demonstrations
if __name__ == "__main__":
    demonstrate_smartphones()
    demonstrate_vehicles()