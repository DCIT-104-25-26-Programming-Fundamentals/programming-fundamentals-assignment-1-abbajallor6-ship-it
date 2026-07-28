def print_fibonacci(n):
    if n <= 0:
        print("Error: Please enter a positive number.")
        return
    
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    print(f"Fibonacci sequence: {' '.join(map(str, sequence))}")

def check_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")

def print_fibonacci(n):
    if n <= 0:
        print("Error: Please enter a positive number.")
        return
    
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    print(f"Fibonacci sequence: {' '.join(map(str, sequence))}")

def check_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")