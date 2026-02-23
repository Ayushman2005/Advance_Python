print("Enter your marks (-1 to stop)")
marks = []
while True:
    mark = float(input("Enter Mark: "))
    if mark == -1:
        break
    marks.append(mark)
print("Marks entered:", marks)
valid_marks = all(0 <= mark <= 100 for mark in marks)
if valid_marks:
    print(f"All marks are valid.{valid_marks}")
else:
    print(f"Some marks are invalid.{valid_marks}")
total = sum(marks)
maximum = max(marks)
minimum = min(marks)
count = len(marks)
print("\nStatistics:")
print(f"Total Marks: {total}")
print(f"Maximum Mark: {maximum}")
print(f"Minimum Mark: {minimum}")
print(f"Number of Subjects: {count}")
print("Subject wise marks:")
for index, mark in enumerate(marks,1):
    print(f"Subject {index}: {mark}")
passing_marks = list(filter(lambda x: x >= 40, marks))
print("Passing Marks:", passing_marks)
print("Number of Passing Marks:", len(passing_marks))
sorted_marks = sorted(marks)
print("Sorted Marks :", sorted_marks)
difference = abs(maximum - minimum)
print(f"Difference between highest and lowest marks: {difference}")