# 1 Intro AC101 Indefinite Iterations

# def getCaptchaAnswer():
#     valid_input = False
#     while not valid_input:
#         validAnswer = showNewCaptcha() # zeigt neues Captcha, gibt die richtige Lösung zurück
#         answer = answer.lower()
#         validAnswer = validAnswer.lower()
#         if answer == validAnswer:
#             valid_input = True
#         else:
#             print('Please try again.')
#     return answer

n = 5
while n > 0:
    print(n)
    n -= 1
print('Blastoff!')



#______________________________

#Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name total.


list1 = [8, 3, 4, 5, 6, 7, 9]

total = 0

for item in list1:
    total = total + item

while list1:
    total += list1.pop()

    
#______________________________
# Listener Loop Basic Structure

num = 0
while num != 100:
    num = int(input("Please enter a number: "))
    print("Checking your number...")

print("Finally! you've entered 100!")

# 4 Listener Loop 1. Write a program that asks the user to input strings, and stops once the user entered a string longer than 20 characters.

def main():
    input_string = ""
    while len(input_string) <= 20:
        input_string = input('Please enter a string:')
    
    
if __name__ == "__main__":
  main()


# 4 Listener Loop 2. Write a program that asks the user to input strings, and stops once the user entered “quit” or “stop”.

def main():
    input_string = ''
    while input_string.lower() not in ('quit', 'stop'):
        input_string = input('Please enter a string, enter <quit> or <stop> to escape this hell of a loop:')
    
if __name__ == '__main__':
    main()

# 4 Listener Loop 3. Write a program that asks the user to input numbers, and stops once 5 even numbers were typed. We’ve create a variable called counter to help you count.

def main():
    counter = 0
    while counter < 5:
        input_number = int(input('Please enter once number at a time until we accumulated five even numbers:'))
        if input_number % 2 == 0:
            counter += 1

if __name__ == '__main__':
    main()

# 5 Validating Input Write a function that asks the user to choose a password. The password has to be longer than 10 characters. The program uses an input validation loop, and returns a valid password only.


def get_and_validate_password():
    password = ''
    while len(password) <= 10:
        password = input('Please choose a password longer than 10 characters:')
    return password


def main():
    valid_password = get_and_validate_password()
    print("The chosen password is", valid_password)


if __name__ == "__main__":
    main()


# 6 Using a Boolean Loop Variable Rewrite the function get_and_validate_password() from last chapter, using the boolean variable pattern. Validate that the chosen password is:
# Between 10 and 20 characters long.
# Contains either one of “!” or “$”.
# Does not contain the word “password”.
# We’ve already created the loop variable password_is_valid for you, but notice that it’s False by default. Hint: Use a not syntax in the while loop condition.

def get_and_validate_password():
    password_is_valid = False #nur T wenn 
    pw_length = False #soll T
    pw_contains_symbols = False #soll T
    pw_is_free_of_password = False #soll T
    while not password_is_valid:
        pw = input('Good luck finding a password:')
        pw_length = 10 <= len(pw) <= 20
        pw_contains_symbols = '!' in pw or '$' in pw
        pw_is_free_of_password = 'password' not in pw.lower()
        password_is_valid = pw_length and pw_contains_symbols and pw_is_free_of_password
    return pw

def main():
  valid_password = get_and_validate_password()
  print("The chosen password is", valid_password)

if __name__ == "__main__":
  main()

# 8 Break and Continue 1. Add a break statement in the while loop, so that it terminates the loop once the user enters a number bigger than 100.

def get_a_big_number():
    num = 0
    while True:
      num = int(input("Please enter a number: "))
      if num > 100:
            break
    return num


def main():
  valid_number = get_a_big_number()
  print("The number is", valid_number)


if __name__ == "__main__":
  main()

# 8 Break and Continue 

n = 0
while True:
  n += 1
  if n % 5 == 0:
    continue
  if n == 9:
    break
  print(n) #  1, 2, 3, 4, 6, 7, 8 The loop skips the print of 5, and breaks before 9.
  #___

  domains = ["cnn.com", "website.net", "whatismyip.com", "example.net"]

print("Printing only .com domains")
for domain in domains:
    if domain.endswith(".net"):
        print("Skipping")
        continue
    print(f"Domain: {domain}") 

#_________________________________
# 9 CHAPTER ASSESSMENT

# 9.1   Create a while loop that has a counter from 1 to 20 (inclusive).
#   If the value of the counter is divisible by 5, just skip it using continue. For the rest of the numbers, print the number. Each number should appear in a new line.

counter = 0
while counter < 20:
    counter += 1
    if counter % 5 == 0:
        continue
    print(counter)

#  9.2 Write a function, until_stop, that gets a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list.
#   The sublist should contain the same values of the original list until it reaches the string “STOP”. The new list should not contain the string “STOP”.
#   Note: the word STOP doesn’t have to appear in the list. If the word “STOP” did not appear in the list, the returned list should be a copy of the original one.
# For example, running until_stop(["hey", "joe", "meow", "STOP", "Hello"]) should return the list ["hey", "joe", "meow"].

def until_stop(list_of_strings):
    index = 0
    list_copy_until_stop = []
    while index < len(list_of_strings):
        if list_of_strings[index].lower() == 'stop':
            break
        list_copy_until_stop.append(list_of_strings[index])
        index += 1
    return(list_copy_until_stop) #sublist should contain the same values as original until STOP, stop is no requirement tho in list

list1 = ["hey", "joe", "meow", "STOP", "Hello"]
list2 = ["hey", "joe", "meow"]

print(until_stop(list1))
print(until_stop(list2))


# 9.3 Write a program that implements a listener pattern, and asks for input from the user constantly. For every string entered, it displays the length of it and the number of words in it. If the string is empty, it will just be skipped using continue. If the input string is “break”, break out of the loop.

def main():
    user_input = ''
    while user_input.lower() != 'break':
        user_input = input('For what you enter, you will find out \na) how many characters you typed and \nb) the number of words.\nPlease type something:')
        if user_input == "":
            continue
        if user_input.lower() == "break":
            break
        print(f'You typed {len(user_input)} characters.')
        print(f'You thought of {len(user_input.split())} words, good job!')


if __name__ == '__main__':
    main()