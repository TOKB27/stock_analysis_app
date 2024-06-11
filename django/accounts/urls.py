from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.auth_view, name="login"),
    path('logout/', views.loguout_view, name='logout'),
]