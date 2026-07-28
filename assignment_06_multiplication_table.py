def print_single_table(num):
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

def print_tables_up_to_n(n):
    for num in range(1, n + 1):
        print_single_table(num)
        print("---------------------------")


num = int(input("Enter a number: "))
if num <= 0:
    print("Error: Please enter a positive number.")
else:
    print_single_table(num)

n = int(input("\nEnter a number N for tables 1 to N: "))
if n <= 0:
    print("Error: Please enter a positive number.")
else:
    print_tables_up_to_n(n)