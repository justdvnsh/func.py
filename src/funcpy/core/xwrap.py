
def _xwrap(fn):
    class _XWrap():
        def __init__(self, fn):
            self.f = fn

        @staticmethod
        def _transducer_init():
            raise NotImplementedError("init not implemented in Xwrap")

        @staticmethod
        def _transducer_result(acc):
            return acc

        def _transducer_step(self, acc, x):
            return self.f(acc, x)

    return _XWrap(fn)