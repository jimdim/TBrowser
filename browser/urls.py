from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    # path('browser/', include('browser.urls')),
]