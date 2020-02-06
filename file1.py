# file1.py
def sub(a, b):
    if isinstance(a, (int, float, complex)) and not(isinstance(a, bool)):
        if isinstance(b, (int, float, complex)) and not(isinstance(b, bool)):
            return a - b
    return False


def min_max(x):
    a = []
    for i in x:
        b = isinstance(i, (int, float, complex)) and not(isinstance(i, bool))
        a.append(b)
    if all(a):
        x.sort()
        return x[0], x[-1]
    return False


if __name__ == '__main__':
    pass
