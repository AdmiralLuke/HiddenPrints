import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def hide(func):
    def wrap(*args, **kwargs):
        with HiddenPrints():
            result = func(*args, **kwargs)
            return result
    return wrap