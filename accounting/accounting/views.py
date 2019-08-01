from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def signup(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm(),
        }
        return render(request, 'signup.html', context)

    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'signup.html',{'form':form})
def _login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username = u,password = p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context = {
                'error':'user with these credential does not exist'
            }
            return redirect(request,'login.html,context')

@login_required(login_url='/login')
def dashboard(request):
    return render(request,'dashboard.html')


