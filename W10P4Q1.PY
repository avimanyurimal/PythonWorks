def calculate_revenue(data):
    revenue = 0
    for product in data:
        revenue += product["UnitsSold"] * product["UnitPrice"]
    return revenue

def calculate_units_sold(data):
    units_sold = 0
    for product in data:
        units_sold += product["UnitsSold"]
    return units_sold

data = []
with open('sales.txt') as f:
    for i, line in enumerate(f):
        if i == 0: # skip the first line (header)
            continue
        fields = line.strip().split(',')
        product = {
            "ProductID": int(fields[0]),
            "ProductName": fields[1],
            "Category": fields[2],
            "UnitsSold": int(fields[3]),
            "UnitPrice": float(fields[4])
        }
        data.append(product)

total_revenue = calculate_revenue(data)
total_units_sold = calculate_units_sold(data)

print("Sales Report:")
print("Total Revenue: ${:.2f}".format(total_revenue))
print("Total Units Sold: {}".format(total_units_sold))
