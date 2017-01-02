from django.db import models

class Product(models.Model):
    product_id = models.TextField(max_length=20)
    name = models.TextField(max_length=100)
    link = models.TextField(max_length=200)
    thumb_image = models.TextField(max_length=100)
    price = models.IntegerField()
    delivery = models.TextField(max_length=15)
    category = models.TextField(max_length=20)

    def __str__(self):
        return "{}:{}원".format(self.name, self.price)