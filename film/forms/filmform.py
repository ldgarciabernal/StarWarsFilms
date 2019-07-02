from django import forms

class FilmForm(forms.Form):
    film_name = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search Star Wars film', 'list' : 'filmNames', 'id' : 'searhInput'}))