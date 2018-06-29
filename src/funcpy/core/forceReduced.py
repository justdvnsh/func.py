import types

def _force_reduced(x):
    return types.SimpleNamespace(_transducer_value=x, _transducer_reduced=True)