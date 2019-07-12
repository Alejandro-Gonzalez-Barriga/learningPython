#Strings a a sequence of character that are enclosed within a single or double quote

# stringName = "string" or 'string'

truck = "Tesla"
print(truck)
#prints 'apple'

#you can directly reference the charachter of a string with square brackets [] and the index of the character
#with the first index being 0
print(truck[0])
#prints 'T'

print(truck[4])
#prints 'a'

#if you reference an index that is out of range the program will return an error

#negative indexes will reference the index starting from the back of the string with the last index being -1
print(truck[-1])
#print 'a'

print(truck[-2])
#print 'l'

#to avoid an apostrophe closing out your string you can use double quotes or
#you can place a back slash before the apostrophe

string = "I'm killing it learning Python"
print(string)
#prints "I'm killing it learning Python"

string2 = 'I\'m killing it learning Python'
print(string2)
#prints "I'm killing it learning Python"

##String formating allows you to referance variables while in an a string using {} and .format() method at the end of the string
programingLang = "Python"
print("I'm killing it at learning {}".format(programingLang))
#prints "I'm killing it at learning Python"

#if the variable is reassigned, the string will be dynamically modified
programingLang = "C++"
print("I'm killing it at learning {}".format(programingLang))
#prints "I'm killing it at learning C++"
