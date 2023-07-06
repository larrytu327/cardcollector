from django.contrib import admin
from .models import Player, Season_Stat, MyTeam
# Register your models here.

admin.site.register(Player) # this line will add the model to the admin panel
admin.site.register(Season_Stat)
admin.site.register(MyTeam)