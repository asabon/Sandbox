def add(a, b):
    """2つの数値を加算して返す"""
    return a + b

def subtract(a, b):
    """2つの数値を減算して返す"""
    return a - b

def multiply(a, b):
    """2つの数値を乗算して返す"""
    return a * b

def divide(a, b):
    """2つの数値を除算して返す。0除算の場合はZeroDivisionErrorを送出する"""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
