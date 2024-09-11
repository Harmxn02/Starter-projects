iterations = int(input("How many times would you like to flip the coin: "))

while iterations < 1:
    iterations = int(input("How many times would you like to flip the coin: "))


from random import randint


def flip_coin():
    log = {
        "heads": 0,
        "tails": 0
    }
    
    for i in range(iterations):
        if (randint(1, 2) == 1):
            log["heads"] += 1
        else:
             log["tails"] += 1
    

    print(log)



flip_coin()