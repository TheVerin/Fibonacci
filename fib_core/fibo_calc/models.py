from django.db import models


class FibResults(models.Model):
    number = models.IntegerField()
    result = models.IntegerField()

    class Metaclass:
        db_table = 'fibo_calc'

    def __int__(self):
        return self.number
