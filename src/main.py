import math

class Calculator:
    def __init__(self):
        self.history = []

    def _log(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def add(self, x, y):
        result = x + y
        self._log(f"{x} + {y}", result)
        return result

    def subtract(self, x, y):
        result = x - y
        self._log(f"{x} - {y}", result)
        return result

    def multiply(self, x, y):
        result = x * y
        self._log(f"{x} * {y}", result)
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        result = x / y
        self._log(f"{x} / {y}", result)
        return result

    def power(self, x, y):
        result = x ** y
        self._log(f"{x} ^ {y}", result)
        return result

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot find square root of negative number")
        result = math.sqrt(x)
        self._log(f"sqrt({x})", result)
        return result

    def get_last_operation(self):
        if not self.history:
            return None
        return self.history[-1]

if __name__ == "__main__":
    calc = Calculator()
    print(f"Pow: {calc.power(2, 3)}")
    print(f"Sqrt: {calc.square_root(25)}")
    print(f"History: {calc.history}")