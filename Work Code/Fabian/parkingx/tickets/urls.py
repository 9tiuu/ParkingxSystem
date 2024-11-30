from django.urls import path
from tickets import views
from .views import CreateRol, CreateUsuario, ListUsuario, UpdateUsuario, DeleteUsuario, CreateProtocolo, UpdateProtocolo, DeleteProtocolo, CreateTicketE, UpdateTicketE, DeleteTicketE, DetailTicketE, ListRol, UpdateRol, DeleteRol, ListTicketState, CreateTicketState, UpdateTicketState, DeleteTicketState, CloseTicketE, TicketSView, DeleteTicketS, UpdateTicketS, DetailTicketS
from .views import custom_logout
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/', views.Home, name='home'),
    
    # ----------------------------------- # ROLES
    path('createrol/', CreateRol.as_view(), name='createrol'),
    path('listrol/', ListRol.as_view(), name='listrol'),
    path('updaterol/<int:pk>/', UpdateRol.as_view(), name='updaterol'),
    path('deleterol/<int:pk>/', DeleteRol.as_view(), name='deleterol'),

    # ----------------------------------- # PRTOCOLOS
    path('protocolos/', CreateProtocolo.as_view(), name='protocolos'),
    path('protocoloUpdate/<int:pk>/', UpdateProtocolo.as_view(), name='protocoloUpdate'),
    path('protocoloDelete/<int:pk>/', DeleteProtocolo.as_view(), name='protocoloDelete'),

    # ----------------------------------- # USUARIOS
    path('usercreate/', CreateUsuario.as_view(), name='usercreate'),
    path('userlist/', ListUsuario.as_view(), name='userlist'),
    path('userupdate/<int:pk>/', UpdateUsuario.as_view(), name='userupdate'),
    path('userdelete/<int:pk>/', DeleteUsuario.as_view(), name='userdelete'),

    # ----------------------------------- # ESTADOS DE TICKETS
    path('statelist/', ListTicketState.as_view(), name='statelist'),
    path('statecreate/', CreateTicketState.as_view(), name='statecreate'),
    path('stateupdate/<int:pk>/', UpdateTicketState.as_view(), name='stateupdate'),
    path('statedelete/<int:pk>/', DeleteTicketState.as_view(), name='statedelete'),

    # ----------------------------------- # TICKETS DE ENTRADA
    path('ticketE/', CreateTicketE.as_view(), name='ticketE'),
    path('ticketEUpdate/<int:pk>/', UpdateTicketE.as_view(), name='ticketEupdate'),
    path('ticketEDelete/<int:pk>/', DeleteTicketE.as_view(), name='ticketEdelete'),
    path('ticketEDetail/<int:pk>/', DetailTicketE.as_view(), name='ticketEdetail'),
    path('ticketEClose/<int:pk>/', CloseTicketE.as_view(), name='ticketEclose'),

    # ----------------------------------- # TICKETS DE SALIDA
    path('ticketS/', TicketSView.as_view(), name='ticketS'),
    path('ticketSUpdate/<int:pk>/', UpdateTicketS.as_view(), name='ticketSupdate'),
    path('ticketSDelete/<int:pk>/', DeleteTicketS.as_view(), name='ticketSdelete'),
    path('ticketSDetail/<int:pk>/', DetailTicketS.as_view(), name='ticketSdetail'),

    path('logout/', custom_logout, name='logout'),
    path('', LoginView.as_view(), name='login'),
]