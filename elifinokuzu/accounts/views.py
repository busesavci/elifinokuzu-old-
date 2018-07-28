from django.contrib.auth import login, authenticate, forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from gravatar import templatetags
from .forms import UserExtendCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserExtendCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            return redirect('home')
    else:
        form = UserExtendCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def dashboard(request):
    # import pdb        #debugger
    # pdb.set_trace()
    return render(request, 'accounts/dashboard.html')
