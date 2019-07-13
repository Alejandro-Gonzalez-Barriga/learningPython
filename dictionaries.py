##Dictionaries is a collection of key-value pairs
## in order to return a value in a dictionary it must be referenced using the key
#dictionaryName = {key1:value1, key2:value2, key3:value3}
steakPrices = {"sirloin":18.99, "t-bone":27.99, "ribeye":29.99}
print(steakPrices)
#prints {'sirloin': 18.99, 't-bone': 27.99, 'ribeye': 29.99}
print(steakPrices["t-bone"])
#prints 27.99

#to change the value of a key use this syntax
steakPrices["sirloin"] = 20.99
print(steakPrices["sirloin"])
#prints 20.99

##Operations

#dictionaryName.keys() calls out all the keys in that particular dictionary
print(steakPrices.keys())
#prints dict_keys(['sirloin', 't-bone', 'ribeye'])

#dictionaryName.values() calls out all the values in that particular dictionary
print(steakPrices.values())
#prints dict_values([20.99, 27.99, 29.99])

#to clone a dictionary you can use dictionaryName.copy()
#Ex.
copyOfSteakPrices = steakPrices.copy()
print(copyOfSteakPrices)
#prints {'sirloin': 20.99, 't-bone': 27.99, 'ribeye': 29.99}

#to delete a key-value pair in a dictionary..
del steakPrices["t-bone"]
print(steakPrices)
#prints {'sirloin': 20.99, 'ribeye': 29.99}

#to clear the contents of a dictionary..
steakPrices.clear()
print(steakPrices)
#prints {}

# to add a key-value pair to a dictionary..
steakPrices["t-bone"] = 27.99
print(steakPrices)
#prints {'t-bone': 27.99}
steakPrices["ribeye"] = 29.99
print(steakPrices)
#prints {'t-bone': 27.99, 'ribeye': 29.99}
