from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('sign_up/', views.signUpPage, name='sign_up'),
    path('add_note/', views.addNote, name='add_note'),
    path('edit_note/<str:pk>/', views.editNote,name='edit_note'),
    path('delete_note/<str:pk>/', views.deleteNote,name='delete_note'),

]
