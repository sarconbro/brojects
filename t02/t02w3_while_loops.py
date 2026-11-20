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
