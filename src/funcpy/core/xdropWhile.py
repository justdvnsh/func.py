from .curry_2 import _curry2
from .xfBase import _XFBase

@_curry2
def _xdrop_while(pred, xf):
    class _XDropWhile(_XFBase):
        def __init__(self, pred, xf):
            self.pred = pred
            self.xf = xf

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            if self.pred:
                if self.pred(input):
                    return result
                else:
                    self.pred = None
            return self.xf._transducer_step(result, input)

    return _XDropWhile(pred, xf)