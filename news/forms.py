from django import forms
from .models import Article, Image, Video
from django.utils.translation import activate, gettext_lazy as _

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = ['title', 'content']
        label = {
            'title' : _('Title'),
            'content' : _('Content'),
        }

class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)

    class Meta:
        model = Image
        fields = ['title', 'image',]
        label = {
            'title' : _('Title'),
            'image' : _('Image'),
        }


class VideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)

    class Meta:
        model = Video
        fields = ['title', 'video',]
        label = {
            'title' : _('Title'),
            'video' : _('Video'),
        }

