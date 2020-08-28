from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import RegistrationForm

def RegistrationView(request):
    context = []
    if request.POST:
        