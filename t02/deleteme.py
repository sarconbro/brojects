import random
from statistics import median

import masterlib
import datetime as dt
#import math


def main():
    print("Welcome to my random number generator!")
    print(random.randint(0, 9))

if __name__ == '__main__':
    main()

print(masterlib.sum_of_digits(11111111111111111111111))

print(masterlib.sum_of_nums(1,2,3,4))

print(dt.date.today())
print(dt.datetime.now())


lee_birthdate = dt.datetime(2001, 7, 4)
d_since_birth = dt.datetime.now() - lee_birthdate
print(d_since_birth.days)

#calc = math.factorial(8)
#print(calc)


grades = [50, 20, 35, 40, 100, 5, 85, 75, 12, 10, 5, 3, 100]

median(grades)
print(median(grades))

def find_median(grades):
    sorted_grades = sorted(grades)
    if len(sorted_grades) % 2 == 1:
        return sorted_grades[len(sorted_grades) // 2]
    else:
        return sorted_grades[len(sorted_grades) // 2 - 1]

print(find_median(grades))

lee_birthdate = dt.datetime(2001, 7, 4)
print(lee_birthdate.strftime('%A'))

lee_birthdate = dt.datetime(2001, 7, 4, 14, 30)
timedelta = dt.datetime.now() - lee_birthdate
print(f'{timedelta.seconds / 60} hours since Lee was born.')


def add(a,b):
    total = a+b
    return total
my_var = 11
print(add(my_var,3))

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
print(my_list.append(99))
print(my_list)


#########


####### Name , Age, Salary, is_fired, performance_score , threshold_score
#### is_fired -> highest Salary , lowest performance
#### is_fired -> performance_score < threshold_score

# def check_if_fired(name, salary, performance, thresh=0.5)


def get_employee_name():
    name = input("What's your name?")
    return name

def greet_employee(name):
    print(f'Hey {name}, welcome this stay-hired or get-fired simulator!')

def  get_employee_salary():
    salary = int(input('What is your salary?'))
    return employee_salary

def hr_analysis():
    employee_name = get_employee_name()
    greet_employee(employee_name)
    employee_salary = get_employee_salary(employee_name)
    print(f'{employee_name} has a salary of {employee_salary} €')
    return employee_name, employee_salary

def hr_decision(employee_name, employee_salary, treshold_score):
    if performance < tresh:
        print(f"Hey {employee_name}, your ass is fired. Bye.")
    else:
        print(f"Close call, {employee_name}, your salary of {employee_salary} is low enough to make up for your subpar performance, so we'll fire you another day.")

def main():
    employee_name, salary = hr_analysis()
    performance_score = float(input("Whats the performance score?"))
    treshold_score = 0,5
    hr_decision(employee_name, employee_salary, performance_score, treshold_score)

main()


####### Name , Age, Salary, is_fired, performance_score , threshold_score
#### is_fired -> highest Salary , lowest performance
#### is_fired -> performance_score < threshold_score

# def check_if_fired(name, salary, performance, thresh=0.5)

def get_employee_name():
    name = input('what is your name, please type in the terminal below ')
    return name


def greet_employee(name):
    print(f"Greetings {name}")


def get_employee_salary():
    salary = int(input("Please enter your salary!"))
    return salary


def hr_analysis():
    employee_name = get_employee_name()
    greet_employee(employee_name)
    employee_salary = get_employee_salary()
    print(f"{employee_name} has a salary of {employee_salary}")
    return employee_name, employee_salary


def hr_decision(employee_name, employee_salary, employee_score,
                threshold_score):  ## Bitte, dachte du wolltest die gleichen verwenden wie oben :) - Julian :D // danke für die Erklärung & zoorriiiiii
    if employee_score < threshold_score:
        print(
            f"You are fired  dear {employee_name} with your salary {employee_salary} and your performance {employee_score} due to the threshold of {threshold_score} ")
    else:
        print(
            f"You survived another month dear {employee_name} with your salary {employee_salary} and your performance {employee_score} ")


def main():
    employee_name, employee_salary = hr_analysis()
    perfomance_score = float(input("performance_score?"))
    threshold_score = 0.5
    hr_decision(employee_name, employee_salary, perfomance_score, threshold_score)


main()


def main():
    name = input("wie heißt duuu?").lower()
    tag = input("was ist heute für ein tag?").lower()
    adjektiv = input(f"guten morgen,{name}. wie du weißt, fängt {tag()} fängt mit {tag[0]} an: sag mir dein lieblingsadjektiv, das mit {tag[0]} anfängt:").lower()
    if adjektiv[0] != tag[0]:
            input(f"ne ne ne, so nicht - das versuchst du nochmal! mit {tag[0]} soll dir anfagen:")
    else:
            print(f"ich wünsche dir, liebe {name}, einen wunderschönen {adjektiv} {tag}! Byeeee")


main()


def dashboard(user):
    print('== DASHBOARD ==')
    print(f"Welcome, {user['username']}!")
    print(f"Balance: ${user['balance']:.2f}")

def main():
    init_database()
    seed_demo_data()
    print('CodeStra Demo Application')
    print('Demo account: demo / demo123')
    user = login_screen()
    if not user:
        print('Login failed.')
        return
    dashboard(user)

if __name__ == '__main__':
    main()

    