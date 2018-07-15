from src.funcpy.pipe import pipe

def compose(*args):
    if len(args) == 0:
        raise ValueError("compose requires at least one argument")
    return pipe(*reversed(args))
