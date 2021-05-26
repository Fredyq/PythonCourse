def pre_process(a):
    def decorator(func):
        def wrapper(*args):
            s = args[0]
            for i in range(len(s)):
                s[i] -= a * s[i-1]
                print('a =', a)
                func(s)
        return wrapper
    return decorator


@pre_process(a=0.93)
def pilot_signal(s):
    for sample in s:
        print(sample)


s = [0, 1, 2, 3]
pilot_signal(s)