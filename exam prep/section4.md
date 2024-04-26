[Back2Overview](https://github.com/jdmc/learning/blob/master/exam.md)  
# PCAP Exam Prep: Section 4: Object-Oriented Programming (score + weight =34%  12 items)

## Understanding Object-Oriented Programming (OOP):

- **OOP** is a programming paradigm that organizes code around objects.
- An **object** is a data structure that encapsulates data (attributes or properties) and the code that operates on that data (methods).
- **Classes** are blueprints for creating objects with specific attributes and methods.
- **Encapsulation** protects data by restricting direct access to attributes and providing methods to access and modify them.
- **Inheritance** allows creating new classes (subclasses) that inherit attributes and methods from existing classes (superclasses).
- **Polymorphism** allows objects of different classes to respond to the same method call in different ways.

## Class and Object Properties:

- **Instance variables**: Attributes specific to an object instance (created using a class).
- **Class variables**: Attributes shared by all objects of a class (declared directly within the class definition).
- __dict__ property: Provides a dictionary-like view of an object's attributes (including both instance and class variables).
- **Private components**: Use double underscores (__) to discourage direct access to attributes or methods (encapsulation). Python uses name mangling to - automatically rename private elements for internal use.

## Equipping a Class with Methods:

- **Methods** are functions defined within a class to operate on the object's data (attributes).
- self parameter: The first argument implicitly passed to every method, referring to the current object instance.
- You can define methods for various purposes, like initialization (__init__()), accessing or modifying attributes, performing calculations, etc.

## Discovering the Class Structure:

- **Introspection**: Examining the structure of objects and classes at runtime.
- hasattr(object, name): Checks if an object has a specific attribute (name).
- **Class properties**:
    - __name__: The class name.
    - __module__: The module where the class is defined.
    - __bases__: A tuple containing the class's superclasses.

## Building Class Hierarchies with Inheritance:

- **Single inheritance**: A subclass inherits from one superclass.
- **Multiple inheritance**: A subclass inherits from multiple superclasses (less common due to potential complexity).
- isinstance(object, class_info): Checks if an object is an instance of a class or its subclass.
- **Overriding**: Redefining an inherited method in a subclass to provide custom behavior.

## Operators and Polymorphism:

- The **is** operator checks for object identity (same object in memory).
- Polymorphism allows objects of different classes to respond to the same method call (e.g., print(obj) might print differently for different class types).
- __str__() method: Overriding this method allows you to customize how an object is represented as a string when printed.
- **Diamond problem** (multiple inheritance): A potential issue when using multiple inheritance, requiring careful design to resolve conflicts.

## Constructing and Initializing Objects:

- **Constructors** (__init__() method): Special method automatically called when creating an object instance.
- The __init__() method is used to initialize object attributes with initial values.