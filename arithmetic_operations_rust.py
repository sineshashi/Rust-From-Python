import ctypes

# Load the Rust library
arithmetic_operations = ctypes.CDLL("./target/release/arithmetic_opertations.dll")  # Replace with the actual path

# Define the function prototypes
add_numbers = arithmetic_operations.add_numbers
add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
add_numbers.restype = ctypes.c_int

subtract_number = arithmetic_operations.subtract_number
subtract_number.argtypes = [ctypes.c_int, ctypes.c_int]
subtract_number.restype = ctypes.c_int

multiply_numbers = arithmetic_operations.multiply_numbers
multiply_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
multiply_numbers.restype = ctypes.c_int

def divide_numbers(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError()
    _divide_numbers = arithmetic_operations.divide_numbers
    _divide_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
    _divide_numbers.restype = ctypes.c_double
    return _divide_numbers(a, b)

# Usage example
print(add_numbers(1, 1))
print(subtract_number(5, 3))
print(multiply_numbers(2, 4))
print(divide_numbers(5, 0))