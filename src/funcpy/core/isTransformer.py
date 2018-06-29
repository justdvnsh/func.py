import collections

def _is_transformer(obj):
    return isinstance(
        getattr(obj, "_transducer_step", None), collections.Callable)