from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', include('products.urls')),
    path('posts/', include('posts.urls'))
]
