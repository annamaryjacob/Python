cloth=int(input("Enter 1 for Cotton, 2 for Silk and 3 for Linen"))
price=int(input("Enter price of cloth"))
if(cloth==1):
    if(price>20000):
        disc=(10/100)*price
    elif((price>15000)&(price<=20000)):
        disc=(9/100)*price
    elif((price>14000)&(price<=15000)):
        disc=(7/100)*price
    elif((price<14000)):
        disc=(2/100)*price
elif(cloth==2):
    if(price>20000):
        disc=(15/100)*price
    elif((price>15000)&(price<=20000)):
        disc=(15/100)*price
    elif((price>14000)&(price<=15000)):
        disc=(9/100)*price
    elif((price<14000)):
        disc=(5/100)*price
else:
    if(price>20000):
        disc=(15/100)*price
    elif((price>15000)&(price<=20000)):
        disc=(10/100)*price
    elif((price>14000)&(price<=15000)):
        disc=(9/100)*price
    elif((price<14000)):
        disc=(5/100)*price
print("You get rupees ",disc," as discount")
tot=price-disc
print("Total amount to be paid is rupees",tot)