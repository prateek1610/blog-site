from django import forms
from blog.models import Post,Comment,Register
from django.contrib.auth.models import User
from django.contrib import auth

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': "form-control",
                                                             'placeholder': "enter username..."}))
    class Meta():
        model=User
        fields=('username','email','password')



class RegisterForm(forms.ModelForm):
    class Meta():
        model=Register
        fields=('name','age')


class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','topic','text')

        widgets={
            'topic':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
