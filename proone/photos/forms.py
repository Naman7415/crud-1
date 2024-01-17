from django import forms
from photos.models import Author

class Find(forms.ModelForm):
    class Meta:
        model=Author
        fields = '__all__'