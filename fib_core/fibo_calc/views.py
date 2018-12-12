from django.shortcuts import render
from fibo_calc.models import FibResults


def calculation(n: int, n0=0, n1=1):
    sl = [n0, n1]
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
    first_num = 0
    second_num = 1
    result = 0

    if request.GET.get('number'):
        number = request.GET.get('number')
        num = int(number)
        if request.GET.get('first_number'):
            first_number = request.GET.get('first_number')
            first_num = int(first_number)
            if request.GET.get('second_number'):
                second_number = request.GET.get('second_number')
                second_num = int(second_number)
                result = calculation(num, first_num, second_num)




    return render(
        request,
        'index.html',
        {
            'number': num,
            #'first_number': first_num,
            #'second_number': second_num,
            'result': result,
        }
    )

