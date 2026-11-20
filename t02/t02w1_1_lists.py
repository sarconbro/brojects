#Code Challenge · Try it yourself
#Create a new list and store it in a variable named items.
#The list should contain three elements - a string, followed by a float, followed by an int.
#Print the list to the screen.

items = ['bird', 1.56, 120]

print(items)

###

#Code Challenge · Crew Members
#Create a list named titanic_crew that contains the names "Captain Smith", "Mr. Murdoch", and "Mr. Lightoller".
#Print the third crew member's name from the titanic_crew list using list indexing.

titanic_crew = ['Captain Smith', 'Mr. Murdoch', 'Mr. Lightoller']

print(titanic_crew[2])

###

#Code Challenge · My Top fruits
#Below is a code with a pre-defined list, representing a person's favorite fruits ranked from most to least favorite.
#Adjust the print statement to showcase the appropriate information.

top_fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
print(f"My list contains a total of {len(top_fruits)} fruits. \nMy most loved fruit is: {top_fruits[0]}. \nMy least loved fruit is: {top_fruits[-1]}")

###

#Code Challenge · Double or Nothing
#Create a function named double_or_nothing that accepts a list as a parameter.
#If the provided list is empty, the function should return it unchanged.
#Otherwise, the function should return the list with its elements repeated (doubled).
#Not sure how to double the list? Do it the same way as you did with strings.

def double_or_nothing(list1):
    if not list1:
        return list1
    else:
        list2 = []
        for i in list1:
            list2.append(i)
            list2.append(i)
        return list2

print(double_or_nothing([1, 2, 3, 'a', 'b', 'c']))

###

#Code Challenge · Remove ends
#Write a function, remove_ends, that accepts a list as input and returns a new list with the first and last elements removed.
#You can assume the given list contains at least two items.
#Example:
#>> remove_ends(["Jack", "Rose", "Cal"])
#[”Rose"]
#>> remove_ends([12, 50, 651, 64, 23])
#[50, 651, 64]
#>> remove_ends(["Jack", "Rose", "Cal"])
#[”Rose"]
#>> remove_ends([12, 50, 651, 64, 23])
#[50, 651, 64]

def remove_ends(names):
    return names[1:-1]

names = ['Jack', 'Rose', 'Cal']
print(remove_ends(names))

###

#Code Challenge · Combine and Double
#Create a function combine_and_double that takes two lists as input.
#The function combines the two lists and then duplicates all the elements.
#The function returns the new, combined and doubled list.
#Example:
#>> combine_and_double(["Jane", "Iman"], ["Tommy", "Kylie"])
#['Jane', 'Iman', 'Tommy', 'Kylie', 'Jane', 'Iman', 'Tommy', 'Kylie']
#>> combine_and_double(["Jane", "Iman"], ["Tommy", "Kylie"])
#['Jane', 'Iman', 'Tommy', 'Kylie', 'Jane', 'Iman', 'Tommy', 'Kylie']

def combine_and_double(list1, list2):
    combine = list1 + list2
    double = combine + combine
    return double


list1 = ['Jane', 'Iman']
list2 = ['Tommy', 'Kylie']
print(combine_and_double(list1, list2))

###

#Code Challenge · Try it Yourself
#Create a list called classes with these strings: "First Class", "Second Class", "Third Class", "Crew".
#A mistake was made and "Crew" is not a class. Replace "Crew" with "Steerage" in the classes list.
#A new class has been created named "Luxury Class". Add "Luxury Class" at the start of the classes list.
#Print the list.

classes = ["First Class", "Second Class", "Third Class", "Crew"]

classes[3] = "Steerage"
classes.insert(0, "Luxury Class")

print(classes)

###

# Code Challenge · Smart append
# Write a function smart_append that takes two parameters - a list and a value (of any type).
# If the value is not already in the list, the function will append it and return the list.
# Otherwise, it will return the list untouched.
# >> smart_append([1, 2, 3], 3)
# [1, 2, 3]
# >> smart_append([1, 2, 3], 4)
# [1, 2, 3, 4]
# >> smart_append([1, 2, 3], 3)
# [1, 2, 3]
# >> smart_append([1, 2, 3], 4)
# [1, 2, 3, 4]

def smart_append(list, value):
    if value not in list:
        list.append(value)
        return list
    else:
        return list

list = [1, 2, 3]
value = 4

print(smart_append(list, value))

###

# Code Challenge · Head and Tail
# Write a function called head_tail that expects a list as a parameter.
# The function checks if the first and last item of the list are equal.
# If they are, they are both removed, and the updated list is returned.
# If they are not, the list is returned unchanged.

def head_tail(new_list):
    if new_list[0] == new_list[-1]:
        return new_list[1:-1]
    else:
        return new_list


print(head_tail([1, 2, 3, 1]))  # Head and tail should be removed
print(head_tail([1, 2, 3, 3]))  # Should stay the same

###

# Code Challenge · Add or Remove fruit
# Let’s create a small user interface for modifying a list of fruits.
# Write a program that asks the user to choose between addition and removal (The user will type one of the words).
# Depending on the choice, the program adds an item to or removes an item from the end of a list.
# If the user wants to add an item, the program will ask him for the name of the fruit to add.

def addition_or_removal(addition_or_removal_input, fruits):
    if addition_or_removal_input.lower() == "addition":
        new_fruit = input("What fruit do you want to add?")
        fruits.append(new_fruit)
        return fruits
    elif addition_or_removal_input.lower() == "removal":
        del fruits[-1]
        return fruits
    else:
        return("Something went wrong, try again.")

fruits = ["apple", "banana", "cherry", "banana"]
addition_or_removal_input = input('Do you want addition or removal? (addition/removal):')
print(addition_or_removal(addition_or_removal_input, fruits))

###

#