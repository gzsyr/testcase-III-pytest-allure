def extend(func):
    def hello(*args, **kwargs):
        print("begin")
        func(*args, **kwargs)
        print("end")
    return hello

@extend
def tmp1():
    #print("begin")
    print("tmp1")
    #print("end")

@extend
def tmp2():
    #print("begin")
    print("tmp2")
    #print("end")

def test_01():
    tmp1()
    tmp2()