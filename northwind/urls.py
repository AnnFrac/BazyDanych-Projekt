from django.urls import path
from . import views
from BD_Northwind_Django.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.products, name = 'products'),
    path('upload/', views.upload_product, name = 'upload-product'),
    path('update/<int:id>', views.update_product, name = 'edit-product'),
    path('delete/<int:id>', views.delete_product, name = 'delete-product'),
    path('detail/<int:id>', views.deatil_product, name = 'detail-product'),
]
