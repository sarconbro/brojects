
def combine(my_list):
    return ''.join(my_list)

print(combine(['a', 'b', 'c', 'd', 'e']))

print('1 A funtion called get_max that returns the maximum value in a list of numbers')
def get_max(my_list):
    return max(my_list)

print(get_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print('2 A function called only_unique that gets a list and returns it withouth duplicates')
def only_unique(my_list):
    return list(set(my_list))

print(only_unique([1, 2, 2, 3, 3, 4, 4, 5, 5]))

print('3 A function called starts_with that checks if a string starts with another string')
def starts_with(string, prefix):
    return string.startswith(prefix)    #prüft ob der string mit dem prefix beginnt boolean wert zurückgegeben wird True oder False

print(starts_with('Hello World', 'Hello'))

print('4 A function called factorial to calculate the factorial of a number') 
def factorial(n):
    if n == 0:                          #mathematische regel 0! = 1, deshalb die if abfrage. factorial gibt die möglichkeiten der anordnung in einer reihe an, denk an bücher. 2! zwei bücher kann man im regal in 2! = 2 möglichkeiten aufstellen. bei 0 büchern goibt es nur eine möglichkeit: ein leered regal.
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

import math                         #lazar hat math importiert, was nicht buiktin functin ist, das ist scon ein bisschen cheaten :D 
def factorial(n):
    return math.factorial(n)

print(factorial(5))

print('5 A function called all_equal that checks if all items of a list are identical')
def all_equal(my_list):
    return len(set(my_list)) == 1       #wenn die länge der set liste 1 ist, dann sind alle elemente gleich, da ein set keine doppelten elemente zulässt. boolean wert zurückgegeben wird True oder False

print(all_equal([1, 1, 1, 1]))
print(all_equal([1, 2, 3, 4]))
print(all_equal(['5, 5, 5, 5']))

def is_all_above_100(numbers):
    for number in numbers:
        if number <= 100:
            return False
    return True

def is_all_above_100(numbers):
    for num in numbers:
        if num <= 100:
            return False
    return True

# Boolean Functions - Classwork (Erik Hölzel) 17.11.2026
# 1 Does the string contain at least one dot (“.”)?
def contains_dot(string):
    return '.' in string

# 2 Does the string contain only dollars (“$”)?
def contains_only_dollars(string):
   if '$' not in string:
       return False
   return True

# 3 Is every number on a list lower than 20 but higher than 10?
def is_every_number_between_10_and_20(numbers):
    for number in numbers:
        if number <= 10 or number >= 20:
            return False
    return True
