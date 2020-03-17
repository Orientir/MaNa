from django.contrib import admin
from .models import Goods
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'slug', 'sale_price', 'created_date', 'sales')
    list_filter = ('author', 'created_date', 'sale_price', 'sales')
    fields = ['author', 'slug', 'title', 'description', ('pln_price', 'uah_price', 'sale_price'), ('sales', 'image')]
    search_fields = ('slug', 'title', 'author')
    readonly_fields = ["image_tag"]

