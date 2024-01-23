from django.contrib import admin
from django.urls import path
from .views import home_page, about_page, contact_page, service_page, price_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('service/', service_page, name='service'),
    path('price/', price_page, name='price'),
]

