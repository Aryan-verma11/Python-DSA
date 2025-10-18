# Function to print Fibonacci series using recursion

def fibonacci(n):
    # Base cases: if n is 0 or 1, return n
    # Because Fibonacci(0) = 0 and Fibonacci(1) = 1
    if n <= 1:
        return n
    
    # Recursive case:
    # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

# Input: number of terms in the series
num = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(num):
    # Print each term by calling the recursive function
    print(fibonacci(i))
