
def foo1(func):
    def foo2():
        print("I got decorated")
        func()
    return foo2

def foo3():
    print('I am ordinary')

pretty = foo1(foo3)
pretty()

'''
def foo1():
    return foo2()

def foo2():
    return foo3()

def foo3():
    print("In foo3")
    return 1

retval = foo1()
print(retval)
'''