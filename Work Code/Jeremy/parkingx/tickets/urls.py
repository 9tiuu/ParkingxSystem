from django.urls import path
from tickets import views
from .views import CreateRol, CreateUsuario, ListUsuario, UpdateUsuario, DeleteUsuario, CreateProtocolo, UpdateProtocolo, DeleteProtocolo
from .views import custom_logout
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('createrol/', CreateRol.as_view(), name='rolcreate'),
    path('protocolos/', CreateProtocolo.as_view(), name='protocolos'),
    path('protocoloUpdate/<int:pk>/', UpdateProtocolo.as_view(), name='protocoloUpdate'),
    path('protocoloDelete/<int:pk>/', DeleteProtocolo.as_view(), name='protocoloDelete'),
    path('usercreate/', CreateUsuario.as_view(), name='usercreate'),
    path('userlist/', ListUsuario.as_view(), name='userlist'),
    path('userupdate/<int:pk>/', UpdateUsuario.as_view(), name='userupdate'),
    path('userdelete/<int:pk>/', DeleteUsuario.as_view(), name='userdelete'),

    path('logout/', custom_logout, name='logout'),
    path('', LoginView.as_view(), name='login'),
]