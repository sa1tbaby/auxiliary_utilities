from time import time

class ExecutionTimer:

    def __init__(
            self,
            func
    ):
        self.func = func
        self.time_stamp = None

    def __enter__(
            self
    ):
        self.time_stamp = time()
        return self

    def __exit__(
            self,
            exc_type,
            exc_val,
            exc_tb
    ):
        print(self.time_stamp)

    def run(
            self,
            *args,
            **kwargs
    ):
        result = self.func(*args, **kwargs)
        self.time_stamp = time() - self.time_stamp

        return result

