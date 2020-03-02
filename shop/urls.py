from django.urls import path

from . import views

# create shop urls

urlpatterns = [
    path('',views.index, name='ShopHome'),
    path('about/',views.about, name='AboutUs'),
    path('contact/',views.contact, name='ContactUs'),
    path('tracker/',views.tracker, name='TrackeringStatus'),
    path('search/',views.search, name='search'),
    path('productview/<int:myid>',views.productview, name='productview'),
    path('checkout/',views.checkout, name='Checkout'),
    path('handlerequest', views.handlerequest, name='handlerequest')
]

