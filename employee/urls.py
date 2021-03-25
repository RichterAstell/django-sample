from django.urls import path

from . import views

app_name = 'employee'
urlpatterns = [
    path('search/', views.search, name='search'),
    # path('login/', views.Login.as_view(), name='login'),
    path('signin/', views.signin, name='signin'),
    path('signin2/', views.signin2, name='signin2'),
    path('signout/', views.signout, name='signout'),
    # path('', views.index, name='search'),
]
