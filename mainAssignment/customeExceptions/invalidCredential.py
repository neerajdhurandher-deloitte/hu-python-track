class InvalidCredential(Exception):
    def __init__(self):
        super()

    def print_msg(self, message):
        print("Error ", message)
