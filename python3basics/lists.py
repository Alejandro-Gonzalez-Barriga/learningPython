# listName = [obj1, obj2, obj3]
favFoods = ["corundas", "carnitas", "birria"]

print(favFoods)
#prints ['corundas', 'carnitas', 'birria']

#just like a string, each object in the list can be referenced by its index number
print(favFoods[0])
#prints 'corundas'
print(favFoods[2])
#prints 'birria'

#to replace an oject in a list you can reassign the value of the index with the following syntax;
favFoods[1]= "gordita"
print(favFoods)
#prints ['corundas', 'gordita', 'birria']


##List operations

# to add an object to the end of a list use list.append()
favFoods.append("pata de puerco(en vinagre)")
print(favFoods)
#prints ['corundas', 'gordita', 'birria', 'Pata de puerco(en vinagre)']

#to insert an object in a specific place of a list use the following syntax;
favFoods.insert(1, "carnitas")
print(favFoods)
#prints ['corundas', 'carnitas', 'gordita', 'birria', 'Pata de puerco(en vinagre)']
#the obj carnitas has been added at index 1 of the list

#to remove an obj from a list use the following syntax;
favFoods.remove("gordita")
print(favFoods)
#prints ['corundas', 'carnitas', 'birria', 'Pata de puerco(en vinagre)']

#to sort a list you can use the list.sort() method, it sorts the the list from smallest value to largest
favFoods.sort()
print(favFoods)
#prints ['birria', 'carnitas', 'corundas', 'pata de puerco(en vinagre)']

#to reverse the items of a list you can use the .reverse() method
favFoods.reverse()
print(favFoods)
#prints ['birria', 'carnitas', 'corundas', 'pata de puerco(en vinagre)']

#to delete and return the last element in the list, use the .pop(method)
favFoods.pop()
print(favFoods)
#prints 'pata de puerco(en vinagre)', 'corundas', 'carnitas']
