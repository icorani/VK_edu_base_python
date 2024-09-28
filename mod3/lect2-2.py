from math import sqrt


class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length):
        return f"{round(2 * cls.pi * sqrt(length / cls.g), 2)}"


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
