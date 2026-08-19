## to create a generator to yield a flatten list from nested list

L1 = [1,2,[3,4,[5,6,7],8],9,[10,11]]

def flatten(L):
    for ele in L:
        if hasattr(ele,'__iter__'):
            yield from flatten(ele) ## flatten recursively
        else:
            yield ele

flat = flatten(L1) ## will create a generator object

flat_list = list(flat)  ## will store the generator output in a list
print("Flatten list is \n",flat_list)