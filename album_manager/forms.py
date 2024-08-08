from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'country_of_origin']
        labels = {
            'name': 'Nombre del Artista',
            'country_of_origin': 'País de Origen',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_year', 'genre', 'artist', 'cover']
        labels = {
            'title': 'Título del Álbum',
            'release_year': 'Año de Lanzamiento',
            'genre': 'Género',
            'artist': 'Artista',
            'cover': 'Portada',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
