from django.contrib import admin
from opencivicdata.models import division as models


@admin.register(models.Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'id')
    search_fields = list_display

