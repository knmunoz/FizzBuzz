def multiples(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        return 1
    
for i in range (1, 101):
    result = multiples(i)

    if result == 1:
        print(i)