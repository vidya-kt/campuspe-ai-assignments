marks = []
fail = False

for i in range(5):
    m = int(input(f"Enter the marks for Subject {i+1}: "))

    if m<=40:
        fail = True

    marks.append(m)

#Marks in each subject
print("\nMarks in each subject:")
for i in range(5):
    print(f"Subject {i+1}:",marks[i])

#Total marks
total_marks = sum(marks)
print("Total Marks:",total_marks,"out of 500")

percentage = (total_marks/500)*100
print("Percentage:",percentage)

#Grade based on percentage
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "c (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

print("Grade:", grade)

#Result based on subject marks
if fail:
    result = "Fail"
else:
    result = "Pass"

print("Result:",result)