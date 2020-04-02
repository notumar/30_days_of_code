import random
import string
def password_generator(length):
    """
    Returns a randomized password of input length
    """
    char_array = []
    suggested_password = ""
    char_array.extend(range(0,10))
    char_array.extend(string.ascii_letters)
    if length < 8:
        return "Password too weak"
    else:
        while len(suggested_password)<length:
            suggested_password += str(random.choice(char_array))
    
    return suggested_password


print(password_generator(30))




    






        