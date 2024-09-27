from .forms import FeedbackForm


def feedback_form(request):
    form = FeedbackForm()
    return {'feedback_form': form}
