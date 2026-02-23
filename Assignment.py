def get_student_marks():
    marks = []
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
        marks.append(mark)
    return marks
def validate_marks(marks):
    return all(0 <= mark <= 100 for mark in marks)
def analyze_marks(marks):
    total = sum(marks)
    maximum = max(marks)
    minimum = min(marks)
    count = len(marks)
    average = total / count if count > 0 else 0
    print("\n--- MARKS ANALYSIS ---")
    print(f"Total Marks: {total}")
    print(f"Maximum Marks: {maximum}")
    print(f"Minimum Marks: {minimum}")
    print(f"Number of Subjects: {count}")
    print(f"Average Marks: {average:.2f}")
    print("\n--- SUBJECT-WISE MARKS ---")
    for index, mark in enumerate(marks, 1):
        print(f"Subject {index}: {mark}")
    passing_score = 40
    passed = list(filter(lambda x: x >= passing_score, marks))
    print(f"\n--- PASSED SUBJECTS (>= {passing_score}) ---")
    print(f"Passed Marks: {passed}")
    print(f"Passed Count: {len(passed)}")
    sorted_marks = sorted(marks)
    print(f"\n--- SORTED MARKS ---")
    print(f"Ascending: {sorted_marks}")
    print(f"Descending: {sorted(marks, reverse=True)}")
    difference = abs(maximum - minimum)
    print(f"\n--- DIFFERENCE ---")
    print(f"Absolute Difference (Max - Min): {difference}")
def main():
    print("=== STUDENT MARKS MANAGEMENT SYSTEM ===\n")
    marks = get_student_marks()
    if not validate_marks(marks):
        print("Error: Marks must be between 0 and 100!")
        return
    analyze_marks(marks)
main()