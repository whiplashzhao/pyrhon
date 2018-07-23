
import functools
import time


def metric(func):
    @functools.wraps(func)
    def run_time(*args, **kw):
        start = time.clock()
        return_value = func(*args, **kw)
        end = time.clock()
        duration = end - start
        print('%s executed in %s ms' % (func.__name__, duration))
        return return_value
    return run_time


@metric
def add_all(a):
    return 100*a

add_all(100)



print(add_all(100))

#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# fast(11, 22)

# f = fast(11, 22)
# s = slow(11, 22, 33)
#
#
#
# if f != 33:
#     print('测试失败1!')
# elif s != 7986:
#     print('测试失败2!')
