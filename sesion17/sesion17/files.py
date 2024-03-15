from zipfile import ZipFile


#context manager
""" with ZipFile('data.zip', 'w') as zip:
    zip.write('data1.txt')
    zip.write('data2.txt') """

#context manager
with ZipFile('data.zip', 'r') as zip:
    zip.extract('data1.txt')

    
