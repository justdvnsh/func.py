from .curry_2 import _curry2
from .xfBase import _XFBase
from .reduce import _reduce

@_curry2
def _xdrop_last_while(fn, xf):
    class _XDropLastWhile(_XFBase):
        def __init__(self, fn, xf):
            self.f = fn
            self.xf = xf
            self.retained = []

        def _transducer_init(self):
            return super().init()

        def _transducer_result(self, result):
            self.retained = None
            return super().result(result)

        def _transducer_step(self, result, input):
            return self.retain(result, input) if self.f(input) else \
                self.flush(result, input)

        def flush(self, result, input):
            result = _reduce(
                self.xf._transducer_step, result, self.retained)
            self.retained = []
            return self.xf._transducer_step(result, input)

        def retain(self, result, input):
            self.retained.append(input)
            return result

    return _XDropLastWhile(fn, xf)
