from rest_framework import serializers

from .models import MainPrice
# from accounts.serializers import UserSerializer

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPrice
        fields = ['id', 'date', 'data_name', 'price_data', 'volumn']

# class MainPrice(models.Model):
#     date = models.TextField()
#     data_name = models.TextField()
#     price_data = models.TextField()
#     volumn = models.TextField()
