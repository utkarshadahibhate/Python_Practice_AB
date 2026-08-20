## global and local variables
## Local variables -
#   declared inside a function, accessible only inside that function.

## Global variables
# declared outside of all functions, at the script/module level.
# Accessible anywhere in the program, including inside functions.

## Modifying global variable inside a function
#  To modify global variable inside a function, declare 'global varname' at the beginning
#   of the function

## local variable inside a function
def fun():
    a = 10
    print('local: ',a)

fun()

## global variable accessed inside a function
print('\n------to access global inside a function--------')
g = 5.25
def fun():
    a = 10
    print('local: ',a)  # local variable
    print('global', g)  # reading global variable inside a function
print('outside_1: ', g)

fun()
print('outside_2: ',g)

## modifying global variable inside a function without global keyword
print("\n-----modify global without keyword----")
g = 5.25
def fun():
    a = 10
    g = 199
    print('local: ',a)
    print('global (local g): ',g) ##creates new local g, does not change global g

print('Outside_1: ',g)
fun()
print('Outside_2: ',g)

## variable declared after function call causes error
# def fun():
#     print(g_1) ## attempt to print global variable
## output: NameError: name g_1 is not defined

# fun()
# g_1 = 5.25    ## declared after fun is called

## using locals() and globals()
print("\n------using locals() and globals()-------")
x, y, z = 5, 1.25, "hi" # global variables

def fun():
    a, b, c = 1, 2, 3
    print("Locals : ",locals()) # dictionary of local variables
    print("Globals : ",globals())   #dictionary of global variables

fun()