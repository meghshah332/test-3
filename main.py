students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 88,
    "Rohan": 95
}

total = 0

for score in students.values():
    total = total + score

average = total / len(students)

print("Class Average:", average)

highest_score = max(students.values())
lowest_score = min(students.values())


for name in students:
    if students[name] == highest_score:
        print("Highest Score:", name, highest_score)
    if students[name] == lowest_score:
        print("Lowest Score:", name, lowest_score)

print("highest score ",highest_score)
print("lowest score ",lowest_score)

input_score =input("Enter a NAME to check score: ")

score=students.get["name"]
print("Score of", input_score, "is:", score)

if input_score is None:
    print("try another name")
else:
    print("thank you")