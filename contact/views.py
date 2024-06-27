from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For now, we'll just print it to the console
            print(form.cleaned_data)
            # Redirect or show a success message
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

