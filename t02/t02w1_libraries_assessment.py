# 1. Use a for statement to print 10 random numbers.

import random
for _ in range(10):
    print(random.randint(1,10))

# 2. Write a program that calculates the value of 8 factorial (8!) using the math module, and assigns the answer to the variable answer.

import math
answer = math.factorial(8)

# 3. In the list grades you can see the grades of seven students in an exam. A median is the middle value in a sorted list of numbers, which divides the list into two equal halves. Write a program that saves the median grade to a variable called median.

grades = [50, 20, 35, 40, 100, 5, 89, 100]

grades.sort()
median1 = grades[len(grades) // 2] # funktioniert nur bei grades == ungerade len
print(median1)

# oder für grades == gerade len

def find_median(grades):
    sorted_grades = sorted(grades)
    middle = len(sorted_grades) // 2
    if len(sorted_grades) % 2 != 0:
        return sorted_grades[middle]
    else:
        left = sorted_grades[middle -1]
        right = sorted_grades[middle]
        return (left + right) / 2
print(find_median(grades))


#oder

from statistics import median
print(median(grades))

# 4. BONUS Lee was born in July 4, 2001. With the given datetime object representing that date, print the weekday in which Lee was born.

import datetime
lee_birthdate = datetime.datetime(2001, 7, 4)
print(lee_birthdate.strftime('%A'))

# 5. BONUS Calculate how many hours it has been since Lee was born, assuming Lee’s birthdate and time is “2001-07-04 14:30:00”. Print the total number of hours in the following format: “X hours since Lee was born.”
#
# TIP: First calculate the seconds.

import datetime
lee_birthdate = datetime.datetime(2001, 7, 4, 14, 30)

seit_geburt = datetime.datetime.now() - lee_birthdate
sek_in_h = 60 * 60 #60 sekunden in 60min ist eine stunde
stunden = seit_geburt.total_seconds() / sek_in_h

print(f'{int(stunden)} hours since Lee was born.')


