from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), #done
    path('projects/', views.save_projects, name="save_projects"), #done
    path('achievment/', views.save_achievements, name="save_achievements"),
    path('contact/', views.save_contacts, name="save_contacts"),
    path('delete/<int:pk>/', views.delete_project, name='delete_project'), #done
    path('edit/<int:pk>/', views.edit_project, name='edit_project'), #done
    #path('delete/', views.delete_comment, name="delete_comment")
    ]