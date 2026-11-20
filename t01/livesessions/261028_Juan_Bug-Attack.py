# 1 Einfacher Taschenrechner
# Das folgende Programm ist eine einfache Taschenrechner-Funktion. Aber etwas stimmt nicht – ich kann nicht teilen.

def simple_calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!") #print direkt unter 0 gesetzt, dann return um weiterzuteilen, falls es nicht null ist
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation!")
        return

    print(f"Result: {result}")


simple_calculator(15, 3, '/') # should be 5.0

#_____________________________________________________________________________________

# 2 Summe der Zahlen
# Das folgende Programm nimmt eine Liste von Zahlen (Ganzzahlen) und gibt die Gesamtsumme aller Zahlen zurück. Aber unser Testlauf scheint nicht zu funktionieren. Versuche, eine print-Anweisung in der Funktion einzufügen, um zu sehen, was dort passiert.


def sum_of_nums(numbers):
    sum = 0
    for n in numbers: # indentation error, for schleife muss unter sum bzw result of schleife
        sum = sum + n
    print(sum) # print statt return wegen aufgabenstellung,

numbers = [1,42,7]
sum_of_nums(numbers) #should be 50, print nach oben in funktion


#_____________________________________________________________________________________

# 3 Altersklassifizierer
# Das folgende Programm nimmt ein Alter und gibt eine Altersgruppe aus. Allerdings scheint hier ein Fehler vorzuliegen. Warum druckt mein Programm „Teenager“?

def age_group_classifier(age):

    if 0 < age <= 12:
        print("Child")
    elif 12 <= age < 19:
        print("Teenager")
    elif 19 <= age < 64:
        print("Adult")
    elif age >= 64:
        print("Senior")
    else:
        print("Invalid age")

# Test cases
age_group_classifier(67) # should print Senior

#_____________________________________________________________________________________

# 4 Keine Leerzeichen
# Das folgende Programm wandelt einen Text (zum Beispiel „Hello world“) in denselben Text ohne Leerzeichen um („HelloWorld“). Aber leider funktioniert es nicht. Versuche, print-Anweisungen an den richtigen Stellen einzufügen, um den Entstehungsprozess besser nachvollziehen zu können.

def text_with_no_spaces(sentence):
    new_text = ""
    for char in sentence:
        if char == " ":
            new_text += "" #muss += sein, weil sonst nur Dokument ausgespielt wird, da das Leerzeichen sonst die char-Kiste komplett leer machen - sagt "mach nichts"
        else:
            new_text += char
    return new_text
# auch möglich A
#       if char == " ":
#            pass
#        else:
#            new_text += char

# auch möglich B
#   for char in sentence:
#       if char != " ": #heißt "ist NICHT gleich"
#           new_text += char

text = "New Document"
print(text_with_no_spaces(text))

#_____________________________________________________________________________________

# 5 Das Root-Verzeichnis ermitteln
# In Linux könnte der vollständige Pfad zu einer Datei beispielsweise so aussehen: /usr/bin/logs. Das bedeutet, dass das Root-Verzeichnis usr ist, darin befindet sich bin und darin logs. Das folgende Programm soll einen vollständigen Pfad entgegennehmen und das Root-Verzeichnis ausgeben – allerdings funktioniert es nicht.

def path_root_dir(path):
    splitted = path.split("/")
    return splitted[1] # list starts with 0 and 0 would be empty, so its 1 and you get usr

path = "/usr/bin/data"
print(path_root_dir(path))

#_____________________________________________________________________________________

# 6 Zahlenprüfer
# Meine Zahlenprüf-Funktion soll mir mitteilen, ob meine Zahl positiv, negativ oder null ist. Aber irgendetwas stimmt nicht? Kannst du mir helfen?


def number_checker(num): # hgier war vorher num und oben num als 0 definiert. man muss auf die variablen achten, funktion muss auch die richtigen variablen nutzen
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(number_checker(5)) # Expected output: Positive

#_____________________________________________________________________________________

# 7 Den Benutzer fragen
# Meine Funktion ask_user soll nach Erhalt eines "yes" vom Benutzer fortfahren, aber das passiert nie. Warum erhalte ich immer dasselbe Ergebnis?

def ask_user():
    user_input = input("Do you want to proceed? (yes/no): ")
    if user_input.lower() == "yes": # hinter .lower muss die Klammer (), sonst funktioniert es nicht und springt zu else
        print("Proceeding with the specific action...")
        # Add your specific action here
    else:
        print("No action taken.")


# Call the function
ask_user()

#_____________________________________________________________________________________

# 8 Nukleare Familie
# Diese Funktion nimmt eine Liste von Familienmitgliedern als Argument. Sie soll mir mitteilen, wie groß meine Familie ist. Ich erwarte, dass ich eine mittelgroße Familie habe, aber aus irgendeinem Grund sagt sie, dass sie klein ist.

def family_size_classifier(family_members):
    num_members = len(family_members) #klammern um family_members [] musste weg, da es sonst eine neue liste war und die immer nur ein (ein string) ausgespielt hat, deshalb waren alle familien small
    if num_members <= 3:
        return "Your family is small."
    elif 4 <= num_members <= 6:
        return "Your family is medium-sized."
    else:
        return "Your family is big!"

# Example usage:
my_family = ["Alice", "Bob", "Charlie", "David"]
result = family_size_classifier(my_family)
print(result) # should be medium-sized

#_____________________________________________________________________________________

# 9 Sind meine Wörter Anagramme?
# Diese Funktion soll mir sagen, ob meine beiden Wörter Anagramme sind. Allerdings stimmt etwas nicht.
# Hinweis 1: Ein Anagramm ist ein Wort, das durch Umordnen der Buchstaben eines anderen Wortes entsteht, wobei alle Buchstaben genau einmal verwendet werden.
# Hinweis 2: Mach dir keine Sorgen, wenn du nicht jeden Teil dieser Funktion verstehst – versuche, den Fehler im Code zu finden, indem du einige print-Anweisungen hinzufügst.

def are_anagrams(word1, word2):
    word1_chars_sorted = sorted(word1.lower()) #needed all lower chars to be comparable
    word2_chars_sorted = sorted(word2.lower())
    sorted_word1 = ''.join(word1_chars_sorted)
    sorted_word2 = ''.join(word2_chars_sorted)
    return sorted_word1 == sorted_word2


print(are_anagrams('Silent', 'Listen'))  # should be True, but gives False
