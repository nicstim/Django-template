from django.http import JsonResponse
from django.views.generic import View

from feedback.forms import FeedbackForm


class FeedbackView(View):
    def post(self, request):
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return JsonResponse({"status": 'ok'})
        return JsonResponse({"status": 'error'})
