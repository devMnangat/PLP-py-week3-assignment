# function to calculate discount

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (100 - discount_percent) / 100  # discount_percent / 100
    else:
        return price


input_price = float(input("Enter the price: "))
input_discount = float(input("Enter the discount: "))
result = calculate_discount(input_price, input_discount)
print("The final price is: ", result)