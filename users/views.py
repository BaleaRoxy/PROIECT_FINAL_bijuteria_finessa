import secrets
from django.shortcuts import render, redirect, Http404, reverse
from users.forms import RegisterForm, UserImageForm, ProfileImageForm
from django.contrib.auth import authenticate, login, logout
from users.email import send_register_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # send_register_mail(user)

            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next', None)

        # if not username or not password:
        #     raise Http404('Username or password not provided!')
        user = authenticate(request, username=username, password=password)

        if user is None:
            raise Http404('Username or password not provided!')
        else:
            login(request, user)

            if next:
                return redirect(next)

            return redirect('/')

    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('/')


def upload_view(request):
    if request.method == 'GET':
        form = UserImageForm()
    else:
        form = UserImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'users/file_uploaded.html')

    return render(request, 'users/upload.html', {
        'form': form
    })


@login_required
def profile_view(request):
    if request.method == 'GET':
        form = ProfileImageForm()
    else:
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form
    })