##we will be wrighting a program that checks wich of two numbers is grater

def findGrater(firstNumber, secondNumber):
  if firstNumber > secondNumber:
    print("First number is grater")
    return firstNumber
  elif secondNumber > firstNumber:
    print("Second number is grater")
    return secondNumber
  else:
    print("Both are equal")
    return firstNumber

print("enter the first number: ")#prompts the user to enter a number
firstNumber = int(input())#turns the input string into an interger using type casting
print("enter the second number: ")#prompts the user to enter a number
secondNumber = int(input())#turns the input string into an interger using type casting
greaterNum = findGrater(firstNumber, secondNumber)
print("greater number = {}".format(greaterNum))
