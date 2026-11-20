# 1 : Extract Area Code

#Write a function called extract_area_code.
#The function will expect one parameter: phone_number, a string containing a phone number in the format “(XXX) YYY-ZZZZ".
#The function will return a new string containing the extracted area code.

def extract_area_code(phone_number):
    return(phone_number[1:4])

#################################################

#2 : Price with Tax 2

#In a certain country, only items that cost more than $100 are taxed. The tax rate is 15%.
#Write a function called add_tax.
#The function will expect one parameter - price (float) - the price of an item in dollars.
#The function will return the full price, including taxes, if applied (float).

def add_tax(price:float): #price of item in dollar
    if price >= 100:
        return price * 1.15 #tax over 100 dollar is 15%
    else:
        return price

#################################################

#3 : Count First Letter

#Write a function called count_first_letter.
#The function will expect one parameter: text, a string containing the text to analyze.
#The function will return the number of times the first letter appears in the text (int).

def count_first_letter(text):
    return text.count(text[:1])

print(count_first_letter("alaska"))

###################################################

# 4 : Reformat Birthdate

#After moving from Europe to the US, Jane found herself constantly struggling with date formats. She decided to write a simple program to automatically reformat her calendar's American-formatted dates into the more familiar European style.
#Write a function called reformat_date. The function will expect one parameter: date, a string in the format MM-DD-YYYY.
#The function will return the same date as a string in the format of DD/MM/YYYY.

def reformat_date(date:str):
    split_date = date.split("-")
    return f"{split_date[1]}/{split_date[0]}/{split_date[2]}"

print(reformat_date("12-25-2021"))

####################################################

#  5 : Pass or Fail

#As part of a university course, students were required to take two exams.
#To successfully complete the course, students needed to fulfill two conditions:
#Their average grade must be 75 or higher
#They must not receive a failing grade (55 or lower) on either exam.
#Write a function called has_passed.
#The function will expect two parameters called grade1 and grade2 (ints).
#The function will return a string “PASS” or “FAIL” according to the above conditions.

def has_passed(grade1, grade2):
    if (grade1 + grade2)/2 < 75: #if average grade is below 75
        return "FAIL"
    if grade1 <= 55 or grade2 <= 55:
        return "FAIL"
    return "PASS"

print(has_passed(60, 80))

####################################################

#  6 : Sentence, Period.

#The editor of a local newspaper has a recurring problem - the reporters hand in articles and forget to add a period at the end of the sentences.
#Write a function called period_adder.  The function will expect one parameter called sentence which holds a single sentence (str).
#The function will return the sentence (str) with a single period at the end, regardless of whether there was a period there in the first place.
#The only exception is sentences that end with a “!”, in which case there is no need to add a period.

def period_adder(sentence):
    if sentence[-1] == "!":
        return sentence
    return f"{sentence}."

####################################################

#  7 : Currency Converter Pro

#Let’s create a currency converter that can handle two directions of conversion: EUR (€) to USD ($) and vice versa.
#Write a function called convert that will receive a string like "$120" or "€50”, perform the conversion, and return it as a string with the other currency symbol.
#Use the following conversion rates:
#1 EUR = 1.10 USD
#You may assume that the input to the convert function will be a whole number.
#The returned price string should be up to 2 digits, you can do that using
     round(float_number, 2)
#Hint: Remember to use type conversion functions to perform arithmetic operations.

def convert(price:str):
    if price[0] == "€":
        extract_price = int(price[1:])
        dollar_price = round(extract_price * 1.10, 2)  #conversion 1 eur to 1 usd
        return f"${dollar_price}"
    extract_price = int(price[1:])
    euro_price = round(extract_price / 1.10, 2)  #conversion 1 eur to 1 usd
    return f"€{euro_price}"

print(convert("$110"))

####################################################

#  8 : Leap Year

#A leap year is a special year that contains an additional day. It’s used to keep our calendar in alignment with the Earth's revolutions around the Sun. It takes the Earth about 365.24 days to complete one full orbit around the Sun. As a result, if we didn't add a leap day approximately every 4 years, our calendar would slowly drift out of sync with the Earth's revolutions.
#Determining which years are leap years involves a few rules:
#The year must be evenly divisible by 4.
#Unless it’s also a century year (like 1900, 2000, etc.), and then it must also be divisible by 400 to be considered a leap year.
#Write a function is_leap that takes a year as input (int) and checks whether it's a leap year or not.
#If it is a leap year, return "Leap year" (str). If it's not a leap year, return "Not a leap year" (str).

def is_leap(year:int):
    if  year % 400 == 0:
        return ("Leap year")
    if year % 100 == 0:
        return ("Not a leap year")
    if year % 4 == 0:
        return "Leap year"
    return "Not a leap year"

print(is_leap(2020))
print(is_leap(2100))


##############
# Sprint 100/100
