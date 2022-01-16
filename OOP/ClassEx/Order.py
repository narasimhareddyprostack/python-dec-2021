class Order:
    price = 5000
    def order_Status(self):
        print("Order Delivered Successfully")


s1 = Order()
s2 = Order()
s3 = Order()
s1.order_Status()
s2.order_Status()
s3.order_Status()
print(s1.price)