shop_items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

sorted_items = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)

print(": ", end="")

for i, item in enumerate(sorted_items[:3]):
    if i == 2:
        print(f"{item[0]}: {item[1]}")
    else:
        print(f"{item[0]}: {item[1]}", end=" ")
