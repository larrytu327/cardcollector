from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Card:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

cards = [
    Card("Buster Posey", "https://upload.wikimedia.org/wikipedia/commons/5/54/Buster_Posey_in_2018_%28cropped%29.jpg", "Buster Posey's number is 28"),
    Card("Brandon Crawford", "https://s.hdnux.com/photos/01/26/05/73/22568647/4/1200x0.jpg", "Brandon Crawford plays Shortstop"),
    Card("Thairo Estrada", "https://www.si.com/.image/t_share/MTkyNTIxMTAwMjQ3MTgxMDQ5/usatsi_19091578.jpg", "Thairo Estrada throws and bats right handed"),
    Card("Mike Yastrzemski", "https://cdn.vox-cdn.com/thumbor/ITGWn0daqCPD2tUDyILCwuW6T9s=/0x0:5131x3421/1200x800/filters:focal(1961x1243:2781x2063)/cdn.vox-cdn.com/uploads/chorus_image/image/67148981/usa_today_14640293.0.jpg", "Mike Yastrzemski is grandson of Red Sox great Carl Yastrzemski"),
]

class CardsList(TemplateView):
    template_name = "cards_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cards"] = cards
        return context