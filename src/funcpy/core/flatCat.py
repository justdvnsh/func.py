import collections

def _make_flat(recursive):
    def flatt(xs):
        result = []
        for item in xs:
            if isinstance(item, collections.Sequence):
                value = flatt(item) if recursive else item
                result += value
            else:
                result.append(item)
        return result
    return flatt