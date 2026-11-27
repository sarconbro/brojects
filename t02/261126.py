# Säcke voller Gold
from statistics import median

sacks = [2.33, 4.1, 8.5, 6.66, 2.4]
total_gold=0
for s in sacks:
    total_gold+=s

print(total_gold)


# Die Flucht
sacks = [2.33, 4.1, 8.5, 6.66, 2.4]
total = 0
for s in sacks:
    if s <= 5:
        total += s
print(total)

# Pechsträhne

necklaces = [12, 13, 22, 18, 13, 10, 30, 15, 13, 12]

badluck = 0
for necklace in necklaces:
  if necklace == 13:
    badluck = badluck + 1
print(f"Pechsträhne: {badluck}")

# Häufige Namen

names = ["Emma", "Felix", "Henry", "Linn", "Lina", "Felix", "Hannah", "Noah", "Marie", "Leon"]

starts_with_H = 0
starts_with_L_and_len_equals_4 = 0

for name in names:
  if name[0] == "H":
    starts_with_H = starts_with_H + 1
  elif name[0] == "L" and len(name) == 4:
    starts_with_L_and_len_equals_4 =  starts_with_L_and_len_equals_4 + 1

print(
    f"Häufige Namen:\n"
    f"* Namen beginnend mit 'H': {starts_with_H}\n"
    f"* Namen beginnend mit 'L' und 4 Buchstaben lang: {starts_with_L_and_len_equals_4}"
)

# Lagerhaus

boxes = [8, 4, 6]
total_boxes = boxes[0] + (boxes[0] * boxes[1]) + (boxes[0] * boxes[1] * boxes[2])
print(f'There is a total of {total_boxes} boxes.')


boxes = [8, 4, 6]
total_boxes = 0
current_level = 1
for box in boxes:
  current_level = current_level * box
  total_boxes = total_boxes + current_level
print(total_boxes)

boxes = [8, 4, 6]
large_boxes = boxes[0]
medium_boxes = large_boxes * boxes[1]
small_boxes = medium_boxes * boxes[2]
total_boxes = large_boxes + medium_boxes + small_boxes
print(total_boxes)




#AAH Danke!! Häckerinnen machen ja 'total_boxes += box', ich bin da allerdings etwas langsam - und ich vertue mich häufig mit listenname, itertionsitem usw. <3

grades = [1.0, 2.1, 1.5, 3.0, 1.0, 1.2, 3.5, 1.0]

sum = 0
for grade in grades:
  sum = sum + grade

average = sum/len(grades)

print(f"Durchschnitt: {average}")

# Bonus: 5km-Lauf

times = [31.3, 29.8, 29.4, 30.3, 28.9, 29.4]
fastest=0
for t in times:
    if t > fastest:
        fastest = t
print(fastest)