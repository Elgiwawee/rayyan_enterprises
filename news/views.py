from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Image, Video
from django.contrib import messages
from .forms import ArticleForm, ImageForm, VideoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.translation import activate, gettext_lazy as _
~~~
def is_admin(user):
    return user.is_authenticated and user.is_staff


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})

@login_required
@user_passes_test(is_admin)
def create_article(request):
    activate('ar')
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('Article created successfully'))
            return redirect('news:article_list')
        else:
            messages.error(request, _('Something went wrong'))
            return redirect('news:create_article')
    else:
        form = ArticleForm()
    return render(request, 'news/article_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def update_article(request, pk):
    activate('ar')
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.info(request, _('Article updated successfully'))
            return redirect('news:article_detail', pk=pk)
        else:
            messages.error(request, _('Something went wrong'))
            return redirect('news:update_article')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news/article_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_article(request, pk):
    activate('ar')
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        messages.info(request, _('Article deleted successfully'))
        return redirect('news:article_list')
    return render(request, 'news/delete_article.html', {'article': article})


def image_list(request):
    """ Show all images """
    images = Image.objects.all().order_by('-created_at')
    return render(request, 'news/image_list.html', {'images': images})

@login_required
@user_passes_test(is_admin)
def add_image(request):
    activate('ar')
    """ Add a new image """
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Image uploaded successfully!"))
            return redirect('news:image_list')
        else:
            messages.error(request, _('Something went wrong!'))
            return redirect('news:add_image')    
    else:
        form = ImageForm()
    return render(request, 'news/image_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_image(request, image_id):
    activate('ar')
    """ Delete an image """
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    messages.success(request, _("Image deleted successfully!"))
    return redirect('news:image_list')

def video_list(request):
    """ Show all videos """
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'news/video_list.html', {'videos': videos})

@login_required
@user_passes_test(is_admin)
def add_video(request):
    activate('ar')
    """ Add a new video """
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Video uploaded successfully!"))
            return redirect('news:video_list')
        else:
            messages.error(request, _('Something went wrong'))
            return redirect('news:add_video')
    else:
        form = VideoForm()
    return render(request, 'news/video_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_video(request, video_id):
    activate('ar')
    """ Delete a video """
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    messages.success(request, _("Video deleted successfully!"))
    return redirect('news:video_list')