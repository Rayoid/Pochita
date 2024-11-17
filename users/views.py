from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Client
from .forms import CustomUserCreationForm, ClientRegistrationForm

def register_client(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        client_form = ClientRegistrationForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            Client.objects.create(
                user=user,
                name=client_form.cleaned_data['name'],
                phone_number=client_form.cleaned_data['phone_number'],
                address=client_form.cleaned_data['address']
            )
            login(request, user)
            messages.success(request, "¡Registro exitoso! Bienvenido a Pochita S.A.")
            return redirect('landing_page')
    else:
        user_form = CustomUserCreationForm()
        client_form = ClientRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'client_form': client_form})
