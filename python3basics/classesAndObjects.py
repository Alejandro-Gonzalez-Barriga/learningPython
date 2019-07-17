#in this file we will go over classes and keyword self in python3

class Robot:#this is syntax to wright a class
  def introduce_self(self):
    print("My name is " + self.name) #the keyword "self" inside the parameter of the function is like "this" in JavaScript


r1 = Robot()#create an object with the class Robot
r1.name = "Tom"#object attributes
r1.color = "red"#object attributes
r1.weight = 30#object attributes

r2 = Robot()#create an object with the class Robot
r2.name = "Jerry"#object attributes
r2.color = "blue"#object attributes
r2.weight = 40#object attributes

r1.introduce_self()#call out the attribute name on object r1 #returns "My name is Tom"
r2.introduce_self()#call out the attribute name on object r2 #returns "My name is Jerry"

## An easier way to perform the code above is by adding a Custom Constructor
#the syntax for a custom constructor is : def __init__(params):

class Robot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight

  def introduce_self(self):
    print("My name is " + self.name)

r1= Robot("Tom", "red", 30)
r2= Robot("Jerry", "blue", 50)

r1.introduce_self()#call out the attribute name on object r1 #returns "My name is Tom"
r2.introduce_self()#call out the attribute name on object r2 #returns "My name is Jerry"
