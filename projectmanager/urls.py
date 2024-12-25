from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    
    
]


urlpatterns += [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('clients_page/', views.clients_page, name='clients_page'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),

]
