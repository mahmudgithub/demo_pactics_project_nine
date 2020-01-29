from django.contrib import admin
from . models import Product,ProductImage,ProductTag

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","active","in_stock","date_updated")
    search_fields = ("name",) #['name', 'roll']
   

admin.site.register(Product,ProductAdmin,)



class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)
    search_fields = ("image",)

admin.site.register(ProductImage,ImageAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ("description","name","active")
    search_fields = ("name",)

admin.site.register(ProductTag,TagAdmin)