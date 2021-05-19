# Say Hello to the user
print("Welcome to BMI Calculator:)")
# User Data 
weight = int(input("Please enter your weight in kg: "))
height = int(input("Please input your height in cm: "))
# Do some math
bmi = round(weight / ((height / 100) ** 2),1)
# show user the results
if bmi < 18.5 :
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25 :
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30 :
    print(f"Your BMI is {bmi}, You are overweight.")
elif bmi < 35 :
    print(f"Your BMI is {bmi}, You are obese.")
else:
    print(f"Your BMI is {bmi}, You are over obese.")