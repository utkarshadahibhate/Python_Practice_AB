#iterators on list
print("-----List------")
L1 = [4,3,8,9,2,5,10,50]
it_1 = iter(L1) #iterator function returns an iterator on the list
print(next(it_1))   # next retrieves each element sequentially until the list is exhausted
print(next(it_1))
print(next(it_1))
print(next(it_1))
print(next(it_1))
print(next(it_1))
print(next(it_1))
print(next(it_1))
# print(next(it_1)) # will throw StopIteration error as the list has ended

# iterators on other iterable types
## Tuple
print("-----Tuple-------")
T1 = (4,3,8,9,2,5,10,50)
it_2 = iter(T1)
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))
print(next(it_2))


## Set (unordered)
print("------Set-----")
S1 = {10,20,30,40,50,60}
it_3 = iter(S1)
print(next(it_3))
print(next(it_3))
print(next(it_3))
print(next(it_3))
print(next(it_3))
print(next(it_3))

## Dictionary
print("-----Dictionary------")
D1 = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60}
it_4 = iter(D1)
print(next(it_4))   # will print key of the dictionary
print(next(it_4))
print(next(it_4))
print(D1[next(it_4)]) # [] will give the element
print(D1[next(it_4)])
print(D1[next(it_4)])


## String
print("----String-----")
String = "Hello"
it_5 = iter(String)
print(next(it_5))
print(next(it_5))
print(next(it_5))
print(next(it_5))

## range function
print("-----range function-----")
r = range(3,10)
it_6 = iter(r)
print(r)
print(next(it_6))
print(next(it_6))
print(next(it_6))
print(next(it_6))
