from django.contrib import admin
from .models import City, Region

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class RegionResource(resources.ModelResource):
    """Клас для реалізації імпорт-експорт моделі областей/районів"""

    name = fields.Field(attribute='name', column_name='Область/район')

    class Meta:
        fields = ('id', 'name')
        models = Region


class RegionAdmin(ImportExportActionModelAdmin):
    """Реєструємо модель областей/районів в адмінпанелі"""

    resource_class = RegionResource
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

    class Meta:
        models = Region


admin.site.register(Region, RegionAdmin)


class CityResource(resources.ModelResource):
    """Клас для реалізації імпорт-експорт моделі населених пунктів"""

    name = fields.Field(attribute='name', column_name='Населений пункт')
    region = fields.Field(attribute='region', column_name='Область/район', widget=ForeignKeyWidget(Region, 'name'))

    class Meta:
        fields = ('id', 'name', 'region')
        models = City


class CityAdmin(ImportExportActionModelAdmin):
    """Реєструємо модель населених пунктів в адмінпанелі"""

    resource_class = CityResource
    list_display = ('id', 'name', 'region')
    search_fields = ('id', 'name', 'region__name')

    class Meta:
        models = City


admin.site.register(City, CityAdmin)
