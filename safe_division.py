def safe_division(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error: Division by Zero")
        return None


result = safe_division(10,0)
if result is not None:
    print(result)