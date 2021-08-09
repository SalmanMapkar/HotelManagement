from django.urls import path, include

from . import views

urlpatterns = [
    # Registration APIs
    path('<str:username>/<str:password>/validate/', views.getAccountView.as_view({'get': 'list'}), name='getAccountView'),
]