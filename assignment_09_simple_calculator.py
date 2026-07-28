# ==============================================================================
# TASK: Console-Based Simple Calculator
# ==============================================================================

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a: float, b: float):
    if b == 0:
        return None
    return a % b


def power(a: float, b: float) -> float:
    return a ** b


def display_menu():
    print("\n==============================")
    print("      SIMPLE CALCULATOR       ")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def format_number(val: float) -> str:
    """Formats a float as an int string if it has no fractional part."""
    if val.is_integer():
        return str(int(val))
    return str(val)


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == '7':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Error: Invalid choice. Please select a number between 1 and 7.")
            continue

        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid number entered.")
            continue

        n1_str = format_number(num1)
        n2_str = format_number(num2)

        if choice == '1':
            res = add(num1, num2)
            print(f"Result: {n1_str} + {n2_str} = {format_number(res)}")

        elif choice == '2':
            res = subtract(num1, num2)
            print(f"Result: {n1_str} - {n2_str} = {format_number(res)}")

        elif choice == '3':
            res = multiply(num1, num2)
            print(f"Result: {n1_str} * {n2_str} = {format_number(res)}")

        elif choice == '4':
            res = divide(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {n1_str} / {n2_str} = {res}")

        elif choice == '5':
            res = modulus(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {n1_str} % {n2_str} = {format_number(res)}")

        elif choice == '6':
            res = power(num1, num2)
            print(f"Result: {n1_str} ** {n2_str} = {format_number(res)}")


if __name__ == "__main__":
    main()