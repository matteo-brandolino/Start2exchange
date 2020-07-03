from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from app.models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            username = form.cleaned_data.get('username')
            wallet= form.cleaned_data.get('wallet')
            profile = Profile.objects.create(user=user, wallet=wallet)
            messages.success(request, f'Welcome, {username}. Now you can trade! {wallet} BTC are deposited in your wallet')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def admin(request):
    users = Profile.objects.all()
    return render(request, 'users/admin.html', {'users':users})
