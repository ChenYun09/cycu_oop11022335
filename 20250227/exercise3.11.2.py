def print_right(text):
    # Calculate how many leading spaces are needed
    spaces_needed = 40 - len(text)
    
    # Print the string with the required number of leading spaces
    print(" " * spaces_needed + text)
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")