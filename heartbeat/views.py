from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.translation import activate
from django.views.generic import TemplateView


def home(request):
    # request.LANGUAGE_CODE = "ar"
    activate("ar")
    return render(request, "home.html")


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        activate("ar")
        return super().get(request, *args, **kwargs)


