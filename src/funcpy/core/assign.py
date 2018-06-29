import functools

def _assign(target, *args):
    return functools.reduce(lambda acc, obj: acc.update(obj) or acc, args, target)