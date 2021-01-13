from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request,'registration/home.html')



@login_required(login_url='/login/')
def user_home(request):
    users=User.objects.all().order_by('username')
    context={'users':users}
    return render (request,'registration/user_home.html',context)



@login_required(login_url='/login/')
def add_user(request):
    if request.method != 'POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            
            return redirect('user:user_home')
    context={'form':form}
    return render(request,'registration/add_user.html',context)



@login_required(login_url='/login/')
def deleteUser(request,pk):
    query=User.objects.get(id=pk)
    if request.method =="POST":
        query.delete()
        return redirect('user:user_home')
    context={'item':query}
    return render(request,'registration/delete.html',context)


@login_required(login_url='/login/')
def edituser(request,user_id):
    user=User.objects.get(id=user_id)
    if request.method != 'POST':
        form=UserCreationForm(instance=user)
    else:
        form=UserCreationForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:user_home')
    context={'form':form,'user':user}
    return render(request,'registration/edit.html',context)