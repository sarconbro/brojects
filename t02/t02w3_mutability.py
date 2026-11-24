# Challenge 1 - Lists
# Create a list named original_list with at least 5 elements (e.g., numbers, strings, or a mix of both).
# Print the original list.
# Modify the first element of the list and print the list again.
# Append a new element to the end of the list and print the list.
# Use slicing to change a subset of the list (e.g., replace elements from index 2 to 4 with new values) and print the updated list.

original_list = [1,2,3,4,5]
print('1. print original list: ', original_list)                    #1
original_list[0] = 20                                               #2
print('2. modify first element: ', original_list)
original_list.append(30)                                            #3
print('3. append: ', original_list)
original_list[2:4] = [40, 50]                                         #4
print('4. slice changed list: ', original_list)


#_____________________________________________________________________________________________________________________________________

# Challenge 2 - Strings
# Create a string named original_string with at least 6 characters.
# Print the original string.
# Modify the third character of the string and print the string again.
# Concatenate a new string to the original string and print the updated string.
# Use string slicing to change a subset of the string (e.g., replace characters from index 1 to 4 with new characters) and print the updated string.

original_string = 'Hello World!'
print('1. print original string: ', original_string)                    #1
original_string = original_string[:3] + 'L' + original_string[4:]       #2
print('2. modify third character: ', original_string)
original_string += ' I like Python!'                                    #3
print('3. concatenate new string: ', original_string)
original_string = original_string[:6] + 'abcd' + original_string[11:]   #4
print('4. slice changed string: ', original_string)


#_____________________________________________________________________________________________________________________________________

# Challenge 3 - Bonus Challenge - Combine Both

# Combine the concepts of lists and strings:
# Create a list of strings where each element is a word.
# b. Choose one of the words and modify it by changing some characters.
# c. Print the updated list of strings.

my_strings = ['Merry', 'Frodo', 'Sam', 'Pippin']
my_strings[0] = my_strings[0].replace('e', 'a')                         #a
my_strings[1] += ' Baggins'                                             #a
print(my_strings)                                                       #b