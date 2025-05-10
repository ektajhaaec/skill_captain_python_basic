class Product :
    def __init__ (self, name, price, quantity):
        self. name = name
        self.price =price
        self.quantity =quantity
    def getProductInfo(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

def productRegistration(name ,price, quantity):
    productlist =[]
    Product1 =Product(name, price, quantity)
    productlist.append(Product1)
    print(productlist[0].name)

productRegistration("mobile",10 ,12)


