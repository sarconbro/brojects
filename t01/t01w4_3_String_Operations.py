#1. String Methods
#Code Challenge: Case Insensitive Comparison

def are_strings_equal(string1, string2):
    if string1.lower() == string2.lower():
        print("Equal")
    else:
        print("Not equal")

# call your function
are_strings_equal("Titanic", "titanic")  # Should print: Equal
are_strings_equal("Titanic", "Bla")  # Should print: Not equal

#________________________________________________________________________________

#Code Challenge: Find and Remove Letters

# your code here
def remove_first_letter_occurrences(string):
    return string.replace(string[0], "")

# Main code
result = remove_first_letter_occurrences("titanic")
print(result)  # Should print: ianic

#________________________________________________________________________________

#Code Challenge: Counting Words

def count_words(sentence):
    # your code here
    return sentence.count(" ") + 1

num_words = count_words("The Titanic was a luxury British steamship")
print(f"Number of words is: {num_words}")  # Should print: 7

#___________________________________________________________________________________

#2. String Ummutability

#Code Challenge: A Buggy Program

def replace_spaces(sentence):
    return sentence.replace(" ", "_")


sentence = input("Enter a sentence: ")
replace_spaces(sentence)
print(f"Modified sentence: {replace_spaces(sentence)}")


#___________________________________________________________________________

#Code Challenge: Fix the Alien Message

def translate_punctuation(message):
    exclamation = message.replace("∆", "!") #replace exclamation marks
    translation = exclamation.replace("Ω", "?") #replace question marks, final translated message
    return translation


#______________________________________________________________________________

#Code Challenge: Case Inverter

def invert_case(text):
    return text.swapcase()

text_input = input("Enter a word to check: ")
new_text = invert_case(text_input)
print(new_text)


#________________________________________________________________________________

#Code Challenge: Email Username (extract username in front of @)

def extract_username(email):
    email_split = email.split("@")
    return email_split[0]


#________________________________________________________________________________

#3. The "in" Keyword

#Code Challenge: File Extension Remover

def remove_extension(filename):
    if "." in filename:
        split_filename = filename.split(".")
        return split_filename[0]
    else:
        return filename

filename = input("Enter a filename: ")
clean_filename = remove_extension(filename)
print(clean_filename)

#_________________________________________________________________________________

#Code Challenge: Email Checker

def valid_email(email):
    if "@" in email and "." in email and len(email) > 5:
        print("Valid Email")
    else:
        print("Invalid Email")

#_________________________________________________________________________________#

#Code Challenge: Does it contain Vowels

def has_vowels(word):
    if "a" in word or  "e" in word or "i" in word or "o" in word  or "u" in word:
        print("Yes")
    else:
        print("No")


#_______________________________________________________________________________

#Code Challenge: Letter in the First Half

def in_first_half(word, char):
    if char in word[:len(word)//2]:
        print("Yes")
    else:
        print("No")

    
