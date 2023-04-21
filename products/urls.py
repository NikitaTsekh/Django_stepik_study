from django.urls import path
from products.views import index,products
from django.conf.urls.static import static
from django.conf import settings
app_name = 'products'

urlpatterns = [
    path('test/',products,name = 'index')

]

