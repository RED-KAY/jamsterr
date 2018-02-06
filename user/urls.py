from django.urls import path
from . import views
from django.contrib.auth.views import login
from django.urls import reverse_lazy

app_name = 'user'

urlpatterns = [
    # /user/register/
    path('register/', views.UserFormView.as_view(), name='register'),
    # /user/login/
    path('login/',views.Login.as_view(), name='login'),
    # /user/logout/
    path('logout/', views.Logout, name='logout'),
]
