def calculate_discount(price, discount_percent):
    if discount_percent >= 20: 
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price 

# Getting user input
original_price = float(input("Enter the original price: "))

discount_percent = float(input("Enter the discount percentage: "))

# The final price
final_price = calculate_discount(original_price, discount_percent)

# Printing the results
print("Final price: ", final_price)
