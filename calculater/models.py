from django.db import models


# Create your models here.
class Cuserdata(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id', auto_created=True)
    username = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    operation = models.IntegerField()

    class Meta:
        db_table = 'Cuserdata'
