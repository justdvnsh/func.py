import collections

def _keys(obj):
    return obj.keys() if isinstance(obj, collections.Mapping) else \
        [idx for idx in range(len(obj))] if isinstance(obj, collections.Sequence) else \
        []