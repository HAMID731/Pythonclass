def get_grade():
    students = int(input("Enter number of students: "))
    subjects = int(input("Enter number of subjects: "))
    scores = []

    for i in range(students):
        print(f"Enter scores for Student {i + 1}:")
        student_scores = []
        for j in range(subjects):
            while True:
                score = int(input(f"Subject {j + 1}: "))
                if 0 <= score <= 100:
                    student_scores.append(score)
                    break
        scores.append(student_scores)

    print("\nClass Summary:")
    for i in range(students):
        total = sum(scores[i])
        print(f"Student {i + 1}: Total = {total}, Average = {total // subjects}")

