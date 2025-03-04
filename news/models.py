from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title

class   Image(models.Model):  
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='videos', null=True, blank=True)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/")  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
