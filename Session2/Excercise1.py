a = int(input("Enter your height (cm) "))
b = int(input("Enter your weight (kg) "))
c = a*0.01
bmi = b/(c*c)
if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")