from django.db import models

# Create your models here.
class MainPrice(models.Model):
    date = models.TextField()
    data_name = models.TextField()
    price_data = models.TextField()
    volumn = models.TextField()

class PredictPrice(models.Model):
    name = models.TextField()
    b_7 = models.TextField()
    b_6 = models.TextField()
    b_5 = models.TextField()
    b_4 = models.TextField()
    b_3 = models.TextField()
    b_2 = models.TextField()
    b_1 = models.TextField()
    b_0 = models.TextField()
    a_1 = models.TextField()
    a_2 = models.TextField()
    a_3 = models.TextField()
    a_4 = models.TextField()
    a_5 = models.TextField()
    a_6 = models.TextField()
    a_7 = models.TextField()

class Output(models.Model):
    o_1 = models.TextField()
    o_2 = models.TextField()
    o_3 = models.TextField()
    o_4 = models.TextField()
    o_5 = models.TextField()
    o_6 = models.TextField()
    o_7 = models.TextField()
    o_8 = models.TextField()
    o_9 = models.TextField()
    o_10 = models.TextField()
    o_11 = models.TextField()
    o_12 = models.TextField()
    o_13 = models.TextField()
    o_14 = models.TextField()
    o_15 = models.TextField()
    o_16 = models.TextField()
    o_17 = models.TextField()



# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)