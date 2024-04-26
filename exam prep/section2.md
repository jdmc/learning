[Back2Overview](https://github.com/jdmc/learning/blob/master/exam.md)  
# PCAP Exam Prep: Section 2: Exceptions (score + weight = 14%  5 items)

## Handling Errors with Built-in Exceptions:

- **except**: Executes code if a specific exception (or subclass) is raised within the try block. You can also use except without an argument to catch all - exceptions (not recommended).
- **except: ... else: ...**: The else block executes only if no exception is raised in the try block.
- **except (ExceptionType1, ExceptionType2)**: Catches multiple specific exception types.
- **Exception Hierarchy**: Python has a built-in hierarchy of exceptions (BaseException -> Exception -> specific exceptions like TypeError, ValueError). Catching - a higher-level exception in the hierarchy (e.g., Exception) will also catch its subclasses (e.g., TypeError).
- **raise**: Manually raises an exception. You can optionally provide an exception object or a string message.
- **assert**: Raises an AssertionError if a condition is not True. Useful for debugging and checking assumptions.

## Using the except E as e Syntax:

- except E as e catches an exception of type E and assigns the raised exception object to the variable e.
- This allows you to access information about the exception, such as its message using e.args.

## Event Classes (Less Common):

These are specialized exceptions for system events like keyboard interrupts (KeyboardInterrupt) or system exit (SystemExit). They are typically not used for general error handling.

## Self-Defined Exceptions:

- You can create custom exception classes that inherit from the built-in Exception class.
- This allows you to define specific exceptions for your application's error scenarios.
- You can provide custom messages or data within your exception class.

## Defining and Using Self-Defined Exceptions:

1. Define the Exception Class:

```python
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)  # Call parent constructor
        self.message = message  # Store custom message

```
2. Raise Your Custom Exception:

```python
def check_value(value):
    if value < 0:
        raise MyCustomException("Value must be non-negative")

```
3. Catch Your Custom Exception:
```python
try:
    check_value(-5)
except MyCustomException as e:
    print(f"Error: {e.message}")

```