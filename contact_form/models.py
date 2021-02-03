from django.db import models


class Contact(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    second_name = models.CharField('Фамилия', max_length=200)
    last_name = models.CharField('Отчество', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    email = models.EmailField('Электронная почта', max_length=150)
    message = models.TextField('Заголовок', blank=True)


    def __str__(self):
         template = '{0.first_name} {0.second_name} {0.last_name} {0.email} {0.message}'
         return template.format(self)