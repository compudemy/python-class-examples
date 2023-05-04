# Nested If's

# In This example, we check if the age of the person trying
# to book is less than 12 years olds - he/she then pays $5 and
# to check if the person is between 13 and 19 then he pays $7 and finally
# if the person is older than 19 years old he/she pays $12

print("Welcome to the rollercoaster")

height = int(input("What is your age in cm "))

if height >= 120:
    print("You can Ride a rollercoaster")
    age = int(input("What is your age "))
    if age < 12:
        print("You Pay $5")
    elif age <= 19:
        print("You pay $7")
    else:
        print("You Pay $12")
else:
    print("You can't Ride a rollercoaster")