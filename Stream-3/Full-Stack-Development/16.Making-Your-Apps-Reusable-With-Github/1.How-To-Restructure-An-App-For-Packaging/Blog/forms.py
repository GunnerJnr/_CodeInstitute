from django import forms
from .models import Post


# inherit from ModelForm
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post  # ties to Post model so it will fetch data types from here
        fields = ('title', 'content', 'images')  # specifies the fields to display
