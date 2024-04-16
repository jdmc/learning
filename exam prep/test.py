class A:
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
C().do()


                