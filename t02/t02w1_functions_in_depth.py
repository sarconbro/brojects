# Keyword Parameters

def final_price(price, vat):
    final = price + price * (vat / 100)
    return final


print(final_price(price=100, vat=17))
print(final_price(vat=17, price=100))  # The order doesn't matter!


def final_price(price, vat):
    final = price + price * (vat / 100)
    print(final)


#final_price(price=100, 17) #SyntaxError - wenn man ein keyword argument genutzt hat, muss man auch keyword arguments
#                             für die anderen nutzen.

# Mixing optional and Keyword Parameters <3

def final_price(price, vat=17):
    final = price + price * (vat / 100)
    print(final)


final_price(100, vat=25)
final_price(price=100)
final_price(100, 17)
final_price(price=100, vat=25)
final_price(100)
final_price(100,25)
final_price(100, vat=25)

# Check your understanding

#func-5-5: What value will be printed for z?
#
def f(x, y=3, z=7):
    print("x, y, z are:", x, y, z)

f(2, 5)
#
# A. 2
# B. 3
# C. 5
# D. 7 X
# E. Runtime error since not enough values are passed in the call to f

# func-6-6: What value will be printed for y?
#
def f(x, y=3, z=7):
     print("x, y, z are:", x, y, z)

 f(2, z=10)
#
# A. 2
# B. 3 X
# C. 5
# D. 10
# E. Runtime error since no value is provided for y, which comes before z

# func-6-7: What value will be printed for x?
#
 def f(x, y=3, z=7):
     print("x, y, z are:", x, y, z)

 f(2, x=5)

# A. 2
# B. 3
# C. 5
# D. 7
# E. Runtime error since two different values are provided for x X

#func-6-8: What value will be printed for z?
#
def f(x, y=3, z=7):
    print ("x, y, z are:", x, y, z)

f()

#A. 2
#B. 7
#C. 0
#D. Error!