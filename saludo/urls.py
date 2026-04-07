from django.urls import path
from .views import UserView, RoleView, hola_mundo 

urlpatterns = [ 
    path('users/', UserView.as_view()), 
    path('roles/', RoleView.as_view()), 
     path('', hola_mundo), 
    
]
