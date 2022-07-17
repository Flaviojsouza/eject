from django.contrib import admin

from .models import Home, Quemsomos, Produtos, Propaganda, Depoimento, Contato

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display=['id','logo','titulo']

admin.site.register(Home, HomeAdmin)
admin.site.register(Produtos)
admin.site.register(Quemsomos)
admin.site.register(Propaganda)
admin.site.register(Depoimento)
admin.site.register(Contato)