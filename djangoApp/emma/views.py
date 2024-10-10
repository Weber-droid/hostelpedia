from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.

def success_view(request):
    return render(request, 'success.html')


def contact_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect after successful form submission
    else:
        form = StudentForm()
    
    return render(request, 'contact.html', {'form': form})
