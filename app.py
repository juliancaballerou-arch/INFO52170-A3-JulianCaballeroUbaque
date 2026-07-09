# app.py - Created by Julian Caballero Ubaque
def greet(name):
    return f"Hello, {name}! Welcome to INFO 52170."

def info(name, class_name):
    return f"{name} is culminating their studies in {class_name} this semester."

if __name__ == "__main__":
    print(greet("Julian"))
    print(info("Julian", "INFO 52170"))

