#39
""" 
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

#BC 
 """


""" def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='')
 """


""" 
def f(n):
    if n == 1:
        return 1
    return n + f(n-1)        
print(f(2))
 """
 
 #63
""" def f(n):
    for i in range(1, n+1):
        yield i
for i in f(2):
    print(i, end=" ") """
# print >  1 2

#73
""" 
class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass

x = Z()
z = Z()
print(isinstance(x,Z), isinstance(z,X)) 
"""

#66

""" 
s ="2a"
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
""" 
the_list = "alpha;beta;gamma".split(":")
the_string = " ".join(the_list)
print(the_string)
print(the_string.isalpha())    
    
    
the_string = "alpha;beta;gamma"[1:-1]
the_string = "".join(the_list)
print(the_string.isalpha())
   """
""" #92
string ="python"[::2]
print(string)
string = string[-1] + string[-2]
print(string)

string[0] == "o"
string is None
len(string) == 3
string[0] == string[-1] """

#97
""" 
class Class:
    __Var = 0
    def foo(self):
        Class._Class__Var += 1
        self.__prop = Class._Class__Var
        
o1 = Class()
o1.foo()
o2 = Class()
o2.foo()
print(o2._Class__Var + o1._Class__prop) """

#98
""" 
class Class:
    Variable = 0
    def __init__(self):
        self.value = 0
        
object_1 = Class()
object_1.Variable +=1
objetc_2 = Class()
objetc_2.value +=1
print (objetc_2.Variable + object_1.value) """

#101
""" 
class A:
    VarA = 1
    def __init__(self) -> None:
        self.prop_a=1
        
class B(A):
    VarA = 1
    def __init__(self) -> None:
        self.prop_b=2
        
obj_a = A ()
obj_aa = A ()
obj_b = B ()
obj_bb = obj_b

isinstance (obj_b,A)
A.VarA == 1
obj_a is obj_aa
B.VarA == 1 """

#102
""" 
class Class:
    Var = data = 1
    def __init__(self,value):
        self.prop = value
        
Object = Class(2)

"data" in Class.__dict__
"Var" in Class.__dict__ """

#104        
"""  [0,1,2] 
class MyClass:
    def __init__ (self, size):
        self.queue = [i for i in range(size)]
        
        def get(self):
            return self.queue
        def get_last(self):
            return self.queue[-1]   
        
        def add_new(self):
            #code
            # self.queue.append(self.get_last()+1)
            # self.queue.append(self.queue[-1]+1)
            pass
            
Object = MyClass(2)
Object.add_new()
print(Object.get())

# self.queue.append(self.get_last()+1)
# self.queue.append(get_last()+1)
# self.queue.append(self.queue[-1]+1)
# queue.append(get_last()+1) """

#108
""" 
my_list = [i for i in range(5)]
m = [my_list[i] for i in range(4,0,-1) if my_list[i] %2 !=0]
print(m) """

#133
""" 
def foo (x,y):
    return y(x) + y(x+1)
print (foo(1,lambda x:x*x)) """

#137
class Class:
    Variable = 0
    def __init__(self):
        self.value = 0
        
object_1 = Class()
Class.Variable +=1
object_2 = Class()
object_2.value +=1
print(object_2.Variable + object_1.value)