[Back2Overview](https://github.com/jdmc/learning/blob/master/exam.md)  

# PCAP Exam Prep: Section 1 : Modules and Packages (score + weight = 12%  6 items)

## Importing Modules and Packages:

- **import**: Brings the entire module into your namespace. You can then access its functions, classes, etc., directly using their names (e.g., print from the builtins module).
- **from ... import ...**: Imports specific elements from a module, avoiding namespace pollution. You prefix them with the module name (e.g., math.sqrt(16)).
- **import ... as ...**: Assigns an alias to a module, making its elements easier to reference (e.g., import random as rnd; rnd.random()).
- **import\***: Imports all elements from a module (caution: can clutter namespace, use with care).

## Nested Modules:

Modules can contain other modules. You can import them with dotted notation (e.g., **from my_package.submodule import my_function**).

### **dir()** *Function*:

Returns a list of names defined within a module or package. Useful for exploring available elements.

### **sys.path** *Variable*:

Contains a list of directories where Python searches for modules. You can modify it to add custom module locations.

### **math** *Module*:

Provides mathematical functions like:

- ceil(x): Rounds x up to the nearest integer.
- floor(x): Rounds x down to the nearest integer.
- trunc(x): Removes the decimal part of x.
- factorial(n): Calculates the factorial of n (n!).
- hypot(x, y): Calculates the Euclidean distance between points (x, y).
- sqrt(x): Calculates the square root of x.

### **random** *Module*:

 Generates random numbers and sequences:

- random(): Returns a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).
- seed(a): Seeds the random number generator for reproducibility (optional).
- choice(sequence): Randomly selects an element from the given sequence.
- sample(population, k): Returns a list of k unique elements chosen from the population without replacement.

### **platform** *Module*:

Discovers information about the host platform:

- platform(): Returns a platform-specific string (e.g., 'linux', 'win32').
- machine(): Returns the computer architecture (e.g., 'x86_64').
- processor(): Returns the processor name (e.g., 'x86').
- system(): Returns the operating system name (e.g., 'Windows', 'Linux').
- version(): Returns the OS release version (e.g., '10.0.19041').
- python_implementation(): Returns the Python implementation (e.g., 'CPython').
- python_version_tuple(): Returns a tuple of Python version numbers (e.g., (3, 8, 10)).

## User-Defined Modules and Packages:

- Idea and Rationale: Break down code into reusable components, organize code base, promote modularity.
- __pycache__ Directory: Where Python stores compiled bytecode versions of your modules for faster loading.
- __name__ Variable: Special variable that holds the module's name ('__main__' when run directly, otherwise the module's filename).
- Public vs. Private Variables: Public (accessed directly; use descriptive names), Private (prefixed with double underscores __ to discourage direct access, promote encapsulation).
- __init__.py File: Empty file in a directory to tell Python it's a package (can also contain initialization code).
- Searching for Modules: Python searches modules in **sys.path** directories, prioritizes packages over individual .py files.
- Nested Packages vs. Directory Trees: Nested packages mirror directory structure, but packages can also have flattened structures where modules reside directly in the package directory.

