from django.db import models


class Region(models.Model):
    """Модель областей/районів для населених пунктів"""

    name = models.CharField(verbose_name='Область/район', max_length=64)

    class Meta:
        verbose_name = 'Область/район'
        verbose_name_plural = 'Області/райони'

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    """Модель населених пунктів"""
    name = models.CharField(verbose_name='Населений пункт', max_length=64)
    region = models.ForeignKey(Region, verbose_name='Область/район', blank=True, null=True, on_delete=models.SET_NULL,
                               related_name='city_in_region')

    class Meta:
        verbose_name = 'Населений пункт'
        verbose_name_plural = 'Населені пункти'

    def __str__(self):
        return f"{self.name} - {self.region}"
