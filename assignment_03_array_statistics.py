
def calculate_sum(numbers: list[float]) -> float:
    """Calculate the total sum using a loop (no built-in sum())."""
    total = 0.0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers: list[float]) -> float:
    """Calculate the average value."""
    if not numbers:
        return 0.0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers: list[float]) -> float:
    """Find the maximum value using a loop (no built-in max())."""
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def find_minimum(numbers: list[float]) -> float:
    """Find the minimum value using a loop (no built-in min())."""
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


def main():
    try:
        count = int(input("How many numbers? "))
        
        # Input validation: N must be a positive integer
        if count <= 0:
            print("Error: The number of elements must be a positive integer.")
            return

        numbers = []
        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        # Output statistical calculations
        print("\nResults:")
        
        # Display sum (formatted nicely if it's a clean integer)
        total_sum = calculate_sum(numbers)
        print(f"Sum: {int(total_sum) if total_sum.is_integer() else total_sum}")
        
        # Display average
        avg = calculate_average(numbers)
        print(f"Average: {avg:.1f}" if avg % 1 != 0 else f"Average: {avg:.0f}")
        
        # Display max and min
        max_val = find_maximum(numbers)
        min_val = find_minimum(numbers)
        print(f"Maximum: {int(max_val) if max_val.is_integer() else max_val}")
        print(f"Minimum: {int(min_val) if min_val.is_integer() else min_val}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()