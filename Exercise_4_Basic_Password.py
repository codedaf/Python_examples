import random
import string

def generate_password(length):
    """Generates a random 12-character password that includes a 
       mix of uppercase letters, lowercase letters, digits, and special characters.
    Args:
        length (_type_): length of 12 characters
    Returns:
        the generate password
    """
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Example usage
desired_length = 12
generated_password = generate_password(desired_length)
print(f"Your generated password is:   {generated_password}")


 