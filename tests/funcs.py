
def get_name(obj):
    {name} = obj
    return  name

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a+b, a
    return a

