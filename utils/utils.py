import random
import string

import main
from utils.color_utils import Colors


def new_id(chars=string.ascii_letters + string.digits) -> str:
    main.a = 2
    return ''.join(random.choice(chars) for _ in range(10))


def print_error(message):
    Colors.print_colored(Colors.ERROR, message)


def print_warning(message):
    Colors.print_colored(Colors.WARNING, message)


def print_success(message):
    Colors.print_colored(Colors.SUCCESS, message)


def print_info(message):
    Colors.print_colored(Colors.INFO, message)
