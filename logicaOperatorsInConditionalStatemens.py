# and
print(2 < 5 and 10 > 7)
#prints True

totalChickens = 95
qualityChickens = 93
if totalChickens >= 90 and qualityChickens >= 90:
  print("you are greate at rasing chickens")
#prints 'you are greate at rasing chickens'
#since both of the conditions are True

qualityChickens = 50
if totalChickens >= 90 and qualityChickens >= 90:
  print("you are greate at rasing chickens")
#there is no output because the second condition was not met

# or
print(2 < 5 or 10 > 7)
#prints True
bird = "chicken"
if bird is "turkey" or bird is "chicken":
  print("i love that bird")
#prints 'i love that bird'
#because at least one of the conditions was met

bird = "quail"
if bird is "turkey" or bird is "chicken":
  print("i love that bird")
#no output
#because at none one of the conditions was met
