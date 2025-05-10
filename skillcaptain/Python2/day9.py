# 1. Create a class called "Product" that represents a product in the e-commerce system. The class should have attributes for the product name, price, and quantity.
# 2. Create a class called "Cart" that represents the user's shopping cart. The cart should have attributes for the user's name and a list to store the added products.
# 3. Implement methods in the "Cart" class to add a product to the cart, remove a product from the cart, and display the cart's contents.
# 4. The "add_to_cart" method should take a "Product" object as a parameter and add it to the cart's list of products.
# 5. The "remove_from_cart" method should take a product name as a parameter and remove the corresponding product from the cart.
# 6. The "display_cart" method should display the products in the cart along with their details.



class Product :
    def __init__ (self, productName ,price ,Quantity):
        self.productName =productName
        self.price =price
        self.quantity =Quantity
    
class Cart :
    def __init__ (self, userName, productList):
        self.userName = userName
        self.productList = productList

    def add_to_cart (self,Product):
        self.productList.append(Product)

    def remove_from_cart (self,productName):
        for product in self.productList:

         if product.productName == productName:
            self.productList.remove(product)

    def display_cart(self):
        for product in self.productList :
            print (product.price )

p1 = Product("pen", 10, 1)
p2 = Product("pencil", 25, 2)
ProductList = []
cart = Cart("Alice",ProductList)
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.display_cart()
cart.remove_from_cart("pencil")




