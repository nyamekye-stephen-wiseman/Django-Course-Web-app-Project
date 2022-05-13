from django.urls import path
from . views import (
project,
projects,
createForm,
updateForm,
deleteProject,
)

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),
    path('create-form/', createForm, name="create-form"),
    path('update-form/<pk>/', updateForm, name='update-form'),
    path('delete-project/<pk>/', deleteProject, name='delete-project'),
    
   
]