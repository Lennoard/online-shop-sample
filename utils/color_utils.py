class Colors:
    HEADER = '\033[95m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    INFO = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    @staticmethod
    def print_colored(color, message):
        print(f"{color}{message}{Colors.ENDC}")
