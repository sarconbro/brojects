# # 5 Transforming a list into a new list
# # 2. For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.

# verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
# ing = []
# for verb in verbs:
#     ing.append(verb + "ing")
# print(ing)

# # 3. Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.

# numbs = [5, 10, 15, 20, 25]
# newlist =[]
# for numb in numbs:
#     newlist.append(numb +5)
# print(newlist)

# ___
# 7 Accumulation results from a list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_sum = 0

for num in nums:
    my_sum += num
print(my_sum)

origlist = [45, 32, 88]
aliaslist = origlist
origlist += ['cat']
origlist = origlist + ['cow']
aliaslist += ['dog']


print(f'origlist is {origlist}')
print(f'aliaslist is {aliaslist}')

# 11 Chapter Assessment
# Palindrome

phrase = "was it a car or a cat I saw"

rev_phrase = phrase[::-1]

if phrase == rev_phrase:
    print('phrase ist a palindrome!')


# For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.

wrds = ["end", "work", "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for word in wrds:
    past_wrds.append(word + 'ed')
print(past_wrds)

# BONUS Write code to create a list of word lengths for the words in words. Assign the answer to a variable length_list. (You should use the len function).

words =  ["end", "work", "play", "start", "participate"]
length_list = []
for word in words:
        length_list.append(len(word))

#Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for char in str1:
    chars.append(char)

# For each word in the list words, double it so that boom becomes boomboom. Create a new list for the double words called double_words.

words = ["boom", "cry", "walk", "dream", "cool", "fly"]

double_words = []

for word in words:
    double_words += [word + word]


# In the following list there are numbers. numbers above 100 are considered “high” and the rest are “low”. Create two lists, high and low. Assign each number to the correct list automatically.

nums = [561,76,132,66,8921,8,0,-124,53]

high = []
low = []

for num in nums:
    if num > 100:
        high.append(num)
        continue
    low.append(num)

# oder 

nums = [561, 76, 132, 66, 8921, 8, 0, -124, 53]

high = [num for num in nums if num > 100]
low  = [num for num in nums if num <= 100]

# Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = [67, 80, 90, 78, 93, 20, 79, 89, 96, 97, 92, 88, 79, 68, 58, 90, 98, 100, 79, 74, 83, 88, 80, 86, 85, 52, 90, 100]

a_scores = 0
for score in scores:
    if score >= 90:
        a_scores += 1

# BONUS Update your code from the exercise above, so that we have two counters - a_scores for the number of grades that are above 90, and failed for the number of grades below 55.

scores = [67, 80, 90, 78, 93, 20, 79, 89, 96, 97, 92, 88, 79, 68, 58, 90, 98, 100, 79, 74, 83, 88, 80, 86, 85, 52, 90, 100]

a_scores = 0
failed = 0
for score in scores:
    if score >= 90:
        a_scores += 1
    if score < 55:
        failed += 1

# BONUS Write code to iterate through the list words and find the longest word in it. Assign the longest word to a variable called longest_word.

words =  ["end", "work", "play", "start", "participate"]

longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word