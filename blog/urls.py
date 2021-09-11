from django.urls import path
### blog アプリの全ての ビューをインポートする
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
