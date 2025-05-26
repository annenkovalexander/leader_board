from django.db import models

class Result(models.Model):
    competition = models.CharField(max_length=255)
    room_id = models.CharField(max_length=255)
    command_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    scenario = models.CharField(max_length=255)
    flight_time = models.FloatField()
    false_start = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name} - {self.competition} - {self.flight_time}"