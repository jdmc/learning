[Back2Overview](https://github.com/jdmc/learning/blob/master/exam.md)  
# PCAP Exam Prep: Section Z: Good to Know

## Brackets

### Indexing  ([]):
- Used to access a single element in a sequence, such as a list, string, or tuple.
- Specify a single index inside square brackets to indicate the position of the desired element.
```python
lista = [10, 20, 30]
print(lista[1])  # Output: 20

```
### Slicing ([start:stop:step]):
- Used to extract a specific part of a sequence using a range of indices.
- Specify three optional parameters inside square brackets: **start, stop, and step**, separated by colons (:).
- start indicates the starting index (**inclusive**), stop indicates the stopping index (**exclusive**), and step indicates the size of the step or increment.
- Slicing allows you to select a subsequence of elements from the original sequence.
```python
cadena = 'Python'
print(cadena[1:4])  # Output: 'yth'

```
### Negative Indexing:
- Used to access elements from the end of the sequence backwards.
- Specify a negative index inside square brackets to indicate the position of the element counting from **the end of the sequence.
```python
lista = [10, 20, 30]
print(lista[-1])  # Output: 30

```
### Nested List Indexing:
- Used to access elements in a list that contains nested lists or other sequences.
- Specify an additional index inside square brackets to indicate the position of the element in the nested list.
```python
lista_anidada = [[1, 2], [3, 4]]
print(lista_anidada[0][1])  # Output: 2

```
### Slicing with Step ([::step]):
- Used to select elements with a certain step within a sequence.
- Specify a third parameter inside square brackets to indicate the step size or increment.
- This allows you to select elements at regular intervals within the sequence.
```python
cadena = 'Python'
print(cadena[::2])  # Output: 'Pto'

```
### Assignment of Values:
- Used to modify or assign a value to a specific element in a sequence.
- Specify an index inside square brackets to indicate the position of the element to be modified, followed by an assignment operator (=).
```python
lista = [10, 20, 30]
lista[1] = 50
print(lista)  # Output: [10, 50, 30]

```
### Deletion of Elements:
- Used to delete an element or a range of elements from a sequence.
- Specify an index or a range of indices inside square brackets, followed by the del keyword.
```python
lista = [10, 20, 30]
del lista[1]
print(lista)  # Output: [10, 30]

```
### Creating Lists:
- Used to define a list of elements.
- Specify the elements separated by commas inside square brackets to create a new list.
```python
lista = [1, 2, 3]

```