# This lecture Introduces, conditionals in python

# For this we are testing if a person is Tall enough to ride a rollercoster
# If the person is Less than 120cm in height
# - We Allow else
# - We Dont Allow

# We have several Operators 

# >     Greater than
# <     Less than
# >=    Greater than or equal to
# <=    Less than or equal to
# ==    Compare Two Values

print("Welcome to the rollercoster")

height = int(input("What is your height in cm? "))

if height > 120:
    print("You can Ride a rollercoaster")
else:
    print("You can't Ride a rollercoaster")

