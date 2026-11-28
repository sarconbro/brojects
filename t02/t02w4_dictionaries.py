# 3. Dictionary Operations
# 3.2.  Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals).
#       In addition, remove the key-value pair of “Lochte”. Do not rewrite the dictionary.

# Don't change this line
swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}

del swimmers['Lochte']
swimmers['Phelps'] += 5

#_____________________-
# 4. Dictionary Methods
# 4.4. We have a dictionary with the events that Italy has won medals in, and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

events = list(medal_events.keys())

#______________________

# 5. Iterating over Dictionaries
# 5. dict-4-4: What is printed by the following statements?

total = 0
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
for key in mydict:
   if len(key) > 3:
      total = total + mydict[key]
print(total)


# 5.1. Using this dictionary of Italy medals and the keys method, count the total number of medals that Italy has won, and store the result into a variable called total_medals.

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

total_medals = 0
for event in medal_events.keys():
    total_medals += medal_events[event]

# 6. Iterating over Dictionaries
# 6.1. Once more, please count the total number of medals that Italy has won, and store the result into a variable called total_medals. But this time, do this using the values method.

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
total_medals = 0
for medals in medal_events.values():
    total_medals += medals

# 6.2. In the following dictionary you can see the numbers of medals the UK have won in each field, separated to Men and Women categories. Please count the total number of medals won by Women using the variable total_medals. Use the items method.

uk_medals = {
    'Shooting (Women)': 4,
    'Shooting (Men)': 4,
    'Fencing (Women)': 4,
    'Fencing (Men)': 2,
    'Judo (Women)': 6,
    'Judo (Men)': 2,
    'Swimming (Women)': 1,
    'Swimming (Men)': 3
}

total_medals = 0
for event, medal in uk_medals.items():
    if 'women' in event.lower():
        total_medals += medal
    continue

# 9 Chapter Assessment - Dictionaries

# A school has decided to use a Python dictionary to keep track of information about a student.
# In this dict, the keys are the field names (strings), and the values are their values (the type varies).
#
# Create a dictionary called student_info which will hold the information for the following student:
#
# name: Gemma Newton
# age: 17
# city: Brighton

student_info = {}
student_info['name'] = 'Gemma Newton'
student_info['age'] = 17
student_info['city'] = 'Brighton'

# The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics.
# Using dictionary iteration, print an output that looks like this:
# Italy - 12 Medals
# Brazil - 15 Medals
# and so on…
#
# Note: The order is not important. Hint: Use f-strings here, it’s fun!

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

for country, gold_count in golds.items():
    print(f'{country} - {gold_count} Medals')

# Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary iteration, print only the categories in which US had more than 5 medals.

US_medals = {"Swimming": 13, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 6, "Archery": 5, "Cycling - Track": 1, "Equestrian": 2, "Golf": 17, "Weightlifting": 1}

for category, medal_count in US_medals.items():
    if medal_count > 5:
        print(category)

#Create a dictionary, freq, that saves each character in the string str1 as the key, and the value is the frequency of the letter as the value.

str1 = "peter piper picked a peck of pickled peppers"

freq = {}
for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] += 1

# Provided is a list of car brands that were spotted on a single street. Create a dictionary, freq_brands, the cars as keys and the frequency in the street as the value

list_of_cars = ["Ford", "Toyota", "Hyundai", "Toyota", "Hyundai", "Ford", "Ford", "Toyota", "Toyota", "Toyota","Toyota", "Hyundai", "Toyota", "Hyundai", "Toyota", "Hyundai", "Ford", "Ford", "Ford"]

freq_brands = {}
for brand in list_of_cars:
    if brand not in freq_brands:
        freq_brands[brand] = 0
    freq_brands[brand] += 1