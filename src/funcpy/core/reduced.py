import types

def _reduced(x):
    return x if x and getattr(x, "_transducer_reduced", False) else \
        types.SimpleNamespace(_transducer_value=x, _transducer_reduced=True)