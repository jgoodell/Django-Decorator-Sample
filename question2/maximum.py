"""A module that defins a decorate that matches
def minimum_x(x):
    '''
    - returns a decorator that can be used to decorate another function
    - verifies argument of the function it decorates <= the given value
    - raises a ValueError on failure.

    Example...

    >>> @minimum_x(6)
    ... def test(arg):
    ...   print arg
    ...

    >>> test(6)
    6

    >>> test(5) # raises ValueError
    '''
"""

def minimum_x(dec_arg):
    '''Raises a ValueError if the arguemnt supplied to the
    function does not match the value.

    Arguments:
    '''
    def f1(f,dec_arg=dec_arg):
        '''f1'''
        def f2(func_arg,dec_arg=dec_arg, func=f):
            '''f2'''
            if func_arg >= dec_arg:
                func(func_arg)
            else:
                raise ValueError('%s is less than %s' % (func_arg, dec_arg))
        return f2
    return f1
    

@minimum_x(6)
def test(arg):
    '''test'''
    print(arg)

def showdoc(f):
    if f.__doc__:
        print("%s: %s" % (f.__name__, f.__doc__))
    else:
        print("%s: No docstring!" % f.__name__)
    return f

if __name__ == "__main__":
    test(6)
    test(5)

