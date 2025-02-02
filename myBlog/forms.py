from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = Post
        fields = '__all__'
        # categorys = [('news', 'news'),('memes', 'memes'),('sport', 'sport'),('music', 'music'),('politic', 'politic')]
        widgets = {
            'title': forms.TextInput(attrs = {"class":"form-control"}),
            'author': forms.Select(attrs={"class": "form-control"}),
            'text': forms.Textarea(attrs={"class": "form-control"}),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholdder':'Enter category'})
        }














