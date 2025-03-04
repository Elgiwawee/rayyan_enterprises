from .models import Program

def program_list(request):
    return {"programs": Program.objects.all()}
