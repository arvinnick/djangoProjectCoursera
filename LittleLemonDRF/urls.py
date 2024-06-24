from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('ratings', views.RatingsView.as_view()),
    path('ratings/<int:pk>/', views.SingleRatingsView.as_view()),
    path('menuitems/<int:pk>/', views.SingleRatingsView.as_view()),
]