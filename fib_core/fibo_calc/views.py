from django.shortcuts import render
from .models import FibResults


def calculation(n: int):
    sl = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n - 1):
            sl.append(sl[-1] + sl[-2])
        return sl[-1]



