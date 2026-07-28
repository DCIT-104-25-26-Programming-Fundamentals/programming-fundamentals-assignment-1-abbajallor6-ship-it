def add_student(students):
    name = input("Student name: ")
    id = input("Student ID: ")
    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)
    
    student = {"name": name, "id": id, "scores": scores}
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_students(students):
    if not students:
        print("No students added yet.")
        return
    
    print("-" * 50)
    print(f"{'Name':<20} {'ID':<10} {'Scores':<20} {'Average':<10}")
    print("-" * 50)
    for s in students:
        avg = sum(s['scores']) / len(s['scores']) if s['scores'] else 0
        scores_str = ', '.join(map(str, s['scores']))
        print(f"{s['name']:<20} {s['id']:<10} {scores_str:<20} {avg:.2f}")
    print("-" * 50)

def calculate_average(students):
    id = input("Enter student ID: ")
    for s in students:
        if s['id'] == id:
            avg = sum(s['scores']) / len(s['scores']) if s['scores'] else 0
            print(f"{s['name']}'s average score: {avg:.2f}")
            return
    print("Student ID not found.")

def main():
    students = []
    while True:
        print("\n================================")
        print("STUDENT RECORD SYSTEM MENU")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            calculate_average(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()