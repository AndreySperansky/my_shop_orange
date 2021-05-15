from django.contrib.auth.decorators import login_required
from .models import ShopUser
from authapp.forms import ShopUserLoginForm
from authapp.forms import ShopUserRegisterForm
from authapp.forms import ShopUserEditForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse



def login(request):
    title = 'Вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        # print(login_form.cleaned_data)

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)


        else:
            messages.error(request, 'Invalid username/password!')


        return HttpResponseRedirect(reverse('main:index'))

    else:
        context = {'login_form': login_form, 'title': title}
        return render(request, 'authapp/login.html', context=context)


@login_required
def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)


        if register_form.is_valid():
            register_form.save()

            # Блок проверки совпадения пароля
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password2'])
            new_user.save()

            return HttpResponseRedirect(reverse('auth:login'))



    else:
        register_form = ShopUserRegisterForm()


    context = {'register_form': register_form, 'title': title}
    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('auth:edit'))

    # Перебрасывается сюда если запрос GET
    else:
        edit_form = ShopUserEditForm(instance=request.user)


    context = {'title': title, 'edit_form': edit_form }
    return render(request, 'authapp/edit.html', context=context)
