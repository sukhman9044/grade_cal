
#This program is for grade cal
#=============================

#this is the score
score = float(input("enter your score:"))
#this is the total points
tp =int (input("enter your total points:"))

#formula 
tgrade= float (score / tp * 100)

#round grade
grade = round(tgrade, 2)

#Letter grade

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"


print("Your grade is", grade,"%,", "which is a", letter)













