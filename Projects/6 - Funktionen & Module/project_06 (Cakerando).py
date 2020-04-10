"""Cakerando
Example for Cake delivery-service

Author: Noah Kamara
"""

from collections import Counter

# Tuples -> like lists but immutable
cakes = [
    ('Erdbeer',  2.99),
    ('Himbeer',  1.99),
    ('Blaubeer', 1.50),
    ('Schoko',   0.99),
    ('Zitrone',  1.40)
]

# Prints the list of cakes
def printList(cakeList):
    for i, cake in enumerate(cakeList):
        index = str(i)
        label = cake[0]
        price = str(cake[1])+"€"
        print(index+" "+label+" "+price)


# groups the order by cake
def calculateOrder(order):
    groupedOrder = {}
    for element in order:
        if element in groupedOrder.keys():
            groupedOrder[element] += 1
        else:
            groupedOrder[element] = 1
    return groupedOrder

## Bestellen
def askOrder():
    bestellProzess = True
    orders = []
    while bestellProzess:
        order = input("Sorte (Enter zum beenden): ")
        if order == "": ## Enter - stop process
            bestellProzess = False
        elif 0 < int(order) or int(order) < len(cakes): ## Test if order int exists in cakeList
            print("Kuchen nicht gefunden")
        else:
            orders.append( int(order) ) # append cake to order
    return orders

# Main Program
## Show Auswahl
print("Auswahl: ")
printList(cakes)

# Ask for order
print("Bestellen: ")
orders = askOrder()

# Show order
print("\n Ihre Bestellung:")
groupedOrder = calculateOrder(orders)

for key in groupedOrder.keys():
    cake = key[0]
    price = key[1]
    amount = groupedOrder[key]
    fullPrice = price * amount
    print(str(amount)+"x "+cake+" ("+str(price)+")\t"+str(fullPrice)+"€")



