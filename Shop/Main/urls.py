from django.urls import path
from .views import *

urlpatterns = [
    path('list/', CategoryList.as_view(), name="CategoryList"),
    path('detail/<int:pk>', SubCategoryList.as_view(), name="SubCategoryList"),
]