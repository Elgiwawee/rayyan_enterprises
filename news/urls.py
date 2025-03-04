from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    article_list, article_detail, create_article,
    update_article, delete_article, image_list, add_image, delete_image,
    video_list, add_video, delete_video
)
app_name = "news"
urlpatterns = [
    path('', article_list, name='article_list'),
    path('<int:pk>/', article_detail, name='article_detail'),
    path('create/', create_article, name='create_article'),
    path('<int:pk>/edit/', update_article, name='update_article'),
    path('<int:pk>/delete/', delete_article, name='delete_article'),

    path('images/', image_list, name='image_list'),
    path('images/add/', add_image, name='add_image'),
    path('images/delete/<int:image_id>/', delete_image, name='delete_image'),

    path('videos/', video_list, name='video_list'),
    path('videos/add/', add_video, name='add_video'),
    path('videos/delete/<int:video_id>/', delete_video, name='delete_video'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
