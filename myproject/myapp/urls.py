# myapp/urls.py
from django.urls import path
from .views import signup, user_login, welcome

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('welcome/', welcome, name='welcome'),
]
