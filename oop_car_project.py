from enum import Enum
from msilib.schema import Class

#Hood area
class Hood:
    Enum HoodType = Regular, Sports, Lifted, None
    Enum Color = Red, Blue, Black, Silver, Green, Yellow
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
                  Print the contents of the class as per requirement in the results     listed at the bottom
    }

#Doors
class Door:
    Color Enum color choices (Red, Blue, Black, Silver, Green, Yellow)
    Price $599.00
    enum  getDoorColor()
    setDoorColor(enum Color)
    String toString()

    {
                  Print the contents of the class as per requirement in the results listed at the bottom
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
                Print the contents of the class as per requirement in the results listed at the bottom
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
        Print vehicleMake, vehicleModel, year plus Call the toString methods of all the car parts here.
    }

#Address
class Address:
    String addressLine1, addressLine2, city, zip, state
    String getAddressLine1( );
    String getAddressLine2( );
    String getCity( );
    String getZip( );
    String getState( );
    setAddressLine1(String address1 );
    setAddressLine2(String address2);
    setCity(String city );
    setZip(String zip );
    setState(String state);
    String toString()
    {
                Print the contents of the address object as per requirement in the results listed at the bottom
    }

#Customer
class Customer:
    String FirstName, MdddleName, LastName
    Address address
    String studentPhone
    Vehicle customerVehicle
    getCustomerFirstName()
    getCustomerMiddleName()
    getCustomerLastName()
    getCustomerPhoneNumber()
    Address getCustomerAddressHome()
    Address getCustomerAddressWork()
    Vehicle getCustomerVehicle()
    setCustomerFirstName(String sFirst)
    setCustomerMiddleName(String sMiddle)
    setCustomerLastName(String sLast)
    setCustomerPhoneNumber(String phone)
    setCustomerAddressHome(Address obj)
    setCustomerAddressWork(Address obj)
    setCustomerVehicle(Vehicle obj)
    String toString()
    {
        Print the contents of the customer object including address as per requirements listed in the result.
    }

#Create two customers
customer1 = new Customer(“Syed”, “Ali”, “Naqvi”, “12345 Good Ave”, “Number 1”, “Hastings”, “MN”,  “55022”)
customer2 = new Customer(“Gloria”, “J”, “Redford”, “499 Apple Street”, “”, “Eagan”, “MN”,  “55123”)

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