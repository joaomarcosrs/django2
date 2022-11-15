from django.urls import path

from .views import index, contato, produto, image_upload

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('upload/', image_upload, name='upload'),
]