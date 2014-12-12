from time import clock

def time_it(func):
    def wrapper(*args, **kwargs):
        t1 = clock();
        result = func(*args, **kwargs)
        t2 = clock();
        return t2 - t1
    return wrapper
