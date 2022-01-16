class Product:
    def __init__(self,p_id,p_name):
        self.p_id = p_id
        self.p_name = p_name
        print("Constructor execututed automatically")

    def display_Product(self):
        print("Normal Methods")

p1 = Product(101,' iphone 12')
print(p1.p_id)
print(p1.p_name)
p1.display_Product()
p1.display_Product()
p1.display_Product()
p1.display_Product()
p1.display_Product()
p1.display_Product()
p1.display_Product()
p1.display_Product()