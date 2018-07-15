from src.funcpy.core.curry_2 import _curry2

@_curry2
def pick_by(test, obj):
    result = {}
    for key, value in obj.items():
        if test(value, key, obj) is not False:
            result[key] = value
    return result