from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduced import _reduced


@_curry2
def _xfind_index(pred, xf):
    class _XFindIndex(_XFBase):
        def __init__(self, pred, xf):
            self.pred = pred
            self.xf = xf
            self.idx = -1
            self.found = False

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            if not self.found:
                result = self.xf._transducer_step(result, -1)
            return self.xf._transducer_result(result)

        def _transducer_step(self, result, input):
            self.idx += 1
            if self.pred(input):
                self.found = True
                result = _reduced(self.xf._transducer_step(result, self.idx))
            return result

    return _XFindIndex(pred, xf)