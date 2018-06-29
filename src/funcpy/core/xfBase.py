class _XFBase():
    def init(self):
        return self.xf._transducer_init()

    def result(self, result):
        return self.xf._transducer_result(result)