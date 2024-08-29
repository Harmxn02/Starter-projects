


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 | i % 5) == 0:
            print(f"{i} - Fizz Buzz")
        if (i % 3) == 0:
            print(f"{i} - Fizz")
        if (i % 5) == 0:
            print(f"{i} - Buzz")
        else:
            print(f"{i}")
        

    
fizzbuzz()