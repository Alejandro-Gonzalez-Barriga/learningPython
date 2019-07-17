##functions

#syntax ; def functionName():
#           blockOfCode

def holaMundo():
  print("Hola Mundo!")

#syntax to call out a function
holaMundo()
#prints  Hola Mundo!

## lets compute the area of a rectangle
#area = length * width

lengthOne = 8
widthOne = 3
areaOne = lengthOne * widthOne
print(areaOne)
#prints 24

lengthTwo = 10
widthTwo = 4
areaTwo = lengthTwo * widthTwo
print(areaTwo)
#prints 40

#we will create a function that will prevent us from having to re-wright the prvious blocks of
#code for every rectangle

def computeArea(length, width):
  area = length * width
  print(area)

#Now lets call out the function with the paramaters we defined earlier
computeArea(lengthOne, widthOne)
#prints 24

#we can use the same function with diferent parameters
computeArea(lengthTwo, widthTwo)
#prints 40

computeArea(10, 5)
#prints 50

#return statements
#you must set a variable that will store the value of the executed function
def computeArea(length, width):
  area = length * width
  return area

newArea = computeArea(lengthOne, widthOne)
print(newArea)
#prints 24

newArea = computeArea(50, 10)
print(newArea)
#prints 500

##Continue to programThree.py
