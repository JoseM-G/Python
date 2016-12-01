#Jose Martinez
#jmarti85@ucsc.edu
#programming assignment 2
#This program takes in a user specified number of grades and calculates the average of the user inputed grades. The desired input being a grade, the range of acceptable inputed grades is from 0 to 100. The program also comments on the class average depending if it is below or above a 70.


def Average():
    Sum = 0
    total_grades = eval(input("How many grades will you be entering? "))
    if type(total_grades) == float:
        for i in range(1000):
            total_grades = eval(input("You can't enter "+str(total_grades)+" grades! How many will you be entering? "))
            if type(total_grades) == int:
                break

            
    for j in range(total_grades):
        grade = eval(input("Please enter a grade between 0 and 100: "))
        if grade > 100 or grade < 0:
            for k in range(1000):
                grade = eval(input("Your number is out of range! Please enter a grade between 0 and 100: "))
                if grade <= 100 and grade >= 0:
                    break
        Sum = Sum + grade

        
    Average = Sum / total_grades
    if Average >= 70:
        print("Your class did great! The average was ", Average)
    if Average < 70:
        print("Your class did poorly. The average was ", Average)
    


Average()
