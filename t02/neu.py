# Namensdrucker
names = ["Anna", "Bob", "Charlie", "David", "Eva"]

def list_of_names(names):
    for name in names:
        if name == "Charlie":
            print(f'Hello, {name}! You are the best!')
            continue
        print(f'Hello, {name}!')

list_of_names(names)

# Vokalzähler Funkton

def vokalzaehler(text):
   vokale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
   total_vocals = 0
   for char in text:
       if char in vokale:
           total_vocals += 1
           continue
   print(total_vocals)

vokalzaehler("jkuhsjnlgmuh")

# Bestanden oder nicht bestanden

def calculate_total_score(noten):
    total_score = 0
    for note in noten:
        total_score += note
        