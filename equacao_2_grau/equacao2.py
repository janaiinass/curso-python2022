import math

def delta(A, B, C):
    d = B ** 2 - 4*A*C
    return d


def delta1(A, B, d):
    X1 = (-B + math.sqrt(d))/2*A
    return X1


def delta2(A, B, d):
    X2 = (-B - math.sqrt(d))/2*A
    return X2


