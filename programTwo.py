## we will write a prgram to check if a book is existing in your collection

bookCollection = ["Sadako and the Thousand Paper Cranes", "Cuentos Chinos", "Angels and Demons"]
print("Enter the name of a book: ")#prompts the userto enter the name of a book
bookToBeChecked = input()#reasigns user input to the variable bookToBeChecked
for book in bookCollection:#Enters the loop in bookCollection list
  if book == bookToBeChecked:#checks if book in the list is the same as the one the user entered
    print("yes, i do have that book")#if there is am match it will print the quote inside the ()
    break#it the condition is met, the iteration will break. If there was no break statement than the following
    #else statement will be exectute as well
else:#if the condition is not met the the next line will be executed
  print("no, i do not have that book")
