from django import forms
from .models import PostModel, Comment


class PostModelForm(forms.ModelForm):
    Area= forms.CharField(max_length=200)
    bedrooms = forms.IntegerField()
    bathrooms = forms.IntegerField()
    hospitals_nearby = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}))
    colleges_nearby = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}))

    class Meta:
        model = PostModel
        fields = ('title', 'Area', 'bedrooms', 'bathrooms', 'hospitals_nearby', 'colleges_nearby')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'Area', 'bedrooms', 'bathrooms', 'hospitals_nearby', 'colleges_nearby')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))

    class Meta:
        model = Comment
        fields = ('content',)
