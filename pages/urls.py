from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.save_comments, name="save_comments"),
    path('achievment/', views.save_comments_ach, name="save_comments_ach"),
    path('contact/', views.save_contacts, name="save_contacts"),
    path('delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('edit/<int:pk>/', views.edit_comment, name='edit_comment'),
    #path('delete/', views.delete_comment, name="delete_comment")
    ]