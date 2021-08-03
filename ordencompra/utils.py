import string    
import random 


def random_code(value):
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=value)
    )
