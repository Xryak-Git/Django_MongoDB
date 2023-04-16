from datetime import datetime
from django.db import models


# Create your models here.


class Product(models.Model):
    title = models.CharField('Название', max_length=20, default='Хабарчик')
    price = models.IntegerField('Цена', default=0)
    date = models.DateTimeField('Дата публикации', auto_now_add=False, blank=True, default=datetime.now())
    #img =

    def __str__(self):
        return f'{self.title} | {self.price} | {self.date}'

    def get_absolute_url(self): # Тут мы создали новый метод
        return f'/shop/{self.id}'
