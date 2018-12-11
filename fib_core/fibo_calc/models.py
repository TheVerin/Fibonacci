from django.db import models


class FibResults(models.Model):
    number = models.IntegerField()
    result = models.IntegerField()

    class Metaclass:
        db_table = 'fib_results'

    def __unicode__(self):
        return self.number
