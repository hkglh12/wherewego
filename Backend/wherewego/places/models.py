from django.db import models


class RawData(models.Model):
    title = models.CharField(max_length=500, default= " ")
    contents = models.TextField(null=True, blank=True, default=" ")
    #url = models.TextField(null=True, blank=True, default=" ")
    keywords = models.TextField(null=True, blank=True, default=" ")
    class Meta:
        db_table = "rawdata"


class Dic(models.Model):
    local_index = models.IntegerField()
    morpheme = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default=" "
        )
    score = models.IntegerField()
    coord_latitude = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        default=" "
    )
    coord_longitude = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        default=" "
    )

    class Meta:
        db_table = "dic"

class DBContest(models.Model):
    testtext = models.CharField(max_length=500, default="")

    class Meta:
        db_table = "conntestdb"