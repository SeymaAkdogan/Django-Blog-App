from django.urls import path
from . import views

urlpatterns = [
    path("nutrition-record",views.show,name='showNutritionRecord'),
    path("nutrition-record/create",views.createNutritionRecord,name='createNutritionRecord'),
]