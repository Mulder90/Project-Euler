import time


def timeit(f):
    """
    Decorator to test execution's time of a method
    Thanks to Matt Alcock http://blog.mattalcock.com/2013/2/24/timing-python-code/
    """

    def timed(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print("Function '{function_name}' with args: [{args}, {kwargs}] executed in {time}s".format(
            function_name=f.__name__, args=args, kwargs=kwargs, time=elapsed_time))
        return result

    return timed
