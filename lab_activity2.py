def process_full_name(full_name):
    """Extracts and capitalizes first and last names."""
    full_name = full_name.strip()
    first_name, last_name = full_name.split()
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print("First Name:", first_name)
    print("Last Name:", last_name)
    return first_name, last_name

def create_file_name(first_name, last_name):
    """Creates a formatted file name with timestamp."""
    return f"{first_name.lower()}_{last_name.lower()}_report_20241006.txt"

def is_valid_password(password):
    """Checks if password has at least 8 characters and one digit."""
    return len(password) >= 8 and any(ch.isdigit() for ch in password)

def reverse_words(sentence):
    """Reverses the order of words in a sentence."""
    words = sentence.split()
    return " ".join(words[::-1])



print("\n=== Laboratory Activity 2 - Set A ===")

full_name = input("Enter your full name (first and last): ")
first, last = process_full_name(full_name)


file_name = create_file_name(first, last)
print("Generated File Name:", file_name)


def is_valid_password(password):
   
    if len(password) < 8:
        return False
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    return has_number

while True:
    password = input("Enter a password to validate: ")

    if is_valid_password(password):
        print("Password is valid ✅")
        break 
    else:
        print("Password is invalid ❌ (must be at least 8 characters and include a number)\n")


sentence = input("Enter a sentence to reverse: ")
print("Reversed Sentence:", reverse_words(sentence))
