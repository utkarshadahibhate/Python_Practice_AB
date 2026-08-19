## Generator function mimicking range function

def myrange(m):
    i = 0
    while i < m:
        i += 1
        yield i ## this function uses 'yield' to return values lazily one by one
                    # until i reaches m

r = myrange(5)  ## creates an iterable object
print(next(r))
print(next(r))
print(next(r))
print(next(r))

print()
## Generator function cycling through days of the week infinitely
def days():
    days = ['Sun','Mon','Tue','Wed','Thurs','Fri','Sat']
    i = 0
    while True:
        yield days[i]
        i = (i + 1) % 7  # taking the remainder

day_generator = days()
print(next(day_generator))  # remainder = 1
print(next(day_generator))  # 2
print(next(day_generator))  # 3
print(next(day_generator))  # 4
print(next(day_generator))  # 5
print(next(day_generator))  # 6
print(next(day_generator))  # 7
print(next(day_generator))  # 1
print(next(day_generator))  # 2

