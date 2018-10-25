from django.db import models


class Herder(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return 'Herder {}'.format(self.name)


class Farm(models.Model):
    herder = models.ForeignKey(Herder, on_delete=models.CASCADE)

    def __str__(self):
        return 'Farm'


class Goat(models.Model):
    name = models.CharField(max_length=50)
    herder = models.ForeignKey(Herder, on_delete=models.CASCADE)

    def __str__(self):
        return 'Goat {}'.format(self.name)
