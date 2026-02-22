def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

if __name__ == "__main__":
    # Small manual check if you run this file directly
    print("App is running...")
    print(f"2 + 2 = {add(2, 2)}")