# Number of terms to generate
n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a, b = 0, 1

print("Fibonacci Series:")

for _ in range(n):
    print(a, end=' ')
    # Calculate the next number
    a,b=b,a+b 