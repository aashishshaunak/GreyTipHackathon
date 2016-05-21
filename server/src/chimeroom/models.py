from django.db import models

class chimeRoom(models.Model):
    capacity = models.IntegerField()
    floor = models.IntegerField()
    name = models.CharField(max_length=50)
    active = models.BooleanField()
    white_board = models.BooleanField()
    projector = models.BooleanField()
    internet = models.BooleanField()
    wi_fi = models.BooleanField()
    intercom = models.BooleanField()
    tele_conferencing = models.BooleanField()
    video_conferencing = models.BooleanField()
    is_locked = models.BooleanField()