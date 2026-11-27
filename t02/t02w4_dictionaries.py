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