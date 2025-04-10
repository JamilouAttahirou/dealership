from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Photo, Financing, Message, User
from django.forms import modelformset_factory # Formset for handling multiple photos


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'



class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=3)  # extra=3 means 3 blank forms by default


class FinancingForm(ModelForm):
    class Meta:
        model = Financing
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
