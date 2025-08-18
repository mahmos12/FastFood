import enum
from abc import ABC,abstractmethod

class DeliveryType(enum.Enum):
    Bike=20
    MotorCycle=50
    Car = 100
    Drone=200
#-----------------------------------------------------------------
class PizzaSize(enum.Enum):
    Small = 1
    Medium = 2
    Larg = 5

#-----------------------------------------------------------------

class Item(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getCost(self):
        pass
#-----------------------------------------------------------------
class Content(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def getPrice(self):
        pass
#-----------------------------------------------------------------

class Tomato(Content):
    def __init__(self,weight):
        super().__init__()
        self.UnitPrice=50
        self.weight = weight

    def getPrice(self):
        return self.UnitPrice * self.weight

#-----------------------------------------------------------------
class Mashroom(Content):
    def __init__(self,weight,canned):
        super().__init__()
        self.UnitPrice=30

        if weight>200:
            weight = 200

        self.weight = weight
        self.canned=canned

    
    def getPrice(self):
        if self.canned ==True:
            return self.UnitPrice * self.weight
        else:
            return self.UnitPrice * self.weight*2

#-----------------------------------------------------------------
class Chiken(Content):
    def __init__(self,weight):
        super().__init__()
        self.UnitPrice=120
        self.weight = weight
    
    def getPrice(self):
         return self.UnitPrice * self.weight

#-----------------------------------------------------------------
class Chikebham(Content):
    def __init__(self,weight):
        super().__init__()
        self.UnitPrice=100
        self.weight = weight
    
    def getPrice(self):
         return self.UnitPrice * self.weight

#-----------------------------------------------------------------
class Beef(Content):
    def __init__(self,weight):
        super().__init__()
        self.UnitPrice=100
        self.weight = weight
    
    def getPrice(self):
        return self.UnitPrice * self.weight

#-----------------------------------------------------------------
class Cheese(Content):
    def __init__(self,weight):
        super().__init__()
        self.UnitPrice=100
        if weight>150:
            weight=150
        self.weight = weight
    
    def getPrice(self):
        return self.UnitPrice * self.weight

#-----------------------------------------------------------------
class Pizza(Item):
    def __init__(self,size):
        super().__init__()
        self.basePrice = 100
        self.size = size
        self.contentList=[]

    def addContent(self,content):
        self.contentList.append(content)

    def getCost(self):
        sum = 0
        for content in self.contentList:
            sum +=content.getPrice()
        sum *=self.size
        sum+=self.basePrice
        return sum

#-----------------------------------------------------------------
class Drink(Item):
    def __init__(self,weight,soda):
        super().__init__()
        self.unitPrice=20
        self.weigt=weight
        self.soda=soda


    def getCost(self):
        if self.soda==True:
            return self.weigt*self.unitPrice+4
        else:
            return self.weigt*self.unitPrice
#-----------------------------------------------------------------

class Order:
    def __init__(self,deliveryType):
        self.DeliveryType=deliveryType
        self.OrderItem=[]

    def addItem(self,item):
        self.OrderItem.append(item)

    def getTotalPrice(self):
        sum = 0
        for item in self.OrderItem:
            sum += item.getCost()
        sum+=self.DeliveryType
        return sum




# #   ------ main  -----
# p1=Pizza(PizzaSize.Medium.value)
# p1.addContent(Tomato(2))
# p1.addContent(Mashroom(1,True))
# p1.addContent(Cheese(1))
# p1.addContent(Beef(2))

# #print(f"Total cost is: {p1.getCost()}")

# d1= Drink(30,True)
# mahdiOrder= Order(DeliveryType.MotorCycle.value)
# mahdiOrder.addItem(p1)
# mahdiOrder.addItem(d1)
# print(mahdiOrder.getTotalPrice())


# # -------- MAIN --------

# # 1. 
# print("Välj leveransmetod:")
# for dt in DeliveryType:
#     print(f"{dt.name} ({dt.value} kr)")
# delivery_choice = input("Skriv typ (Bike/MotorCycle/Car/Drone): ").strip()
# delivery_type = DeliveryType[delivery_choice].value

# order = Order(delivery_type)

# # 2. Välj pizzastorlek
# print("\nVälj pizzastorlek:")
# for ps in PizzaSize:
#     print(f"{ps.name} (storleksfaktor: {ps.value})")
# pizza_choice = input("Skriv storlek (Small/Medium/Larg): ").strip()
# pizza_size = PizzaSize[pizza_choice].value

# pizza = Pizza(pizza_size)

# # 3. Lägg till ingredienser
# while True:
#     ingredient = input("\nLägg till ingrediens (Tomato/Mashroom/Chiken/Chikebham/Beef/Cheese) eller 'klar' för att avsluta: ").strip()
#     if ingredient.lower() == "klar":
#         break

#     weight = int(input("Ange vikt (gram): "))

#     if ingredient == "Tomato":
#         pizza.addContent(Tomato(weight))
#     elif ingredient == "Mashroom":
#         canned = input("Är den konserverad? (ja/nej): ").lower() == "ja"
#         pizza.addContent(Mashroom(weight, canned))
#     elif ingredient == "Chiken":
#         pizza.addContent(Chiken(weight))
#     elif ingredient == "Chikebham":
#         pizza.addContent(Chikebham(weight))
#     elif ingredient == "Beef":
#         pizza.addContent(Beef(weight))
#     elif ingredient == "Cheese":
#         pizza.addContent(Cheese(weight))
#     else:
#         print("Okänd ingrediens.")

# # Lägg till pizzan i ordern
# order.addItem(pizza)

# # 4. Lägg till dryck
# add_drink = input("\nVill du ha en dryck? (ja/nej): ").lower() == "ja"
# if add_drink:
#     weight = int(input("Ange mängd (cl): "))
#     soda = input("Är det läsk? (ja/nej): ").lower() == "ja"
#     order.addItem(Drink(weight, soda))

# # 5. Skriv ut totalpris
# print("\n--- Order Sammanfattning ---")
# print(f"Totalpris: {order.getTotalPrice()} kr")


