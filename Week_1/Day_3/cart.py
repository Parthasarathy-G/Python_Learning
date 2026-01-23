items = []

while True:
    item = input("Add the item (type 'done' to finish):")
    if item.lower() == 'done':
        break
    items.append(item)

print("Items in cart:", " ".join(items))