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
