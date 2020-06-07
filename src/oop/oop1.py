# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass 
# base class

class FlightVehicle(Vehicle):
    pass
# inherits from Vehicle - child of Vehicle

class Starship(FlightVehicle):
    pass
# inherits from FlighVehicle, indirectly inherits from Vehicle - child of FlighVehicle, grandchild of Vehicle

class GroundVehicle(Vehicle):
    pass
# inherits from Vehicle - child of Vehicle 

class Car(GroundVehicle):
    pass 
# inherits from GroundVehicle, indirectly inherits from Vehicle - child of GroundVehicle, grandchild of Vehicle

class Motorcycle(GroundVehicle):
    pass
# inherits from GroundVehicle, indirectly inherits from Vehicle - child of GroundVehicle, grandchild of Vehicle

class Airplane(FlightVehicle):
    pass
# inherits from FlightVehicle, indirectly inherits from Vehicle - child of FlightVehicle, grandchild of Vehicle