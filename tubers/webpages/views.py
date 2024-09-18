from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtubers

# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    team_members = Team.objects.all()
    featured_youtubers = Youtubers.objects.order_by('-created_date').filter(is_featured=True)
    latest_on_board = Youtubers.objects.order_by('-created_date')
    data = {
        "sliders": sliders,
        "team_members": team_members,
        "featured_youtubers": featured_youtubers,
        "latest_on_board":latest_on_board,
    }
    return render(request, "webpages/home.html", data)


def about(request):
    team_members = Team.objects.all()
    data ={
        "team_members": team_members,
    }
    return render(request, "webpages/about.html", data)


def services(request):
    sliders = Slider.objects.all()
    data = {
        "slider": sliders,
    }
    return render(request, "webpages/services.html", data)


def contact(request):
    return render(request, "webpages/contact.html")
