from django import forms 
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'image', 'image_alt')

        widgets = {
            'image': forms.FileInput,
            'image_alt': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),         
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'authorField', 'value':'', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),                   
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'image_alt', 'category')

        widgets = {
            'image': forms.FileInput,
            'image_alt': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),         
            'title': forms.TextInput(attrs={'class': 'form-control'}),       
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}), 
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),         
        }