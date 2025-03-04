from .models import Article, Image, Video


def article_list(request):
    return {"news": Article.objects.all()}

def image_list(request):
    return {"news": Image.objects.all()}

def video_list(request):
    return {"news": Video.objects.all()}