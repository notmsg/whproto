from django.db import models
class Garbage(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    recycled_point = models.IntegerField()
    def display_information(self):
        return f"{self.name} is {self.type} type. Recycled point: {self.recycled_point}"
    def recycle(self):
        return f"Congratulations!!! {self.name} is recycled +{self.recycled_point} point!"