import random
import string


def new_id(chars=string.ascii_letters + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(10))
