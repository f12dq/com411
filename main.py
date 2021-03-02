print("What is your name?")
#primitive data types-string,integer,float,bool.
n =str(input())
print("A random name which is , true or false")
name =input()

if len(n) > 9 and name == "true" :
  print("Long name")
  print("you have {} characters ".format(len(n)))
else:
  print("less than 9 characters")

print("end of this program")
