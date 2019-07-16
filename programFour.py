#Read the names and grade of at least 3 students
#Rank the top three students with the highest grades
#Give cash rewards. $500 for first rank, $300 for second rank and $100 for third rank.  Value cannot be modified
#Appreciate students who secured 95 grade and above

import operator#this is a library that will allow us to turn a dictionary into a list so that we can get a representation of the student record dictionary
#we will convert studentRecord into a list of tuples

def readStudentDetails():
  print()
    # {"john": 600, "ben": 800, "david": 950, "mark": 980}
  print("Eneter the number of students: ")#prompts the user to enter the number of students
  numOfStudents = int(input())#converts the string input into an interger
  studentRecord ={}#this dictionary will store the record of the students
  for student in range (0, numOfStudents):
    print("Enter the name of the student: ")#promts the user to enter the name of the student
    name = input()#stores user input into name variabl
    print("Enter grade of student: ")
    grade = int(input())#type casts the string to interger
    studentRecord[name] = grade
    print()
  return studentRecord

def rankStudents(studentRecord):#this function will sort the students decending order depending on the value of their grade
  print()
  #we will convert studentRecord into a list of tuples(the sorted function comes from the operator library imported at the top)
  sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
  print(sortedStudentRecord)#prints [('mark', 980), ('david', 950), ('ben', 800), ('john', 600)], this is a list of tuples
  print("{} has secured first rank, scoring a grade of {}.".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))# this will give you the name and score of the first record
  print("{} has secured first rank, scoring a grade of {}.".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))# this will give you the name and score of the second record
  print("{} has secured first rank, scoring a grade of {}.".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))# this will give you the name and score of the thrid record
  print()
  return sortedStudentRecord# the list needs to be returned so that it can be accesed outside this function

def rewardStudents(sortedStudentRecord, reward):
  print("{} has recieved a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
  print("{} has recieved a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
  print("{} has recieved a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
  print()


def appreciateStudents(sortedStudentRecord):
  print()
  for record in sortedStudentRecord:
    if record[1] >= 950:
      print("congratulations on scoring {}, {}".format(record[1], record[0]))
    else:
      break
  print()


studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)
