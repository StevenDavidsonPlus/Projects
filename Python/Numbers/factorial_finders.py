# -*- coding: utf-8 -*-

def factorialFinderRecursive(n):
    """Returns the factorial of the positive integer n using
       recursion."""
    if not isinstance(n, int) or n < 0:
        raise TypeError('n should be a positive integer.')
        return None
    if n == 0:
        return 1
    else:
        return n * factorialFinderRecursive(n - 1)
    
def factorialFinderLoops(n):
    """Returns the factorial of the positive integer n using
       loops."""
    if not isinstance(n, int) or n < 0:
        raise TypeError('n should be a positive integer.')
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    assert factorialFinderRecursive(1) == 1
    assert factorialFinderRecursive(5) == 120
    
    assert factorialFinderLoops(1) == 1
    assert factorialFinderLoops(5) == 120
    
    try:
        factorialFinderRecursive('n')
    except TypeError as e:
        assert str(e).startswith('n should be')
    
    try:
        factorialFinderLoops('n')
    except TypeError as e:
        assert str(e).startswith('n should be')
    
if __name__ == "__main__":
    main()