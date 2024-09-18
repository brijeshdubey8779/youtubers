from django.urls import path
from . import views
import youtubers.views as yv

urlpatterns = [
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_user, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("<int:id>", yv.youtubers_detail, name="youtubers_detail"),
]
