from audioop import add
from email.headerregistry import Address
from enum import Enum
from msilib.schema import Class
from os import stat
from re import L
from tkinter.messagebox import RETRY

#Hood area
class Hood(Enum):
    def __init__(self) -> None:
        super().__init__()
    REGULAR, SPORTS, LIFTED, NONE = 499.00, 599.00, 699.00, 0.00
    Enum Color = "Red", "Blue", "Black", "Silver", "Green", "Yellow"
    #Hood type price Regular=$499.00, Sports=$599.00, Lifted=$699.00, None=$0.00
    getHoodPrice()
    Enum  getHoodColor()
    setHoodColor(Enum Color) 
    Enum getHoodType()
    setHoodType(Enum)
    String toString()
    {
        # Print the contents of the class as per requirement in the results listed at the bottom
    }

#Fender
class Fender:
    Enum FenderType = Regular, Sports, Carbon Fiber
    Color enum color choices (Red, Blue, Black, Silver, Green, Yellow)
    Price for Items: Regular = $100.00, Sports = $200.00, Carbon Fiber = $1000.00
    float getFenderPrice()
    Enum  getFenderColor()
    setFenderColor(enum Color)
    Enum getFenderType()
    setFenderType(Enum )
    String toString()
    {
        #Print the contents of the class as per requirement in the results     listed at the bottom
    }

#Doors
class Door:
    Color Enum color choices (Red, Blue, Black, Silver, Green, Yellow)
    Price $599.00
    enum  getDoorColor()
    setDoorColor(enum Color)
    String toString()
    {
        #Print the contents of the class as per requirement in the results listed at the bottom
    }

#Wheelset
    class Wheelset:
    Wheelset constructor should take all as parameters
    Enum WheelsetType = Support all listed models listed in the drawing provided above
    WheelsetType price All supported are for $1299.00, and no cost if not selected=$0.00
    float getWheelsetPrice()
    enum getWheelsetType()
    setWheelsetType(enum )
    String toString()
    {
        #Print the contents of the class as per requirement in the results listed at the bottom
    }

#Vehicle
##Vehicle constructor should take all as parameters
class Vehicle:
    Vehicle ( String vehicleMake, String vehicleModel, String year, Hood h, Fender f, Door d, Wheelset ws);
    Hood hood; 
    Fender fender;
    Door door;
    Wheelset wheel;
    float totalPrice;  //this should contain the total price of all the selected options
    float getTotalPrice();
    String toString()
    {
        #Print vehicleMake, vehicleModel, year plus Call the toString methods of all the car parts here.
    }

#Address
class Address:
    def __init__(self,address1,address2,city,state,zip):
        self.addressLine1, self.addressLine2, self.city, self.state, self.zip = address1,address2,city,state,zip
    def getAddressLine1(self):
        return self.addressLine1
    def getAddressLine2(self):
        return self.addressLine2
    def getCity(self):
        return self.city
    def getZip(self):
        return self.zip
    def getState(self):
        return self.state
    def setAddressLine1(self, address1):
        self.addressLine1 = address1
    def setAddressLine2(self, address2):
        self.addressLine2 = address2
    def setCity(self, city):
        self.city = city
    def setZip(self, zip):
        self.zip = zip
    def setState(self, state):
        self.state = state
    def addresstoString(self):
        addressReadLine1 = ", ".join([self.addressLine1,self.addressLine2])
        addressReadLine2 = ", ".join([self.city," ".join([self.state,self.zip])])
        fullAddress = "\n".join([addressReadLine1,addressReadLine2])
        return print(fullAddress)

#Customer
class Customer():
    def __init__(self,firstName, middleName, lastName,address1,address2,city,state,zip):
        self.homeAddress = Address(address1,address2,city,state,zip)
        self.firstName, self.middleName, self.lastName = firstName,middleName,lastName

    def getCustomerFirstName(self):
        return self.firstName
    def getCustomerMiddleName(self):
        return self.middleName
    def getCustomerLastName(self):
        return self.lastName
    def getCustomerFullName(self):
        return " ".join([self.firstName,self.middleName,self.lastName])
    def getCustomerPhoneNumber(self):
        return self.phoneNumber
    def getCustomerAddressHome(self):
        return self.homeAddress.addresstoString()
    def getCustomerAddressWork(self):
        return self.workAddress.addresstoString()
    def getCustomerVehicle(self):
        return self.customerVehicle
    def setCustomerFirstName(self, sFirst):
        self.firstName = sFirst
    def setCustomerMiddleName(self, sMiddle):
        self.middleName = sMiddle
    def setCustomerLastName(self, sLast):
        self.lastName = sLast
    def setCustomerPhoneNumber(self, phone):
        self.phoneNumber = phone
    def setCustomerAddressHome(self, address1,address2,city,state,zip):
        self.homeAddress = Address(address1,address2,city,state,zip)
    def setCustomerAddressWork(self, address1,address2,city,state,zip):
        self.workAddress = Address(address1,address2,city,state,zip)
    #def setCustomerVehicle(Vehicle obj)
    # def toString(self):
    #     customerName = self.getCustomerFullName()
    #     #req = "\n".join([customerName, self.homeAddress])
    #     return print(req)

#Create two customers
customer1 =  Customer('Syed', 'Ali', 'Naqvi', '12345 Good Ave', 'Number 1', 'Hastings', 'MN',  '55022')
customer2 =  Customer('Gloria', 'J', 'Redford', '499 Apple Street', '', 'Eagan', 'MN', '55123')

## Vehicle1
#Create a Vehicle Object for Ali’s requirements as follows and call it vehicle1. You need to call the Vehicle constructor to pass all the following objects to it. Remember that the Vehicle object resides inside the CustomerClass.

# Make Tesla, Model Model 3, Year 2019
# Needs the following:
# Hood = Lifted, Color=Silver
# Fender = Carbon Fiber, Color = Black.
# Doors Color=Black
# Wheelset = Paint-coated

## Vehicle2
#Create a Vehicle Object for Gloria’s requirements as follows and call it vehicle2. You need to call the Vehicle constructor to pass all the following objects to it.

# Make Ford, Model F150, Year 2016
# Needs the following:
# Hood = None, Color=no color option
# Fender = Carbon Fiber, Color = Black.
# Doors Color=Yellow
# Wheelset = Powder-coated