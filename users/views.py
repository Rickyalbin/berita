from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from myproject.views import login

from .models import Biodata
# Create your views here.
from.forms import UserForms


def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title':'List Pengguna',
        'list_user':list_user
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_detil(request, id):
    template_name = "back/user_detil.html"
    try:
        user_info = User.objects.get(id=id)
        biodataku = Biodata.objects.get(user=user_info)
    except:

        return redirect(users)
    context = {
        'title': 'User Detail',
        'user_info': user_info,
        'biodataku': biodataku,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_edit(request, id):
    template_name = "back/user_edit.html"
    try:
        user_info = User.objects.get(id=id)
        biodataku = Biodata.objects.get(user=user_info)
    except:
        return redirect(users)

    if request.method == "POST":
        forms_user = UserForms(request.POST, instance=user_info)
        if forms_user.is_valid():
            test = forms_user.save(commit=False)
            test.is_active = True
            test.save()
            print('testing form')
            return redirect(users)
    else:
        forms_user = UserForms(instance=user_info)
        
    context = {
        'title': 'User Edit',
        'user_info': user_info,
        'biodataku': biodataku,

        'form_user':forms_user,
            
        }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_delete(request, id):
    try:
        User.objects.get(id=id).delete()
    except:
        pass
    return redirect('users')