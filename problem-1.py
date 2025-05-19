class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def compute(self):
        if self.operation in ["add", "addition"]:
            return self.a + self.b
        elif self.operation in ["subtract", "subtraction"]:
            return self.a - self.b
        elif self.operation in ["multiply", "multiplication"]:
            return self.a * self.b
        elif self.operation in ["divide", "division"]:
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"


if __name__ == "__main__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    op = input("Enter operation (add/subtract/multiply/divide): ")
    calc = Calculator(a, b, op)
    print("Result:", calc.compute())
