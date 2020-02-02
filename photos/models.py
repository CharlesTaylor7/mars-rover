from django.db import models


class Rover(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(db_index=True, max_length=200)
    landing_date = models.DateField(default=None)
    launch_date = models.DateField(default=None)
    status = models.CharField(max_length=50)
    max_sol = models.IntegerField()
    max_date = models.DateField(default=None)
    total_photos = models.IntegerField()


class Camera(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(db_index=True, max_length=50)
    full_name = models.CharField(max_length=200)
    rover = models.ForeignKey(Rover, on_delete=models.SET_NULL, null=True)


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    sol = models.IntegerField()
    img_src = models.CharField(max_length=200)
    earth_date = models.DateField(db_index=True, default=None)
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, null=True)
