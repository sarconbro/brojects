# TUPLES
# 2 Tuple Packing
# 2.2. Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.

practice = 'y', 'h', 'z', 'x'

# 2.3. Change the following function neighbours so that it returns a tuple instead of a list. Don’t use parentheses!

def neighbours(num):
   return num - 1, num + 1

result = neighbours(10)
print(result)
print(type(result))

# 3. Tuple Unpacking
# 3.1. Try to make the print function work without changing it.

product_name, product_price = ("Coke bottle", 2.2)  # Tuple for name, price
print(f"Hey! In order to buy the product {product_name} you would need to pay {product_price}$ which is {product_price*100} cents")

# 4. Swapping values
# 4.1. Swap the variables so the values fit the names of the variables. Use only tuple swapping and not hardcoding!

first = "2"
second = "3"
third = "1"

first, second, third = third, first, second

print(first, second, third)


