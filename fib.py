fibvaluemap = {}

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # While brute force, this is naive and bad. O(2^N)
        #return fib(n - 1) + fib(n - 2)

        savedfib = fibvaluemap.get(n, 0)
        if savedfib > 0:
            return savedfib
        else:
            newfib = fib(n - 1) + fib(n - 2)
            fibvaluemap[n] = newfib
            return newfib

n = 100
nthfib = fib(n)
print "the nth fibonacci sequence, for n == %d is %d" % (n, nthfib)
