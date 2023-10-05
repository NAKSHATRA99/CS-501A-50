# CS 175/501A
# Nakshatra Nitin Kawthale
# restaurant

while True:
    vegetarian = input("Is anyone in your party vegetarian? (yes/no): ").lower()
    if vegetarian in ["yes", "no"]:
        break
     else:
         print("Please enter a valid response (yes or no).")
 
while True:
     vegan = input("Is anyone in your party vegan? (yes/no): ").lower()
     if vegan in ["yes", "no"]:
         break
     else:
         print("Please enter a valid response (yes or no).")
 
while True:
     gluten_free = input("Is anyone in your party gluten-free? (yes/no): ").lower()
     if gluten_free in ["yes", "no"]:
         break
     else:
         print("Please enter a valid response (yes or no).")
 
if vegetarian == "no" and vegan == "no" and gluten_free == "no":
     print("Joes Gourmet Burgers")
     print("Main Street Pizza Company")
     print("Corner Café")
     print("Mamas Fine Italian")
     print("The Chef’s Kitchen")
elif vegetarian == "yes" and vegan == "no" and gluten_free == "no":
     print("Main Street Pizza Company")
     print("Corner Café")
     print("Mamas Fine Italian")
     print("The Chef’s Kitchen")
elif vegetarian == "no" and vegan == "no" and gluten_free == "yes":
     print("Main Street Pizza Company")
     print("Corner Café")
     print("The Chef’s Kitchen")
elif vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
     print("Main Street Pizza Company")
     print("Corner Café")
     print("The Chef’s Kitchen")
 else:
     print("Corner Café")
     print("The Chef’s Kitchen")
     
