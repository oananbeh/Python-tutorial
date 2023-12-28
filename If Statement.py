number = 5
if number > 10:
    print("This number is positive.")

else:
    print("This number is not positive")

number = 6
if number > 0:
    print("This number is positive.")
elif number == 0:
    print("This number is zero.")
else:
    print("This number is negative.")

number = 4

if number % 2 == 0:
  print(number, "is even")
else:
  print(number, "is odd")

age = 17

if (age >= 18):

  print("You are eligible to vote.")
else:
  print("You are not eligible to vote yet.")

grade = 85
if grade >= 90:
    print("Excellent!")
elif grade >= 80:
    print("Very good!")
else:
    print("Keep working hard!")


age = 16
eligibility = "You are eligible to vote." if age >= 18 else "You are not eligible to vote yet."
print(eligibility)  

quantity=5
original_price=10
discount = 10 if quantity > 10 else 5
price = original_price - (original_price * discount / 100)
print(price)