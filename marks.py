def analyze_marks(marks):
    if len(marks) == 0:
        return 0, 0, 0, "No Data"

    total = sum(marks)
    average = total / len(marks)

    highest = max(marks)
    lowest = min(marks)

    # Grade system
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return average, highest, lowest, grade


# Input marks
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Analyze
avg, high, low, grade = analyze_marks(marks)

# Output
print("Average:", avg)
print("Highest:", high)
print("Lowest:", low)
print("Grade:", grade)
