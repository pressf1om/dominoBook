from .forms import FeedbackForm


def feedback_form(request):
    return {'form': FeedbackForm()}