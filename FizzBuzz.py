def multiples(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return 1
    
for i in range (1, 101):
    result = multiples(i)

