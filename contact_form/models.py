from django.db import models


class Contact(models.Model):
    first_name = models.CharField('Имя', max_length=200)
    second_name = models.CharField('Фамилия', max_length=200)
    last_name = models.CharField('Отчество', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    email = models.EmailField('Электронная почта', max_length=150)




    number_choice = (('1', '1'),
                   ('2', '2'),
                   ('3', '3'),
                   ('4', '4'),
                   ('5', '5'),
                   ('6', '6'),
                   ('7', '7'),
                   ('8', '8'),
                   ('9', '9'),
                   ('10', '10'),
                   ('11', '11'),
                   ('12', '12'),

                   )

    number = models.CharField('Выберите ваш уникальный индефикатор ', max_length=50, blank=True, choices=number_choice , unique=True)


    def __str__(self):
        template = '{0.first_name} {0.second_name} {0.last_name} {0.email} {0.number}'
        return template.format(self)