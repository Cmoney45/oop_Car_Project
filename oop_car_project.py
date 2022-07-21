from enum import Enum, auto

class carColors(Enum):
    RED, BLUE, BLACK, SILVER, GREEN, YELLOW, NONE = object(), object(),object(),object(),object(),object(),object()
class hoodType(Enum):
    REGULAR, SPORTS, LIFTED, NONE = 499.00, 599.00, 699.00, 0.00
class FenderType(Enum):
    REGULAR, SPORTS, CARBONFIBER = 100.00, 200.00, 1000.00
class WheelType(Enum):
    POWDER_COATED, PAINT_COATED, CLEAR_COATED, CHROME_PLATED, BARE_POLISHED, NONE = 1,2,3,4,5,0.0

class carPartColor:
    def __init__(self,color):
        self.color = carColors[color.upper()]
    def getColor(self):
        return self.color.name.lower().capitalize()
    def setColor(self, color):
        self.color = carColors[color.upper()]
    def toString(self):
        return print("{}: {} in {} color, Price: ${:,.2f}".format(
            self.partName,
            self.getType(),
            self.getColor(),
            self.getPrice()))

#Hood area <- carPartColor
class Hood(carPartColor):
    def __init__(self,type,color):
        super().__init__(color)
        self.type = hoodType[type.upper()]
        self.partName = "Hood"
    def getPrice(self):
        return float(self.type.value)
    def getType(self):
        return self.type.name.lower().capitalize()
    def setType(self, type):
        self.type = hoodType[type.upper()]

#Fender <- carPartColor
class Fender(carPartColor):
    def __init__(self,type,color):
        super().__init__(color)
        self.type = FenderType[type.replace(" ","").upper()]
        self.partName = "Fender"

    def getPrice(self):
        return self.type.value
    def getType(self):
        if self.type.name == "CARBONFIBER":
            return "Carbon Fiber"
        else:
            return self.type.name.lower().capitalize()
    def setType(self, type):
        self.type = hoodType[type.upper()]

#Doors <- carPartColor
class Door(carPartColor):
    def __init__(self,color):
        super().__init__(color)
        self.price = 599.00
        self.partName = "Door"
    def getPrice(self):
        return self.price
    def toString(self):
        return print("{}: {} color, Price: ${:,.2f}".format(
            self.partName,
            self.getColor(),
            self.price
        ))

#Wheelset
class Wheelset:
    def __init__(self,type):
        self.type = WheelType[type.replace("-","_").upper()]
    def getPrice(self):
        if float(self.type.value) > 0:
            return 1299.00
        else:
            return 0.00
    def getType(self):
        return self.type.name.replace("_","-").lower().capitalize()
    def setType(self, type):
        self.type = WheelType[type.replace("-","_").upper()]
    def toString(self):
        return print("Wheelset: {}, Price: ${:,.2f}".format(
            self.getType(),
            self.getPrice()
        ))

#Vehicle -> Hood, Fender, door, Wheel
class Vehicle:
    def __init__(self,make,model,year,h,f,d,ws):
        self.vehicleMake,self.vehicleModel,self.year = make,model,year
        self.hood = Hood(h[0],h[1])
        self.fender = Fender(f[0],f[1])
        self.door = Door(d)
        self.wheel = Wheelset(ws) 

    def getTotalPrice(self):
        self.totalPrice = float(float(self.hood.getPrice()) + float(self.fender.getPrice()) + float(self.door.getPrice()) + float(self.wheel.getPrice()))
        return print("\nTotal Price: ${:,.2f}\n".format(self.totalPrice))
    def toString(self):
        print("Make: {}\nModel: {}\nYear: {}\nCustomer selected the following options".format(self.vehicleMake,self.vehicleModel,self.year))
        self.hood.toString()
        self.fender.toString()
        self.door.toString()
        self.wheel.toString()
        self.getTotalPrice()

#Address -> Customer
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
    def toString(self):
        addressReadLine1 = ", ".join([self.addressLine1,self.addressLine2])
        addressReadLine2 = ", ".join([self.city," ".join([self.state,self.zip])])
        fullAddress = "\n".join([addressReadLine1,addressReadLine2])
        return fullAddress

#Customer
class Customer():
    def __init__(self,firstName, middleName, lastName,address1,address2,city,state,zip):
        self.homeAddress = Address(address1,address2,city,state,zip)
        self.firstName, self.middleName, self.lastName = firstName,middleName,lastName
        self.vehicleList = []
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
        return self.homeAddress.toString()
    def getCustomerAddressWork(self):
        return self.workAddress.toString()
    def getCustomerVehicle(self):
        for vehicle in self.vehicleList:
            print(vehicle.toString())
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
    def setCustomerVehicle(self, *specs):
        self.currentVehicle = Vehicle(*specs)
        self.vehicleList.append(self.currentVehicle)
    def toString(self):
        print(self.getCustomerFullName())
        print(self.getCustomerAddressHome())
        print("\n")
        self.getCustomerVehicle()

#Create two customers
customer1 =  Customer('Syed', 'Ali', 'Naqvi', '12345 Good Ave', 'Number 1', 'Hastings', 'MN',  '55022')
customer2 =  Customer('Gloria', 'J', 'Redford', '499 Apple Street', '', 'Eagan', 'MN', '55123')
customer1.setCustomerVehicle("Tesla","Model 3",2019,["lifted","silver"],["carbon fiber","black"],"black","Paint-coated")
customer1.setCustomerVehicle("Lexus","RCX350",2021,["none","none"],["sports","black"],"black","chrome-plated")

customer2.setCustomerVehicle("Ford","F150",2016,["none","None"],["Carbon Fiber","black"],"yellow","Powder-coated")
customer1.toString()
customer2.toString()