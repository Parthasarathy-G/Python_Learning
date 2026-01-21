delivery_partner = 'Zomato'
def hotel():
    item = 'Pizza'

    def order_name():
        quantity = 2
        print(f'Order received: {quantity} {item} from {delivery_partner}')
    order_name()
hotel()