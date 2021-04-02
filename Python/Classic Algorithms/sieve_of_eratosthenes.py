# -*- coding: utf-8 -*-

from math import floor, sqrt

def sieveOfEratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n should be an integer larger than 1.')
        return None
    if not n > 1:
        raise ValueError('n should be an integer larger than 1.')
        return None
    sieve = [True for _ in range(n+1)]
    for i in range(2, floor(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return list(i for i in range(2, n+1) if sieve[i])

def main():
    assert sieveOfEratosthenes(10) == [2, 3, 5, 7]
    
    try:
        sieveOfEratosthenes('n')
    except TypeError as e:
        assert str(e) == 'n should be an integer larger than 1.'
    
    try:
        sieveOfEratosthenes(1)
    except ValueError as e:
        assert str(e) == 'n should be an integer larger than 1.'
    
if __name__ == "__main__":
    main()
