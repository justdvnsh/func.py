from .curry_2 import _curry2
from .xfBase import _XFBase
import collections

@_curry2
def _xdrop_last(n, xf):
    class _XDropLast(_XFBase):
        def __init__(self, n, xf):
            self.xf = xf
            self.n = n
            self.full = False
            self.acc = collections.deque([], n)

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            if self.full:
                result = self.xf._transducer_step(result, self.acc[0])
            self.store(input)
            return result

        def store(self, input):
            self.acc.append(input)
            if len(self.acc) == self.acc.maxlen:
                self.full = True

    return _XDropLast(n, xf)