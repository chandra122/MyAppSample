from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

"""Creating a register View"""
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})

