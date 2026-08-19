## fibonacci series using generator function
def fab(m):
    a,b = 0,1

    for i in range(m+1):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    num = 10
    for terms in fab(num):
        print(terms, end=" ")


