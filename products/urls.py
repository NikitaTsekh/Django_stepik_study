from django.urls import path
from products.views import index,products
from django.conf.urls.static import static
from django.conf import settings
app_name = 'products'

urlpatterns = [
    path('',products,name = 'index'),
    path('category/<int:category_id>/',products,name = 'category'),
    path('page/<int:page_number>/',products,name = 'paginator')

]

