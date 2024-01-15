# function to add two numbers
def add(m, s):
    return m + s

# function to subtract two numbers
def subtract(m, s):
    return m - s

# function to multiply two numbers
def multiply(m, s):
    return m * s

# function to divide two numbers
def divide(m, s):
    return m / s


print("Select operation...")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    ch = input("Enter choice : ")

    # check if choice is one of the four options
    if ch in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif ch == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif ch == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif ch == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        
        # check if user wants to do more calculation
        # break the while loop if answer is no
        p = input("Do you want to do next calculation? (yes/no) : ")
        if p == "no":
          break
    else:
        print("Invalid Input")
