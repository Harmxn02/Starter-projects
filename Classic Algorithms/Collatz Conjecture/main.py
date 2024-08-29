import collections.abc as c


def collatz(num):
    steps = 0
    path = [num]
    
    while num != 1:
        if (num % 2) == 0:
            num = num / 2
            path.append(int(num))
        else:
            num = (num * 3) + 1
            path.append(int(num))
        
        steps += 1

    # print("steps: " + str(steps))

    return path



if __name__ ==  "__main__":
    print(collatz(7))