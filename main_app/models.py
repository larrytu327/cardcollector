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
    ab = models.IntegerField(default=0)
    ba = models.IntegerField(default=0)
    obp = models.IntegerField(default=0)
    hr = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    sb = models.IntegerField(default=0)
    r = models.IntegerField(default=0) 
    h = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    team = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="season_stats")

    def __str__(self):
        return self.year
    class Meta:
        ordering = ['year']

class MyTeam(models.Model):
    name = models.CharField(max_length=150)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name
    