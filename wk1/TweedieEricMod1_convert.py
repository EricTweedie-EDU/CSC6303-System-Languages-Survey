# Eric Tweedie CSC6303 week 1
# Python code to find the factorial of a number provided by the user
def fact():
    n = int(input("Enter a positive Integer: "))
    while ((n < 0)):
        n = int(input("Sorry, only positive numbers, enter again: "))
    if (n == 0):
        print("The factorial of 0 is 1")
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        print("The factorial of ", n, "is ", f)

fact()