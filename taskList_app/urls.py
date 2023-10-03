from django.urls import path

from taskList_app import views
\

urlpatterns = [
    path('', views.home, name="home"),
    path('how-it-works/', views.howitworks, name="how-it-works"),
    path('login/', views.loginPage, name="login"),
    path('signup/', views.signupPage, name="signup"),
]
