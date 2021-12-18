from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('game', views.game, name='game'),
    path('AU', views.AU, name='about'),
    path('ps', views.PS, name='pst'),
    path('reg', views.register, name='registers'),
    path('XBOX',views.XBOX, name='XBOX'),
    path('news', views.news, name='news'),
    path('PC', views.PC, name='PC'),
    path('pay', views.pay, name='pay'),
    path('auth', views.auth, name='auth'),
]
