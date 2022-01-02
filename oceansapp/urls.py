from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="main"),
    path('hemi', views.put_to_hemishere),
    path('hemi/<hemishere>/', views.get_hemishere),
    path('deep/', views.get_deep),
    path('/Pacific,%20Atlantic,%20Indian/', views.get_hemi),
    path('deepone/<int:int_deepone>', views.get_deepone, name="deepone"),

    path('<int:water>/', views.get_info_number),
    path('<str:water>/', views.get_info, name = "oceansapp_name"),

]