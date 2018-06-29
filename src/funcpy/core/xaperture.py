from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced
import collections


@_curry2
def _xaperture(n, xf):
    class _XAperture(_XFBase):
        def __init__(self, n, xf):
            self.xf = xf
            self.full = False
            self.acc = collections.deque([], n)

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            self.acc = None
            return self.xf._transducer_result(result)

        def _transducer_step(self, result, input):
            self.store(input)
            return self.xf._transducer_step(result, self.get_copy()) \
                if self.full else result

        def store(self, input):
            self.acc.append(input)
            if len(self.acc) == self.acc.maxlen:
                self.full = True

        def get_copy(self):
            return list(self.acc)

    return _XAperture(n, xf)