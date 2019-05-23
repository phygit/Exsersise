format = input ("if you use kg and meter pls put YES other wise NO :")
weight = float (input ("please enter your weight : "))
height = float (input ("please enter your height : "))

bmi = round((weight / (height * height)), 2)

if format != "YES" :

    bmi = bmi*703

print(bmi)

