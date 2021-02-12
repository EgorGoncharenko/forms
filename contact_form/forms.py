from django.forms import  ModelForm
from  django.forms import  Textarea
from  .models import Contact





class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'second_name', 'last_name', 'phone', 'email','user_all' ]

