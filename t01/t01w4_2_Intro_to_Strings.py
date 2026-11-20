#Code Challenge: Underline it!

def underline_print(text):
    print(text)
    print("-" * (len(text)))

text = input("Enter your text: ")
underline_print(text)

#___________________________________________________________

#Code Challenge: Which is longer?

def which_is_longer(str1, str2):
    if len(str1) < len(str2):
        print(str2)
    if len(str2) < len(str1):
        print(str1)
    if len(str1) == len(str2):
        print("The strings are equally long")

which_is_longer("123", "321")

#___________________________________________________________

#Code Challenge: Right Aligned (Fill remaining space from 20 characters with *)

def align_right(text):
    length = 20 - len(text)
    print("*" * length + text)

text = input("Enter a word: ")
align_right(text)

#___________________________________________________________

#Code Challenge: Finding the Middle Character

def middle_character(word):
    length = len(word)
    print(word[length//2])

word = input("Please enter an odd length word: ")
middle_character(word)


#___________________________________________________________

#Code Challenge: First and Last

def first_and_last(word):
    print(f'First character: {word[0]}, Last character: {word[-1]}')

text = input("Enter a word: ")
first_and_last(text)


#___________________________________________________________

#Code Challenge: Are First and Last Equal?

def first_and_last_equal(text):
    if text[0] == text[-1]:
        print("Yes")
    else:
        print("No")

text = input("Enter a word: ")
first_and_last_equal(text)

#___________________________________________________________

#Code Challenge: First Half and Second Half

def first_half_second_half(text):
    length = len(text)
    print(text[:length//2])
    print(text[length//2:])

# call your function
first_half_second_half("Dinosaur")  # Should print: Dino and saur


#___________________________________________________________

#Code Challenge: Domain Extractor (https://www.example.com)

def extract_domain(dot_com):
    return (dot_com[12:-4])


#___________________________________________________________

#Code Challenge: Conditional Slicing (some names have an underscore in front)

def clean_name(name):
    if name[0] == "_":
        return name[1:]
    else:
        return name


#___________________________________________________________

#Code Challenge: Dollar to Yuan

def convert_to_yuan(dollar:str):
    get_int_dollar = int(dollar[:-1])
    yuan = get_int_dollar * 7.15 #conversion rate of 1 dollar to 7.15 yuan
    return int(yuan)

# ___________________________________________________________


