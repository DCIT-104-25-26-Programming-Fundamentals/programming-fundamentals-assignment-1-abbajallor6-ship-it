def is_prime(number):
    """
    Checks whether a given integer is a prime number.
    Returns True if prime, False otherwise.
    """
    # Numbers less than 2 are NOT prime
    if number < 2:
        return False

    # Check for factors from 2 up to the square root of the number
    # (Checking up to int(number**0.5) + 1 is efficient, or range(2, number))
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, so it's not prime

    return True  # No divisors found, so it is prime


# Main execution block
def main():
    # Get integer input from user
    num = int(input("Enter a number: "))

    # Check primality and display expected output
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")


if __name__ == "__main__":
    main()