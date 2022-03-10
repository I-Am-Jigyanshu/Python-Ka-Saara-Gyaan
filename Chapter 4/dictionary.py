#Dictionary is key value pairs.
d1 = {}
print(type(d1))
d2 ={ "Jiggu":"Burger", "Rohan":"Fish", "Ravi":"Roti"}
#print(d2["Jiggu"]) case sensitive,tell about there syn...
#we can make dictionary inside a dictionary
d3 = {"Jiggu":"Burger", "Rohan":"Fish", "Ravi":"Roti",
      "Pagal":{"B":"Oats","L": "Rice","D":"Chicken"}}
'''
d3["Ankit"] = "Junk Food"
d3[3453] = "Kabab"
del d3[3453]
'''
print(d3.get("Jiggu"))



