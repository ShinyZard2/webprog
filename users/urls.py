from django.urls import path, include
from . import views

urlpatterns = [
    path('uhome', views.uhome, name='uhome'),
    path('create', views.create, name='create'),
    path('<int:plan_id>', views.fitplan, name='fitplan'),
    path('<int:plan_id>/upvotes', views.upvotes, name='upvotes'),
]