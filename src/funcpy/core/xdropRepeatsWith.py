from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduce import _reduce

@_curry2
def _xdrop_repeats_with(pred, xf):
    class _XDropRepeatsWith(_XFBase):
        def __init__(self, pred, xf):
            self.pred = pred
            self.xf = xf
            self.last_value = None
            self.seen_first_value = False

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            return super().result(result)

        def _transducer_step(self, result, input):
            same_as_last = False
            if not self.seen_first_value:
                self.seen_first_value = True
            elif self.pred(self.last_value, input):
                same_as_last = True
            self.last_value = input
            return result if same_as_last else self.xf._transducer_step(
                result, input)

    return _XDropRepeatsWith(pred, xf)