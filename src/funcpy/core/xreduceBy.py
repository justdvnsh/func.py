from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced
import functools
from .curry_N import _curryN

@functools.partial(_curryN, 4, [])
def _xreduce_by(value_fn, value_acc, key_fn, xf):
    class _XReduceBy(_XFBase):
        def __init__(self, value_fn, value_acc, key_fn, xf):
            self.value_fn = value_fn
            self.value_acc = value_acc
            self.key_fn = key_fn
            self.xf = xf
            self.inputs = {}

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            for key, value in self.inputs.items():
                result = self.xf._transducer_step(result, value)
                if getattr(result, "_transducer_reduced", False):
                    result = result._transducer_value
                    break
            self.inputs = None
            return super().result(result)

        def _transducer_step(self, result, input):
            key = self.key_fn(input)
            self.inputs[key] = self.inputs.get(key, [key, self.value_acc])
            self.inputs[key][1] = self.value_fn(self.inputs[key][1], input)
            return result

    return _XReduceBy(value_fn, value_acc, key_fn, xf)