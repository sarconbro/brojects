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