def factorial(number):
    factorial = 1
    if number > 0:
        for i in range(1, number+1):
            factorial=factorial*i
        print("Result ----> ", factorial)
    elif number == 0:
        print("Result ----> 0")
    else:
        print("There is no factorial negative numbers")


x = int(input("Enter a number: "))
factorial(x)
