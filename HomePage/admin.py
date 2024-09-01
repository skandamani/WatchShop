from django.contrib import admin
from . models import Watches, WatchesUploads, Wishlist, Cart, WatchReview, CartItem

# Register your models here.

admin.site.register(Watches)


#WatchUploads
class WatchUploadsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'price', 'image', 'count')
    list_filter = ('name', 'price')
    search_fields= ('name', 'description')
    fields=  ['id', 'name', 'description', 'price', 'image', 'count']
admin.site.register(WatchesUploads, WatchUploadsAdmin)

#WishList
# class WishlistAdmin(admin.ModelAdmin):
#     list_display= ('user', 'products')
#     list_filter= ('user','products')
# admin.site.register(Wishlist,  WishlistAdmin)
admin.site.register(Wishlist)


admin.site.register(Cart)
admin.site.register(CartItem)

#Watch Review
class WatchReviewAdmin(admin.ModelAdmin):
    list_display= ('user', 'product', 'rating', 'review_text')
    list_filter =  ('user', 'product', 'rating')
admin.site.register(WatchReview, WatchReviewAdmin)
