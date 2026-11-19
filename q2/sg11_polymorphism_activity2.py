# NUMBER 1.
"""
a. What is duck typing, as explained in the video?

Duck typing is another way aside from inheritance in achieving polymorphism. 
The objects must have minimum necessary methods or attributes to be used. 
It is based on the concept of "If it looks like a duck and quacks like a duck, then it must be a duck."
So, if an object has necessary methods/ attributes, then it can be used in a similar way as another object, regardless of inheritance.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

To make it work inside the same loop as Dog and Cat, the Car class must have the same exact method name as of the two classes, which is speak(). 
Thus, the car class needed to change its horn() method to speak() method, so it can be used in the same loop.

"""

# NUMBER 2. 

# Creating 3 classes, Car, Boat, and Drone. And each has a method called move(), describing how they move.  
class Car:
  def move(self):
    print("The car drives on the road.")

class Boat:
  def move(self):
    print("The boat sails on the water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

# Creating a function named start_trip(), taking in a vehicle object as an argument, then the move() method is called on the vehicle object.
def start_trip(vehicle):
    vehicle.move()

# Creates one object of each class
car = Car()
boat = Boat()
drone = Drone()

# Calls start_trip() method on per vehicle object  
start_trip(car)
start_trip(boat)
start_trip(drone)



# NUMBER 3.
""" 
3. How does the code in 2.2 demonstrate polymorphism?

Just because it doesn't apply inheritance doesn't mean polymorphism cannot be achieved. 
In the code, to apply polymorphism, we must have the same method name, which is move() in all the classes. 
Afterwards, the start_trip() function is created, taking in a vehicle object, then calls their own individual move() method.
 We can achieve polymorphism by duck typing, which is exhibited in this code.

"""

