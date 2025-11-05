from django import forms
from .models import Publication, Comments




class CreatePublicationForm(forms.ModelForm):
    
    class Meta:
        model = Publication
        fields = ("title", "text" )



class CreateCommentsForms(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
