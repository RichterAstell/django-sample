from django.urls import path

from . import views

app_name = 'employee'
urlpatterns = [
    # path('signin/', views.signin.signin, name='signin'),
    # path('signin/', views.signin.signin2, name='signin2'),
    # path('search/', views.search, name='search'),
    # path('signin/', views.signin, name='signin'),
    # path('signin2/', views.signin2, name='signin2'),
    # path('signout/', views.signout, name='signout'),
    # path('login/', views.Login.as_view(), name='login'),
    path('/search', views.signin.index, name='search'),
]
