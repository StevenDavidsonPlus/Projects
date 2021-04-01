# -*- coding: utf-8 -*-

def fibSeqToNth(n):
    """Returns the Fibonacci sequences to the nth entry as a list of
       integers."""
    if not isinstance(n, int) or n < 0:
        raise TypeError('n should be a positive integer.')
        return None
    if n < 0:
        raise ValueError('n should be a positive integer.')
        return None
    result = [0, 1]
    if n < 2:
        return result[:n+1]
    for i in range(1, n):
        result.append(result[i]+result[i-1])
    return result

def fibSeqToX(x):
    """Returns the Fibonacci sequences to the integer n as a list of
       integers."""
    if not isinstance(x, int) or x < 0:
        raise TypeError('x should be a positive integer.')
        return None
    if x < 0:
        raise ValueError('x should be a positive integer.')
        return None
    result = [0, 1]
    if x in result:
        return result[:x+1]
    for i in range(1, 10 ** 100):
        result.append(result[i]+result[i-1])
        if (x <= result[-1]):
            break
    return result

def main():
    assert fibSeqToNth(1) == [0, 1]
    assert fibSeqToNth(5) == [0, 1, 1, 2, 3, 5]
    
    assert fibSeqToX(1) == [0, 1]
    assert fibSeqToX(5) == [0, 1, 1, 2, 3, 5]
    
if __name__ == "__main__":
    main()
