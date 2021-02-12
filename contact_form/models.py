from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Contact(models.Model):
    first_name = models.CharField('Имя', max_length=200, null=False, blank=True, )
    second_name = models.CharField('Фамилия', max_length=200, null=True, blank=True )
    last_name = models.CharField('Отчество', max_length=200, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=200, null=True, blank=True )
    email = models.EmailField('Электронная почта', max_length=150,)
    user_all = models.IntegerField('Номер билета' , validators=[MinValueValidator(1),
                                       MaxValueValidator(13)], unique=True)



    def __str__(self):
        template = '{0.first_name} {0.second_name} {0.last_name} {0.email}  {user_all} '
        return template.format(self)