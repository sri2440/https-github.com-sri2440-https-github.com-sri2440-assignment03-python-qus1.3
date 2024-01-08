def variable_arguments_example(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

# Example 1: Call with positional and keyword arguments
variable_arguments_example(1, "two", 3.0, option1="value1", option2="value2")

# Example 2: Call with only positional arguments
variable_arguments_example("hello", 42, [1, 2, 3])

# Example 3: Call with only keyword arguments
variable_arguments_example(optionA="apple", optionB="banana")

# Example 4: Call with no arguments
variable_arguments_example()
