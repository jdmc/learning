from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Entrando en el contexto")
    val = object()
    print(id(val))
    try:
        yield val
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Saliendo del contexto")


with my_context_manager() as ctx:
    print("Dentro del contexto")
    print(id(ctx))
    print(id(ctx))
    #raise Exception("Error desde el with (context)")

print("Fuera del contexto")

