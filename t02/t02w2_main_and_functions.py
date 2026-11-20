def get_prices_and_percent_from_user():
    get_prices = input("Please enter the prices separated by commas: ")
    list_of_prices_string = get_prices.split(",")
    list_of_prices_float = []
    for price in list_of_prices_string:
        list_of_prices_float.append(float(price))
    percent = float(input("Please enter the discount percentage: "))
    return list_of_prices_float, percent

def apply_manipulation_on_price(price, percent, discount=True):
    if discount:
        return price * (1 - percent / 100)
    else:
        return price * (1 + percent / 100)

def apply_discount_on_a_list_of_prices(list_of_prices, percent):
    discounted_prices = []
    for price in list_of_prices:
        discounted_price = apply_manipulation_on_price(price, percent, discount=True)
        discounted_prices.append(discounted_price)
    return discounted_prices

def main1():
    list_of_prices_float, percent = get_prices_and_percent_from_user()
    discounted_prices = apply_discount_on_a_list_of_prices(list_of_prices_float, percent)
    print("Discounted prices:", discounted_prices)

#_______


def get_price_and_amount():
    input_price = input("Please enter the price: ")
    price = float(input_price.strip('$'))
    input_amount = input("Please enter the amount the customer gave: ")
    amount = float(input_amount.strip('$') )
    return price, amount

def calculate_price_plus_tax(price, tax_rate=0.115): # tax rate is 11.5%
    price_plus_tax = price * (1 + tax_rate)
    return price_plus_tax

def calculate_change_for_customer(price_plus_tax, amount):
    change = amount - price_plus_tax
    return change

def main2():
    price, amount = get_price_and_amount()
    price_plus_tax = calculate_price_plus_tax(price)
    print(f"The price plus tax is: {price_plus_tax:.2f} $")
    change = calculate_change_for_customer(price_plus_tax, amount)
    print(f"The change for the customer is: {change:.2f} $")

main2()