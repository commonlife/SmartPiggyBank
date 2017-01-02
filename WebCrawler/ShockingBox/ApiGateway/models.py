from django.db import models

class Money(models.Model):
    user = models.TextField(max_length=20)
    money = models.IntegerField()
    won_500 = models.IntegerField()
    won_100 = models.IntegerField()

    def __str__(self):
        return "{} : {}".format(self.user, self.money)