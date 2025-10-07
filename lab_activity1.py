def calculate_area(length, width):
    """Returns the area of a rectangle."""
    return length * width

def greet_user(name, greeting="Hello"):
    """Returns a greeting message with a default 'Hello'."""
    return f"{greeting}, {name}!"

def find_max(*args):
    """Finds and returns the largest number manually (no built-in max() used)."""
    if not args:
        return None
    max_value = args[0]
    for num in args[1:]:
        if num > max_value:
            max_value = num
    return max_value

def create_user_profile(first_name, last_name, **kwargs):
    """Creates a user profile dictionary with optional keyword info."""
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(kwargs)
    return profile



print("=== Laboratory Activity 1 - Set A ===")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of Rectangle:", calculate_area(length, width))

name = input("Enter your name: ")
greeting = input("Enter a greeting message (press Enter to use default): ")
if greeting.strip() == "":
    print(greet_user(name))
else:
    print(greet_user(name, greeting))

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
manual_max = find_max(*numbers)
print("Maximum Value (manual):", manual_max)
print("Check with built-in max():", max(numbers))  # for verification

first = input("Enter first name: ")
last = input("Enter last name: ")
age = input("Enter age: ")
city = input("Enter city: ")
role = input("Enter role: ")
print("User Profile:", create_user_profile(first, last, age=age, city=city, role=role))
