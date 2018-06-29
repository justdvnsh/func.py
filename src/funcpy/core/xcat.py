from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduce import _reduce
from .forceReduced import _force_reduced
import collections

def _xcat(xf):
    class _PreservingReduced(_XFBase):
        def __init__(self, xf):
            self.xf = xf

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return self.xf._transducer_result(result)

        def _transducer_step(self, result, input):
            ret = self.xf._transducer_step(result, input)
            return _force_reduced(ret) if getattr(ret, "_transducer_reduced", False) \
                else ret

    class _XCat(_XFBase):
        def __init__(self, xf):
            self.rxf = _PreservingReduced(xf)

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return self.rxf._transducer_result(result)

        def _transducer_step(self, result, input):
            return _reduce(self.rxf, result, [input]) \
                if not isinstance(input, collections.Sequence) \
                else _reduce(self.rxf, result, input)

    return _XCat(xf)
