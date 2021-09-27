from django.contrib import admin
from .models import Image

admin.site.register(Image)

# Register your models here.

from .models import vol_model, ideas_model, count_model, donors_model

admin.site.register(vol_model)
admin.site.register(ideas_model)

class countAdmin(admin.ModelAdmin):
    """
    Don't allow addition of more than one model instance in Django admin
    """
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(count_model, countAdmin)

class donorsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 4:
            return False
        else:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if self.model.objects.count() > 1:
            return True
        else:
            return False

    

admin.site.register(donors_model, donorsAdmin)