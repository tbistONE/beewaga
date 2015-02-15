from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from beewaga_app.models import UserProfile
from beewaga_app.forms import UserCreateForm, AuthenticateForm


def home(request, user_form=None, auth_form=None):
    #If user is logged in, show different stuff.
    if request.user.is_authenticated():
        user = request.user
        return render(request, 
                     'buddies.html',
                     {'supporters': None, 'next_url': '/','username': user.username})
    #Else show blank page
    else:
        user_form = UserCreateForm()
        auth_form = AuthenticateForm()
        return render(request, 
                     'home.html',
                     {'user_form': user_form, 'auth_form': auth_form})


#Go to '/login' when 'Log in' button pressed.
def login_page(request):
    form = AuthenticateForm
    return render(request,
                'login.html',
                {'auth_form': form})


#Validate user's credentials upon logging in, redirect to home page.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            #Success!
            return redirect('/')
        else:
            #Failure!
            return home(request, auth_form = form)
    return redirect('/')

def register_view(request):
    form = UserCreateForm()
    return render(request,
                  'register.html',
                  {'user_form': form})





def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            # Want more sophisticated email verification here.
            login(request, user)
            return redirect('/')
        else:
            return home(request, user_form=user_form)
    return redirect('/')