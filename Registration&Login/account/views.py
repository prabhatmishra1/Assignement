from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 

# Create your views here.
def Login_Signup(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form = AuthenticationForm(request.POST)
            error="Your username and password didn't match. Please try again."
            return render(request, 'login_signup.html', {'login_form': login_form,'error':error})
    else:
        login_form = AuthenticationForm()
        signup_form = UserCreationForm()
        return render(request, 'login_signup.html', {'login_form': login_form, 'signup_form':signup_form})


def CreateUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')

@login_required(login_url='/login/')
def homepage(rquest):
   return render(rquest,'home.html',{}) 
