from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True)
    stash = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    def __str__(self):
        return self.name
