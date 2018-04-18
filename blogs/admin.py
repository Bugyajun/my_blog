from django.contrib import admin
from blogs import models
# Register your models here.

class AirticleAdmin(admin.ModelAdmin):
    list_display = ('title','create_time','update_time','author','category','details')


admin.site.register(models.airticle,AirticleAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)