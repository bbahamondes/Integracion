from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signin', views.login, name='login'),
    path('signin', views.validate, name='validate'),
    path('web/index', views.index, name='index'),
]
#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('web/', include('django.contrib.auth.urls')),
]