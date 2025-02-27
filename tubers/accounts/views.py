from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Youtubers
from django.shortcuts import render, get_object_or_404
from  contactinfo.models import Contactinfo
# from .models import Profile


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Succesfully logged in!")
            return redirect("dashboard")
        else:
            messages.error(
                request, "PLease check the credentials! OR regiter if you are new here."
            )
            return redirect("login")
        # contactinfo = Contactinfo.objects.latest('id')
        # contactinfo = User.objects.latest('id')
    # data = {
    #     'contactinfo':contactinfo,
    # }
    return render(request, "accounts/login.html")


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exits")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exits")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=firstname,
                        last_name=lastname,
                        username=username,
                        email=email,
                        password=password,
                    )
                    user.save()
                    messages.success(request, "Account crearted succesfully")
                    return redirect("login")
        else:
            messages.warning(request, "Password do not match")
            return redirect("register")

    return render(request, "accounts/register.html")


def logout_user(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def dashboard(request):
    tubers = Youtubers.objects.order_by('-created_date')
    # tuber = get_object_or_404(Youtubers)
    contactinfo = User.objects.latest('id')
    data ={
        'tuber':tubers,
        'contactinfo':contactinfo,
    }
    return render(request, 'accounts/dashboard.html', data)