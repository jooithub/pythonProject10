# section3.py

# super() and __init__()

# Refer
# https://arvimal.wordpress.com/2016/07/01/inheritance-and-super-object-oriented-programming/
# https://github.com/arvimal/Python-and-OOP/blob/master/42-super-3.py

class A(object):
    def foo(self):
        print("A")


class B(A):
    def AA():
        def foo(self):
            print("B")

    AA()


class C(A):
    def foo(self):
        print("C")
           super(C, self).foo()


class D(B, C):
    def foo(self):
        self.BAS()

    def BAS(self):
        print("D")
        super(D, self).foo()


d = D()
d.foo()
