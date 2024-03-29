fruits = ["Dragon Fruit", "Jack Fruit", 'Rambutan', "Lychee"]

## for loop
# for variable in sequence

for fruit in fruits:
  print(fruit)
#prints Dragon Fruit
#Jack Fruit
#Rambutan
#Lychee

## range function
for num in range(1, 10):
  print(num)
#prints
#1
#2
#3
#4
#5
#6
#7
#8
#9

## while loop
#the following function will print the temperature dynamically as long
#as the conditions are met
#line 37 subtracts 1 from temp on every iteration
#if line 37 is removed the loop will run infinetly

temp = 77

while temp >= 68 and temp <= 77:
  print("Room temperature is maintained at {} degree fahrenheit".format(temp))
  temp = temp -1
#prints
#Room temperature is maintained at 77 degree fahrenheit
#Room temperature is maintained at 76 degree fahrenheit
#Room temperature is maintained at 75 degree fahrenheit
#Room temperature is maintained at 74 degree fahrenheit
#Room temperature is maintained at 73 degree fahrenheit
#Room temperature is maintained at 72 degree fahrenheit
#Room temperature is maintained at 71 degree fahrenheit
#Room temperature is maintained at 70 degree fahrenheit
#Room temperature is maintained at 69 degree fahrenheit
#Room temperature is maintained at 68 degree fahrenheit

## nested loop
#we will be creating a matrix using nested loops
num = 1

for row in range(1, 4):#iterates through rows in matrix
  for column in range(1, 4):#iterates through the columns the matrix
    print(num, end = " ")#prints the num and ends with a space after every print statement
    num = num + 1 #adds 1 to num after every print statement
  print()#this empty print function will print the num dymanically after every column loop is executed

#prints
#1 2 3
#4 5 6
#7 8 9

## break,  based on a certain condigion the looping statement stops

for number in range(1, 11):
    if number == 5:
        break
    else:
        print(number)

#prints
#1
#2
#3
#4

## continue, skips a particular StopAsyncIteration

for number in range(1, 11):
  if number == 5:
    continue
  else:
    print(number)

#prints
#1
#2
#3
#4
#6
#7
#8
#9
#10

## else, this is how else works without an if condition
#in the following example the condition if condition will never be met
#so the last if statement will be executed

for number in range(1, 11):
  if number == 15:
    break
  else:
    print(number)
else:
  print("All numbers where printed without a breaking the loop")

#prints
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#All numbers where printed without a breaking the loop

##what happens if the condition is met?

for number in range(1, 11):
  if number == 5:
    break
  else:
    print(number)
else:
  print("All numbers where printed without a breaking the loop")

#prints
#1
#2
#3
#4


###go to file called programTwo.py
