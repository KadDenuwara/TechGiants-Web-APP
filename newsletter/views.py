from django.shortcuts import redirect, render

from .forms import SubscriberForm

def newsletter_signup(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_success')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/signup.html', {'form': form})

def newsletter_success(request):
    return render(request, 'newsletter/success.html')
