from django.urls import path,include
from first_recall import views

app_name='first_recall'

urlpatterns=[
path('register/',views.register,name="register"),
path('login/',views.user_login,name="user_login")
]
