from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def signout(request):
    logout(request)
    return redirect('products:index')

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)

            return redirect('products:index')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context) 