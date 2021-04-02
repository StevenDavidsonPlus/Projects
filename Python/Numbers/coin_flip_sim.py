# -*- coding: utf-8 -*-

from random import choice

coin_sides = ('heads', 'tails')

def coin_flip(n):
    """Returns a dictionary with coin's sides as the keys, and with its
       value corresponding to the number of times that side was landed
       on."""
    result = {}
    for coin_side in coin_sides:
        result[coin_side] = 0
    for _ in range(n):
        result[choice(coin_sides)] += 1
    return result