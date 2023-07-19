
# Function that uses if statements and inputs to display final grade and percentage
def finalgrade(name, homework, assessment, finalExam, grade):
    return f" {name}, your final ICT percentage is {calc}%. Your grade is {grade}"

# Inputs needed for grade calculations 
name = input("Input Student Name: ")
homework = int(input("Input Student Homework Score: "))
assessment = int(input("Input Student Assessment Score: "))
finalExam = int(input("Input Student Final Exam Score: "))

# If statements to calculate what percentage would be what grade
calc = int((homework + assessment + finalExam)/175*100)
if calc >= 80:
        grade = "A"
elif calc >= 70:
        grade = "B"
elif calc >= 60:
        grade = "C"
elif calc >= 50:
        grade = "D"
elif calc >= 40:
        grade = "E"
elif calc < 40:
        grade = "You Failed"

print(finalgrade(name, homework, assessment, finalExam, grade))