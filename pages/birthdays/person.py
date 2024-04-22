class Person:
    def __init__(self):
        self.full_name = ''
        self.details = ''
        self.birthday = ''

# person = Person()
# attribute_names = Person().__dict__.keys()
print(list(Person().__dict__.keys()))
