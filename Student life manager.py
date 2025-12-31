# Ephrem Adise
# UGR/0035/26
# Section 01
def calculate_average(total_sum, count):
    if count == 0:
        return 0
    return round(total_sum / count)

def evaluate_performance(average):
    if average >= 90:
        return "Excellent"
    elif 70 <= average <= 89:
        return "Good"
    else:
        return "Needs Improvement"
def can_afford(budget, cost):
    return cost <= budget

def body():
    name = input("Enter your name: ")
    budget = float(input("Enter your total monthly budget: "))
    total_grades = 0
    count = 0
    subjects = {}
    print("\nEnter the Subject name then your result one by one (type 'done' to finish):")
    while True:
        subject = input("Enter subject, type 'done' to finish: ").lower()

        if subject == "done":
            break
        grade_input = float(input(f"Enter your score for {subject}"))
        grade = float(grade_input)
        subjects[subject] = grade_input
        total_grades += grade
        count += 1

    average = calculate_average(total_grades, count)
    status = evaluate_performance(average)
    celebration_cost = float(input("\nCelebration meal cost: "))
    affordable = can_afford(budget, celebration_cost)

    print("\nSummary Report")
    print("Student Name:", name)
    print("Total number of Subjects:", count)
    for subject, grade_input in subjects.items():
        print(subject, " : ", grade_input)
    print("Final Average:", average)
    print("Performance Status:", status)
    if affordable:
        print("You can afford the celebration meal!")
    else:
         print("You can not afford the celebration meal!")

    return subjects, count, total_grades, budget, name

body()