# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from album import forms 
from album import models
from album.models import Album

def home(request):
    data = Album.objects.all()
    print(data)
    return render(request, 'home.html', {'data' : data})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id) # get_object_or_404 
    album_form = forms.AlbumForm(instance=album)
     
    if request.method == 'POST':  
         album_form = forms.AlbumForm(request.POST, instance=album)  
         if album_form.is_valid():  
              album_form.save() 
              return redirect('homepage')  
         
    
    return render(request, 'add_album.html', {'form' : album_form})




def delete_post(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')


