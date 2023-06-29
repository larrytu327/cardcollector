from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Player, Season_Stat
from django.urls import reverse


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class PlayersList(TemplateView):
    template_name = "players_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["players"] = Player.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["players"] = Player.objects.all()
            context["header"] = "Favorite Players"
        return context

class PlayerCreate(CreateView):
    model = Player
    fields = ['name', 'img', 'bio']
    template_name = "player_create.html"
    success_url = "/players/"

    def get_success_url(self):
        return reverse('player_detail', kwargs={'pk': self.object.pk})

class PlayerDetail(DetailView):
    model = Player
    template_name = "player_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["season_stats"] = Season_Stat.objects.all()
        return context

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name','img', 'bio']
    template_name = "player_update.html"
    success_url = "/players/"

    def get_success_url(self):
        return reverse('player_detail', kwargs={'pk': self.object.pk})

class PlayerDelete(DeleteView):
    model = Player
    template_name = "player_delete_confirmation.html"
    success_url = "/players/"

class Season_StatCreate(View):

    def post(self, request, pk):
        ab = request.POST.get("ab")
        ba = request.POST.get("ba")
        obp = request.POST.get("obp")
        hr = request.POST.get("hr")
        rbi = request.POST.get("rbi")
        sb = request.POST.get("sb")
        r = request.POST.get("r")
        h = request.POST.get("h")
        g = request.POST.get("g")
        year = request.POST.get("year")
        team = request.POST.get("team")
        player = Player.objects.get(pk=pk)
        Season_Stat.objects.create(ab=ab, ba=ba, obp=obp, hr=hr, rbi=rbi, sb=sb, r=r, h=h, g=g, year=year, team=team, player=player)
        return redirect('player_detail', pk=pk)