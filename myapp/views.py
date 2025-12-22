from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from myapp.models import Contact,Registeration
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect



# Create your views here.

def homepage(request):
    return render(request, 'home.html')

@login_required
def aboutpage(request):
    return render(request, 'about.html')

@login_required
def servicespage(request):
    return render(request, 'services.html')

def contactuspage(request):
    if request.method=="POST":
        fullname=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        img = request.FILES.get('image')


        model = Contact.objects.create(
            full_name=fullname, 
            email=email,
            phone_no=phone,
            subject=subject,
            message=message,
            img=img)
        model.save()
    
    
    return render(request, 'contactus.html')

def submitpage(request):
    pass

@login_required
def contactdetailpage(request):
    model = Contact.objects.all()

    return render(request, 'contactdetail.html', {"det": model})
       



def loginpage(request):
    # Use AuthenticationForm which handles validation & non-field errors
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # redirect to named URL 'home' (change if your url is different)
            return redirect('home')
        else:
            # AuthenticationForm provides non_field_errors; show a friendly message
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html", {"form": form})


def registrationpage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                # Create the auth user (this hashes the password)
                new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=raw_password
                )

                # OPTIONAL: save to your Registeration profile model
                # If Registeration has fields username/email/password currently,
                # it's better to convert it to a profile with OneToOne to User.
                try:
                    profile = form.save(commit=False)   # creates Registeration instance
                    # If your Registeration model has a ForeignKey/OneToOne to User:
                    # profile.user = new_user
                    # If not, and it stores duplicate fields, set them:
                    # profile.username = username
                    # profile.email = email
                    # DO NOT store raw password in profile. If you must store something,
                    # store nothing or a hashed value — better: remove password field from profile.
                    profile.save()
                except Exception:
                    # If your form isn't a ModelForm for Registeration, ignore silently.
                    pass

                messages.success(request, "Registration successful. Please log in.")
                return redirect('login')   # or redirect('myapp:login') if namespaced

        else:
            # shows field-specific errors in template because we return the bound form
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegisterForm()

    return render(request, "registration.html", {"form": form})




def logoutpage(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")   # or redirect('myapp:login') if namespaced
