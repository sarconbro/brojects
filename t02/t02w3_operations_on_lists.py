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

