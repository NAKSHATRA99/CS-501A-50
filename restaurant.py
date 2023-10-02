# CS 175/501A
# Nakshatra Nitin Kawthale
# restaurant

vegetarian = input(" is anyone in your party vegetarian?").lower()
vegan = input("is enyone in your party vegan?").lower()
gluten_free = input("is anyone in your party gluten free?").lower()


if vegetarian == "no" and vegan == "no" and gluten_free == "no":
 print("Joes Gourment Burgers")
 print("Main Street Pizza Company")
 print("Corner Café")
 print("Mamas Fine Italian")
 print("The Chef’s Kitchen")
elif vegetarian == "yes"  and vegan == "no" and gluten_free == "no":
 print("Main Street Pizza Company")
 print("Corner Café")
 print("Mamas Fine Italian")
 print("The Chef’s Kitchen")
elif vegetarian == "no"  and vegan == "no" and gluten_free == "yes":
 print("Main Street Pizza Company")
 print("Corner Café")
 print("The Chef’s Kitchen")
elif vegetarian == "yes"  and vegan == "no" and gluten_free =="yes":
 print("Main Street Pizza Company")
 print("Corner Café")
 print("The Chef’s Kitchen")
else:
 print("Corner Café")
 print("The Chef’s Kitchen")
