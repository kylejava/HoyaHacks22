class User:
    def __init__(self, name, phone_number, sign):
        self.name = name
        self.phone_number = phone_number
        self.sign = sign

    def print_data(self):
        print(self.name)
        print(self.phone_number)
        print(self.sign)
