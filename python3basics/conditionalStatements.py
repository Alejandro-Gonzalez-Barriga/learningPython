##Conditional statements
#checks single or multiple conditions for a program to execute or not

#if
totalChickens = 95

if totalChickens >= 90:#the colon denotes that there is a block of code that will exectute if the condition evalueates to true
  print("yes it is")#indentation is IMPORTANT
#this prints 'yes it is'

totalChickens = 80

if totalChickens >= 90:
  print("yes it is")#indentation is IMPORTANT
#nothing will be printed because the condition was not met

#if-else
if totalChickens >= 90:
  print("yes it is")
else:#indentation is IMPORTANT
  print("no its not")
#prints 'no its not'

#if-elif
totalChickens = 60

if totalChickens >= 90:
  print("yes it is")
elif totalChickens >=40:
  print("no but its grater than 40")
else:
  print("no its not")
#prints 'no but its grater than 40'

#nested-if
totalChickens = 100
if totalChickens >= 90:
  print("yes it is")
  if totalChickens == 100:#indentation is IMPORTANT
    print ("you have a hundred chickens!")
#prints 'you have a hundred chickens!'
