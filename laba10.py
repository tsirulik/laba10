import typer
import math
from sympy import *
from functools import lru_cache
import random
import string

app = typer.Typer()

def recursive_solution(n):
    if n == 0:
        return 3
    else:
        return sqrt(3 + recursive_solution(n-1))

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.command()
def calculate_recursive(n: int):
    recursive_result = recursive_solution(n)
    typer.echo(f"Result using recursive solution: {recursive_result}")

@app.command()
def calculate_fibonacci(n: int):
    for i in range(1, n+1):
        typer.echo(f"{i} {fib(i)}")

@app.command()
def generate_password_command(length: int = 8):
    password = generate_password(length)
    typer.echo(f"Generated password: {password}")

if __name__ == "__main__":
    app()  