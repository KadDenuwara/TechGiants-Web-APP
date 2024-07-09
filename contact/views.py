from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            print(form.cleaned_data)
            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        else:
            # Return a JSON response indicating failure and form errors
            return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
