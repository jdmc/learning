import threading

def proceso1():
    for i in range(5):
        print("Proceso 1")


def proceso2():
    for i in range(5):
        print("Proceso 2")

def proceso3():
    for i in range(5):
        print("Proceso 3")


#proceso lineal
#proceso1()
#proceso2()
#proceso3()
        

#proceso concurrente
t1 = threading.Thread(target=proceso1)
t2 = threading.Thread(target=proceso2)
t3 = threading.Thread(target=proceso3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Final de programa")


