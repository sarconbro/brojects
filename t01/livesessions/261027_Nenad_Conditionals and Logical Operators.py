
def altersklasse(age):
  if age < 13:
      print ("child")
  elif 13 <= age <= 19:
      print ("teenager")
  elif age > 20 and age < 64:
      print ("adult")
  elif age > 65:
      print ("senior")

altersklasse(70)

def login(username, password):
  if " " in username or " " in password:
    print("Invalid Input, please remove spaces.")
  elif username == "admin" and password =="admin123":
    print("Welcome admin!")
  elif username == "user" and password == "user123":
    print("Welcome user!")
  else:
    print("Access denied.")

login("admin", "admin123") #admin yes
login("user", "user123") #user yes
login("sarah","sarah123") #no
login(" sa arh", "sarah123") #no, spaces
login("sarah", "s a af12 3") #no, spaces
