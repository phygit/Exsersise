format = input ("if you use kg/meter pls put YES if Pound/inc put No :")
weight = float (input ("please enter your weight : "))
height = float (input ("please enter your height : "))


if format.lower() != "yes" :

    bmi = round((weight / (height * height)), 2)*703
else :

    bmi = round((weight / (height * height)), 2)
print(bmi)



if bmi < 18.5 :
    print("under weight")
if bmi > 30 :
    print("obesity")
elif 18.5 < bmi < 25 :
    print("Normal")
else :
    print("overweight")


