class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value if (value >= 0) else 0


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
