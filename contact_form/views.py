from django.shortcuts import render
from django.views.generic import CreateView
from .models import  Contact
from django.urls   import   reverse_lazy
from django.http  import HttpResponse
from django.core.mail import send_mail
from .forms import  ContactForm
class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]}Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject,content):
 send_mail(subject, content, 'supporlib39@yandex.ru', ['bioshoker88@gmail.com'] )


def success(request):
      return  HttpResponse('Вы зарегистрированы на мероприятие Молодежной площадки КОНБ'
                           'Тема встречи:Ораторское мастерство'
                           'Cпикер:Михаил Мирошниченко'
                           'Дата:Проведения:05.02.2021'
                          'Начало:17:00'
                           'Место:Калининградская областная библиотека,Читальный зал,2 этаж '
                           'Адрес:пр.Мира,9/11'
                           'Продолжительность:60-80 минут')