from django.urls import path

from . import views

urlpatterns = [
     
     
     path('<int:id>', views.edit_album, name='edit_album'),
     path('<int:id>', views.delete_post, name='delete_album'),


]