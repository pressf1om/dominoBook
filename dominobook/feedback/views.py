from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)  # Остаёмся на той же странице
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'form': form})

