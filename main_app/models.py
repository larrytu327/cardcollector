from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Player: " + self.name
    class Meta:
        ordering = ['name']

class Season_Stat(models.Model):
    AB = models.IntegerField(default=0)
    BA = models.IntegerField(default=0)
    OBP = models.IntegerField(default=0)
    HR = models.IntegerField(default=0)
    RBI = models.IntegerField(default=0)
    SB = models.IntegerField(default=0)
    R = models.IntegerField(default=0) 
    H = models.IntegerField(default=0)
    G = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    team = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="season_stats")

    def __str__(self):
        return self.year

