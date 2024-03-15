class DataContextManager:
    def __init__(self):
        print("Inicio contexto")
    
    def __enter__(self):
        print("Abriendo contexto")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Cerrando contexto")
        return True
    

ctx_mgr = DataContextManager()

with ctx_mgr as mgr:
    print("Dentro del contexto")
    print(id(mgr))

print('Otra operación fuera del contexto')