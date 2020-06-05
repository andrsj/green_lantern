from django.contrib import admin
from django.utils.safestring import mark_safe


from apps.cars.models import Car, Color, CarModel, CarBrand, CarEngine, FuelType


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', '_image')

    def _image(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="weight: 50px;">')
        return 'Not found image'


@admin.register(CarEngine)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'extra_title',)
