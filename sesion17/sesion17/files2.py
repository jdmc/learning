from pathlib import Path
import shutil

p = Path('data1.txt')
print(type(p))

path = p.parent.absolute()
print(path)

print(p.is_file())
print(p.is_dir())

p = Path('.')

for entrada in p.glob('*'):
    print('File:' if entrada.is_file() else 'Dir:', entrada)


base = Path('ejemplo_data')
base.mkdir(exist_ok=True)

path_b = base / 'A' / 'B'
path_b.mkdir(parents=True, exist_ok=True)

""" for fichero in ('data1.txt', 'data2.txt'):
    with open(path_b / fichero, 'w') as stream:
        stream.write(f'Python ficheros {fichero}\n')

path_d = base / 'A' / 'D'

shutil.move(path_b, path_d)

data1 = path_d / 'data1.txt'
data1.rename(data1.parent / 'data1_renombrado.txt')

print(data1.absolute())
print(data1.name) 
print(data1.parent.absolute())


with open('write.txt', 'x') as file:
    file.write('Hola mundo')

with open('write.txt', 'x') as file:
    file.write('Hola mundo2')



 """


import platform

print(platform.architecture())
print(platform.version())
