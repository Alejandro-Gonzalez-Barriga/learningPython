##tuple is a collection of immutable objects
#such as birth dates, historic dates, eye color
#syntax  tupleName = (obj1, obj2, obj3)

#tuple to store my date of birth and date of graduation from HC
importantDates = (1990, 2019)
print(importantDates[0])
#prints 1990
#importantDates[1] = 2008
#this will produce an error because items in a tuple cannot be
#modified

#tuples can be deleted with the following syntax
del(importantDates)


print(importantDates)
#this will give you an error because importantDates has been deleted
