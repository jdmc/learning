""" class A:
    def a(self):
        print("A", end="")
        def b(self):
            self.a()
class B(A):
    def a(self):
        print("B", end="")
        def do(self):
            self.b()
class C(A):
    def a(self):
        print("C", end="")
        def do(self):
            self.b()
                        
B().do()
C().do() """


""" def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='')
 """


""" def f(n):
    if n == 1:
        return 1
    return n + f(n-1)        
print(f(2))
 """
 
def f(n):
    for i in range(1, n+1):
        yield i
for i in f(2):
    print(i, end=" ")