## a recursive function calls itself to simplify a problem into smaller sub problems

## recursive function to print numbers from 1 to n
def num(n):
    if n > 0:   # base condition
        print(n)
        num(n - 1)  #recursive call

print("recursive call output--")
num(5)

## recursive call to calculate factorial
def fact(n):
    if n <= 0: # base condition
        return 1
    else:
        return n * fact(n - 1)

print('factorial is:',fact(5))