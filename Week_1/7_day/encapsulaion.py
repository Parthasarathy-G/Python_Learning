class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount


    def __calculate_final(self):
     return self.__total_amount - self.__discount

    def _get_admin_view(self):
     return{
    "Customer": self.customer_name,
    "Items": self.items, 
    "Total amount": f"{self.__total_amount}",
    "Discount applied": f"{self.__discount}",
     "Final Bill": F"{self.__calculate_final()}" }

    def get_customer_view(self):
     return{
    "Customer": self.customer_name,
    "Items": self.items, 
    "Final Bill": F"{self.__calculate_final()}" }

class AdminPortal:
    def show_order(self, order):
        return order._get_admin_view()

class CustomerApp:
    def show_order(self, order):
        return order.get_customer_view()
    
order = Order("Gowtham",["Pizza","Chicken Burger"],600,150)

admin = AdminPortal()
print(admin.show_order(order))

customer = CustomerApp()
print(customer.show_order(order))