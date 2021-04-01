# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fast_exp(a, b):
    """Returns a^b in O(lg n) time complexity, where a and b are both
       integers."""
    if not isinstance(a, int) == isinstance(b, int) == True:
         raise TypeError('a and b should both be integers.')
         return None
    if b < 0:
        return 0
    result = 1
    while (b != 0):
        if b & 1 == 1:
            result *= a
        b >>= 1
        a *= a     
    return result

def main():
    assert fast_exp(2, 2) == 2 ** 2
    assert fast_exp(2, 15) == 2 ** 15
    assert fast_exp(5, 3) == 5 ** 3

    assert fast_exp(10, -2) == 0
    
    try:
        fast_exp('a', 'b')
    except TypeError as e:
        assert str(e).startswith('a and b')
    
if __name__ == "__main__":
    main()
