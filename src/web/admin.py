from django.contrib import admin
from .models import Slide, Category, CategoryForMen, CategorForWomen, Brand, Limelight, Testimonial, Product, GalleryImage
from .models import Order, OrderItem




@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(Category)
admin.site.register(CategoryForMen)
admin.site.register(CategorForWomen)
admin.site.register(Brand)
admin.site.register(Limelight)
admin.site.register(Testimonial)
admin.site.register(Product)
admin.site.register(GalleryImage)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  
    fields = ('product', 'quantity')  


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'get_purchased_products')  
    list_filter = ('created_at',)  
    search_fields = ('user__username',) 
    inlines = [OrderItemInline]  

   
    def get_purchased_products(self, obj):
        return ", ".join([str(item.product.title) for item in obj.items.all()])
    get_purchased_products.short_description = 'Purchased Products' 


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)




