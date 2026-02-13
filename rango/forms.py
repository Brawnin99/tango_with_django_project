from django.contrib.auth.models import User
from django import forms
from rango.models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)
        help_texts = {
            'name' : "Please enter the category name."
        }


class PageForm(forms.ModelForm):
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)
        help_texts = {
            'title' : "Please enter the title of the page.",
            'url' : "Please enter the URL of the page.",
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('website', 'picture')