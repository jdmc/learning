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
 
""" def f(n):
    for i in range(1, n+1):
        yield i
for i in f(2):
    print(i, end=" ") """
    
""" s ="2a"
try:
    n= int(s)
except TypeError:
    n=3
except LookupError:
    n=2
except:
    n=1
    print(n) """
    
""" class E (Exception):
    def __init__(self,message):
        self.message = message
        def __str__(self):
            return "It's nice to see you"
        
try:
    print("I feel fine")
    raise Exception ("What a pitty")
except E as e:
    print (e)
else:
    print("the show must go on") """
    
""" string = str(1/3)
dummy = ''
for character in string:
    dummy = character + dummy
print(dummy[-1]) """

#90
the_list = "alpha;beta;gamma".split(":")
the_string = "".join(the_list)
print(the_string.isalpha())    
    
    
            
        