import os

# Set variable
os.environ["test_var"] = "test_var"

# Get variable
print(os.environ["test_var"])

# List all variables in the os.environ dictionary
print([x for x in os.environ.keys()])