from django.urls import path
from .views import (
	FoodListView,
	FoodDetailView,
	FoodCreateView,
	FoodUpdateView,
	FoodDeleteView,
)
from . import views

urlpatterns = [
	path('food/', FoodListView.as_view(), name='food-home'),
	path('food/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
	path('food/new/', FoodCreateView.as_view(), name='food-create'),
	path('food/<int:pk>/update/', FoodUpdateView.as_view(), name='food-update'),
	path('food/<int:pk>/delete/', FoodDeleteView.as_view(), name='food-delete'),
	path('food/about/', views.about, name='food-about'),
]