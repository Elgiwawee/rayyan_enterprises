from .models import Article, Image, Video

def news_content(request):
    return {
        "articles": Article.objects.all(),
        "images": Image.objects.all(),
        "videos": Video.objects.all(),
    }