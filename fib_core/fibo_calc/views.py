from django.shortcuts import render
from fibo_calc.models import FibResults


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

def fib_nums(request):
    num = 0
    result = 0

    if request.GET.get('number'):
        number = request.GET.get('number')
        num = int(number)
        result = calculation(num)



    return render(
        request,
        'index.html',
        {
            'number': num,
            'result': result,
        }
    )

