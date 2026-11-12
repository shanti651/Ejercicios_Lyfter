price = int(input("Enter the product price"))
discount = 0
if (price < 100):
    discount = price * 0.02
    price = price - discount
else:
    discount = price * 0.10
    price = price - discount

print(f"The discount is {discount}")
print(f"The final price is {price}")