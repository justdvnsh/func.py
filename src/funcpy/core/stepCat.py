import types
from .identity import _identity
from .assign import _assign
import collections
from .isTransformer import _is_transformer

def _step_cat(obj):
    _step_cat_array = types.SimpleNamespace(
        _transducer_init=lambda: [],
        _transducer_step=lambda a, b: a.append(b) or a,
        _transducer_result=_identity)

    _step_cat_string = types.SimpleNamespace(
        _transducer_init=lambda: "",
        _transducer_step=lambda a, b: a + str(b),
        _transducer_result=_identity)

    _step_cat_obj = types.SimpleNamespace(
        _transducer_init=lambda: {},
        _transducer_step=lambda result, input: _assign(
            result, dict([input[:2]]) if not isinstance(
                input, collections.Mapping) else input),
        _transducer_result=_identity)

    if _is_transformer(obj):
        return obj
    elif isinstance(obj, collections.Mapping):
        return _step_cat_obj
    elif isinstance(obj, str):
        return _step_cat_string
    elif isinstance(obj, collections.Iterable):
        return _step_cat_array

    raise ValueError("Cannot create transformer for {}".format(obj))