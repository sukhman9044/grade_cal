
#This program is for grade cal
#=============================

#this is the score
score =float (input("enter your score:"))
#this is the total points
tp =int (input("enter your total points:"))

#formula 
tgrade= float (score / tp * 100)

#round grade
grade = round(tgrade, 2)

print("Your grade is", grade,"%")













