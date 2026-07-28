# ==============================================================================
# PROGRAMMING FUNDAMENTALS - Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# ==============================================================================

def get_grade(score: float):
    """
    Validates score (0-100) and returns corresponding letter grade.
    Returns None if score is out of bounds.
    """
    if score < 0 or score > 100:
        return None
    
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    try:
        score_input = float(input("Enter student score (0-100): "))
        grade = get_grade(score_input)
        
        if grade is None:
            print("Error: Score must be between 0 and 100.")
        else:
            print(f"Grade: {grade}")
            
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()