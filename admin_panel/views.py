from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from news.models import Article, Image, Video
from programs.models import Program
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import activate, gettext_lazy as _
from django.contrib import messages

def is_admin(user):
    return user.is_authenticated and user.is_staff  # Only staff can access

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    articles = Article.objects.all()
    programs = Program.objects.all()
    images = Image.objects.all()
    videos = Video.objects.all()
    return render(request, 'admin_panel/dashboard.html', {
        'articles': articles, 
        'images':images,
        'videos':videos, 
        'programs': programs,
    })

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:admin_dashboard')  # Prevent logged-in users from seeing login page

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Only allow staff users
            login(request, user)
            return redirect('admin_panel:admin_dashboard')
        else:
            messages.error(request, _("Invalid credentials or not an admin."))
            return redirect('admin_panel:admin_login')

    return render(request, 'admin_panel/login.html')

def admin_logout(request):
    logout(request)
    messages.info(request, _("You have been logged out."))
    return redirect('admin_panel:admin_login')
