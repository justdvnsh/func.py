import math

def _identical(a, b):
    if isinstance(a, float) and math.isnan(a):
        return isinstance(b, float) and math.isnan(b)
    if isinstance(a, str) and isinstance(b, str):
        return a == b
    return id(a) == id(b)
