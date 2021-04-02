# -*- coding: utf-8 -*-

def collatzConjecture(n):
    """Returns the Fibonacci sequences to the nth entry as a list of
       integers."""
    if not isinstance(n, int):
        raise TypeError('n should be an integer larger than 1.')
        return None
    if not n > 1:
        raise ValueError('n should be an integer larger than 1.')
        return None
    result = 0
    while (n != 1):
        result += 1
        if (n & 1 == 1):
            n = 3 * n + 1
        else:
            n //= 2
    return result

def main():
    assert collatzConjecture(27) == 111
    
    try:
        collatzConjecture('n')
    except TypeError as e:
        assert str(e) == 'n should be an integer larger than 1.'
    
    try:
        collatzConjecture(1)
    except ValueError as e:
        assert str(e) == 'n should be an integer larger than 1.'
    
if __name__ == "__main__":
    main()
