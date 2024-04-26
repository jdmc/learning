# PCAP Exam Prep: Section 5: Miscellaneous (score + weight =22%  9 items)

Scope: List Comprehensions, Lambdas, Closures, and I/O Operations

## 1. List Comprehensions (Building Complex Lists):

- List comprehensions are a concise way to create lists based on existing iterables.

- They use a single line of code to express what might take multiple lines with loops and conditional statements.

    - Syntax: [expression for item in iterable if condition]

    - expression: Operation performed on each item in the iterable.

    - iterable: The list or sequence you're iterating over.

    - condition (optional): Filters items based on a boolean expression.

    - Example: squares = [x**2 for x in range(5)] (creates a list of squares from 0 to 4)

    - Nested comprehensions: Create multi-dimensional lists.

## 2. Lambdas (Embedding Functions in Code):

- Lambdas are small, anonymous functions defined using the lambda keyword.

- They are useful for short, one-line functions within your code.

    - Syntax: lambda arguments: expression

    - arguments: Comma-separated list of parameters for the lambda.

    - expression: The function body, evaluated when the lambda is called.

    - Example: sorted(data, key=lambda x: x[1]) (sorts a list data by the second element in each sublist)

    - Self-defined functions taking lambdas as arguments: Pass lambdas as arguments to functions to provide dynamic behavior.

## 3. Closures (Functions with Preserved State):

- Closures are inner functions that remember and access variables from their enclosing scope even after the enclosing function has finished executing.
-
- They allow you to create functions that "remember" state or data.

Defining a closure: Create an inner function that references variables in its outer scope.

Example:

```Python
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
```

- create_multiplier returns an inner function (multiplier) that remembers the value of n.

## 4. Input/Output (I/O) Operations (Understanding and Performing):

### Basic Terminology:

- I/O modes: Modes for opening files ('r' for reading, 'w' for writing, 'a' for appending).
- Predefined streams: Standard input (sys.stdin), standard output (sys.stdout), standard error (sys.stderr).
- Handles vs. streams: Handles manage file objects, streams represent the flow of data.
- Text vs. binary modes: Text mode works with strings, binary mode works with raw bytes.

### Performing I/O Operations:

- open(filename, mode): Opens a file and returns a file object.
- errno variable: Contains error codes for file operations.
- File object methods:
    - close(): Closes the file.
    - .read(size): Reads size bytes from the file (or all remaining if no size is specified).
    - .write(string): Writes a string to the file.
    - .readline(): Reads a single line from the file (including the newline character).
    - .readlines(): Reads all lines from the file and returns a list of strings.
- bytearray: Used for working with binary data as a mutable sequence of bytes.