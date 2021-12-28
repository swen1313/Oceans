from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="main"),
    path('hemi', views.put_to_hemishere),
    path('hemi/<hemishere>/', views.get_hemishere),

    path('<int:water>/', views.get_info_number),
    path('<str:water>/', views.get_info, name = "oceansapp_name"),
]