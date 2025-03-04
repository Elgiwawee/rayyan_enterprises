from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Program
from .forms import ProgramForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.translation import activate, gettext_lazy as _


def is_admin(user):
    return user.is_authenticated and user.is_staff


# List all programs
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})

# View a single program's details
def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'programs/program_detail.html', {'program': program})

# Create a new program
@login_required
@user_passes_test(is_admin)
def create_program(request):
    activate('ar')
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _('Program created successfully'))
            return redirect('programs:program_list')  # Redirect to the program list
        else:
            messages.error(request, _('Something went wrong'))
            return redirect('programs:create_program')    
    else:
        form = ProgramForm()
    return render(request, 'programs/program_form.html', {'form': form})

# Update an existing program
@login_required
@user_passes_test(is_admin)
def update_program(request, pk):
    activate('ar')
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.info(request, _('Program updated successfully'))
            return redirect('programs:program_list')
        else:
            messages.error(request, _('Something went wrong'))
            return redirect('programs:update_program')   
    else:
        form = ProgramForm(instance=program)
    return render(request, 'programs/program_form.html', {'form': form})

# Delete a program
@login_required
@user_passes_test(is_admin)
def delete_program(request, pk):
    activate('ar')
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        messages.info(request, _('Program deleted successfully'))
        return redirect('programs:program_list')
    return render(request, 'programs/delete_program.html', {'program': program})
