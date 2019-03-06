for i in range(1, int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(f'{i:{i}<{i}}')  # Nice answer, but I'm using strings
    # oh, ok - N is less than 10
    print((111111111 * i) // (10 ** (10 - i - 1)))  # Trick is the whole number division!

