from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('upload', views.Upload, name = "upload_images"),
    path('login', views.login_page, name = "login"),
    path('signup', views.signup_user, name = "signup"),
    path('logout', views.logout_user, name = "logout"),
    path('product/<int:id>', views.show_product, name='product'),
    path('addtowish/<int:id>', views.addtowish, name='addtowish'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('wishlist', views.show_wishlist, name= 'show_wishlist'),
    path('cart', views.show_cart, name='show_cart'),
    path('removewish/<int:id>', views.removewish, name="removewish"),
    path('removecart/<int:id>', views.removecart, name="removecart"),
    path('dummy', views.show_data, name= 'dummy')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


