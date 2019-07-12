# the # sign is used to make a commment

#variableName = value

totalChickens = 95

print(totalChickens)

#prints 95,

######Reasigning variables

totalChickens = 100

print(totalChickens)

#prints 100

##### rules to define a variables
#four rules

#rule1
#variable names should start with an alphabet letter or an underscore and may be
#followed by a combination of alphabet letters numbers or underscores

totalChickens = 95
#this is correct

_totalChickens123 = 100
#this is correct

123totalChickens = 200
#this has a syntax error

#rule2
#variable names are case sesative

totalChickens = 95
print(totalChickens)
#this prints out 95

TotalChickens = 100
print(TotalChickens)
#this prints out 100 and is a totally diferent variable than totalChickens variable

#rule3
#variable names cannot be reserved names in python
#example
# 'print' and 'for' are reseved names

for = 95
#SyntaxError

#rule4
#the only special character is the underscore '_', no other character is allowed.
totalChickens$ = 100
#this has a SyntaxError
