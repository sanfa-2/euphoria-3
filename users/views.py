from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from users.forms import UserForm
from .models import Profile



def login(request):
    next_url = request.GET.get('next') 
    context = {'title': 'Login', 'next': next_url}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next') 

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
               
                return HttpResponseRedirect( reverse('web:index'))

        context.update({
            'error': True,
            'message': 'Invalid username or password',
        })

    return render(request, 'users/login.html', context)



def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:index'))

def signup(request):
    context = {}  

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            
            user = User.objects.create_user(
                username=instance.username,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name,
                password=instance.password
            )

            
            user = authenticate(request, username=instance.username, password=instance.password)
            auth_login(request, user)

            return HttpResponseRedirect(reverse('web:index'))
        else:
           
            context['form'] = form

    else:
        form = UserForm()

    
    context.update({
        'title': 'Signup',
        'form': form
    })

    return render(request, 'users/signup.html', context=context)



@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/update_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

  