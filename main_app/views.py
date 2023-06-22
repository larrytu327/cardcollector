from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Card

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CardsList(TemplateView):
    template_name = "cards_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # name = self.request.GET.get('name')
        # if name != None:
        #     context["cards"] = Card.objects.filter(name__icontains=name)
        # else:
        context["cards"] = Card.objects.all()
        return context