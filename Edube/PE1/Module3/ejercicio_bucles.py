secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

print("Introduce un número entero", input= int())

while secret_number != 777:

    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    
    secret_number = 777
    
print("¡Bien hecho, muggle! Eres libre ahora")