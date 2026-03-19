def decorator_factory(arg_for_decorator):
    """A decorator factory that takes arguments and returns a decorator."""
    print(f"I've got arg = {arg_for_decorator} for decorator!")

    def simple_decorator(my_function):
        print(f"Hello! I'm Decorator with arg = {arg_for_decorator}")

        def wrapper(arg_x, arg_y):
            print(f"Hi! I am Function. I've got {arg_x}, {arg_y}. Function starts working...")
            result = my_function(arg_x, arg_y) + arg_for_decorator
            print("See you!")
            return result
            
        return wrapper
    
    return simple_decorator

# Example usage:
@decorator_factory(10)
def add_numbers(x, y):
    return x + y

# Test the decorated function
print(add_numbers(5, 3))  # Output will be 18 (5+3+10)
