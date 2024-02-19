from ficheros import escribir_data, leer_data

if __name__ == "__name__":
    #escribir_data('items.txt', 'Hola', 'Adios')
    
    data = leer_data('items.txt')
    print(f"DATA:{data}")