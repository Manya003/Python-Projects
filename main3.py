def A():
    print("A")
    B()

def B():
    print("B")
    C()

def C():
    print("C")

A()

lst = [x for x in range(5)]
print(lst)